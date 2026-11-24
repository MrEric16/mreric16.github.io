import json,time,urllib.parse,urllib.request,urllib.error
UA="SafinaLearningPage/1.0 (https://mreric16.github.io; teacher project; contact via GitHub MrEric16)"
T=[];seen=set()
for l in open('art_titles.txt',encoding='utf8'):
    tag,t=l.strip().split('|')
    if (tag,t) not in seen: seen.add((tag,t));T.append((tag,t))
out={}
for i in range(0,len(T),20):
    ch=T[i:i+20]
    u="https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1&explaintext=1&exlimit=20&redirects=1&format=json&titles="+urllib.parse.quote('|'.join(t for _,t in ch))
    d=None
    for k in range(8):
        try:
            d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60).read().decode());break
        except urllib.error.HTTPError as e:
            w=int(e.headers.get('Retry-After') or 0) or 30*(k+1);print('HTTP',e.code,'wait',w,flush=True);time.sleep(min(w,120))
        except Exception as e: print('ERR',e,flush=True);time.sleep(10)
    if not d: print('FAIL batch',i);continue
    q=d['query'];red={}
    for r in q.get('normalized',[])+q.get('redirects',[]): red[r['from']]=r['to']
    pages={p['title']:p for p in q['pages'].values()}
    for tag,t in ch:
        n=t
        for _ in range(3): n=red.get(n,n)
        p=pages.get(n)
        if p and p.get('extract'): out[(tag,t)]={'tag':tag,'req':t,'title':p['title'],'text':p['extract']}
        else: print('MISSING',t)
    print('batch',i,len(out),flush=True);time.sleep(5)
json.dump([dict(v) for v in out.values()],open('art_intro.json','w',encoding='utf8'),ensure_ascii=False)
