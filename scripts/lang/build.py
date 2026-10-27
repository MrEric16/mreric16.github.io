#!/usr/bin/env python3
"""Builds data/lang/<id>.json + index.json from scripts/lang/src/*.txt.
Format: header lines NAME:/ID:/BADGE:/NOTE:, then [sounds] [numbers] [greetings] [phrases] [vocab] [grammar].
Items are 'english | target | say(optional)'. '## Title' starts a group (or a grammar lesson). Grammar lesson lines: '> paragraph', 'row: a | b | c', 'ex: en | t | s'."""
import json, re, glob, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
SRC = os.path.join(ROOT, 'scripts', 'lang', 'src'); OUT = os.path.join(ROOT, 'data', 'lang')
def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
def parts(s): return [x.strip() for x in s.split('|')]
def parse(path):
    L = {'sounds': None, 'numbers': [], 'greetings': [], 'phrases': [], 'vocab': [], 'grammar': []}
    sec = None; cur = None
    for n, raw in enumerate(open(path, encoding='utf-8'), 1):
        line = raw.rstrip('\n')
        if not line.strip() or line.startswith('//'): continue
        m = re.match(r'^(NAME|ID|BADGE|NOTE):\s*(.*)$', line)
        if m and sec is None: L[m.group(1).lower()] = m.group(2).strip(); continue
        m = re.match(r'^\[(\w+)\]$', line.strip())
        if m:
            sec = m.group(1); cur = None
            if sec == 'sounds': L['sounds'] = {'intro': '', 'rows': [], 'notes': []}
            continue
        if sec == 'sounds':
            if line.startswith('INTRO:'): L['sounds']['intro'] = line[6:].strip()
            elif line.startswith('NOTE:'): L['sounds']['notes'].append(line[5:].strip())
            else: L['sounds']['rows'].append(parts(line))
            continue
        if line.startswith('## '):
            t = line[3:].strip()
            if sec == 'grammar': cur = {'id': slug(t), 'title': t, 'text': [], 'rows': [], 'ex': []}
            else: cur = {'id': slug(t), 'title': t, 'items': []}
            L[sec].append(cur); continue
        if cur is None: raise SystemExit('%s:%d item outside group: %s' % (path, n, line))
        if sec == 'grammar':
            if line.startswith('>'): cur['text'].append(line[1:].strip())
            elif line.startswith('row:'): cur['rows'].append(parts(line[4:]))
            elif line.startswith('ex:'):
                p = parts(line[3:]); 
                if len(p) < 2: raise SystemExit('%s:%d bad ex' % (path, n))
                cur['ex'].append(p)
            else: raise SystemExit('%s:%d bad grammar line: %s' % (path, n, line))
        else:
            p = parts(line)
            if len(p) < 2 or not p[0] or not p[1]: raise SystemExit('%s:%d bad item: %s' % (path, n, line))
            cur['items'].append(p)
    return L
def main():
    os.makedirs(OUT, exist_ok=True); idx = []
    for f in sorted(glob.glob(os.path.join(SRC, '*.txt'))):
        L = parse(f)
        for g in ('numbers', 'greetings', 'phrases', 'vocab'):
            ids = [x['id'] for x in L[g]]
            assert len(ids) == len(set(ids)), (f, g, 'duplicate group')
        if not L['sounds']: L['sounds'] = None
        cnt = sum(len(g['items']) for s in ('numbers', 'greetings', 'phrases', 'vocab') for g in L[s]) + sum(len(l['ex']) for l in L['grammar'])
        json.dump(L, open(os.path.join(OUT, L['id'] + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
        idx.append({'id': L['id'], 'name': L['name'], 'badge': L['badge'], 'count': cnt})
        print(L['id'], cnt)
    idx.sort(key=lambda x: x['name'])
    json.dump(idx, open(os.path.join(OUT, 'index.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
main()
