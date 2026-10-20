#!/usr/bin/env python3
"""Removes hyphenated words (verbs/nouns/adverbs only), drops sides < 2 words, then drops repeated words. Usage: lexclean.py file [startline]"""
import sys
f=sys.argv[1]; start=int(sys.argv[2]) if len(sys.argv)>2 else 1
strip_h = not f.endswith('lex_adj.txt')
seen=set(); out=[]
for n,l in enumerate(open(f,encoding='utf8').read().split('\n'),1):
    if not l.strip() or l.startswith('#'): out.append(l); continue
    dom,body=l.split('|',1); sides=[]
    for sd in body.split('~'):
        ws=[]
        for w in sd.split(','):
            w=w.strip()
            if not w: continue
            if n>=start and strip_h and '-' in w: print('hyphen drop',w); continue
            if w.lower() in seen and n>=start: print('dup drop',w,n); continue
            seen.add(w.lower()); ws.append(w)
        sides.append(ws)
    if n>=start and any(len(x)<2 for x in sides):
        good=[x for x in sides if len(x)>=2]
        if len(good)<len(sides): print('side dropped line',n,l[:70])
        sides=good
    if not sides: print('LINE LOST',n); continue
    out.append(dom+'|'+' ~ '.join(','.join(x) for x in sides))
open(f,'w',encoding='utf8').write('\n'.join(out)+'\n')
