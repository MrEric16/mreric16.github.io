import json,re,os,unicodedata,logging
logging.disable(logging.CRITICAL)
from wordfreq import zipf_frequency
D='/home/claude/repo_clone/'
raw={}
if os.path.exists(D+'scripts/safina/art_intro.json'):
    for x in json.load(open(D+'scripts/safina/art_intro.json',encoding='utf8')): raw[(x['tag'],x['req'])]=x
if os.path.exists(D+'scripts/safina/art_cache.jsonl'):
    for l in open(D+'scripts/safina/art_cache.jsonl',encoding='utf8'):
        try: x=json.loads(l)
        except: continue
        raw[(x['tag'],x['req'])]=x   # full text overrides intro
CANON={'science':'sciences','éthique':'philosophie','culture':'art','éducation':'études','santé':'psychologie','personnel':'quotidien','fiction':'quotidien','amitié':'quotidien'}
STOP=('Notes et références','Notes','Références','Voir aussi','Bibliographie','Liens externes','Annexes','Sources','Articles connexes','Liens internes','Publications','Discographie','Filmographie','Œuvres','Distinctions')
def slug(s): return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFD',s.lower()).encode('ascii','ignore').decode()).strip('-')
def clean(t):
    t=re.sub(r'\s*\((?:[^()]*\/[^()]*\/[^()]*)\)','',t)         # IPA
    t=re.sub(r'\[\d+\]','',t); t=t.replace('\t',' ')
    out=[];n=0
    for p in t.split('\n'):
        p=p.strip()
        if not p: continue
        if len(p)<70 and not re.search(r'[.!?:;]$',p) and p.strip() in STOP: break
        if len(p)>=70 or len(p)<70:
            out.append(p)
        n+=len(p)
        if n>4200 and len(p)>=70: break
    # drop trailing headings
    while out and len(out[-1])<70 and not re.search(r'[.!?]$',out[-1]): out.pop()
    return '\n'.join(out)
def vocab(text,k=8):
    toks=re.findall(r"[a-zà-ÿœ]{7,}",text)
    caps=set(w.lower() for w in re.findall(r"(?<![.!?\n] )(?<!^)\b[A-ZÀ-Ý][a-zà-ÿœ]{6,}",text))
    c={}
    for w in toks:
        if w in caps: continue
        z=zipf_frequency(w,'fr')
        if 2.3<=z<=3.7 and zipf_frequency(w,'en')<z-0.5 and not w.endswith('ing'): c[w]=z
    return [w for w,_ in sorted(c.items(),key=lambda kv:(kv[1],kv[0]))[:k]]
byf={};idx=[]
for (tag,req),x in raw.items():
    t=clean(x['text'])
    if len(t)<500: continue
    ct=CANON.get(tag,tag);f=slug(ct);aid=slug(x['title'])
    if any(i['id']==aid for i in idx): continue
    byf.setdefault(f,[]).append({'id':aid,'title':x['title'],'text':t,'words':vocab(t)})
    idx.append({'id':aid,'tag':ct,'title':x['title'],'f':f})
for f,A in byf.items():
    json.dump(A,open(D+f'data/safina/articles-{f}.json','w',encoding='utf8'),ensure_ascii=False,separators=(',',':'))
json.dump(idx,open(D+'data/safina/articles-index.json','w',encoding='utf8'),ensure_ascii=False,separators=(',',':'))
print(len(idx),'articles;',{f:len(a) for f,a in byf.items()})
tot=sum(len(a['text']) for A in byf.values() for a in A);print('chars',tot)
if idx:
    a=byf[idx[0]['f']][0];print(a['title'],a['words'],a['text'][:300])
