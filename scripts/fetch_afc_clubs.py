#!/usr/bin/env python3
"""Extra-competition games the league feeds miss: Pakhtakor's AFC Champions League, English clubs' Carabao Cup (ESPN public API).
Writes data/afc-clubs.json: {generatedAt, clubs:{<club key>:{rows:[{home,away,homeScore,awayScore,start,finished,comp}]}}}
The club cards on the home page merge these rows with the domestic league rows."""
import json, os, datetime as dt, urllib.request, urllib.error
OUT = "data/afc-clubs.json"
# slugs: ESPN competitions to ask about for this club (a club absent from a competition just yields no rows)
CLUBS = {
    "pakhtakor": {"id": "7123", "match": ["pakhtakor"], "slugs": ["afc.champions", "afc.cup"]},
    "man_utd": {"id": "360", "match": ["manchester united"], "slugs": ["eng.league_cup"]},
    "liverpool": {"id": "364", "match": ["liverpool"], "slugs": ["eng.league_cup"]},
    "chelsea": {"id": "363", "match": ["chelsea"], "slugs": ["eng.league_cup"]},
    "man_city": {"id": "382", "match": ["manchester city"], "slugs": ["eng.league_cup"]},
    "tottenham": {"id": "367", "match": ["tottenham"], "slugs": ["eng.league_cup"]},
}

def log(*a): print("[afc]", *a, flush=True)
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r: return json.load(r)
    except Exception as e:
        log("fail", url, str(e)[:120]); return None

def num(x):
    if isinstance(x, dict): x = x.get("value", x.get("displayValue"))
    try: return int(float(x))
    except Exception: return None

def h_a_equal(c):
    try:
        sc = [num(x.get("score")) for x in c["competitors"]]
        return len(sc) == 2 and sc[0] == sc[1]
    except Exception: return False

def parse(ev, comp_name):
    try:
        c = ev["competitions"][0]; cs = c["competitors"]
        h = next(x for x in cs if x.get("homeAway") == "home"); a = next(x for x in cs if x.get("homeAway") == "away")
        if ev.get("status", {}).get("type", {}).get("completed") and h_a_equal(c): log("DRAW RAW", json.dumps(c)[:1800])
        done = bool(ev.get("status", {}).get("type", {}).get("completed") or c.get("status", {}).get("type", {}).get("completed"))
        return {"id": str(ev.get("id")), "home": h["team"].get("displayName") or h["team"].get("name"), "away": a["team"].get("displayName") or a["team"].get("name"),
                "homeScore": num(h.get("score")) if done else None, "awayScore": num(a.get("score")) if done else None,
                "homePen": num(h.get("shootoutScore")) if done else None, "awayPen": num(a.get("shootoutScore")) if done else None,
                "start": ev.get("date"), "finished": done, "comp": comp_name}
    except Exception as e:
        log("parse fail", str(e)[:80]); return None

def collect(club):
    rows = {}
    for slug in club['slugs']:
        for url in (f"https://site.api.espn.com/apis/site/v2/sports/soccer/{slug}/teams/{club['id']}/schedule",
                    f"https://site.api.espn.com/apis/site/v2/sports/soccer/{slug}/teams/{club['id']}/schedule?fixture=true"):
            d = get(url)
            if not d: continue
            evs = d.get("events") or []
            log(slug, "schedule events:", len(evs))
            for ev in evs:
                r = parse(ev, (d.get("league", {}) or {}).get("name") or slug)
                if r: rows[r["id"]] = r
        today = dt.date.today()
        rng = f"{(today - dt.timedelta(days=120)):%Y%m%d}-{(today + dt.timedelta(days=240)):%Y%m%d}"
        d = get(f"https://site.api.espn.com/apis/site/v2/sports/soccer/{slug}/scoreboard?dates={rng}&limit=500")
        if d:
            evs = d.get("events") or []
            log(slug, "scoreboard events:", len(evs))
            for ev in evs:
                names = " ".join((t.get("team", {}).get("displayName") or "").lower() for t in ev.get("competitions", [{}])[0].get("competitors", []))
                ids = [str(t.get("team", {}).get("id")) for t in ev.get("competitions", [{}])[0].get("competitors", [])]
                if club["id"] in ids or any(m in names for m in club["match"]):
                    r = parse(ev, (d.get("leagues") or [{}])[0].get("name") or slug)
                    if r: rows[r["id"]] = r
    return sorted(rows.values(), key=lambda r: r["start"] or "")

def main():
    out = {"generatedAt": dt.datetime.utcnow().isoformat() + "Z", "clubs": {}}
    old = {}
    if os.path.exists(OUT):
        try: old = json.load(open(OUT, encoding="utf-8")).get("clubs", {})
        except Exception: pass
    for key, club in CLUBS.items():
        rows = collect(club)
        log(key, "rows:", len(rows), [(r["start"][:10], r["home"], r["homeScore"], r["awayScore"], r["away"], r.get("homePen"), r.get("awayPen")) for r in rows])
        out["clubs"][key] = {"rows": rows} if rows else old.get(key, {"rows": []})
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
main()
