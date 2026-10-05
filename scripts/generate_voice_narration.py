#!/usr/bin/env python3
"""
Generate narrated audio for a Dispatches article using a cloned voice via
smallest.ai's Waves TTS API.

How this fits the site:
  - This repo is a static GitHub Pages site. It cannot call a paid TTS API
    at page-load time (that would expose the API key to every visitor).
  - So narration audio is pre-generated here, offline, by this script, and
    the resulting mp3 is committed into data/audio/ like any other static
    asset. The site just plays a static file.
  - Scripts are plain text files under scripts/narration_scripts/<slug>.txt.
    Mr Eric reviews/approves the text before it is ever sent to this script
    (per his explicit instruction: "Reviewed at first. Then when we build
    trust - automatic"). This script does not write, rewrite, or summarize
    text -- it only sends exactly the text it's given to the TTS API.

Usage:
    SMALLEST_AI_API_KEY=... python3 scripts/generate_voice_narration.py \
        --slug ikea-effect \
        --voice-id voice_AQH6kCXwOc

Reads:  scripts/narration_scripts/<slug>.txt
Writes: data/audio/<slug>.mp3

The API key is read ONLY from the SMALLEST_AI_API_KEY environment variable
(the GitHub Actions secret of the same name). It is never hardcoded and
never logged.
"""
import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
import urllib.error

API_URL = "https://api.smallest.ai/waves/v1/tts"
# NOTE: cloned voices are pinned to the model pool they were cloned onto
# (see the voiceId's modelIds in a GET /waves/v1/voice-cloning response).
# Mr Eric's "Lounge" voices all came back modelIds=["lightning-v3.1-pro"],
# so lightning_v3.1_pro is the correct default here, not the base pool.
DEFAULT_MODEL = "lightning_v3.1_pro"

# ---------------------------------------------------------------------------
# ElevenLabs provider (added 2026-10-05: Mr Eric's chosen voice lives there).
# POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}, `xi-api-key` header.
# The voice's own saved settings are used (voice_settings is deliberately omitted),
# so the voice sounds like it did in the ElevenLabs voice test.
# Key comes ONLY from the ELEVENLABS_API_KEY env var / GitHub secret. Never logged.
# ---------------------------------------------------------------------------
EL_URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format=mp3_44100_128"
EL_DEFAULT_MODEL = "eleven_multilingual_v2"   # most stable for long-form (10,000 char limit)
EL_CHUNK_CHARS = 4500                          # under every model's per-request limit (v3 = 5,000)


def split_paragraphs(text, limit):
    """Pack whole paragraphs into chunks of <= limit chars. Never splits mid-paragraph
    unless a single paragraph alone exceeds the limit (then it splits on sentence ends)."""
    chunks, cur = [], ""
    def flush():
        nonlocal cur
        if cur.strip():
            chunks.append(cur.strip())
        cur = ""
    for para in [p.strip() for p in text.split("\n\n") if p.strip()]:
        if len(para) > limit:
            flush()
            sent_buf = ""
            for sent in para.replace("? ", "?|").replace("! ", "!|").replace(". ", ".|").split("|"):
                if len(sent_buf) + len(sent) + 1 > limit:
                    chunks.append(sent_buf.strip()); sent_buf = ""
                sent_buf += sent + " "
            if sent_buf.strip():
                chunks.append(sent_buf.strip())
            continue
        if len(cur) + len(para) + 2 > limit:
            flush()
        cur += para + "\n\n"
    flush()
    return chunks


