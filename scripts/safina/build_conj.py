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
_PP={}
def pp(inf):
    """masculine singular past participle, taken from the 'il' passé composé"""
    if inf not in _PP:
        _PP[inf]=None
        for x in moods(inf)['indicatif']['passé-composé']:
            if x['pr']=='il':
                _PP[inf]=STRIP.sub('',x['c'][0]).strip().split(' ')[-1]; break
    return _PP[inf]
def variants(a,pr='nous',inf=None):
    w=a.split(' ')
    if len(w)<2 or w[-2] not in etre(): return [a]
    base=pp(inf) if inf else None
    if not base or not w[-1].startswith(base[:-1]): return [a]
    m_pl=base if base[-1] in 'sx' else base+'s'
    # nous = several people: plural agreement only. vous = plural first, singular (polite vous) also correct.
    ends=[m_pl,base+'es'] if pr=='nous' else [m_pl,base+'es',base,base+'e']
    out=[]
    for e in ends:
        v=' '.join(w[:-1]+[e])
        if v not in out: out.append(v)
    return out
def forms(inf,t,pr):
    m,te=TENSE[t]
    out=[]
    for x in moods(inf)[m][te]:
        if x['pr']==pr:
            for c in x['c']:
                a=STRIP.sub('',c).strip()
                for v in (variants(a,pr,inf) if pr in ('nous','vous') else [a]):
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
