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
import os
import sys
import urllib.request
import urllib.error

API_URL = "https://api.smallest.ai/waves/v1/tts"
DEFAULT_MODEL = "lightning_v3.1"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True, help="narration slug, e.g. ikea-effect")
    parser.add_argument("--voice-id", required=True, help="smallest.ai cloned voice id, e.g. voice_AQH6kCXwOc")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"TTS model/pool (default: {DEFAULT_MODEL}); must match the pool the voice was cloned onto")
    parser.add_argument("--speed", type=float, default=1.0, help="playback speed, 0.5-2.0 (default 1.0)")
    parser.add_argument("--sample-rate", type=int, default=44100, choices=[8000, 16000, 24000, 44100])
    args = parser.parse_args()

    api_key = os.environ.get("SMALLEST_AI_API_KEY")
    if not api_key:
        print("ERROR: SMALLEST_AI_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    script_path = os.path.join("scripts", "narration_scripts", f"{args.slug}.txt")
    if not os.path.isfile(script_path):
        print(f"ERROR: no script file at {script_path}", file=sys.stderr)
        sys.exit(1)

    with open(script_path, encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print(f"ERROR: {script_path} is empty", file=sys.stderr)
        sys.exit(1)

    print(f"[generate_voice_narration] slug={args.slug} voice_id={args.voice_id} model={args.model} chars={len(text)}")

    body = {
        "text": text,
        "voice_id": args.voice_id,
        "model": args.model,
        "sample_rate": args.sample_rate,
        "speed": args.speed,
        "output_format": "mp3",
    }
    import json
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
    with open(out_path, "wb") as f:
        f.write(audio_bytes)

    print(f"[generate_voice_narration] wrote {out_path} ({len(audio_bytes)} bytes)")


if __name__ == "__main__":
    main()
