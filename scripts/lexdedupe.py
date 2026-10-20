#!/usr/bin/env python3
"""Drops words from lines >= START (1-based) that already appeared earlier in the same file (or in any other lex file). Prints what changed."""
import sys,re,glob
f=sys.argv[1]; start=int(sys.argv[2])
seen=set()
for g in glob.glob('scripts/content/lex_*.txt'):
    continue
    for l in open(g,encoding='utf8'):
        if l.strip() and not l.startswith('#'):
            for w in re.split(r'[,~|]',l.split('|',1)[1]): seen.add(w.strip().lower())
out=[]
for n,l in enumerate(open(f,encoding='utf8').read().split('\n'),1):
    if not l.strip() or l.startswith('#'): out.append(l); continue
    dom,body=l.split('|',1); sides=[]
    for sd in body.split('~'):
        ws=[]
        for w in sd.split(','):
            w=w.strip()
            if not w: continue
            if w.lower() in seen and n>=start: print('drop',w,'line',n); continue
            seen.add(w.lower()); ws.append(w)
        sides.append(ws)
    if n>=start:
        if any(len(x)<2 for x in sides):
            if len(sides)==2 and all(len(x)>=2 for x in sides): pass
            elif len(sides)==2:
                keep=[x for x in sides if len(x)>=2]
                print('SIDE TOO SMALL line',n, sides)
                sides=keep
            if not sides or len(sides[0])<2: print('LINE REMOVED',n,l[:50]); continue
    out.append(dom+'|'+' ~ '.join(','.join(x) for x in sides))
open(f,'w',encoding='utf8').write('\n'.join(out))
