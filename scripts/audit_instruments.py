import re, json, html, sys, concurrent.futures as cf, requests
HDRS={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36","Accept-Language":"en"}
rows=json.load(open("scripts/instruments.json"))
GATE=re.compile(r"(sign in to (continue|use|view)|log ?in to (continue|use|view)|create (a free )?account to|subscribe to (read|continue|access)|start (your )?free trial|upgrade to (pro|premium)|premium (plan|feature)|\bpricing\b|per month|/month|members only|paywall|credit card)",re.I)
def txt(p):
    p=re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>","",p,flags=re.S|re.I)
    return re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",p))).strip()
def one(i):
    n,d,u,f=rows[i]; r={"i":i,"name":n,"fac":f,"url":u}
    try: resp=requests.get(u,headers=HDRS,timeout=30,allow_redirects=True)
    except Exception as ex:
        r.update(status=None,err=type(ex).__name__);return r
    r["status"]=resp.status_code; r["final"]=resp.url
    p=resp.text[:600000]; r["len"]=len(p)
    m=re.search(r"<title[^>]*>(.*?)</title>",p,re.S|re.I); r["title"]=html.unescape(m.group(1)).strip()[:120] if m else ""
    low=p.lower()
    r["canvas"]=low.count("<canvas"); r["inputs"]=low.count("<input")+low.count("<select")+low.count("<textarea")
    r["buttons"]=low.count("<button"); r["scripts"]=low.count("<script"); r["iframes"]=low.count("<iframe"); r["svg"]=low.count("<svg")
    t=txt(p); r["text_len"]=len(t); r["snippet"]=t[:240]
    g=GATE.findall(t[:60000]); r["gate"]=sorted({x[0].lower() for x in g})[:5]
    return r
with cf.ThreadPoolExecutor(12) as ex: out=list(ex.map(one,range(len(rows))))
json.dump(out,open("scripts/instruments-audit.json","w"),indent=1)
from collections import Counter
print(Counter(o.get("status") for o in out))
