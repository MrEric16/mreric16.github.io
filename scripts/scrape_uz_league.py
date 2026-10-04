#!/usr/bin/env python3
"""
Fetches Uzbekistan Super League (top flight) standings, fixtures, and results
from flashscore.com. Runs daily via GitHub Actions so this stays fresh without
manual updates.

flashscore.com is JS-rendered (confirmed: a plain requests.get() only returns
the page shell, no table/match data), so this uses Playwright like the events
calendar scraper does for afisha.uz.

IMPORTANT -- this is a first real attempt at flashscore's DOM structure. Their
exact CSS class names are not something I could verify from a sandboxed
environment with no network access to flashscore.com, so this is built on
commonly-documented flashscore markup patterns, not a live-verified inspection.
A debug HTML dump is written on every run specifically so a real failure here
can be diagnosed from actual output rather than guessed at -- same discipline
this project has needed before when a scraper's real behavior didn't match
what was assumed.

Output: data/uz-league-live.json
"""
import json
import re
import time
from datetime import datetime

STANDINGS_URL = "https://www.flashscore.com/football/uzbekistan/super-league/standings/QeABV06b/standings/overall/"
RESULTS_URL = "https://www.flashscore.com/football/uzbekistan/super-league/results/"
FIXTURES_URL = "https://www.flashscore.com/football/uzbekistan/super-league/fixtures/"
OUTPUT_PATH = "data/uz-league-live.json"
DEBUG_DIR = "scripts"


def log(msg):
    print(f"[uz-league] {msg}", flush=True)


_PREVIOUS_OUTPUT = {}


def guard_against_empty_scrape(field, new_value):
    """If this run scraped zero rows for `field` but the existing file on disk
    already has real rows there, keep the existing rows instead of wiping them
    with an empty list -- a failed/blocked scrape should never erase good data.
    See the real-incident comment in main() for why this exists."""
    if new_value:
        return new_value
    previous = _PREVIOUS_OUTPUT.get(field) or []
    if previous:
        log(f"WARNING: scrape returned 0 {field} but existing file has "
            f"{len(previous)} {field} -- keeping existing {field} instead of "
            f"overwriting with empty (this is very likely a scrape failure, "
            f"not a real gap)")
        return previous
    return new_value


def scrape_standings(page):
    log("loading standings page...")
    page.goto(STANDINGS_URL, wait_until="networkidle", timeout=45000)
    page.wait_for_timeout(3000)
    with open(f"{DEBUG_DIR}/debug-uz-standings.html", "w", encoding="utf-8") as f:
        f.write(page.content())

    rows = page.query_selector_all(".ui-table__row")
    log(f"found {len(rows)} standings rows")
    teams = []
    for row in rows:
        text = row.inner_text().strip()
        if not text:
            continue
        # Flashscore standings rows render as one big text block with the
        # rank, team name, and stats each on their own line -- split and
        # parse defensively rather than assuming a fixed column count.
        parts = [p.strip() for p in text.split("\n") if p.strip()]
        log(f"  raw row parts: {parts}")
        if len(parts) < 8:
            continue
        try:
            rank = int(re.sub(r"\D", "", parts[0]))
            name = parts[1]
            pld = int(parts[2])
            w = int(parts[3])
            d = int(parts[4])
            l = int(parts[5])
            goals = parts[6]  # format like "33:6"
            gf, ga = (int(x) for x in goals.split(":"))
            # BUG FIXED VIA A REAL TEST RUN: parts[-1] was grabbing a form-guide
            # letter (W/D/L) because each row has goal-difference and 5 form
            # letters trailing AFTER points, not before it. Confirmed row shape:
            # [rank, name, pld, w, d, l, "gf:ga", goalDiff, pts, "?", W,D,L,W,D]
            pts = int(parts[8])
            teams.append({
                "name": name, "pld": pld, "w": w, "d": d, "l": l,
                "gf": gf, "ga": ga, "pts": pts,
            })
        except (ValueError, IndexError) as e:
            log(f"  could not parse row {parts}: {e}")
    return teams


