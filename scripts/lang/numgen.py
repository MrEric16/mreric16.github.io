#!/usr/bin/env python3
"""numgen.py <id>... : writes src/<id>.num.txt (Tens, Hundreds, Thousands, Big numbers) from the language's built JSON + specs in numspec.py."""
import json, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
NAMES = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
TENS = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def item(x):
    """'t|s|sc' -> (t,s,sc)"""
    if isinstance(x, tuple): return x
    p = x.split('|'); p += [''] * (3 - len(p))
    return (p[0].strip(), p[1].strip(), p[2].strip() or None)
def load(i):
    d = json.load(open(os.path.join(ROOT, 'data', 'lang', i + '.json'), encoding='utf-8'))
    m = {}
    for g in d['numbers']:
        for it in g['items']:
            if it[0] not in m:
                sc = it[3] if len(it) > 3 and it[3] else None
                m[it[0]] = (it[1], it[2] if len(it) > 2 else '', sc)
    return d, m
def join(items, sep=' ', ssep=None, scsep=None):
    ssep = sep if ssep is None else ssep
    scsep = sep if scsep is None else scsep
    t = sep.join(x[0] for x in items)
    s = ssep.join(x[1] for x in items if x[1]) if all(x[1] for x in items) else ''
    sc = scsep.join(x[2] for x in items) if all(x[2] for x in items) else None
    return (t, s, sc)
WARN = []
def fmt(en, it, script):
    t, s, sc = it
    CUR.append((en, it))
    if script:
        return '%s | %s | %s | %s' % (en, t, s, sc or t)
    return '%s | %s | %s' % (en, t, s) if s else '%s | %s' % (en, t)
CUR = []
def gen(i, S):
    d, m = load(i)
    del CUR[:]
    script = bool(d.get('script') or S.get('script'))
    ov = {k: item(v) for k, v in S.get('ov', {}).items()}   # english-key overrides (any item)
    def get(k):
        if k in ov: return ov[k]
        if k in m: return m[k]
        raise SystemExit('%s: missing %s' % (i, k))
    uov = {int(k): item(v) for k, v in S.get('u', {}).items()}
    def u(n):
        return uov[n] if n in uov else get(NAMES[n])
    sep, ssep, scsep = S.get('sep', ' '), S.get('ssep'), S.get('scsep')
    tsep, tssep, tscsep = S.get('tsep', sep), S.get('tssep', ssep), S.get('tscsep', scsep)
    out = ['DROP: ' + S.get('drop', 'tens-and-big-numbers'), '[numbers]', '## Tens']
    tens = S.get('tens')
    for k in TENS:
        out.append(fmt(k, get(k), script))
    if 'twenty-one' in ov or 'twenty-one' in m: out.append(fmt('twenty-one', get('twenty-one'), script))
    out.append('## Hundreds')
    hund = item(S['hund']) if 'hund' in S else None
    for n in range(1, 10):
        k = 'hundred-%d' % n
        if k in ov: it = ov[k]
        elif n == 1 and 'h1' in S: it = item(S['h1'])
        elif n == 1 and 'one hundred' in m: it = m['one hundred']
        else: it = join([hund, u(n)] if S.get('hpre') else [u(n), hund], sep, ssep, scsep)
        out.append(fmt(('one hundred' if n == 1 else NAMES[n] + ' hundred'), it, script))
    out.append('## Thousands')
    thou = item(S['thou']) if 'thou' in S else None
    for n in range(1, 10):
        k = 'thousand-%d' % n
        if k in ov: it = ov[k]
        elif n == 1 and 't1' in S: it = item(S['t1'])
        elif n == 1 and 'one thousand' in m: it = m['one thousand']
        else: it = join([thou, u(n)] if S.get('tpre') else [u(n), thou], tsep, tssep, tscsep)
        out.append(fmt(('one thousand' if n == 1 else NAMES[n] + ' thousand'), it, script))
    out.append('## Big numbers')
    for k, comp in (('ten thousand', lambda: join([get('ten'), thou], tsep, tssep, tscsep)),
                    ('one hundred thousand', lambda: join([item(S.get('h1')) if 'h1' in S else m['one hundred'], thou], tsep, tssep, tscsep)),
                    ('one million', None), ('one billion', None)):
        if k in S.get('skip', []): continue
        if k in ov: it = ov[k]
        elif k in m: it = m[k]
        elif comp: it = comp()
        else: raise SystemExit('%s: need %s' % (i, k))
        out.append(fmt(k, it, script))
    for en, it in CUR:
        if en in m and m[en][0] != it[0] and en not in ('ten','twenty'): print('  DIFF', i, en, 'old:', m[en][0], 'new:', it[0])
    return '\n'.join(out) + '\n'
if __name__ == '__main__':
    from numspec import SPEC
    ids = sys.argv[1:] or list(SPEC)
    for i in ids:
        txt = gen(i, SPEC[i])
        open(os.path.join(ROOT, 'scripts', 'lang', 'src', i + '.num.txt'), 'w', encoding='utf-8').write(txt)
        print('ok', i)
