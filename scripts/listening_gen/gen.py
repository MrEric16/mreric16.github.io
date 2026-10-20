#!/usr/bin/env python3
"""Usage: gen.py BATCH PER_SECTION OUTDIR [--dry]
Builds PER_SECTION fresh items for each of Sections 1-4, renders audio with edge-tts (British neural voices), and writes
OUTDIR/BATCH.json (item data) plus OUTDIR/audio/<id>.mp3 files."""
import asyncio, json, os, random, re, subprocess, sys, tempfile, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import make, make_lecture, Item
from s1 import S1
from s2 import S2
from s3 import S3
from s4 import LECT
from s4d import S4D
V = {'M1': 'en-GB-RyanNeural', 'F1': 'en-GB-SoniaNeural', 'M2': 'en-GB-ThomasNeural', 'F2': 'en-GB-LibbyNeural'}
BAD = re.compile(r'--|—|\bgotten\b|\{|\}')
def build(per, seed):
    rnd = random.Random(seed); items = []
    for sec, tpls in (('S1', S1), ('S2', S2), ('S3', S3)):
        order = []
        while len(order) < per: t = tpls[:]; rnd.shuffle(t); order += t
        for tpl in order[:per]:
            for _ in range(20):
                try: it = make(tpl, rnd, sec); break
                except Item: continue
            else: raise SystemExit('template failed ' + tpl['id'])
            items.append(it)
    for k in range(per):
        if k % 2 == 0:
            tp = rnd.choice(LECT); items.append(make_lecture(tp, rnd))
        else:
            tpl = rnd.choice(S4D)
            for _ in range(20):
                try: it = make(tpl, rnd, 'S4'); break
                except Item: continue
            else: raise SystemExit('template failed ' + tpl['id'])
            items.append(it)
    for it in items:
        strs = [t['t'] for t in it['turns']] + [q['q'] for q in it['qs']] + [str(o) for q in it['qs'] for o in q.get('o', [])] + [it['title']]
        for x in strs:
            if BAD.search(x): raise SystemExit('bad text in %s: %s' % (it['title'], x))
    return items
async def say(sem, text, voice, path):
    import edge_tts
    async with sem:
        for a in range(5):
            try: await edge_tts.Communicate(text, voice, rate='-4%').save(path); return
            except Exception as e:
                await asyncio.sleep(2 + 3 * a)
        raise RuntimeError('tts failed: ' + text[:40])
async def render(items, outdir, tmp):
    sem = asyncio.Semaphore(8); sil = os.path.join(tmp, 'sil.mp3')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=24000:cl=mono', '-t', '0.7', '-b:a', '48k', sil], check=True)
    async def build_one(it):
        files = []; jobs = []
        for k, t in enumerate(it['turns']):
            p = os.path.join(tmp, '%s_%02d.mp3' % (it['id'], k)); files.append(p); jobs.append(say(sem, t['t'], V[t['v']], p))
        await asyncio.gather(*jobs)
        seq = []
        for k, p in enumerate(files):
            seq.append(p)
            if k < len(files) - 1: seq.append(sil)
        lst = os.path.join(tmp, it['id'] + '.txt'); open(lst, 'w').write(''.join("file '%s'\n" % f for f in seq))
        out = os.path.join(outdir, 'audio', it['id'] + '.mp3')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-ar', '24000', '-ac', '1', '-b:a', '48k', out], check=True)
        for f in files: os.remove(f)
        r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out], capture_output=True, text=True)
        it['dur'] = round(float(r.stdout.strip() or 0))
        print('done', it['id'], it['title'], it['dur'], 's', flush=True)
    async def one(it):
        try: await build_one(it)
        except Exception as e:
            it['fail'] = True; print('FAILED', it['id'], str(e)[:80], flush=True)
    await asyncio.gather(*[one(it) for it in items])
def main():
    batch, per, outdir = sys.argv[1], int(sys.argv[2]), sys.argv[3]; dry = '--dry' in sys.argv
    seed = int(re.sub(r'\D', '', batch) or '1') + int(time.time())
    items = build(per, seed)
    for i, it in enumerate(items): it['id'] = '%s-%s%03d' % (batch, it['sec'], i % per + 1)
    os.makedirs(os.path.join(outdir, 'audio'), exist_ok=True)
    if not dry: asyncio.run(render(items, outdir, tempfile.mkdtemp()))
    shard = []
    for it in items:
        if it.get('fail'): continue
        shard.append({'id': it['id'], 's': it['sec'], 'title': it['title'], 'tx': it['tx'], 'qs': it['qs'], 'dur': it.get('dur', 0)})
    json.dump({'batch': batch, 'tag': 'lp-' + batch[:8], 'items': shard}, open(os.path.join(outdir, batch + '.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    print('items', len(items))
if __name__ == '__main__': main()
