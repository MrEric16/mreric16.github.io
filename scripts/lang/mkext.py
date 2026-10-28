#!/usr/bin/env python3
"""mkext.py <id>...: work/<id>.ext.txt ('english :: target | say [| script]', with the same [section]/## headers as work/ext.txt)
-> src/<id>.add2.txt. Applies <id>.conv/.lex/.rev like mk.py."""
import sys, os, re
sys.argv_save = sys.argv; ids = sys.argv[1:]; sys.argv = ['mk.py']
import mk
W = mk.W; S = mk.S
import glob
def run(i):
    conv = mk.load_conv(i); rev = mk.load_rev(i)
    sk = [l.rstrip('\n') for l in open(os.path.join(W, 'ext.txt'), encoding='utf-8') if l.strip()]
    D = {}
    for f in sorted(glob.glob(os.path.join(W, i + '.ext*.txt'))):
        for r in open(f, encoding='utf-8'):
            r = r.rstrip('\n')
            if ' :: ' not in r or r.startswith('//'): continue
            en, t = r.split(' :: ', 1); D[en.strip()] = t
    keys = [s for s in sk if not s.startswith(('[', '##'))]
    miss = [k for k in keys if k not in D]; extra = [k for k in D if k not in set(keys)]
    if extra: print(i, 'EXTRA (ignored)', extra[:10])
    if miss and os.environ.get('PARTIAL'):
        print(i, 'PARTIAL: skipping', len(miss), 'items without a reliable translation')
        miss = []
    if miss:
        print(i, 'MISSING', len(miss)); open(os.path.join(W, i + '.missing.txt'), 'w', encoding='utf-8').write('\n'.join(miss) + '\n')
        for k in miss[:400]: print('  ', k)
        return 1
    out = []
    for s in sk:
        if s.startswith(('[', '##')): out.append(s); continue
        if s not in D: continue
        pp = [z.strip() for z in D[s].split('|')]
        while len(pp) < 2: pp.append('')
        if rev: pp = [rev(pp[0]), pp[1], pp[0]]
        elif conv and len(pp) < 3: pp = pp[:2] + [conv(pp[0])]
        out.append(s + ' | ' + ' | '.join(pp))
    # drop group headers (## ...) that ended up with no items (partial mode)
    res = []
    for k, x in enumerate(out):
        if x.startswith('##'):
            nxt = out[k+1] if k+1 < len(out) else ''
            if not nxt or nxt.startswith(('##', '[')): continue
        res.append(x)
    out = res
    open(os.path.join(S, i + '.add2.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('ok', i, len([x for x in out if '|' in x])); return 0
for i in ids:
    run(i)
    if mk.MISSING:
        print('MISSING WORDS', i, sorted(mk.MISSING)[:20]); mk.MISSING.clear()
