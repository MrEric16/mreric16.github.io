import re, json, html, requests, concurrent.futures as cf
H={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36","Accept-Language":"en"}
urls=json.load(open("scripts/probe_urls.json"))
def txt(p):
    p=re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>","",p,flags=re.S|re.I)
    return re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",p))).strip()
def one(u):
    r={"url":u}
    try:
        x=requests.get(u,headers=H,timeout=30,allow_redirects=True)
        r["status"]=x.status_code; r["final"]=x.url
        if x.status_code!=200: return r
        p=x.text[:700000]; t=txt(p)
        m=re.search(r"<title[^>]*>(.*?)</title>",p,re.S|re.I); r["title"]=html.unescape(m.group(1)).strip()[:140] if m else ""
        r["len"]=len(t)
        ctx=[]
        for pat in [r"\bfree\b",r"\$\s?\d+|£\s?\d+|€\s?\d+|\bUSD\b",r"\bticket",r"\bregist",r"\bzoom\b|\bwebinar\b|\bonline\b|\bvirtual\b|livestream|live stream",r"\b(ages?|grades?|teens?|students?|high school|all ages|adults)\b",r"\b20(25|26)\b"]:
            c=[]
            for mm in list(re.finditer(pat,t,re.I))[:3]: c.append(t[max(0,mm.start()-70):mm.end()+90])
            ctx.append(c)
        r["ctx"]=ctx; r["head"]=t[:300]
    except Exception as e: r["status"]=type(e).__name__
    return r
with cf.ThreadPoolExecutor(8) as ex: out=list(ex.map(one,urls))
json.dump(out,open("scripts/probe-report.json","w"),indent=1)
print(len(out))
