#!/usr/bin/env python3
"""python3 check_full.py <id>: compares built data/lang/<id>.json to es.json (benchmark): missing/extra English per group."""
import sys, json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'lang')
def keys(d):
    k = {}
    for s in ('numbers', 'greetings', 'phrases', 'vocab'):
        for g in d[s]: k[(s, g['title'])] = [i[0] for i in g['items']]
    for l in d['grammar']: k[('grammar', l['title'])] = [e[0] for e in l['ex']]
    return k
es = keys(json.load(open(os.path.join(D, 'es.json'))))
for i in sys.argv[1:]:
    d = json.load(open(os.path.join(D, i + '.json'))); k = keys(d); tot = sum(len(v) for v in k.values())
    for g, lst in es.items():
        if g[0] == 'grammar' and g not in k: continue
        got = k.get(g)
        if got is None: print(i, 'NO GROUP', g); continue
        for en in lst:
            if en not in got: print(i, 'MISSING', g, en)
    print(i, 'items', tot, 'spanish', sum(len(v) for v in es.values()))
