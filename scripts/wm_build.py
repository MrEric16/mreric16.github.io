#!/usr/bin/env python3
"""Builds data/writing/models.json from wm_src_*.py (Writing model answers). Validates word counts and house rules."""
import sys, os, re, json
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from wm_src_t1 import T1; from wm_src_g import G; from wm_src_t2 import T2
from wm_src_roles import ROLES; from wm_src_guides import GUIDES
W = lambda t: len(re.findall(r"[A-Za-z]+(?:['’-][A-Za-z]+)*|\d[\d,]*", t))
AM = re.compile(r'\b(color|favorite|organize|organized|center|behavior|realize|realise d|program\b|analyze|gotten|neighbor|labor\b|defense|practice session)', re.I)
bad = 0; out = []
for x in T1 + G + T2:
    body = ' '.join(x['model'][1:-2] if x['task'] == 't1g' else x['model'])
    n = W(body); x['words'] = n
    mn = 250 if x['task'] == 't2' else 150
    if n < mn + 5: print('SHORT', x['id'], n); bad += 1
    allt = json.dumps(x, ensure_ascii=False)
    if re.search('—|–|--', allt) or AM.search(allt): print('STYLE', x['id'], AM.search(allt) and AM.search(allt).group(0)); bad += 1
    for k in ('Task Achievement', 'Task Response', 'Coherence', 'Lexical Resource', 'Grammar'): pass
    if x['task'] == 't2':
        et, roles = ROLES[x['id']]
        if len(roles) != len(x['model']): print('ROLES', x['id'], len(roles), len(x['model'])); bad += 1
        x['etype'] = et; x['roles'] = roles
    out.append(x)
ids = [x['id'] for x in out]; assert len(ids) == len(set(ids))
os.makedirs(os.path.join(here, '..', 'data', 'writing'), exist_ok=True)
json.dump({'v': 2, 'models': out, 'guides': GUIDES}, open(os.path.join(here, '..', 'data', 'writing', 'models.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
print(len(out), 'models,', bad, 'problems'); sys.exit(1 if bad else 0)
