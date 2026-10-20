#!/usr/bin/env python3
"""Generates natural British neural-voice MP3s for the Listening page from data/games/listening.json using edge-tts.
Output: data/audio/listening/NN.mp3 (index = position in listening.json). Run on a GitHub runner (needs ffmpeg + internet)."""
import asyncio, json, re, subprocess, os, sys, tempfile
import edge_tts
V = {'M1': 'en-GB-RyanNeural', 'F1': 'en-GB-SoniaNeural', 'M2': 'en-GB-ThomasNeural', 'F2': 'en-GB-LibbyNeural'}
D = json.load(open('data/games/listening.json', encoding='utf8'))
LABELED = {6: {'Tutor': 'M1', 'Dilnoza': 'F1'}, 7: {'Tutor': 'M1', 'Student': 'F2'}, 12: {'Aziz': 'M1', 'Madina': 'F1', 'Jahongir': 'M2'}}
CUTS = {
 0: ('F1', 'M1', ["Hello, I'd like", "Certainly.", "Yes, I'm at", "Then you can", "Can I use", "Yes, the pool", "Great. I'll", "Please bring"]),  # clerk first
 1: ('F1', 'M1', ["Can you describe", "It's a dark green", "What was inside?", "A blue notebook", "Do you remember what time", "About quarter past", "The driver handed in", "Ours is green.", "Let me check the shelf.", "It's Karimova", "You can collect it"]),  # clerk, caller alternating from start? see below
 11: ('M1', 'F1', ["Of course.", "Three days, from Friday.", "For three days the price", "An electric one would", "It's fifteen pounds", "I'll take the standard", "We need a deposit", "Where is your shop?", "It's on Mill Street", "Can I pick it up", "Sorry, we close"]),
}
MONO = {2: 'M1', 3: 'F1', 4: 'M2', 5: 'F1', 8: 'M1', 9: 'F2', 10: 'M2', 13: 'F1'}
def turns(i, s):
    if i in LABELED:
        parts = re.split(r'\b(' + '|'.join(LABELED[i]) + r'):\s*', s)
        out = [(LABELED[i][parts[k]], parts[k + 1].strip()) for k in range(1, len(parts), 2)]
        return out
    if i in CUTS:
        first, second, cuts = CUTS[i]
        pos = [0]
        for c in cuts:
            p = s.index(c, pos[-1] + 1 if pos[-1] else 0); pos.append(p)
        pos.append(len(s)); segs = [s[pos[k]:pos[k + 1]].strip() for k in range(len(pos) - 1)]
        spk = [first, second]
        out = []
        who = 0
        # explicit alternation: segment 0 = first speaker; each cut flips speaker, except consecutive same speaker cases handled below
        cur = spk[0]; out.append((cur, segs[0]))
        for k, seg in enumerate(segs[1:]):
            cur = spk[1] if cur == spk[0] else spk[0]; out.append((cur, seg))
        return out
    return [(MONO[i], s)]
async def say(text, voice, path):
    await edge_tts.Communicate(text, voice, rate='-4%').save(path)
async def main():
    os.makedirs('data/audio/listening', exist_ok=True)
    man = []
    tmp = tempfile.mkdtemp()
    sil = os.path.join(tmp, 'sil.mp3')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=24000:cl=mono', '-t', '0.6', '-q:a', '9', sil], check=True)
    for i, x in enumerate(D):
        t = turns(i, x['s'])
        joined = re.sub(r'\s+', ' ', ' '.join(a for _, a in t)).strip()
        base = re.sub(r'\s+', ' ', re.sub(r'\b(Tutor|Dilnoza|Student|Aziz|Madina|Jahongir):\s*', '', x['s'])).strip()
        assert joined == base, (i, joined[:80], base[:80])
        files = []
        for k, (spk, text) in enumerate(t):
            p = os.path.join(tmp, '%02d_%02d.mp3' % (i, k))
            for attempt in range(3):
                try: await say(text, V[spk], p); break
                except Exception as e:
                    print('retry', i, k, str(e)[:80]); await asyncio.sleep(3)
            else: sys.exit('failed ' + str(i))
            files.append(p)
            if k < len(t) - 1: files.append(sil)
        lst = os.path.join(tmp, '%02d.txt' % i)
        open(lst, 'w').write(''.join("file '%s'\n" % f for f in files))
        out = 'data/audio/listening/%02d.mp3' % i
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-ar', '24000', '-ac', '1', '-b:a', '48k', out], check=True)
        print(i, x['t'], len(t), 'turns', os.path.getsize(out) // 1024, 'KB')
        man.append({'i': i, 't': x['t'], 'file': out})
    json.dump(man, open('data/audio/listening/manifest.json', 'w'))
asyncio.run(main())
