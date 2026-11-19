"""Builds scripts/grammar-bank-src/g_mixed-past.txt: a mixed past-tense tile made from five existing topics
(past simple be / other verbs, irregular verbs [past-simple items only], past simple or continuous, past continuous),
the same number of items from each, so a set of 20 is spread evenly. Run gg_compile.py afterwards."""
import json, random, re, os
ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
SRC = ['past-simple-be', 'past-simple-other', 'irregular-verbs', 'past-simple-vs-continuous', 'past-continuous']
PER = {'easy': 200, 'medium': 200, 'hard': 200}
PERF = re.compile(r"\b(have|has|haven't|hasn't|had|hadn't|been)\b|past participle", re.I)
def enc(a): return ' ;; '.join('|'.join(g) for g in a)
rng = random.Random(2026)
out = ['@topic mixed-past | Mixed past tenses']
for lv in ('easy', 'medium', 'hard'):
    out.append('@' + lv)
    pools = []
    for t in SRC:
        d = json.load(open(os.path.join(ROOT, 'data/grammar', t + '.json'), encoding='utf-8'))
        arr = d['levels'][lv]
        if t == 'irregular-verbs': arr = [x for x in arr if not PERF.search(x['q'])]
        arr = [x for x in arr if '|' not in x['q'] and ' => ' not in x['q'] and all('|' not in y and ';;' not in y for g in x['a'] for y in g)]
        rng.shuffle(arr); pools.append(arr[:PER[lv]])
    n = min(len(p) for p in pools)
    items = [x for p in pools for x in p[:n]]
    rng.shuffle(items)
    for x in items: out.append(x['q'] + ' => ' + enc(x['a']))
    print(lv, n, 'per source,', len(items))
open(os.path.join(ROOT, 'scripts/grammar-bank-src/g_mixed-past.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
