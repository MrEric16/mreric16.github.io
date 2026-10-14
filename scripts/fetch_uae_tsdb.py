#!/usr/bin/env python3
"""UAE Pro League fallback: TheSportsDB (free key). ESPN has no UAE league (verified: 219 leagues, none UAE).

Used when worldfootball.net (Cloudflare) blocks the primary scraper. TheSportsDB's free tier only returns
the latest and next few events, so this MERGES them into the existing file: new results are added, played
fixtures are removed, standings are recomputed from all results. generatedAt is only advanced when the file
can be trusted as current, i.e. no fixture is overdue (kicked off >3h ago) without a result.
"""
import json, re, sys, difflib, unicodedata, datetime as dt, urllib.request, urllib.error

LEAGUE = "4678"
SEASON = "2026-2027"
OUT = "data/uae-league-live.json"
T = "https://www.thesportsdb.com/api/v1/json/3/"
CANON = ['Al Jazira Club', 'Al Ain FC', 'Al Wasl', 'Shabab Al Ahli Club', 'Sharjah FC', 'Al Wahda',
         'Ajman Club', 'United FC', 'Al Nasr SC', 'Ittihad Kalba FC', 'Khor Fakkan Club', 'Hatta Club',
         'Al Dhafra', 'Baniyas SC']
ALIAS = {"bani yas": "Baniyas SC", "baniyas": "Baniyas SC", "kalba": "Ittihad Kalba FC",
         "al ittihad kalba": "Ittihad Kalba FC", "ittihad kalba": "Ittihad Kalba FC",
         "shabab al ahli": "Shabab Al Ahli Club", "al jazira": "Al Jazira Club", "al ain": "Al Ain FC",
         "sharjah": "Sharjah FC", "ajman": "Ajman Club", "khor fakkan": "Khor Fakkan Club",
         "hatta": "Hatta Club", "al nasr": "Al Nasr SC", "united fc dubai": "United FC",
         "united fc": "United FC", "dubai united": "United FC"}
TZ = dt.timezone(dt.timedelta(hours=5))


def log(m):
    print(f"[uae-tsdb] {m}", flush=True)


def get(path):
    req = urllib.request.Request(T + path, headers={"User-Agent": "Mozilla/5.0"})
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
    return None


def parse(ev):
    h, a = canon(ev.get("strHomeTeam")), canon(ev.get("strAwayTeam"))
    ts = ev.get("strTimestamp")
    if not h or not a or not ts:
        return None
    start = dt.datetime.fromisoformat(ts).replace(tzinfo=dt.timezone.utc).astimezone(TZ)
    row = {"home": h, "away": a, "start": start.isoformat(timespec="seconds")}
    hs, as_ = ev.get("intHomeScore"), ev.get("intAwayScore")
    if hs not in (None, "") and as_ not in (None, ""):
        row.update(homeScore=int(hs), awayScore=int(as_), finished=True)
    return row


def same(a, b):
    if (a["home"], a["away"]) != (b["home"], b["away"]):
        return False
    da = dt.datetime.fromisoformat(a["start"]); db = dt.datetime.fromisoformat(b["start"])
    return abs((da - db).total_seconds()) < 3 * 86400


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


def main():
    old = json.load(open(OUT))
    seen = []
    for ep in (f"eventspastleague.php?id={LEAGUE}", f"eventsnextleague.php?id={LEAGUE}",
               f"eventsseason.php?id={LEAGUE}&s={SEASON}"):
        try:
            evs = get(ep).get("events") or []
        except Exception as e:
            log(f"{ep} failed: {e}")
            continue
        log(f"{ep}: {len(evs)} events")
        seen += [p for p in (parse(e) for e in evs) if p]
    if not seen:
        log("TheSportsDB returned nothing; file untouched")
        return 1
    results, fixtures = list(old["results"]), list(old["fixtures"])
    added = 0
    for p in seen:
        if p.get("finished"):
            if not any(same(p, r) for r in results):
                results.append(p); added += 1
                log(f"NEW RESULT {p['home']} {p['homeScore']}-{p['awayScore']} {p['away']} {p['start']}")
            fixtures = [f for f in fixtures if not same(p, f)]
        elif not any(same(p, f) for f in fixtures) and not any(same(p, r) for r in results):
            fixtures.append(p); added += 1
            log(f"NEW FIXTURE {p['home']} v {p['away']} {p['start']}")
    results.sort(key=lambda r: r["start"]); fixtures.sort(key=lambda r: r["start"])
    now = dt.datetime.now(dt.timezone.utc)
    overdue = [f for f in fixtures if dt.datetime.fromisoformat(f["start"]) + dt.timedelta(hours=3) < now]
    out = dict(old)
    out.update(results=results, fixtures=fixtures, standings=table_from(results))
    if overdue:
        log(f"{len(overdue)} fixture(s) kicked off >3h ago with no result in TheSportsDB; NOT advancing generatedAt")
        for f in overdue[:5]:
            log(f"  overdue: {f['home']} v {f['away']} {f['start']}")
    else:
        out["generatedAt"] = now.isoformat()
        out["source"] = "thesportsdb-fallback"
        log(f"verified current: last result {results[-1]['start']}, next fixture {fixtures[0]['start'] if fixtures else 'none'}")
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=2)
    log(f"wrote {OUT}: {len(results)} results, {len(fixtures)} fixtures, {added} new; leader {out['standings'][0]['team']} {out['standings'][0]['points']} pts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
