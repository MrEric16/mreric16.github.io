#!/usr/bin/env python3
"""UAE Pro League fallback source: ESPN's public API (the same host fetch_espn_goals.py uses).

Why this exists: worldfootball.net, the original source, started serving a Cloudflare
challenge page to GitHub's runners on 2026-10-09, so scrape_uae_league.py has kept the last
good file untouched ever since and the league went stale. ESPN has no such wall.

Output is the SAME shape as data/uae-league-live.json (teams, standings, fixtures, results),
with team names mapped onto the canonical names the app already uses. Times are written with
a +05:00 offset like the existing file. Existing results are kept and merged so nothing
already shown disappears if ESPN is missing an early-season match.
"""
import json, re, sys, difflib, unicodedata, datetime as dt, urllib.request, urllib.error

SLUG = "uae.1"
OUT = "data/uae-league-live.json"
SEASON_START = dt.date(2026, 8, 1)
SEASON_END = dt.date(2027, 6, 30)
CANON = ['Al Jazira Club', 'Al Ain FC', 'Al Wasl', 'Shabab Al Ahli Club', 'Sharjah FC', 'Al Wahda',
         'Ajman Club', 'United FC', 'Al Nasr SC', 'Ittihad Kalba FC', 'Khor Fakkan Club', 'Hatta Club',
         'Al Dhafra', 'Baniyas SC']
ALIAS = {"bani yas": "Baniyas SC", "baniyas": "Baniyas SC", "kalba": "Ittihad Kalba FC",
         "al ittihad kalba": "Ittihad Kalba FC", "ittihad kalba": "Ittihad Kalba FC",
         "shabab al ahli": "Shabab Al Ahli Club", "al jazira": "Al Jazira Club",
         "al ain": "Al Ain FC", "sharjah": "Sharjah FC", "ajman": "Ajman Club",
         "khor fakkan": "Khor Fakkan Club", "khorfakkan": "Khor Fakkan Club", "hatta": "Hatta Club",
         "al nasr": "Al Nasr SC", "al wahda": "Al Wahda", "al-wahda": "Al Wahda",
         "al wasl": "Al Wasl", "al dhafra": "Al Dhafra", "united": "United FC",
         "dubai united": "United FC", "emirates": "United FC"}
TZ = dt.timezone(dt.timedelta(hours=5))


def log(m):
    print(f"[uae-espn] {m}", flush=True)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def norm(s):
    s = "".join(c for c in unicodedata.normalize("NFKD", s or "") if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s.lower().replace("-", " "))).strip()


def canon(name):
    n = norm(name)
    if n in ALIAS:
        return ALIAS[n]
    for c in CANON:
        if norm(c) == n:
            return c
    best = difflib.get_close_matches(n, [norm(c) for c in CANON], n=1, cutoff=0.72)
    if best:
        return CANON[[norm(c) for c in CANON].index(best[0])]
    log(f"UNMAPPED team name: {name!r}")
    return name


