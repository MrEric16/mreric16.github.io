#!/usr/bin/env python3
"""Validates scripts/content/words_{phr,col}*.txt against data/vocab/words.json.
Line format: level|headword|definition|example"""
import json,glob,re,sys,os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')+'/'
def records(kind):
    out=[]
    for f in sorted(glob.glob(R+'scripts/content/words_%s*.txt'%kind)):
        for n,l in enumerate(open(f).read().splitlines(),1):
            if not l.strip() or l.startswith('#'): continue
            p=l.split('|')
            out.append((os.path.basename(f),n,p))
    return out
def check():
    d=json.load(open(R+'data/vocab/words.json'))
    have={r[0].lower() for r in d['w']}
    probs=[];seen={}
    for kind in ('phr','col'):
        for f,n,p in records(kind):
            if len(p)!=4: probs.append((f,n,'fields',len(p))); continue
            lv,h,df,ex=p; hl=h.lower().strip()
            if lv not in('1','2','3'): probs.append((f,n,'level',lv))
            if hl in have: probs.append((f,n,'exists in words.json',h))
            if hl in seen: probs.append((f,n,'duplicate of %s:%d'%seen[hl],h))
            seen[hl]=(f,n)
            if '--' in l or '—' in l or '–' in l if (l:='|'.join(p)) else False: probs.append((f,n,'dash',h))
            if re.search(r'\b'+re.escape(hl.split()[0])+r'\b',df.lower()) and len(hl.split())==1: probs.append((f,n,'definition has headword',h))
            if kind=='col' and hl not in ex.lower(): probs.append((f,n,'example lacks collocation',h))
            if not ex.endswith(('.','?','!')): probs.append((f,n,'example punctuation',h))
            if len(df)<5 or len(ex)<12: probs.append((f,n,'too short',h))
            if h!=h.strip() or '  ' in h: probs.append((f,n,'spacing',h))
            if re.search(r'\b(color|center|organize|realize|favorite|behavior)\b',ex+df,re.I): probs.append((f,n,'US spelling?',h))
    return probs,len(seen)
if __name__=='__main__':
    p,n=check()
    for x in p: print(x)
    print(n,'records;',len(p),'problems')
