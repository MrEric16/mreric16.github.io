import json, urllib.request, urllib.error
B="https://site.api.espn.com/apis/site/v2/sports/soccer/"
def t(u):
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30)
        b=r.read().decode()
        try:
            j=json.loads(b); ev=j.get("events"); print("OK",u,"events=",None if ev is None else len(ev), "leagues=",[l.get("name") for l in j.get("leagues",[])][:2])
        except Exception: print("OK-nonjson",u,b[:150])
    except urllib.error.HTTPError as e:
        print("ERR",e.code,u,e.read()[:200])
    except Exception as e: print("EXC",u,e)
t(B+"uae.1/scoreboard")
t(B+"uae.1/scoreboard?dates=20261010")
t(B+"uae.1/scoreboard?dates=20261001-20261031")
t(B+"uae.1/scoreboard?dates=20260801-20260831&limit=300")
t(B+"uae.1/scoreboard?dates=2026")
t(B+"uae.1/standings")
t("https://site.api.espn.com/apis/v2/sports/soccer/uae.1/standings")
t(B+"uae.1/teams")
t(B+"eng.1/scoreboard?dates=20261001-20261031")
try:
    j=json.load(urllib.request.urlopen(urllib.request.Request("https://sports.core.api.espn.com/v2/sports/soccer/leagues?limit=500",headers={"User-Agent":"Mozilla/5.0"}),timeout=30))
    print([i["$ref"] for i in j["items"] if "uae" in i["$ref"] or "arab" in i["$ref"]])
except Exception as e: print("leagues list",e)
for d in ["20261003","20261010","20261011"]:
    t(B+"uae.1/scoreboard?dates="+d)
