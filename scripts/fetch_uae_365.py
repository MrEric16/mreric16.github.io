#!/usr/bin/env python3
"""UAE Pro League fallback #2: 365Scores public web API (competition id 549).

Runs after worldfootball.net (Cloudflare) and TheSportsDB (403 from runners since 2026-10-20) both fail.
Same merge rules as fetch_uae_tsdb.py: results added, played fixtures removed, standings recomputed from all
results, generatedAt advanced only when no fixture is overdue (kicked off >3h ago with no result).
Logs the raw response shape so a format change is diagnosable from scripts/uae-league-log.txt.
"""
import json, sys, datetime as dt, urllib.request, urllib.error
sys.path.insert(0, "scripts")
from fetch_uae_tsdb import canon, same, table_from, OUT, TZ

BASE = "https://webws.365scores.com/web/games/{kind}/?appTypeId=5&langId=1&timezoneName=Asia/Tashkent&userCountryId=8&competitions=549&showOdds=false"


def log(m):
    print(f"[uae-365] {m}", flush=True)


def get(kind):
    req = urllib.request.Request(BASE.format(kind=kind), headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36",
        "Accept": "application/json", "Origin": "https://www.365scores.com", "Referer": "https://www.365scores.com/"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def parse(g):
    h, a = g.get("homeCompetitor") or {}, g.get("awayCompetitor") or {}
    hn, an = canon(h.get("name")), canon(a.get("name"))
    st = g.get("startTime")
    if not hn or not an or not st:
        return None
    start = dt.datetime.fromisoformat(st).astimezone(TZ)
    row = {"home": hn, "away": an, "start": start.isoformat(timespec="seconds")}
    hs, as_ = h.get("score"), a.get("score")
    finished = g.get("statusGroup") == 4 or "ended" in str(g.get("statusText", "")).lower() or str(g.get("shortStatusText", "")).upper() in ("FT", "AET", "AP")
    if finished and isinstance(hs, (int, float)) and isinstance(as_, (int, float)) and hs >= 0 and as_ >= 0:
        row.update(homeScore=int(hs), awayScore=int(as_), finished=True)
    return row


def main():
    old = json.load(open(OUT))
    seen = []
    for kind in ("results", "fixtures"):
        try:
            data = get(kind)
        except Exception as e:
            log(f"{kind} failed: {e}")
            continue
        games = data.get("games") or []
        log(f"{kind}: keys={list(data)[:8]} games={len(games)}")
        if games:
            g = games[0]
            log(f"  sample: {json.dumps({k: g.get(k) for k in ('startTime','statusGroup','statusText','shortStatusText')})} home={g.get('homeCompetitor',{}).get('name')} {g.get('homeCompetitor',{}).get('score')} away={g.get('awayCompetitor',{}).get('name')} {g.get('awayCompetitor',{}).get('score')}")
        seen += [p for p in (parse(g) for g in games) if p]
    if not seen:
        log("365Scores returned nothing; file untouched")
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
        log(f"{len(overdue)} fixture(s) overdue with no result; NOT advancing generatedAt")
    else:
        out["generatedAt"] = now.isoformat()
        out["source"] = "365scores-fallback"
        log("verified current")
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=2)
    log(f"wrote {OUT}: {len(results)} results, {len(fixtures)} fixtures, {added} new")
    return 0


if __name__ == "__main__":
    sys.exit(main())
