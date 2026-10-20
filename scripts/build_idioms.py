#!/usr/bin/env python3
"""Builds data/games/idioms.json for Idiom Match.
Sources: IDIOM_OF_THE_DAY_POOL in index.html (read only), idiom records (topic 15) in
data/vocab/words.json, and hand-written scripts/content/idioms_new*.txt.
Output: {"i":[[idiom,meaning,example],...], "t":[[tagIdx,...],...], "x":{"idx":[idx,...]}}
Two idioms may never appear together in one question if they share a tag (same meaning
family) or are listed in x (high meaning-word overlap)."""
import json,re,glob,difflib,os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')+'/'
def norm(s):
    s=s.lower().replace("’","'"); s=re.sub(r"[^a-z' ]"," ",s)
    s=re.sub(r"\b(someone|somebody|one's|your|yourself|my|his|her|their|our)\b","",s)
    s=re.sub(r"^(a|an|the|to|it is|it's|be|get|have|you)\s+","",s.strip())
    s=re.sub(r"\b(a|an|the|to|in|on|of)\b"," ",s)
    return re.sub(r"\s+"," ",s).strip()
def load():
    src=open(R+'index.html').read()
    i=src.index('IDIOM_OF_THE_DAY_POOL = ')+len('IDIOM_OF_THE_DAY_POOL = '); j=src.index('];',i)+1
    items=[dict(idiom=p['idiom'],meaning=p['meaning'],example=p['example'],group=None) for p in json.loads(src[i:j])]
    d=json.load(open(R+'data/vocab/words.json'))
    for r in d['w']:
        if r[2]==15:
            m=r[4].strip(); m=m[0].upper()+m[1:]; m=m if m.endswith('.') else m+'.'
            items.append(dict(idiom=r[0][0].upper()+r[0][1:],meaning=m,example=r[5],group=None))
    for f in sorted(glob.glob(R+'scripts/content/idioms_new*.txt')):
        for l in open(f).read().splitlines():
            if not l.strip() or l.startswith('#'): continue
            g,i,m,e=l.split('|'); items.append(dict(idiom=i,meaning=m,example=e,group=g))
    return items
def dedupe(items):
    out=[];keys=[]
    for it in items:
        k=norm(it['idiom'])
        if any(k==k2 or difflib.SequenceMatcher(None,k,k2).ratio()>0.88 for k2 in keys): continue
        keys.append(k); out.append(it)
    return out
