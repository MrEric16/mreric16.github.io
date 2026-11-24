import json,logging
logging.disable(logging.CRITICAL)
import build_conj as B
PRS=['je','tu','il','nous','vous','ils']
TS=['pr','pc','imp','pqp','ps','pa','fs','fa','cp','cpa','sp','spa','sip','spp']
seen=set();V=[];bad=[]
for fn in ('verbs.txt','verbs_extra.txt'):
  for l in open(fn,encoding='utf-8'):
    l=l.strip()
    if not l: continue
    inf,gl=l.split('|')
    if inf in seen or inf in ("s'en aller",'falloir'): continue
    seen.add(inf)
    try: pred=json.loads(B.cg.conjugate(inf).to_json())['verb']['predicted']
    except Exception: pred=True
    if pred: bad.append(inf+'(pred)');continue
    f={};ok=True
    try:
        for t in TS:
            f[t]=['/'.join(B.forms(inf,t,p)) for p in PRS]
    except Exception: ok=False
    if not ok: bad.append(inf);continue
    avail=[i for i,p in enumerate(PRS) if all(f[t][i] for t in TS)]
    if len(avail)<6:
        if avail not in ([2],[2,5]): bad.append(inf+'(defective)');continue
        for t in TS:
            f[t]=[x if i in avail else '' for i,x in enumerate(f[t])]
    V.append({'v':inf,'g':gl,'f':f})
json.dump(V,open('../../data/safina/verbs.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
import os;print(len(V),'bad',bad);print(os.path.getsize('../../data/safina/verbs.json')//1024,'KB')
for r in V:
    if r['v'] in('être','pouvoir','mourir','vaincre','pleuvoir','parler'):
        print(r['v'],{t:r['f'][t][2:4] for t in ('ps','sip','pa','cpa')})
