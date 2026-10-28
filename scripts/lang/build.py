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
    import tempfile
    base = path[:-4]; adds = sorted(glob.glob(base + '.add*.txt'))
    if adds:
        txt = open(path, encoding='utf-8').read().rstrip('\n') + '\n'
        for a in adds: txt += open(a, encoding='utf-8').read().rstrip('\n') + '\n'
        tmp = tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False, encoding='utf-8'); tmp.write(txt); tmp.close(); path = tmp.name
    L = {'sounds': None, 'numbers': [], 'greetings': [], 'phrases': [], 'vocab': [], 'grammar': []}
    sec = None; cur = None
    for n, raw in enumerate(open(path, encoding='utf-8'), 1):
        line = raw.rstrip('\n')
        if not line.strip() or line.startswith('//'): continue
        m = re.match(r'^(NAME|ID|BADGE|NOTE|FLAG|SCRIPT):\s*(.*)$', line)
        if m and sec is None: L[m.group(1).lower()] = m.group(2).strip(); continue
        m = re.match(r'^\[(\w+)\]$', line.strip())
        if m:
            sec = m.group(1); cur = None
            if sec == 'sounds' and not L['sounds']: L['sounds'] = {'intro': '', 'rows': [], 'notes': []}
            continue
        if sec == 'sounds':
            if line.startswith('INTRO:'): L['sounds']['intro'] = line[6:].strip()
            elif line.startswith('NOTE:'): L['sounds']['notes'].append(line[5:].strip())
            else: L['sounds']['rows'].append(parts(line))
            continue
        if line.startswith('## '):
            t = line[3:].strip()
            old = [x for x in L[sec] if x['id'] == slug(t)]
            if old: cur = old[0]; continue
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
        elif line.startswith('>'):
            cur['note'] = (cur.get('note', '') + ' ' + line[1:].strip()).strip()
        else:
            p = parts(line)
            if len(p) < 2 or not p[0] or not p[1]: raise SystemExit('%s:%d bad item: %s' % (path, n, line))
            cur['items'].append(p)
    return L
def clean(p):
    while p and p[-1] == '': p.pop()
    return p
def script_map(L, path):
    sm = {}
    if os.path.exists(path):
        for raw in open(path, encoding='utf-8'):
            if '=>' in raw and not raw.startswith('//'):
                a, b = raw.rstrip('\n').split('=>', 1); sm[a.strip()] = b.strip()
    missing = set()
    def fix(p):
        if len(p) >= 4 and p[3]: return
        sc = sm.get(p[1])
        if sc:
            while len(p) < 3: p.append('')
            if len(p) == 3: p.append(sc)
            else: p[3] = sc
        else: missing.add(p[1])
    for sec in ('numbers', 'greetings', 'phrases', 'vocab'):
        for g in L[sec]:
            for it in g['items']: fix(it)
    for les in L['grammar']:
        for it in les['ex']: fix(it)
    return missing
def main():
    os.makedirs(OUT, exist_ok=True); idx = []
    for f in sorted([x for x in glob.glob(os.path.join(SRC, '*.txt')) if not x.endswith('.script.txt') and '.add' not in os.path.basename(x)]):
        L = parse(f)
        for g in ('numbers', 'greetings', 'phrases', 'vocab'):
            ids = [x['id'] for x in L[g]]
            assert len(ids) == len(set(ids)), (f, g, 'duplicate group')
        if not L['sounds']: L['sounds'] = None
        L['note'] = ''
        miss = set()
        if L.get('script'):
            miss = script_map(L, f[:-4] + '.script.txt')
            if miss:
                open('/tmp/al/missing_%s.txt' % L['id'], 'w', encoding='utf-8').write('\n'.join(sorted(miss)))
                print('  MISSING SCRIPT', L['id'], len(miss))
        cnt = sum(len(g['items']) for s in ('numbers', 'greetings', 'phrases', 'vocab') for g in L[s]) + sum(len(l['ex']) for l in L['grammar'])
        json.dump(L, open(os.path.join(OUT, L['id'] + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
        idx.append({'id': L['id'], 'name': L['name'], 'flag': L.get('flag', ''), 'script': bool(L.get('script')), 'count': cnt})
        print(L['id'], cnt)
    GROUPS = [('', ['uz']), ('Romance', ['es', 'pt', 'fr', 'it', 'ro']),
              ('Europe', ['de', 'nl', 'sv', 'pl', 'uk', 'cs', 'hu', 'fi', 'el']),
              ('Turkic', ['tr', 'az', 'kk', 'ky', 'ug', 'tt']), ('Caucasus', ['ka', 'hy']),
              ('Middle East and India', ['khl', 'fa', 'tg', 'ur', 'he', 'hi']),
              ('East and Southeast Asia', ['ja', 'ko', 'th', 'vi', 'id']), ('Africa', ['sw', 'yo', 'xh', 'am']),
              ('More languages', ['mn', 'eu', 'eo']),
              ('Niche and historic', ['la', 'grc', 'egy', 'sa', 'ine', 'arc', 'chg', 'cmn', 'non', 'ang', 'shk', 'cy', 'ga', 'haw', 'rom', 'jam', 'tok', 'sjn'])]
    pos = {}
    for gi, (gn, ids) in enumerate(GROUPS):
        for i, x in enumerate(ids): pos[x] = (gi, i, gn)
    for x in idx:
        assert x['id'] in pos, 'ungrouped ' + x['id']
        x['group'] = pos[x['id']][2]
    idx.sort(key=lambda x: pos[x['id']][:2])
    json.dump(idx, open(os.path.join(OUT, 'index.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
main()
