#!/usr/bin/env python3
"""Validates scripts/content/wordforms_*.jsonl. Line: [base, forms|null, [[pos, sentence], ...]]"""
import json,glob,os,re,sys
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')+'/'
def lines(pat):
    for f in sorted(glob.glob(R+'scripts/content/'+pat)):
        for n,l in enumerate(open(f).read().splitlines(),1):
            if l.strip(): yield os.path.basename(f),n,json.loads(l)
def check():
    base=json.load(open(R+'data/games/wordforms.json'))
    fam={x['b']:x for x in base}
    probs=[]; newb={}
    for f,n,(b,forms,items) in lines('wordforms_new*.jsonl'):
        if b in fam or b in newb: probs.append((f,n,'family exists',b))
        newb[b]={'b':b,'f':forms,'i':[]}
        if not forms: probs.append((f,n,'no forms',b))
    allfam=dict(fam); allfam.update(newb)
    for f,n,(b,forms,items) in list(lines('wordforms_new*.jsonl'))+list(lines('wordforms_add.jsonl')):
        fm=forms or (allfam.get(b) or {}).get('f')
        if not fm: probs.append((f,n,'unknown family',b)); continue
        seen=set(p for p,_ in (fam.get(b,{}).get('i') or []))
        for p,s in items:
            if p not in fm: probs.append((f,n,'pos %s missing in forms'%p,b))
            if s.count('___')!=1: probs.append((f,n,'blank count',b))
            if p in seen: probs.append((f,n,'pos %s repeated'%p,b))
            seen.add(p)
            if re.search(r'--|—|–',s): probs.append((f,n,'dash',b))
            if p in fm and re.search(r'\b'+re.escape(fm[p])+r'\b',s,re.I): probs.append((f,n,'answer visible in sentence',b))
            if not s.rstrip().endswith(('.','?','!')): probs.append((f,n,'punctuation',b))
        for p,w in (forms or {}).items():
            if p not in('n','v','adj','adv') or not re.fullmatch(r"[a-z]+",w): probs.append((f,n,'bad form %s=%s'%(p,w),b))
    return probs,len(newb)
if __name__=='__main__':
    p,n=check()
    for x in p: print(x)
    print(n,'new families;',len(p),'problems')
