#!/usr/bin/env python3
"""Merges scripts/content/wordforms_add.jsonl (extra items for existing families) and
wordforms_new*.jsonl (new families) into data/games/wordforms.json. Idempotent."""
import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wordforms_check as C
P=C.R+'data/games/wordforms.json'
d=json.load(open(P)); idx={x['b']:x for x in d}
na=ni=nf=0
for f,n,(b,forms,items) in C.lines('wordforms_add.jsonl'):
    fam=idx[b]; have={tuple(i) for i in fam['i']}
    for p,s in items:
        if [p,s] not in fam['i'] and p not in {q for q,_ in fam['i']}: fam['i'].append([p,s]); na+=1
for f,n,(b,forms,items) in C.lines('wordforms_new*.jsonl'):
    if b in idx: continue
    fam={'b':b,'f':forms,'i':[[p,s] for p,s in items]}; d.append(fam); idx[b]=fam; nf+=1; ni+=len(items)
json.dump(d,open(P,'w'),ensure_ascii=False,separators=(',',':'))
print('added',na,'items to existing,',nf,'new families,',ni,'items; total',len(d),'families,',sum(len(x['i']) for x in d),'sentences')
