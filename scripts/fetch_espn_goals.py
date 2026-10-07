#!/usr/bin/env python3
"""Fetch scorer + minute + HT for finished matches from ESPN's public scoreboard API.
Writes data/espn-goals.json in the same shape as goal-results.json entries.
Team names are canonicalised to the names football-live.json uses so the client's
name matching hits."""
import json, re, sys, datetime as dt, urllib.request, urllib.error

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
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read()[:300].decode("utf-8", "replace")
        raise RuntimeError(f"HTTP {e.code} {url} :: {body}")

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
    """Returns (display, sortkey, first_half). display is int or "45+2" style string."""
    m = re.match(r"(\d+)'?\s*(?:\+\s*(\d+))?", (clock or "").strip())
    if not m: return None, 9999, None
    base = int(m.group(1)); extra = int(m.group(2)) if m.group(2) else 0
    disp = f"{base}+{extra}" if extra else base
    return disp, base * 100 + extra, base <= 45

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
        disp, key, first = minute(d.get("clock", {}).get("displayValue"))
        g = {"scorer": name, "minute": disp, "_k": key, "_h1": first}
        # for an own goal ESPN lists the team of the player who scored it; credit the other side
        tid = d.get("team", {}).get("id")
        home_side = (tid == hid)  # ESPN already credits an own goal to the benefiting team
        (hg if home_side else ag).append(g)
    hg.sort(key=lambda x: x["_k"]); ag.sort(key=lambda x: x["_k"])
    ftH, ftA = int(h["score"]), int(a["score"])
    complete = len(hg) == ftH and len(ag) == ftA
    ht_h = sum(1 for g in hg if g["_h1"]) if complete else None
    ht_a = sum(1 for g in ag if g["_h1"]) if complete else None
    for g in hg + ag:
        g.pop("_k", None); g.pop("_h1", None)
    return {"url": f"espn:{ev['id']}", "date": ev["date"][:10], "utc": ev["date"], "home": canon(h["team"]["displayName"]),
            "away": canon(a["team"]["displayName"]), "htHome": ht_h, "htAway": ht_a,
            "ftHome": ftH, "ftAway": ftA, "homeGoals": hg, "awayGoals": ag, "competition": code,
            "complete": complete}

def fill_ht(results):
    """For matches where goal detail is incomplete, take HT from football-data's halfTime."""
    try:
        f = json.load(open("data/football-live.json"))
    except Exception:
        return
    ms = []
    for lg in f.get("matches", {}).values(): ms += lg.get("results", [])
    ms += f.get("arsenalFinishedMatches", [])
    for r in results:
        if r["htHome"] is not None: continue
        for m in ms:
            sc = m.get("score", {})
            ft, ht = sc.get("fullTime", {}), sc.get("halfTime", {})
            if ht.get("home") is None: continue
            if m["utcDate"][:10] == r["date"] and m["homeTeam"]["shortName"] == r["home"] and m["awayTeam"]["shortName"] == r["away"] and ft.get("home") == r["ftHome"]:
                r["htHome"], r["htAway"] = ht["home"], ht["away"]; break

def probe():
    for u in ["https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard",
              "https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard?dates=20250921",
              "https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard?dates=20260919",
              "https://site.web.api.espn.com/apis/v2/sports/soccer/eng.1/scoreboard?dates=20260919",
              "https://www.espn.com/soccer/scoreboard/_/league/eng.1/date/20260919"]:
        try:
            r = get(u); print("PROBE OK", u, str(r)[:200])
        except Exception as e:
            print("PROBE FAIL", e)

def main():
    today = dt.datetime.utcnow().strftime("%Y%m%d")
    results, seen = [], set()
    for code, slug in LEAGUES.items():
        events = []
        d0 = dt.datetime.strptime(START, "%Y%m%d")
        d_end = dt.datetime.utcnow()
        while d0 <= d_end:
            d1 = d0
            rng = f"{d0:%Y%m%d}"
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
    fill_ht(results)
    bad = [r for r in results if not r["complete"]]
    print("total", len(results), "incomplete", len(bad))
    for r in bad[:20]: print(" incomplete:", r["date"], r["home"], r["ftHome"], r["ftAway"], r["away"], len(r["homeGoals"]), len(r["awayGoals"]))
    results.sort(key=lambda r: r["date"], reverse=True)
    if not results:
        print("no results; keeping existing file"); return
    json.dump({"generatedAt": dt.datetime.utcnow().isoformat() + "Z", "results": results}, open(OUT, "w"), indent=1, ensure_ascii=False)

if __name__ == "__main__":
    main()
