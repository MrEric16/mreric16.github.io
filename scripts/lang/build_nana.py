#!/usr/bin/env python3
"""Builds data/lang/den.json ("Nana", the harder German tile) from scripts/lang/nana/*.txt and adds a hidden entry to index.json.
Nana is not in the main language list; German's home page links to it."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'build.py'), encoding='utf-8').read()
src = src.rsplit('\nmain()', 1)[0]
g = {'__file__': os.path.join(HERE, 'build.py'), '__name__': 'build_lib'}
exec(compile(src, 'build.py', 'exec'), g)
parse = g['parse']; OUT = g['OUT']
def load_reading(path):
    out = []; cur = None; sents = {}
    def close():
        if cur is None: return
        toks = re.findall(r'\{(\d)\}', ' '.join(p['t'] for p in cur['paras']))
        assert sorted(toks) == ['1', '2', '3', '4', '5'], (cur['id'], 'tokens', toks)
        cur['f'] = []
        for k in range(1, 6):
            ss = [sents.get((k, v)) for v in range(4)]
            assert all(ss) and len(set(ss)) == 4, (cur['id'], 'fact', k, ss)
            q = cur['_q'][k]; assert len(q[1]) == 4 and len(set(q[1])) == 4, (cur['id'], 'opts', k, q)
            cur['f'].append({'q': q[0], 'o': q[1], 's': ss})
        del cur['_q']
    for n, line in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
        line = line.rstrip()
        if not line: continue
        if line.startswith('## '):
            close(); sents = {}
            pid, title, en, lv = [x.strip() for x in line[3:].split('|')]
            cur = {'id': pid, 'title': title, 'en': en, 'lv': lv, 'paras': [], '_q': {}}; out.append(cur)
        elif re.match(r'^[A-F]: ', line): cur['paras'].append({'l': line[0], 't': line[3:]})
        elif re.match(r'^Q[1-5]: ', line):
            qt, op = line[4:].split('||'); cur['_q'][int(line[1])] = (qt.strip(), [x.strip() for x in op.split('|')])
        elif re.match(r'^[1-5]\.[0-3]: ', line): sents[(int(line[0]), int(line[2]))] = line[5:]
        else: raise SystemExit('%s:%d bad line %s' % (path, n, line))
    close()
    return out
L = parse(os.path.join(HERE, 'nana', 'den.txt'))
L['sounds'] = None; L['note'] = ''
for s in ('numbers', 'greetings', 'phrases', 'vocab'):
    ids = [x['id'] for x in L[s]]; assert len(ids) == len(set(ids)), (s, 'duplicate group')
L['reading'] = load_reading(os.path.join(HERE, 'nana', 'read.txt'))
cnt = sum(len(gr['items']) for s in ('numbers', 'greetings', 'phrases', 'vocab') for gr in L[s]) + sum(len(l['ex']) for l in L['grammar'])
json.dump(L, open(os.path.join(OUT, 'den.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
ip = os.path.join(OUT, 'index.json'); idx = [x for x in json.load(open(ip, encoding='utf-8')) if x['id'] != 'den']
idx.append({'id': 'den', 'name': 'Nana', 'flag': 'de', 'script': False, 'count': cnt, 'group': '', 'hidden': True})
json.dump(idx, open(ip, 'w'), ensure_ascii=False, separators=(',', ':'))
print('den', cnt, {s: len(L[s]) for s in ('phrases', 'vocab', 'grammar', 'reading')})
