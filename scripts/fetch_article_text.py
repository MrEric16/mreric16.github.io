import re, json, html, requests, concurrent.futures as cf
H={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36","Accept-Language":"en"}
urls=json.load(open("scripts/article_urls.json"))
def txt(p):
    p=re.sub(r"<(script|style|noscript|nav|header|footer|aside|form)[^>]*>.*?</\1>","",p,flags=re.S|re.I)
    p=re.sub(r"</(p|h1|h2|h3|li|div|br)>","\n",p,flags=re.I)
    t=html.unescape(re.sub(r"<[^>]+>"," ",p))
    lines=[re.sub(r"[ \t]+"," ",l).strip() for l in t.split("\n")]
    return "\n".join(l for l in lines if len(l)>40)
def one(u):
    r={"url":u}
    try:
        x=requests.get(u,headers=H,timeout=40,allow_redirects=True)
        r["status"]=x.status_code
        if x.status_code==200:
            t=txt(x.text[:900000]); r["words"]=len(t.split()); r["text"]=t[:30000]
    except Exception as e: r["status"]=type(e).__name__
    return r
with cf.ThreadPoolExecutor(6) as ex: out=list(ex.map(one,urls))
json.dump(out,open("scripts/article-text.json","w"),indent=1,ensure_ascii=False)
print([(o["url"][-40:],o.get("status"),o.get("words")) for o in out])
