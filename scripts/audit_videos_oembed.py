import json, requests, concurrent.futures as cf, re
rows=json.load(open("scripts/watch_videos_all.json"))
H={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) Chrome/124 Safari/537.36","Accept-Language":"en-US,en;q=0.9"}
def w(s): return {x for x in re.findall(r"[a-z0-9]+",s.lower()) if len(x)>3}
def one(r):
    o=dict(r)
    for _ in range(3):
        try:
            e=requests.get("https://www.youtube.com/oembed",params={"url":"https://www.youtube.com/watch?v="+r["id"],"format":"json"},headers=H,timeout=20)
            o["oembed"]=e.status_code
            if e.status_code==200:
                j=e.json(); o["real_title"]=j.get("title"); o["channel"]=j.get("author_name")
                a,b=w(r["title"]),w(j.get("title",""))
                o["overlap"]=round(len(a&b)/max(1,len(a)),2)
            if e.status_code in (200,401,404): break
        except Exception as ex: o["oembed"]=type(ex).__name__
    return o
with cf.ThreadPoolExecutor(8) as ex: out=list(ex.map(one,rows))
json.dump(out,open("scripts/video-oembed-audit.json","w"),indent=1)
import collections; print(collections.Counter(o["oembed"] for o in out))