def scrape_matches(page, url, label):
    log(f"loading {label} page...")
    page.goto(url, wait_until="networkidle", timeout=45000)
    page.wait_for_timeout(3000)
    with open(f"{DEBUG_DIR}/debug-uz-{label}.html", "w", encoding="utf-8") as f:
        f.write(page.content())

    match_els = page.query_selector_all(".event__match")
    log(f"found {len(match_els)} {label} match elements")
    matches = []
    for el in match_els:
        try:
            # BUG FIXED VIA A REAL TEST RUN + inspecting the actual debug HTML:
            # the originally-assumed classes (.event__participant--home/away,
            # .event__time) don't exist on flashscore's real markup. Confirmed
            # real classes: .event__homeParticipant / .event__awayParticipant
            # containing the team name in a nested .wcl-name_jjfMf span, and
            # the date/time in .event__stageTime--date (format "03.08. 15:30").
            home = el.query_selector(".event__homeParticipant .wcl-name_jjfMf")
            away = el.query_selector(".event__awayParticipant .wcl-name_jjfMf")
            time_el = el.query_selector(".event__stageTime--date")
            score_home = el.query_selector(".event__score--home")
            score_away = el.query_selector(".event__score--away")
            home_name = home.inner_text().strip() if home else None
            away_name = away.inner_text().strip() if away else None
            raw_time = time_el.inner_text().strip() if time_el else None
            entry = {"home": home_name, "away": away_name, "raw_time": raw_time}
            # BUG FIXED VIA A REAL TEST RUN: for fixtures (matches that haven't
            # happened yet), the score elements still EXIST in the DOM but
            # contain a placeholder dash "-" rather than being absent -- so
            # checking "if score_home and score_away" (element presence) was
            # always true and crashed trying to int() a dash. Check the
            # actual text content is a real digit string instead.
            home_score_text = score_home.inner_text().strip() if score_home else ""
            away_score_text = score_away.inner_text().strip() if score_away else ""
            if home_score_text.isdigit() and away_score_text.isdigit():
                entry["homeScore"] = int(home_score_text)
                entry["awayScore"] = int(away_score_text)
            matches.append(entry)
        except Exception as e:
            log(f"  could not parse a {label} match: {e}")
    return matches


def _load_previous_output():
    try:
        with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def main():
    # Real incident (2026-10-04): this scraper ran clean every ~6-7 hours for two
    # straight months (16 teams, 20 results every single time since mid-August) --
    # then one single run came back with 0 teams and 0 results (fixtures still
    # worked fine), and nothing stopped that empty result from overwriting two
    # months of good data. Pakhtakor and Bunyodkor's "Previous result" cards went
    # blank because of one transient flashscore hiccup, not because the site or
    # the season actually ran out of data. scrape_khl.py already learned this
    # exact lesson (liveresult.ru timing out for 4 days straight silently wiped
    # fixtures/results) and guards against it; this scraper never got the same
    # guard. _load_previous_output() + guard_against_empty_scrape() below port
    # that same protection here: if a scrape for ANY of teams/results/fixtures
    # comes back empty while the existing file on disk already has real rows for
    # that same field, keep the existing rows instead of wiping them, and log
    # loudly so a real failure is still visible in the Action's log output.
    global _PREVIOUS_OUTPUT
    _PREVIOUS_OUTPUT = _load_previous_output()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        log("playwright NOT INSTALLED -- aborting")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
            viewport={"width": 1280, "height": 2000},
            locale="en-US",
        )
        page = context.new_page()

        teams = scrape_standings(page)
        time.sleep(2)
        results = scrape_matches(page, RESULTS_URL, "results")
        time.sleep(2)
        fixtures = scrape_matches(page, FIXTURES_URL, "fixtures")

        browser.close()

    teams, results, fixtures = (
        guard_against_empty_scrape("teams", teams),
        guard_against_empty_scrape("results", results),
        guard_against_empty_scrape("fixtures", fixtures),
    )

    output = {
        "generatedAt": datetime.utcnow().isoformat() + "Z",
        "teams": teams,
        "results": results[:20],   # most recent 20 only, matches trimming convention elsewhere
        "fixtures": fixtures[:20],
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    log(f"done: {len(teams)} teams, {len(results)} results, {len(fixtures)} fixtures")


if __name__ == "__main__":
    main()
