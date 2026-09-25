#!/usr/bin/env python3
"""
Checks a small set of trustworthy, pre-approved sources for free, educational, live
online events, and queues any new ones it finds into Supabase's pending_events table for
Mr Eric to approve or reject in review.html. Nothing this script finds ever reaches the
live site directly -- see scripts/publish_approved_events.py, which is the only thing
that writes to data/events-virtual.json, and only for rows a human has actually approved.

WHY QUEUED RATHER THAN PUBLISHED DIRECTLY: this category was hand-curated from the start
specifically because "free + educational + appropriate for a teen audience + relevant"
needs real judgment per item that a scraper can't reliably make (see the note field
already in data/events-virtual.json). Queuing instead of auto-publishing keeps that
judgment step intact -- the scraper's job is just to surface candidates from sources
already trusted enough to be worth a human's five seconds to glance at, not to make the
appropriateness call itself.

SOURCES: NASA's scheduled-events page (plus.nasa.gov/scheduled-events/) and the NGA
Center for Advanced Study news page. NASA's URL/format was updated 2026-09-25: the old
nasa.gov/live/ text-list page ("Tuesday, Aug. 18 · 7 a.m. | <description>" inside plain
<p><strong> tags) has been replaced by NASA with a JS-rendered card layout on
plus.nasa.gov -- confirmed directly by fetching the live page, not assumed, after this
scraper had been silently returning 0 NASA candidates on every run since the migration
(caught when Mr Eric asked why nothing new was showing up and pointed out the old
"check the real page before writing the pattern" discipline). New pattern: each event is
a heading (h1-h5) containing a link to a `/scheduled-video/...` URL -- a stable,
meaningful URL naming convention, used here instead of guessing CSS class names, which
are far more likely to change on NASA's next redesign than their URL scheme is. The
date/time text ("Today 9:00 am" was the only example seen live, since the page had just
one scheduled item at write time) sits in the same card container as the heading; parsed
liberally (several date-shape patterns tried) with any unparseable card logged clearly by
its raw text, rather than silently dropped, specifically so a THIRD silent breakage would
show up in the log instead of just going quiet again.

Output: rows inserted into Supabase's pending_events table (see review.html's SQL note
for the schema). Writes nothing to the repo itself.
"""
import json
import os
import re
from datetime import datetime, timedelta, timezone

import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

SUPABASE_URL = "https://uugjyucgeyopyvmhckdg.supabase.co"
SUPABASE_SERVICE_ROLE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
NASA_LIVE_URL = "https://plus.nasa.gov/scheduled-events/"
EVENTS_VIRTUAL_PATH = "data/events-virtual.json"

# How far ahead to look for candidates. Was 12 days - far too narrow once a person
# expects to see "this month"'s events: from anywhere after the 18th or so of a month,
# 12 days can't even reach the end of THAT month, let alone into the next one. 45 days
# comfortably covers "the rest of this month plus next month" from any starting date.
WINDOW_DAYS = 45


def log(msg):
    print(f"[event-candidates] {msg}", flush=True)


NGA_NEWS_URL = "https://www.nga.gov/research/center/news-center"
NGA_DATE_PATTERN = re.compile(r"([A-Z][a-z]{2,8})\s+(\d{1,2})(?:[\u2013\-]\d{1,2})?,\s*(\d{4})")
NGA_HEADING_PATTERN = re.compile(r"^(.+?)\s*:\s*(.+)$")


