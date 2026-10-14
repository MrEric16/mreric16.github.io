import json, urllib.request, urllib.error, gzip
H={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36","Accept-Encoding":"identity","Accept":"application/json,text/html"}
def g(u):
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30); b=r.read()
        if b[:2]==b'\x1f\x8b': b=gzip.decompress(b)
        return b.decode(errors="replace")
    except urllib.error.HTTPError as e:
        return "ERR %s %s"%(e.code,e.read()[:120])
    except Exception as e: return "EXC %s"%e
T="https://www.thesportsdb.com/api/v1/json/3/"
print("TSDB leagues", g(T+"search_all_leagues.php?c=United_Arab_Emirates&s=Soccer")[:500])
print("TSDB search", g(T+"searchleagues.php?l=UAE%20Pro%20League")[:300])
for i in ("4668","4669","5006"):
    print("TSDB next",i,g(T+"eventsnextleague.php?id="+i)[:200])
print("SOFA search", g("https://api.sofascore.com/api/v1/search/all?q=uae%20pro%20league")[:400])
print("FOTMOB", g("https://www.fotmob.com/api/leagues?id=536")[:300])
print("FOTMOB search", g("https://www.fotmob.com/api/searchapi/suggest?term=uae%20pro%20league&lang=en")[:400])
print("WIKI", g("https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=2026-27+UAE+Pro+League&format=json")[:600])
print("WORLDFB", g("https://www.worldfootball.net/competition/uae-arabian-gulf-league/")[:150])
print("BBC", g("https://www.bbc.co.uk/sport/football/")[:80])
print("365", g("https://webws.365scores.com/web/standings/?appTypeId=5&langId=1&timezoneName=Asia/Tashkent&userCountryId=1&competitions=7101")[:300])
print("LIVESCORE", g("https://www.livescore.com/en/football/uae/pro-league/")[:100])