def month_ranges():
    d = SEASON_START
    while d <= SEASON_END:
        nxt = (d.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
        yield d, min(nxt - dt.timedelta(days=1), SEASON_END)
        d = nxt


def fetch_events():
    events = {}
    for a, b in month_ranges():
        url = (f"https://site.api.espn.com/apis/site/v2/sports/soccer/{SLUG}/scoreboard"
               f"?dates={a:%Y%m%d}-{b:%Y%m%d}&limit=300")
        try:
            data = get(url)
        except Exception as e:
            log(f"scoreboard {a}..{b} failed: {e}")
            continue
        evs = data.get("events", [])
        log(f"scoreboard {a:%Y-%m}: {len(evs)} events")
        for ev in evs:
            events[ev.get("id")] = ev
    return list(events.values())


def parse_event(ev):
    comp = (ev.get("competitions") or [{}])[0]
    teams = comp.get("competitors") or []
    home = next((t for t in teams if t.get("homeAway") == "home"), None)
    away = next((t for t in teams if t.get("homeAway") == "away"), None)
    if not home or not away:
        return None
    start = dt.datetime.fromisoformat(ev["date"].replace("Z", "+00:00")).astimezone(TZ)
    status = (comp.get("status") or ev.get("status") or {}).get("type", {})
    row = {"home": canon(home["team"].get("displayName") or home["team"].get("name")),
           "away": canon(away["team"].get("displayName") or away["team"].get("name")),
           "start": start.isoformat(timespec="seconds")}
    if status.get("completed") or status.get("state") == "post":
        try:
            row["homeScore"] = int(float(home.get("score")))
            row["awayScore"] = int(float(away.get("score")))
        except (TypeError, ValueError):
            return None
        row["finished"] = True
    return row


def key(r):
    return (r["home"], r["away"], r["start"][:10])


def table_from(results):
    t = {c: dict(team=c, played=0, won=0, drawn=0, lost=0, gf=0, ga=0, gd=0, points=0) for c in CANON}
    for r in results:
        h, a = t.get(r["home"]), t.get(r["away"])
        if h is None or a is None:
            continue
        hs, as_ = r["homeScore"], r["awayScore"]
        for x, f, g in ((h, hs, as_), (a, as_, hs)):
            x["played"] += 1; x["gf"] += f; x["ga"] += g
        if hs > as_: h["won"] += 1; a["lost"] += 1; h["points"] += 3
        elif hs < as_: a["won"] += 1; h["lost"] += 1; a["points"] += 3
        else: h["drawn"] += 1; a["drawn"] += 1; h["points"] += 1; a["points"] += 1
    for x in t.values():
        x["gd"] = x["gf"] - x["ga"]
    return sorted(t.values(), key=lambda x: (-x["points"], -x["gd"], -x["gf"], x["team"]))


def espn_standings():
    try:
        data = get(f"https://site.api.espn.com/apis/v2/sports/soccer/{SLUG}/standings")
    except Exception as e:
        log(f"standings endpoint failed: {e}")
        return None
    rows = []
    for ch in data.get("children", [data]):
        for e in (ch.get("standings") or {}).get("entries", []):
            st = {s["name"]: s.get("value") for s in e.get("stats", [])}
            try:
                rows.append(dict(team=canon(e["team"]["displayName"]), played=int(st["gamesPlayed"]),
                                 won=int(st["wins"]), drawn=int(st["ties"]), lost=int(st["losses"]),
                                 gf=int(st["pointsFor"]), ga=int(st["pointsAgainst"]),
                                 gd=int(st["pointDifferential"]), points=int(st["points"]),
                                 rank=int(st.get("rank") or 0)))
            except Exception as ex:
                log(f"standings row skipped ({e.get('team',{}).get('displayName')}): {ex}")
    if len(rows) != len(CANON):
        log(f"standings has {len(rows)} rows, expected {len(CANON)}; ignoring")
        return None
    rows.sort(key=lambda r: (r["rank"] or 99))
    for r in rows:
        r.pop("rank", None)
    return rows


def main():
    try:
        old = json.load(open(OUT))
    except Exception:
        old = {"results": [], "fixtures": []}
    parsed = [p for p in (parse_event(e) for e in fetch_events()) if p]
    log(f"parsed {len(parsed)} matches from ESPN")
    if len(parsed) < 10:
        log("ESPN returned too little; keeping existing file untouched")
        return 1
    results = {key(r): r for r in old.get("results", [])}
    fixtures = {}
    for p in parsed:
        if p.get("finished"):
            results[key(p)] = p
        else:
            fixtures[key(p)] = p
    for k in list(fixtures):
        if k in results:
            del fixtures[k]
    res = sorted(results.values(), key=lambda r: r["start"])
    fix = sorted(fixtures.values(), key=lambda r: r["start"])
    mine = table_from(res)
    theirs = espn_standings()
    standings = theirs or mine
    if theirs:
        a = {r["team"]: (r["played"], r["points"], r["gd"]) for r in theirs}
        b = {r["team"]: (r["played"], r["points"], r["gd"]) for r in mine}
        diff = [k for k in a if a[k] != b.get(k)]
        log(f"standings: ESPN vs computed-from-results differ for {diff or 'nobody'}")
    out = {"generatedAt": dt.datetime.now(dt.timezone.utc).isoformat(), "teams": CANON,
           "standings": standings, "fixtures": fix, "results": res,
           "source": "espn-fallback"}
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=2)
    log(f"wrote {OUT}: {len(res)} results, {len(fix)} fixtures; leader {standings[0]['team']} {standings[0]['points']} pts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