def elevenlabs_tts(chunks, voice_id, model, api_key):
    audio = b""
    for i, chunk in enumerate(chunks):
        body = {"text": chunk, "model_id": model}
        # context for smooth joins between chunks (prosody carries across the seam)
        if i > 0:
            body["previous_text"] = chunks[i - 1][-500:]
        if i < len(chunks) - 1:
            body["next_text"] = chunks[i + 1][:500]
        req = urllib.request.Request(
            EL_URL.format(voice_id=voice_id),
            data=json.dumps(body).encode("utf-8"),
            method="POST",
            headers={"xi-api-key": api_key, "Content-Type": "application/json", "Accept": "audio/mpeg"},
        )
        for attempt in range(1, 4):
            try:
                with urllib.request.urlopen(req, timeout=180) as resp:
                    audio += resp.read()
                print(f"[generate_voice_narration] elevenlabs chunk {i+1}/{len(chunks)} ok ({len(chunk)} chars)")
                break
            except urllib.error.HTTPError as e:
                err = e.read().decode("utf-8", errors="replace")
                if e.code in (429, 500, 502, 503) and attempt < 3:
                    wait = 5 * attempt
                    print(f"[generate_voice_narration] HTTP {e.code}, retrying in {wait}s (attempt {attempt}/3)", file=sys.stderr)
                    time.sleep(wait)
                    continue
                hint = ""
                if e.code == 401:
                    hint = "  -> API key rejected: check the ELEVENLABS_API_KEY secret (and that the key has Text to Speech permission)."
                elif e.code in (402, 403):
                    hint = "  -> Plan/permission issue: this voice or model may need a paid plan for API use, or credits are exhausted."
                elif e.code in (404, 422):
                    hint = "  -> Check the voice ID (Voices > the voice > copy ID) and model name."
                print(f"ERROR: ElevenLabs request failed: HTTP {e.code}\n{err}\n{hint}", file=sys.stderr)
                sys.exit(1)
            except urllib.error.URLError as e:
                print(f"ERROR: could not reach ElevenLabs: {e}", file=sys.stderr)
                sys.exit(1)
    return audio


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True, help="narration slug, e.g. ikea-effect")
    parser.add_argument("--provider", default="smallest", choices=["smallest", "elevenlabs"], help="TTS provider (default: smallest)")
    parser.add_argument("--voice-id", required=True, help="voice id (smallest.ai e.g. voice_AQH6kCXwOc, or an ElevenLabs voice ID)")
    parser.add_argument("--model", default=None, help=f"TTS model. smallest default: {DEFAULT_MODEL} (must match the pool the voice was cloned onto). elevenlabs default: {EL_DEFAULT_MODEL}")
    parser.add_argument("--speed", type=float, default=1.0, help="playback speed, 0.5-2.0 (default 1.0)")
    parser.add_argument("--sample-rate", type=int, default=44100, choices=[8000, 16000, 24000, 44100])
    parser.add_argument("--language", default="en", help="ISO 639-1 language code (default: en). Some accounts/regions reject the API's own 'auto' default.")
    parser.add_argument("--no-deess", action="store_true", help="skip the de-essing EQ pass (raw TTS output has harsh/lisp-y S and SH sounds on this clone)")
    args = parser.parse_args()

    key_env = "ELEVENLABS_API_KEY" if args.provider == "elevenlabs" else "SMALLEST_AI_API_KEY"
    api_key = os.environ.get(key_env)
    if not api_key:
        print(f"ERROR: {key_env} environment variable is not set (add it as a GitHub Actions secret of the same name).", file=sys.stderr)
        sys.exit(1)
    if not args.model:
        args.model = EL_DEFAULT_MODEL if args.provider == "elevenlabs" else DEFAULT_MODEL

    script_path = os.path.join("scripts", "narration_scripts", f"{args.slug}.txt")
    if not os.path.isfile(script_path):
        print(f"ERROR: no script file at {script_path}", file=sys.stderr)
        sys.exit(1)

    with open(script_path, encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print(f"ERROR: {script_path} is empty", file=sys.stderr)
        sys.exit(1)

    print(f"[generate_voice_narration] provider={args.provider} slug={args.slug} voice_id={args.voice_id} model={args.model} chars={len(text)}")

    if args.provider == "elevenlabs":
        chunks = split_paragraphs(text, EL_CHUNK_CHARS)
        audio_bytes = elevenlabs_tts(chunks, args.voice_id, args.model, api_key)
        if not audio_bytes or len(audio_bytes) < 1000:
            print(f"ERROR: response too small ({len(audio_bytes)} bytes) to be real audio -- not writing output", file=sys.stderr)
            sys.exit(1)
        out_dir = os.path.join("data", "audio")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{args.slug}.mp3")
        with open(out_path, "wb") as f:
            f.write(audio_bytes)
        print(f"[generate_voice_narration] wrote {out_path} ({len(audio_bytes)} bytes, {len(chunks)} chunk(s), no post-processing)")
        return

    body = {
        "text": text,
        "voice_id": args.voice_id,
        "model": args.model,
        "sample_rate": args.sample_rate,
        "speed": args.speed,
        "output_format": "mp3",
        "language": args.language,
    }
    data = json.dumps(body).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            audio_bytes = resp.read()
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        print(f"ERROR: TTS request failed: HTTP {e.code}\n{err_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: TTS request failed to reach the API: {e}", file=sys.stderr)
        sys.exit(1)

    if not audio_bytes or len(audio_bytes) < 1000:
        print(f"ERROR: response too small ({len(audio_bytes)} bytes) to be real audio -- not writing output", file=sys.stderr)
        sys.exit(1)

    out_dir = os.path.join("data", "audio")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{args.slug}.mp3")
    raw_path = os.path.join(out_dir, f"{args.slug}.raw.mp3")

    with open(raw_path, "wb") as f:
        f.write(audio_bytes)

    if args.no_deess:
        os.replace(raw_path, out_path)
        print(f"[generate_voice_narration] wrote {out_path} ({len(audio_bytes)} bytes, no de-ess)")
        return

    # This voice clone (recorded on a phone mic) produces noticeably harsh,
    # almost lisp-y S/SH sibilants in raw TTS output. Rather than re-record
    # the clone samples, tame it with a static de-essing EQ: two moderate
    # cuts centered on the sibilance band (~5.5kHz and ~8kHz), gentle enough
    # that it doesn't dull the voice, narrow enough that it doesn't eat
    # normal consonant clarity. Tune the two `g=` (gain, dB) values here if
    # a render still sounds harsh or starts sounding muffled.
    deess_filter = (
        "equalizer=f=5500:width_type=o:width=1.5:g=-6,"
        "equalizer=f=8000:width_type=o:width=1.5:g=-4"
    )
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", raw_path, "-af", deess_filter, "-q:a", "2", out_path],
            check=True, capture_output=True, text=True,
        )
    except FileNotFoundError:
        print("[generate_voice_narration] ffmpeg not found -- skipping de-ess, using raw output", file=sys.stderr)
        os.replace(raw_path, out_path)
        return
    except subprocess.CalledProcessError as e:
        print(f"[generate_voice_narration] ffmpeg de-ess failed, using raw output:\n{e.stderr}", file=sys.stderr)
        os.replace(raw_path, out_path)
        return

    os.remove(raw_path)
    final_size = os.path.getsize(out_path)
    print(f"[generate_voice_narration] wrote {out_path} ({final_size} bytes, de-essed)")


if __name__ == "__main__":
    main()