# meaning-family tags, matched against the meaning text
TAGS={
 'angry':r"\b(angry|furious|temper|irritate|annoy)",'happy':r"\b(happy|delighted|joy|pleased|cheerful)",
 'sad':r"\b(sad|depress|unhappy|miserable)",'easy':r"\b(easy|simple|effortless|without (any )?(problems|trouble))",
 'difficult':r"\b(difficult|hard to|tough|challeng)",'expensive':r"\b(expensive|high price|too much money|pay too)",
 'cheap':r"\b(cheap|inexpensive|low price|for far less)",'poor':r"\b(poor|short of money|little money|not enough money)",
 'rich':r"\b(rich|wealthy|great deal of money|lot of money)",'die':r"\b(die|dead|death)\b",
 'secret':r"\b(secret|private|confidential)",'trouble':r"\b(in trouble|serious trouble)",
 'start':r"\b(start|begin|first step|beginning)",'end':r"\b(end|finish|stop|cease)",
 'fail':r"\b(fail|failure|unsuccessful|collapse)",'succeed':r"\b(succe|win|triumph|achieve)",
 'tired':r"\b(tired|exhaust|energy)",'ill':r"\b(ill|sick|unwell|illness)\b",'quick':r"\b(quick|fast|soon|immediately|rapid)",
 'slow':r"\bslow",'calm':r"\b(calm|relax)",'nervous':r"\b(nervous|anxious|frighten|afraid|worr)",
 'surprise':r"\b(surpris|shock|unexpected)",'embarrass':r"\b(embarrass|foolish|ashamed)",
 'lie':r"\b(deceiv|trick|lie\b|fool someone|dishonest|cheat)",'honest':r"\b(honest|truth|frank|directly)",
 'ignore':r"\b(ignor|not listen|refuse to listen)",'listen':r"\blisten",'watch':r"\b(watch|look carefully|observe)",
 'understand':r"\b(understand|make sense|grasp)",'forget':r"\b(forget|forgot|remember|memor)",
 'help':r"\bhelp",'agree':r"\bagree",'argue':r"\b(argue|argument|disagree|quarrel)",
 'chance':r"\b(luck|chance)",'risk':r"\b(risk|danger)",'effort':r"\b(effort|work hard|try hard|hard work)",
 'lazy':r"\b(lazy|idle|do nothing|avoid work)",'busy':r"\b(busy|too much work|lot to do)",
 'similar':r"\b(similar|alike|same as|exact copy|resembl)",'different':r"\b(different|differ)",
 'important':r"\b(important|essential|vital|necessary)",'money':r"\b(money|profit|debt|owe)",
 'time':r"\b(time|late|early|hour|deadline)",'praise':r"\b(prais|compliment|credit)",
 'criticise':r"\b(critic|scold|blame|complain)",'control':r"\b(control|in charge|power)",
 'decide':r"\b(decid|undecided|choose|decision)",'wait':r"\b(wait|patien)",
 'love':r"\b(love|romantic|marry|married)",'talk':r"\b(talk|chat|speak|say|conversation)",
 'stubborn':r"\b(stubborn|refuse to change)",'proud':r"\b(proud|boast|show off|arrogan)",
 'jealous':r"\b(jealous|envy)",'crazy':r"\b(crazy|mad\b|insane)",'clever':r"\b(clever|intelligent|smart)",
 'stupid':r"\b(stupid|foolish|not (very )?intelligent)",'change':r"\b(change|different way|new way)",
 'safe':r"\b(safe|unharmed|careful|caution)",'unimportant':r"\b(unimportant|not important|small amount)",
 'kind':r"\b(kind|generous)",'mean':r"\b(mean\b|stingy|unwilling to spend)",
 'noisy':r"\b(noise|noisy|loud)",'quiet':r"\b(quiet|silent|silence)",
 'rumour':r"\b(rumour|gossip|spread)",'common':r"\b(common|usual|typical|ordinary)",'rare':r"\b(rare|seldom|unusual|rarely)",
 'obvious':r"\b(obvious|clear|plain)",'certain':r"\b(certain|sure|definite)",'uncertain':r"\b(uncertain|unsure|undecided|unclear)",
}
TAGS={k:re.compile(v,re.I) for k,v in TAGS.items()}
STOP=set("a an the to of in on at or and is are be was it its that this who which with for from by as not very more most than into up out do does doing your you one someone something their they them his her we our just can may so such have has had been being when what while about over also but if".split())
def stem(w): return re.sub(r"(ing|ed|es|s|ly)$","",w)
def toks(s): return {stem(w) for w in re.findall(r"[a-z]+",s.lower()) if w not in STOP and len(w)>2}
def main():
    items=dedupe(load())
    names=list(TAGS); gnames={}
    T=[]
    for it in items:
        ts=set(i for i,n in enumerate(names) if TAGS[n].search(it['meaning']))
        if it['group']:
            ts.add(len(names)+gnames.setdefault(it['group'],len(gnames)))
        T.append(sorted(ts))
    tk=[toks(it['meaning']) for it in items]
    x={}
    for a in range(len(items)):
        for b in range(a+1,len(items)):
            if set(T[a])&set(T[b]): continue
            i=tk[a]&tk[b]
            if i:
                j=len(i)/len(tk[a]|tk[b])
                if j>=0.25 or len(i)>=2:
                    x.setdefault(a,[]).append(b); x.setdefault(b,[]).append(a)
    # meaning must be unique and must not contain the idiom's own key words
    seen=set(); keep=[]
    for n,it in enumerate(items):
        if it['meaning'] in seen: continue
        seen.add(it['meaning']); keep.append(n)
    remap={old:new for new,old in enumerate(keep)}
    out={'i':[[items[n]['idiom'],items[n]['meaning'],items[n]['example']] for n in keep],
         't':[T[n] for n in keep],
         'x':{str(remap[a]):[remap[b] for b in v if b in remap] for a,v in x.items() if a in remap}}
    json.dump(out,open(R+'data/games/idioms.json','w'),separators=(',',':'),ensure_ascii=False)
    print(len(out['i']),'idioms;',sum(len(v) for v in out['x'].values())//2,'extra conflict pairs;',os.path.getsize(R+'data/games/idioms.json')//1024,'KB')
if __name__=='__main__': main()
