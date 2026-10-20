#!/usr/bin/env python3
"""Appends hand-written phrasal verbs, collocations (scripts/content/words_*.txt) and
the Idiom Match idioms (data/games/idioms.json) to data/vocab/words.json. Idempotent:
a headword already present is skipped."""
import json,glob,os,sys,difflib,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wordscheck, build_idioms
R=wordscheck.R
P=R+'data/vocab/words.json'
d=json.load(open(P),object_pairs_hook=None)
have={r[0].lower() for r in d['w']}
added={'phr':0,'col':0,'idm':0}
for kind,topic in (('phr',19),('col',3)):
    for f,n,p in wordscheck.records(kind):
        lv,h,df,ex=p
        if h.lower() in have: continue
        d['w'].append([h,kind,topic,int(lv),df,ex]); have.add(h.lower()); added[kind]+=1
idm_keys=[build_idioms.norm(r[0]) for r in d['w'] if r[2]==15]
ij=json.load(open(R+'data/games/idioms.json'))
for idiom,meaning,example in ij['i']:
    h=idiom[0].lower()+idiom[1:] if not idiom.startswith(("I ","I'")) else idiom
    if h.lower() in have: continue
    k=build_idioms.norm(idiom)
    if any(k==k2 or difflib.SequenceMatcher(None,k,k2).ratio()>0.88 for k2 in idm_keys): continue
    m=meaning.strip().rstrip('.'); m=m[0].lower()+m[1:]
    lv=2 if len(idiom.split())<=3 else 3
    d['w'].append([h,'idm',15,lv,m,example]); have.add(h.lower()); idm_keys.append(k); added['idm']+=1
json.dump(d,open(P,'w'),ensure_ascii=False,separators=(',',':'))
print(added,len(d['w']))
