#!/usr/bin/env python3
"""Builds data/writing/models.json from wm_src_*.py (Writing model answers). Validates word counts and house rules."""
import sys, os, re, json
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from wm_src_t1 import T1; from wm_src_g import G; from wm_src_t2 import T2
from wm_src_roles import ROLES; from wm_src_guides import GUIDES
import wm_src_b9 as B9
B9ONLY = {'t2-libraries', 't2-practical', 't2-online-shop', 't2-graduates', 't2-cities', 't2-ageing'}
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
extra = json.dumps([B9.LESSONS, B9.QTYPE, B9.OPEN, B9.HEDGE, B9.NOUN, B9.LINK, GUIDES], ensure_ascii=False)
if re.search('\u2014|\u2013|--', extra) or re.search(r'gotten', extra, re.I): print('STYLE extra'); bad += 1
ids = [x['id'] for x in out]; assert len(ids) == len(set(ids))
os.makedirs(os.path.join(here, '..', 'data', 'writing'), exist_ok=True)
def parse(items, opts=None):
    out = []
    for it in items:
        if opts is None:
            parts = it['q'].split('|'); q, o = parts[0], parts[1:]
        else:
            q, o = it['q'], opts
        assert 0 <= it['a'] < len(o) and len(o) >= 2, it
        out.append({'q': q, 'opts': o, 'a': it['a'], 'why': it['why']})
    return out
drills = [
 {'id': 'qtype', 'title': 'Spot the question type', 'desc': 'Read an IELTS Task 2 question and name its type.', 'items': parse(B9.QTYPE, B9.QTYPE_OPTS)},
 {'id': 'open', 'title': 'Pick the stronger opening', 'desc': 'Two first sentences for the same topic. Which one would an examiner prefer?', 'items': parse(B9.OPEN)},
 {'id': 'link', 'title': 'Link your sentences and paragraphs', 'desc': 'Choose the best linking phrase or summary noun.', 'items': parse(B9.LINK)},
 {'id': 'noun', 'title': 'Nouns for efficiency', 'desc': 'Choose the tighter, more academic version.', 'items': parse(B9.NOUN)},
 {'id': 'hedge', 'title': 'Hedge or not?', 'desc': 'Decide which sentence has the right level of caution.', 'items': parse(B9.HEDGE)},
]
b9 = [x for x in out if x['id'] in B9ONLY or (x['task'] == 't2')]
os.makedirs(os.path.join(here, '..', 'data', 'writing'), exist_ok=True)
json.dump({'v': 3, 'models': [x for x in out if x['id'] not in B9ONLY]}, open(os.path.join(here, '..', 'data', 'writing', 'models.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
json.dump({'v': 1, 'essays': b9, 'guides': GUIDES, 'lessons': B9.LESSONS, 'drills': []}, open(os.path.join(here, '..', 'data', 'writing', 'band9.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
print(len(out), 'models,', len(b9), 'band9 essays,', sum(len(d['items']) for d in drills), 'drill items,', bad, 'problems'); sys.exit(1 if bad else 0)
