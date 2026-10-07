#!/usr/bin/env python3
"""Fetch scorer + minute + HT for finished matches from ESPN's public scoreboard API.
Writes data/espn-goals.json in the same shape as goal-results.json entries.
Team names are canonicalised to the names football-live.json uses so the client's
name matching hits."""
import json, re, sys, datetime as dt, urllib.request

LEAGUES = {"PL": "eng.1", "PD": "esp.1", "BL1": "ger.1", "SA": "ita.1", "FL1": "fra.1", "CL": "uefa.champions"}
START = "20260801"
OUT = "data/espn-goals.json"
ALIAS = {"man": "manchester", "utd": "united", "spurs": "tottenham", "wolves": "wolverhampton",
         "psg": "paris", "saint": "saint", "germain": "germain", "internazionale": "inter"}
STOP = {"fc", "afc", "cf", "ac", "as", "sc", "the", "and", "&", "de", "of", "ssc", "fk", "club", "calcio", "1", "04"}

def toks(s):
    s = re.sub(r"[^a-z0-9 ]", " ", (s or "").lower().replace("&", " "))
    out = set()
    for t in s.split():
        t = ALIAS.get(t, t)
        if t not in STOP: out.add(t)
    return out

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def known_names():
    names = set()
    try:
        f = json.load(open("data/football-live.json"))
        for lg in f.get("standings", {}).values():
            if isinstance(lg, list):
                for r in lg:
                    if r.get("name"): names.add(r["name"])
        for lg in f.get("matches", {}).values():
            for k in ("results", "fixtures"):
                for m in lg.get(k, []):
                    for side in ("homeTeam", "awayTeam"):
                        n = m[side].get("shortName")
                        if n: names.add(n)
        for m in f.get("arsenalFinishedMatches", []):
            for side in ("homeTeam", "awayTeam"):
                n = m[side].get("shortName")
                if n: names.add(n)
    except Exception as e:
        print("known_names failed", e, file=sys.stderr)
    return names

KNOWN = known_names()
KT = {n: toks(n) for n in KNOWN}

def canon(espn_name):
    t = toks(espn_name)
    best, score = None, 0
    for n, kt in KT.items():
        if not kt or not t: continue
        inter = len(t & kt)
        if inter and inter / max(len(kt), 1) >= 0.5 and inter > score:
            best, score = n, inter
    return best or espn_name

def minute(clock):
    m = re.match(r"(\d+)'?(?:\+(\d+))?", (clock or "").strip())
    if not m: return None
    return int(m.group(1)) + (int(m.group(2)) if m.group(2) else 0)

def parse(ev, code):
    comp = ev["competitions"][0]
    if not comp["status"]["type"].get("completed"): return None
    teams = {c["homeAway"]: c for c in comp["competitors"]}
    h, a = teams["home"], teams["away"]
    hid, aid = h["team"]["id"], a["team"]["id"]
    def ls(c):
        l = c.get("linescores") or []
        return int(l[0]["value"]) if l else None
    hg, ag = [], []
    for d in comp.get("details", []):
        if not (d.get("scoringPlay") or d.get("type", {}).get("text", "").lower().startswith("goal") or d.get("type", {}).get("text", "") in ("Penalty - Scored", "Own Goal")):
            continue
        ath = (d.get("athletesInvolved") or [{}])[0]
        name = ath.get("shortName") or ath.get("displayName") or "Unknown"
        txt = d.get("type", {}).get("text", "")
        if d.get("ownGoal") or "Own" in txt: name += " (og)"
        elif d.get("penaltyKick") or "Penalty" in txt: name += " (pen)"
        g = {"scorer": name, "minute": minute(d.get("clock", {}).get("displayValue"))}
        # for an own goal ESPN lists the team of the player who scored it; credit the other side
        tid = d.get("team", {}).get("id")
        home_side = (tid == hid)
        if "(og)" in name: home_side = not home_side
        (hg if home_side else ag).append(g)
    hg.sort(key=lambda x: (x["minute"] is None, x["minute"])); ag.sort(key=lambda x: (x["minute"] is None, x["minute"]))
    ftH, ftA = int(h["score"]), int(a["score"])
    return {"url": f"espn:{ev['id']}", "date": ev["date"][:10], "home": canon(h["team"]["displayName"]),
            "away": canon(a["team"]["displayName"]), "htHome": ls(h), "htAway": ls(a),
            "ftHome": ftH, "ftAway": ftA, "homeGoals": hg, "awayGoals": ag, "competition": code,
            "complete": len(hg) == ftH and len(ag) == ftA}

def main():
    today = dt.datetime.utcnow().strftime("%Y%m%d")
    results, seen = [], set()
    for code, slug in LEAGUES.items():
        events = []
        d0 = dt.datetime.strptime(START, "%Y%m%d")
        d_end = dt.datetime.utcnow()
        while d0 <= d_end:
            d1 = min(d0 + dt.timedelta(days=6), d_end)
            rng = f"{d0:%Y%m%d}-{d1:%Y%m%d}" if d1 > d0 else f"{d0:%Y%m%d}"
            try:
                events += get(f"https://site.api.espn.com/apis/site/v2/sports/soccer/{slug}/scoreboard?dates={rng}").get("events", [])
            except Exception as e:
                print(code, rng, "FAILED", e)
            d0 = d1 + dt.timedelta(days=1)
        data = {"events": events}
        n = 0
        for ev in data.get("events", []):
            try:
                r = parse(ev, code)
            except Exception as e:
                print("parse fail", ev.get("id"), e); continue
            if r and r["url"] not in seen:
                seen.add(r["url"]); results.append(r); n += 1
        print(code, "events", len(data.get("events", [])), "finished", n)
    bad = [r for r in results if not r["complete"]]
    print("total", len(results), "incomplete", len(bad))
    for r in bad[:20]: print(" incomplete:", r["date"], r["home"], r["ftHome"], r["ftAway"], r["away"], len(r["homeGoals"]), len(r["awayGoals"]))
    results.sort(key=lambda r: r["date"], reverse=True)
    if not results:
        print("no results; keeping existing file"); return
    json.dump({"generatedAt": dt.datetime.utcnow().isoformat() + "Z", "results": results}, open(OUT, "w"), indent=1, ensure_ascii=False)

if __name__ == "__main__":
    main()
