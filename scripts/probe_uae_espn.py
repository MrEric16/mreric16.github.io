import json, urllib.request, urllib.error, gzip
H={"User-Agent":"Mozilla/5.0","Accept-Encoding":"identity"}
def g(u):
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30); b=r.read()
        if b[:2]==b'\x1f\x8b': b=gzip.decompress(b)
        return b.decode()
    except urllib.error.HTTPError as e:
        b=e.read()
        if b[:2]==b'\x1f\x8b': b=gzip.decompress(b)
        return "ERR %s %s"%(e.code,b[:150])
    except Exception as e: return "EXC %s"%e
for s in ["uae.1","are.1","uae.pro","uae.1.pro","arab.1","uae1","uae.league","uae.2"]:
    print(s, g("https://site.api.espn.com/apis/site/v2/sports/soccer/%s/scoreboard"%s)[:160])
print(g("https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard")[:100])
for p in range(1,4):
    t=g("https://sports.core.api.espn.com/v2/sports/soccer/leagues?limit=300&page=%d"%p)
    try:
        j=json.loads(t); print("page",p,j.get("pageCount"),len(j["items"]))
        for i in j["items"]:
            r=i["$ref"]; 
            s=r.split("/leagues/")[1].split("?")[0]
            if any(k in s for k in ("uae","are","arab","emir")): print("CAND",s)
    except Exception as e: print("list",t[:200])
print(g("https://www.espn.com/soccer/league/_/name/uae.1")[:200])
