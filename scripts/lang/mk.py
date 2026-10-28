#!/usr/bin/env python3
"""mk.py <id> [<id>...]: builds src/<id>.txt from work/<id>.head.txt + work/<id>.body.txt (+ work/skeleton.txt) + work/<id>.gram.txt.
body lines: '## Title' as in the skeleton and 'target | say | script' per item (same order as the skeleton). Name = LANG: line in head."""
import sys, os, re
W = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'work'); S = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
def rd(p): return [l.rstrip('\n') for l in open(p, encoding='utf-8')]
MISSING = set()
def lex_conv(path):
    lex = {}; punct = {}
    for l in open(path, encoding='utf-8'):
        l = l.rstrip('\n')
        if not l.strip() or l.startswith('//'): continue
        if l.startswith('#punct'):
            for kv in l.split()[1:]:
                a, b = kv.split('=', 1); punct[a] = b
            continue
        a, b = l.split('=', 1); lex[a.strip().lower()] = b.strip()
    mx = max([len(k.split()) for k in lex] or [1])
    def conv(s):
        toks = re.findall(r"[\w'\u2019-]+|[^\w\s]", s.lower()); out = []; i = 0
        while i < len(toks):
            t = toks[i]
            if not re.match(r"[\w'\u2019-]", t): out.append(punct.get(t, t)); i += 1; continue
            for n in range(min(mx, len(toks) - i), 0, -1):
                seg = toks[i:i + n]
                if any(not re.match(r"[\w'\u2019-]", z) for z in seg): continue
                k = ' '.join(seg)
                if k in lex: out.append(lex[k]); i += n; break
            else:
                MISSING.add(t); out.append('?' + t + '?'); i += 1
        return ' '.join(out).replace(' ' + punct.get('?', '?'), punct.get('?', '?')).replace(' ' + punct.get(',', ','), punct.get(',', ','))
    return conv
def load_conv(i):
    p = os.path.join(W, i + '.conv.py')
    if os.path.exists(p):
        ns = {}; exec(open(p, encoding='utf-8').read(), ns); return ns['conv']
    p = os.path.join(W, i + '.lex.txt')
    if os.path.exists(p): return lex_conv(p)
    return None
def load_rev(i):
    p = os.path.join(W, i + '.rev.py')
    if os.path.exists(p):
        ns = {}; exec(open(p, encoding='utf-8').read(), ns); return ns['rev']
    return None
def main(i):
    conv = load_conv(i); rev = load_rev(i)
    head = rd(os.path.join(W, i + '.head.txt'))
    L = [l[5:].strip() for l in head if l.startswith('LANG:')]
    L = L[0] if L else i
    head = [l for l in head if not l.startswith('LANG:')]
    sk = [l for l in rd(os.path.join(W, 'skeleton.txt')) if l.strip()]
    body = [l for l in rd(os.path.join(W, i + '.body.txt')) if l.strip() and not l.startswith('//')]
    gram = rd(os.path.join(W, i + '.gram.txt'))
    out = list(head) + ['']
    # group-wise alignment
    def split(lines):
        g = []; cur = None
        for l in lines:
            if re.match(r'^\[\w+\]$', l) or l.startswith('## '): cur = [l, [], []]; g.append(cur)
            elif l.startswith('>'): cur[2].append(l)
            else: cur[1].append(l)
        return g
    a, b = split(sk), split(body)
    if [x[0] for x in a] != [x[0] for x in b]:
        for x, y in zip(a, b):
            if x[0] != y[0]: print('HEADER MISMATCH', x[0], '<>', y[0]); break
        raise SystemExit('%s: group list mismatch (%d vs %d)' % (i, len(a), len(b)))
    bad = False
    for x, y in zip(a, b):
        if len(x[1]) != len(y[1]):
            print('COUNT', i, x[0], len(x[1]), 'vs', len(y[1])); bad = True
    if bad: raise SystemExit(1)
    if rev:
        for y in b:
            ny = []
            for t in y[1]:
                pp = [z.strip() for z in t.split('|')]
                while len(pp) < 2: pp.append('')
                ny.append(' | '.join([rev(pp[0]), pp[1], pp[0]]))
            y[1] = ny
    for x, y in zip(a, b):
        out.append(x[0]); out += y[2]
        for en, t in zip(x[1], y[1]):
            tt = t
            if conv:
                pp = [z.strip() for z in t.split('|')]
                while len(pp) < 2: pp.append('')
                tt = ' | '.join(pp[:2] + [conv(pp[0])])
            out.append(en.replace('{L}', L) + ' | ' + tt)
    out.append('')
    if conv:
        g2 = []
        for l in gram:
            if l.startswith('ex:') or l.startswith('row:'):
                kind = l[:l.index(':') + 1]; pp = [z.strip() for z in l[len(kind):].split('|')]
                if kind == 'ex:':
                    while len(pp) < 3: pp.append('')
                    l = kind + ' ' + ' | '.join(pp[:3] + [conv(pp[1])])
                elif len(pp) == 2: l = kind + ' ' + ' | '.join(pp + [conv(pp[1])])
            g2.append(l)
        gram = g2
    if rev:
        g2 = []
        for l in gram:
            if l.startswith('ex:') or l.startswith('row:'):
                kind = l[:l.index(':') + 1]; pp = [z.strip() for z in l[len(kind):].split('|')]
                if kind == 'ex:':
                    while len(pp) < 3: pp.append('')
                    l = kind + ' ' + ' | '.join([pp[0], rev(pp[1]), pp[2], pp[1]])
                elif len(pp) == 2: l = kind + ' ' + ' | '.join([pp[0], rev(pp[1]), pp[1]])
            g2.append(l)
        gram = g2
    out += gram
    open(os.path.join(S, i + '.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('ok', i)
if __name__ == "__main__":
  for i in sys.argv[1:]:
    main(i)
    if MISSING:
        open('/tmp/al/miss_%s.txt' % i, 'w', encoding='utf-8').write('\n'.join(sorted(MISSING)))
        print('MISSING WORDS', len(MISSING)); sys.exit(2)
