import re,json,sys,logging
logging.disable(logging.CRITICAL)
from verbecc import CompleteConjugator
cg=CompleteConjugator('fr')
cache={}
def moods(v):
    if v not in cache: cache[v]=json.loads(cg.conjugate(v).to_json())['moods']
    return cache[v]
TENSE={'sp':('subjonctif','présent'),'spa':('subjonctif','passé'),'sip':('subjonctif','imparfait'),'spp':('subjonctif','plus-que-parfait'),'cp':('conditionnel','présent'),'cpa':('conditionnel','passé'),'pr':('indicatif','présent'),'imp':('indicatif','imparfait'),'ps':('indicatif','passé-simple'),'fs':('indicatif','futur-simple'),'fa':('indicatif','futur-antérieur'),'pc':('indicatif','passé-composé'),'pqp':('indicatif','plus-que-parfait'),'pa':('indicatif','passé-antérieur')}
PR={'je','tu','il','elle','on','nous','vous','ils','elles'}
STRIP=re.compile(r"^(?:que |qu')?(?:j'|je |tu |il |elle |on |nous |vous |ils |elles )")
_ETRE=None
def etre():
    global _ETRE
    if _ETRE is None:
        _ETRE=set()
        M=moods('être')
        for mo,tes in (('indicatif',('présent','imparfait','futur-simple','passé-simple')),('conditionnel',('présent',)),('subjonctif',('présent','imparfait'))):
            for te in tes:
                for x in M[mo][te]:
                    for c in x['c']:
                        _ETRE.add(STRIP.sub('',c).strip())
    return _ETRE
def variants(a):
    w=a.split(' ')
    if len(w)<2 or w[-2] not in etre(): return [a]
    p=w[-1];base=p
    for suf in ('es','e','s'):
        if p.endswith(suf) and len(p)>len(suf)+1: base=p[:-len(suf)];break
    return [' '.join(w[:-1]+[base+x]) for x in ('','e','s','es')]
def forms(inf,t,pr):
    m,te=TENSE[t]
    out=[]
    for x in moods(inf)[m][te]:
        if x['pr']==pr:
            for c in x['c']:
                a=STRIP.sub('',c).strip()
                for v in (variants(a) if pr in ('nous','vous') else [a]):
                    if v not in out: out.append(v)
    return out
if __name__=='__main__':
    items=[];bad=[]
    for l in open('frames.txt',encoding='utf-8'):
        l=l.strip()
        if not l: continue
        txt,note=l.split('|')
        mm=re.search(r"\{([^:}]+):([a-z]+):([a-z]+)\}",txt)
        inf,t,pr=mm.groups();inf=inf.lower()
        try: a=forms(inf,t,pr)
        except Exception as e: a=[]
        if not a: bad.append((txt,inf,t,pr));continue
        pre,post=txt[:mm.start()],txt[mm.end():]
        items.append({'pre':pre,'post':post,'inf':inf,'t':t,'pr':pr,'ans':a,'note':note})
    json.dump(items,open('../../data/safina/conj-sentences.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
    print(len(items),'bad',bad)
    for i in items[::6]: print(i['pre'],'[',i['ans'],']',i['post'])
