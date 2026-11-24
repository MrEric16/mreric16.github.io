import json,time,urllib.parse,urllib.request,urllib.error,os
UA="SafinaLearningPage/1.0 (https://mreric16.github.io; teacher project; contact via GitHub MrEric16)"
cache='art_cache.jsonl'
done={}
if os.path.exists(cache):
    for l in open(cache,encoding='utf8'):
        try:
            d=json.loads(l);done[(d['tag'],d['req'])]=d
        except: pass
# seed from first run? (not saved) -> refetch
titles=[]
seen=set()
for l in open('art_titles.txt',encoding='utf8'):
    tag,t=l.strip().split('|')
    if (tag,t) not in seen: seen.add((tag,t));titles.append((tag,t))
f=open(cache,'a',encoding='utf8')
for tag,t in titles:
    if (tag,t) in done: continue
    u="https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&exsectionformat=plain&redirects=1&format=json&titles="+urllib.parse.quote(t)
    d=None
    for k in range(8):
        try:
            r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=40).read().decode()
            d=json.loads(r);break
        except urllib.error.HTTPError as e:
            w=int(e.headers.get('Retry-After') or 0) or 30*(k+1)
            print('HTTP',e.code,t,'wait',w,flush=True);time.sleep(min(w,120))
        except Exception as e:
            print('ERR',t,e,flush=True);time.sleep(10)
    if not d: print('FAIL',t,flush=True);continue
    p=list(d['query']['pages'].values())[0]
    x=p.get('extract')
    if not x: print('MISSING',t,flush=True);continue
    f.write(json.dumps({'tag':tag,'req':t,'title':p['title'],'text':x},ensure_ascii=False)+'\n');f.flush()
    print('ok',t,len(x),flush=True)
    time.sleep(3)
