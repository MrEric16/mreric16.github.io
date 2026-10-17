#!/usr/bin/env python3
"""Compile scripts/grammar-bank-src/t*.txt into data/grammar-bank.json (Grammar Practice).
Format per line:  question with ___ per blank => accepted|alt ;; accepted for blank 2
A line with no ___ is a whole-sentence answer (rewrite / correct the mistake). Contractions,
capitalisation, punctuation and American spellings are forgiven by the app's checker."""
import glob, json, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
topics, bad = [], 0
files = sorted(glob.glob(os.path.join(root, 'scripts/grammar-bank-src/t*.txt'))) + sorted(glob.glob(os.path.join(root, 'scripts/grammar-bank-src/g_*.txt')))
byid = {}
for f in files:
    cur = lvl = None
    for ln, l in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
        l = l.strip()
        if not l: continue
        if l.startswith('@topic'):
            i, n = [x.strip() for x in l[6:].split('|')]
            if i in byid: cur = byid[i]; continue
            cur = {'id': i, 'name': n, 'levels': {'easy': [], 'medium': [], 'hard': []}}; topics.append(cur); byid[i] = cur; continue
        if l in ('@easy', '@medium', '@hard'): lvl = l[1:]; continue
        if ' => ' not in l: print('NO =>', f, ln); bad += 1; continue
        q, a = l.rsplit(' => ', 1)
        groups = [[x.strip() for x in g.split('|') if x.strip()] for g in a.split(' ;; ')]
        if (q.count('___') or 1) != len(groups) or any(not g for g in groups): print('BAD', f, ln, l); bad += 1; continue

        cur['levels'][lvl].append({'q': q, 'a': groups})
for t in topics:
    for k, arr in t['levels'].items():
        seen, out = set(), []
        for it in arr:
            if it['q'] in seen: continue
            seen.add(it['q']); out.append(it)
        t['levels'][k] = out
if bad: sys.exit(1)
open(os.path.join(root, 'data/grammar-bank.json'), 'w', encoding='utf-8').write(json.dumps({'topics': topics}, ensure_ascii=False, separators=(',', ':')) + '\n')
print(len(topics), 'topics written')
