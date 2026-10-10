import re, json, html, requests, concurrent.futures as cf
H={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36","Accept-Language":"en"}
urls=json.load(open("scripts/read_urls.json"))
BAD=re.compile(r"(subscribe|sign up|newsletter|cookie|privacy policy|all rights reserved|advertis|follow us|read more|related:|click here|download mp3)",re.I)
def clean(s): return re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",s))).strip()
def words_of(p):
    full=p
    p=re.sub(r"<(script|style|noscript|nav|header|footer|aside|form|figure|figcaption)[^>]*>.*?</\1>","",p,flags=re.S|re.I)
    m=re.search(r"<article[^>]*>(.*?)</article>",p,flags=re.S|re.I) or re.search(r"<main[^>]*>(.*?)</main>",p,flags=re.S|re.I)
    body=m.group(1) if m else p
    paras=[clean(x) for x in re.findall(r"<p[^>]*>(.*?)</p>",body,flags=re.S|re.I)]
    seen=set();out=[]
    for t in paras:
        if len(t.split())<8 or BAD.search(t) or t in seen: continue
        seen.add(t);out.append(t)
    wp=sum(len(t.split()) for t in out)
    w=wp
    if True:
        pg=re.sub(r"<(script|style|noscript|nav|header|footer|aside|form|figure|figcaption)[^>]*>.*?</\1>","",full,flags=re.S|re.I)
        t=re.sub(r"</(p|h1|h2|h3|li|div|br)>","\n",pg,flags=re.I)
        t=html.unescape(re.sub(r"<[^>]+>"," ",t))
        lines=[re.sub(r"[ \t]+"," ",l).strip() for l in t.split("\n")]
        seen=set();o2=[]
        for l in lines:
            if len(l)<=40 or BAD.search(l) or l in seen: continue
            seen.add(l);o2.append(l)
        wl=sum(len(l.split()) for l in o2)
        w=wp if wp>=150 else wl
    return [w,wp,wl]
def one(u):
    r={"url":u}
    try:
        x=requests.get(u,headers=H,timeout=40,allow_redirects=True)
        r["status"]=x.status_code
        if x.status_code==202:
            import time; time.sleep(8); x=requests.get(u,headers=H,timeout=40,allow_redirects=True); r["status"]=x.status_code
        if x.status_code==200:
            a=words_of(x.text[:1500000]); r["words"]=a[0]; r["wp"]=a[1]; r["wl"]=a[2]
    except Exception as e: r["status"]=type(e).__name__
    return r
with cf.ThreadPoolExecutor(8) as ex: out=list(ex.map(one,urls))
json.dump(out,open("scripts/read-times.json","w"),indent=1)
print(len(out),sum(1 for o in out if o.get("words")))
