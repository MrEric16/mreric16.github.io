import re, json, html, sys, concurrent.futures as cf
from urllib.parse import urljoin, urlparse
import requests
H={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36","Accept-Language":"en"}
SEEDS=json.load(open("scripts/event_seeds.json"))
WIN=("2026-10-09","2026-12-31")
def get(u):
    try:
        r=requests.get(u,headers=H,timeout=25,allow_redirects=True)
        return r.status_code, r.url, (r.text[:900000] if r.status_code==200 else "")
    except Exception as e: return None,u,""
def jsonld(page):
    out=[]
    for m in re.finditer(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>',page,re.S|re.I):
        try: d=json.loads(html.unescape(m.group(1)).strip())
        except Exception: continue
        st=[d]
        while st:
            x=st.pop()
            if isinstance(x,list): st+=x
            elif isinstance(x,dict):
                t=x.get("@type"); ts=t if isinstance(t,list) else [t]
                if any(isinstance(a,str) and a.endswith("Event") for a in ts): out.append(x)
                for v in x.values():
                    if isinstance(v,(list,dict)): st.append(v)
    return out
def norm(ev,page_url):
    off=ev.get("offers"); 
    if isinstance(off,list): off=off[0] if off else {}
    price=(off or {}).get("price") if isinstance(off,dict) else None
    loc=ev.get("location"); 
    if isinstance(loc,list): loc=loc[0] if loc else {}
    org=ev.get("organizer"); org=org[0] if isinstance(org,list) and org else org
    return {"name":ev.get("name"),"start":str(ev.get("startDate") or "")[:25],"mode":str(ev.get("eventAttendanceMode") or "").split("/")[-1],
      "price":price,"loc":(loc.get("name") if isinstance(loc,dict) else str(loc))[:60] if loc else "", "url":ev.get("url") or page_url,
      "org":(org.get("name") if isinstance(org,dict) else org) , "desc":html.unescape(re.sub("<[^>]+>"," ",str(ev.get("description") or "")))[:200], "page":page_url}
def crawl(seed):
    res=[]; sc,final,page=get(seed)
    rec={"seed":seed,"status":sc,"final":final,"events":[],"sublinks":0}
    if not page: return rec
    for e in jsonld(page): res.append(norm(e,final))
    host=urlparse(final).netloc
    links=[]
    for m in re.finditer(r'href="([^"#]+)"',page):
        u=urljoin(final,html.unescape(m.group(1)))
        p=urlparse(u)
        if p.netloc==host and re.search(r"event|webinar|lecture|whats-on|online|livestream|calendar|talk",p.path,re.I) and not re.search(r"\.(jpg|png|pdf|css|js)$",p.path) and u not in links and u!=final: links.append(u)
    links=links[:40]; rec["sublinks"]=len(links)
    for u in links:
        s,f,pg=get(u)
        for e in jsonld(pg): res.append(norm(e,f))
    seen=set();ev=[]
    for r in res:
        k=(r["name"],r["start"])
        if k in seen: continue
        seen.add(k);ev.append(r)
    rec["events"]=ev
    return rec
with cf.ThreadPoolExecutor(8) as ex: out=list(ex.map(crawl,SEEDS))
json.dump(out,open("scripts/event-discovery.json","w"),indent=1)
tot=sum(len(o["events"]) for o in out);print("seeds",len(out),"events",tot)
for o in out: print(o["status"],len(o["events"]),o["sublinks"],o["seed"][:70])