def fetch_nga_candidates():
    """Covers art specifically, per Mr Eric's explicit ask. Confirmed real structure via
    direct fetch (2026-08-16), not guessed from a search snippet: each program entry is a
    heading link reading 'DATE : TITLE', followed by a description paragraph. The feed
    mixes genuinely virtual events ("This virtual panel...") with DC-only in-person ones
    (a bookstore book launch, gallery lecture hall talks) -- there's no single reliable
    online/in-person flag field, so only entries whose own title or description text
    explicitly says "virtual" or "online" are queued. Conservative on purpose: missing an
    ambiguous hybrid event is a much smaller problem than flooding the review queue with
    DC-only events Mr Eric's students can't actually attend."""
    candidates = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(NGA_NEWS_URL, timeout=30000)
            page.wait_for_timeout(3000)
            text = page.content()
            browser.close()
    except Exception as e:
        log(f"NGA page fetch failed: {e}")
        return candidates

    log(f"NGA page: captured {len(text)} chars")

    soup = BeautifulSoup(text, "html.parser")
    headings = soup.find_all(["h2", "h3"])
    log(f"NGA page: found {len(headings)} h2/h3 headings to check")
    now = datetime.now(timezone.utc)

    checked = 0
    for h in headings:
        a = h.find("a")
        if not a:
            continue
        heading_text = a.get_text(strip=True)
        m = NGA_HEADING_PATTERN.match(heading_text)
        if not m:
            continue
        date_part, title = m.groups()
        date_match = NGA_DATE_PATTERN.search(date_part)
        if not date_match:
            continue
        checked += 1

        desc_el = h.find_next_sibling("p")
        description = desc_el.get_text(strip=True) if desc_el else ""
        combined = f"{title} {description}".lower()
        if "virtual" not in combined and "online" not in combined:
            continue

        month_name, day, year = date_match.groups()
        try:
            candidate_date = datetime.strptime(f"{month_name} {day} {year}", "%B %d %Y")
        except ValueError:
            try:
                candidate_date = datetime.strptime(f"{month_name} {day} {year}", "%b %d %Y")
            except ValueError:
                continue
        if candidate_date.date() < now.date():
            continue  # NGA's feed includes recent past events too, only want upcoming

        url = a.get("href", "")
        if url.startswith("/"):
            url = "https://www.nga.gov" + url

        candidates.append({
            "title": title.strip()[:200],
            "org": "National Gallery of Art",
            "description": description.strip()[:500],
            "start_date": candidate_date.strftime("%Y-%m-%d"),
            "time_text": "",
            "category": "culture",
            "url": url or NGA_NEWS_URL,
            "source": "NGA News from the Center",
        })

    log(f"NGA page: checked {checked} dated headings, found {len(candidates)} explicitly-virtual/online candidate(s)")
    return candidates


def fetch_all_candidates():
    return fetch_nasa_candidates() + fetch_nga_candidates()


MONTHS = {
    'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,
    'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12,
    'january':1,'february':2,'march':3,'april':4,'june':6,'july':7,
    'august':8,'september':9,'october':10,'november':11,'december':12,
}
# Today H:MM am/pm  (the only example seen live), or a weekday/month-day date followed
# by a time, in whatever order/punctuation NASA happens to use -- tried as several
# alternatives rather than one rigid pattern, since only ONE live example (a same-day
# "Today" card) existed to confirm a format against when this was written. A card whose
# text matches none of these gets logged with its raw text rather than silently
# skipped, so a genuinely new format shows up in the log instead of just another silent
# zero.
NASA_TODAY_PATTERN = re.compile(r"\bToday\b[^\d]*?(\d{1,2})(?::(\d{2}))?\s*([ap])\.?m\.?", re.IGNORECASE)
NASA_DATE_TIME_PATTERN = re.compile(
    r"\b([A-Za-z]{3,9})\.?\s+(\d{1,2})\b[^\d]{0,20}?(\d{1,2})(?::(\d{2}))?\s*([ap])\.?m\.?",
    re.IGNORECASE,
)


def _parse_nasa_card_datetime(card_text, now):
    """Returns (candidate_date, time_text) or (None, None) if nothing recognisable."""
    m = NASA_TODAY_PATTERN.search(card_text)
    if m:
        hour_12, minute, meridiem = m.groups()
        minute = int(minute) if minute else 0
        return now.date(), f"{hour_12}:{minute:02d} {meridiem.upper()}M"

    m = NASA_DATE_TIME_PATTERN.search(card_text)
    if m:
        month_name, day, hour_12, minute, meridiem = m.groups()
        month = MONTHS.get(month_name.lower())
        if not month:
            return None, None
        minute = int(minute) if minute else 0
        year = now.year
        try:
            candidate_date = datetime(year, month, int(day)).date()
        except ValueError:
            return None, None
        if candidate_date < now.date():
            candidate_date = datetime(year + 1, month, int(day)).date()
        return candidate_date, f"{hour_12}:{minute:02d} {meridiem.upper()}M"

    return None, None


