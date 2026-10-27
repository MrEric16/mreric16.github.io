#!/usr/bin/env python3
"""python3 check_pack.py <id> : verifies src/<id>.add.txt covers every English line of pack_en.txt (per group)."""
import sys, os, re
here = os.path.dirname(os.path.abspath(__file__))
def read(path):
    out = {}; sec = grp = None
    for raw in open(path, encoding='utf-8'):
        line = raw.rstrip('\n')
        if not line.strip() or line.startswith('//') or line.startswith('>') or line.startswith('row:'): continue
        if line.startswith('['): sec = line.strip(); continue
        if line.startswith('## '): grp = (sec, line[3:].strip()); out[grp] = []; continue
        if grp is None: continue
        en = line[3:].split('|')[0].strip() if line.startswith('ex:') else line.split('|')[0].strip()
        out.setdefault(grp, []).append(en)
    return out
pack = {}
for line in open(os.path.join(here, 'pack_en.txt'), encoding='utf-8'):
    pass
# pack: English-only lines
sec = grp = None
for raw in open(os.path.join(here, 'pack_en.txt'), encoding='utf-8'):
    line = raw.rstrip('\n')
    if not line.strip(): continue
    if line.startswith('['): sec = line.strip(); continue
    if line.startswith('## '): grp = (sec, line[3:].strip()); pack[grp] = []; continue
    pack[grp].append(line.strip())
for i in sys.argv[1:]:
    a = read(os.path.join(here, 'src', i + '.add.txt'))
    bad = 0
    for g, lst in pack.items():
        got = a.get(g, [])
        for en in lst:
            if en not in got: print(i, 'MISSING', g, en); bad += 1
        for en in got:
            if en not in lst: print(i, 'EXTRA', g, en)
    print(i, 'ok' if not bad else '%d missing' % bad)
