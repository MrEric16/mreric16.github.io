import os,re,json,sys,collections
SRC=os.path.join(os.path.dirname(__file__),'src')
OUT=os.path.join(os.path.dirname(__file__),'..','..','data','vocab','words.json')
TOPICS={'acad1':'Academic','acad2':'Academic','env':'Environment','edu':'Education','tech':'Technology','health':'Health','soc':'Society','work':'Work','econ':'Economy','media':'Media','travel':'Travel','crime':'Crime','fam':'Family','sci':'Science','cult':'Culture','phr1':'Phrasal verbs','phr2':'Phrasal verbs','idm1':'Idioms','idm2':'Idioms','link':'Linking words','col1':'Collocations','col2':'Collocations','gov':'Government','psych':'Psychology','food':'Food','sport':'Sport','arts':'Arts','urban':'Cities','trans':'Transport','desc':'Describing','task1':'Task 1 language','lang':'Language','shop':'Shopping','home':'Home and leisure','more':'Academic','phr3':'Phrasal verbs','idm3':'Idioms','col3':'Collocations','acad3':'Academic','acad4':'Academic','acad5':'Academic','more2':'Academic'}
POS={'n','v','adj','adv','phr','idm','col','conj','prep'}
seen={};errs=[];warn=[]
BR={'color':'colour','center':'centre','organize':'organise','realize':'realise','behavior':'behaviour','favorite':'favourite','analyze':'analyse','recognize':'recognise','skeptical':'sceptical'}
for fn in sorted(os.listdir(SRC)):
    if not fn.endswith('.txt'):continue
    key=fn[:-4]
    if key not in TOPICS and key.endswith('x') and key[:-1] in TOPICS: TOPICS[key]=TOPICS[key[:-1]]
    if key not in TOPICS:errs.append('no topic for '+key);continue
    for i,l in enumerate(open(os.path.join(SRC,fn),encoding='utf8'),1):
        l=l.rstrip('\n')
        if not l.strip():continue
        p=l.split('|')
        loc=f'{fn}:{i}'
        if len(p)!=5:errs.append(f'{loc} fields={len(p)}: {l[:60]}');continue
        w,pos,band,d,ex=[x.strip() for x in p]
        if pos not in POS:errs.append(f'{loc} pos {pos}');continue
        if band not in('6','7','8'):errs.append(f'{loc} band {band}');continue
        if '--' in l or '—' in l or '–' in l:errs.append(f'{loc} dash');continue
        if re.search(r'\bgotten\b',l):errs.append(f'{loc} gotten');continue
        for a,b in BR.items():
            if re.search(r'\b'+a,l,re.I):warn.append(f'{loc} US spelling {a}')
        if not d or not ex:errs.append(f'{loc} empty');continue
        stem=re.sub(r'[^a-z ]','',w.lower())
        first=stem.split()[0] if stem else stem
        root=first[:max(4,len(first)-3)]
        if len(w.split())==1 and re.search(r'\b'+re.escape(root),d.lower()):warn.append(f'{loc} def uses root of {w}')
        if root not in ex.lower():warn.append(f'{loc} example lacks {w}')
        k=w.lower()
        if k in seen:continue
        seen[k]=[w,pos,TOPICS[key],int(band)-5,d,ex]
tl=sorted({v[2] for v in seen.values()})
rows=[[v[0],v[1],tl.index(v[2]),v[3],v[4],v[5]] for v in seen.values()]
os.makedirs(os.path.dirname(OUT),exist_ok=True)
json.dump({'t':tl,'w':rows},open(OUT,'w',encoding='utf8'),ensure_ascii=False,separators=(',',':'))
print('entries',len(rows),'topics',len(tl),'bytes',os.path.getsize(OUT))
print('pos',collections.Counter(r[1] for r in rows))
print('errors',len(errs),'warnings',len(warn))
for e in errs[:40]:print('E',e)
for e in warn[:400]:print('W',e)