def fetch_nasa_candidates():
    candidates = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(NASA_LIVE_URL, timeout=30000)
            page.wait_for_timeout(3000)
            html = page.content()
            browser.close()
    except Exception as e:
        log(f"NASA scheduled-events page fetch failed: {e}")
        return candidates

    log(f"NASA scheduled-events page: captured {len(html)} chars")
    soup = BeautifulSoup(html, "html.parser")
    now = datetime.now(timezone.utc)

    # Anchored on the /scheduled-video/ URL pattern rather than a CSS class name -
    # NASA's own stable per-event URL scheme, far less likely to change on a future
    # redesign than whatever class names this particular layout happens to use.
    seen_urls = set()
    headings = [h for h in soup.find_all(["h1", "h2", "h3", "h4", "h5"])
                if h.find("a", href=re.compile(r"/scheduled-video/"))]
    log(f"NASA scheduled-events page: found {len(headings)} event heading(s) via /scheduled-video/ links")

    unparsed = 0
    for h in headings:
        a = h.find("a", href=re.compile(r"/scheduled-video/"))
        url = a.get("href", "")
        if url.startswith("/"):
            url = "https://plus.nasa.gov" + url
        if url in seen_urls:
            continue
        seen_urls.add(url)

        title = a.get_text(strip=True)
        if not title:
            continue

        # The date/time and description sit in the same card as the heading - walk up
        # one ancestor at a time and stop at the SMALLEST container that holds exactly
        # this one event heading (not zero - too small still - and not more than one -
        # too big, merges in a neighbouring card's text). A fixed walk-up depth was
        # tried first and confirmed broken by testing: it went past the card boundary
        # into a shared ancestor holding every card, so every event on the page ended
        # up reading the FIRST card's date/time. Adapting to whatever the real
        # nesting turns out to be avoids assuming a specific depth at all.
        card = h
        while card.parent is not None:
            candidate = card.parent
            matching = sum(1 for hh in candidate.find_all(["h1", "h2", "h3", "h4", "h5"])
                           if hh.find("a", href=re.compile(r"/scheduled-video/")))
            if matching > 1:
                break  # candidate already spans more than one event - card is as far as we go
            card = candidate
        card_text = card.get_text(" ", strip=True)

        candidate_date, time_text = _parse_nasa_card_datetime(card_text, now)
        if not candidate_date:
            unparsed += 1
            log(f"  could not parse a date/time from NASA card {title!r} - raw card text: {card_text[:200]!r}")
            continue

        desc_el = h.find_next_sibling("p")
        description = desc_el.get_text(strip=True) if desc_el else title

        candidates.append({
            "title": title[:200],
            "org": "NASA",
            "description": description.strip()[:500],
            "start_date": candidate_date.strftime("%Y-%m-%d"),
            "time_text": time_text,
            "category": "science",
            "url": url or NASA_LIVE_URL,
            "source": "NASA scheduled events page",
        })

    log(f"NASA scheduled-events page: found {len(candidates)} candidate(s), {unparsed} card(s) with an unparseable date")
    return candidates


def dedup_key(title, start_date):
    return f"{title.strip().lower()}|{start_date}"


def load_existing_published_keys():
    """(title, date) keys already published to the live site -- never re-suggest these."""
    try:
        with open(EVENTS_VIRTUAL_PATH, encoding="utf-8") as f:
            data = json.load(f)
        return {dedup_key(e.get("title", ""), e.get("startDate", "")) for e in data.get("dated", [])}
    except Exception as e:
        log(f"could not read {EVENTS_VIRTUAL_PATH}, proceeding with an empty published set: {e}")
        return set()


def load_existing_pending_keys():
    """(title, date) keys already sitting in the review queue (any status) -- never queue
    a duplicate. Selects title+start_date, not url, since NASA's live page reuses one
    generic URL for every event -- url alone can't tell candidates apart."""
    try:
        r = requests.get(
            f"{SUPABASE_URL}/rest/v1/pending_events?select=title,start_date",
            headers={"apikey": SUPABASE_SERVICE_ROLE_KEY, "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}"},
            timeout=20,
        )
        r.raise_for_status()
        return {dedup_key(row["title"], row["start_date"]) for row in r.json()}
    except Exception as e:
        log(f"could not read existing pending_events, proceeding with an empty set: {e}")
        return set()


def insert_candidate(candidate):
    r = requests.post(
        f"{SUPABASE_URL}/rest/v1/pending_events",
        headers={
            "apikey": SUPABASE_SERVICE_ROLE_KEY,
            "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal",
        },
        json=candidate,
        timeout=20,
    )
    r.raise_for_status()


def main():
    if not SUPABASE_SERVICE_ROLE_KEY:
        log("SUPABASE_SERVICE_ROLE_KEY is not set -- nothing to do, exiting without error so the workflow doesn't show a false failure before the secret is configured")
        return

    published_keys = load_existing_published_keys()
    pending_keys = load_existing_pending_keys()
    already_seen = published_keys | pending_keys
    log(f"{len(published_keys)} already published, {len(pending_keys)} already pending review")

    now = datetime.now(timezone.utc)
    window_end = now + timedelta(days=WINDOW_DAYS)

    all_candidates = fetch_all_candidates()

    queued = 0
    for c in all_candidates:
        try:
            c_date = datetime.strptime(c["start_date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if not (now.date() <= c_date.date() <= window_end.date()):
            continue
        key = dedup_key(c["title"], c["start_date"])
        if key in already_seen:
            continue
        try:
            insert_candidate(c)
            already_seen.add(key)
            queued += 1
        except Exception as e:
            log(f"  could not queue {c['title']!r}: {e}")

    log(f"done: queued {queued} new candidate(s) for review")


if __name__ == "__main__":
    main()
