import json,sys,logging
logging.disable(logging.CRITICAL)
import build_conj as B
PRS=['je','tu','il','nous','vous','ils']
seen=set();V=[];bad=[]
IMP=('pleuvoir','falloir',"s'agir")
for l in open('verbs.txt',encoding='utf-8'):
    l=l.strip()
    if not l: continue
    inf,gl=l.split('|')
    if inf in seen: continue
    seen.add(inf)
    try:
        pred=json.loads(B.cg.conjugate(inf).to_json())['verb']['predicted']
    except Exception: pred=True
    if pred or inf=="s'en aller":
        bad.append(inf+'(pred)');continue
    rec={'v':inf,'g':gl,'f':{}}
    ok=True
    for t in ['sp','spa','cp','cpa']:
        try: rec['f'][t]={p:B.forms(inf,t,p) for p in PRS}
        except Exception: ok=False;break
        if inf in IMP:
            rec['f'][t]={p:(f if p=='il' else []) for p,f in rec['f'][t].items()}
            if not rec['f'][t]['il']: ok=False
        elif any(not rec['f'][t][p] for p in PRS): ok=False;break
    if ok: V.append(rec)
    else: bad.append(inf)
json.dump(V,open('../../data/safina/verbs.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(V),'bad',bad)
import os;print(os.path.getsize('../../data/safina/verbs.json')//1024,'KB')
for r in V:
    if r['v'] in("s'asseoir",'acquérir','mourir','résoudre',"s'en aller",'pleuvoir','vaincre','envoyer','falloir'):
        print(r['v'],r['f']['sp'],r['f']['cp']['nous'],r['f']['cpa']['ils'])
