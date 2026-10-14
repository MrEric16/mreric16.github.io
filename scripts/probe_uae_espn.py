import json, urllib.request, urllib.error
H={"User-Agent":"Mozilla/5.0"}
def g(u):
    try: return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30).read().decode(errors="replace")
    except urllib.error.HTTPError as e: return "ERR %s"%e.code
    except Exception as e: return "EXC %s"%e
T="https://www.thesportsdb.com/api/v1/json/3/"
j=json.loads(g(T+"search_all_leagues.php?c=United_Arab_Emirates&s=Soccer"))
lid=None
for l in j["countries"]:
    print(l["idLeague"],l["strLeague"],l.get("strCurrentSeason"))
    if "pro league" in l["strLeague"].lower() or "arabian" in l["strLeague"].lower(): lid=l["idLeague"]
print("LID",lid)
for ep in ("eventsnextleague.php?id=%s"%lid,"eventspastleague.php?id=%s"%lid,"eventsseason.php?id=%s&s=2026-2027"%lid,"lookuptable.php?l=%s&s=2026-2027"%lid):
    t=g(T+ep)
    try:
        d=json.loads(t); k=list(d.keys())[0]; v=d[k] or []
        print(ep,k,len(v)); 
        if v: print(json.dumps(v[0])[:900])
    except Exception: print(ep,t[:200])
print(g("https://en.wikipedia.org/w/index.php?title=2026%E2%80%9327_UAE_Pro_League&action=raw")[:3000])
