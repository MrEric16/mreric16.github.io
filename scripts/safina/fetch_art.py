import json,time,sys,urllib.parse,urllib.request,re
UA="SafinaLearningPage/1.0 (https://mreric16.github.io; teacher project; contact via GitHub MrEric16)"
out=[];seen=set()
for l in open('art_titles.txt',encoding='utf8'):
    tag,t=l.strip().split('|')
    if (tag,t) in seen: continue
    seen.add((tag,t))
    u="https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&exsectionformat=plain&redirects=1&format=json&titles="+urllib.parse.quote(t)
    for k in range(4):
        try:
            r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=30).read().decode()
            d=json.loads(r);break
        except Exception as e:
            d=None;time.sleep(5*(k+1))
    time.sleep(1.2)
    if not d: print('FAIL',t);continue
    p=list(d['query']['pages'].values())[0]
    x=p.get('extract')
    if not x: print('MISSING',t);continue
    out.append({'tag':tag,'title':p['title'],'text':x})
    print('ok',t,len(x),flush=True)
json.dump(out,open('/home/claude/repo_clone/scripts/safina/art_raw.json','w',encoding='utf8'),ensure_ascii=False)
