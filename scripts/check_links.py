#!/usr/bin/env python3
"""Audit every article URL in index.html's DISPATCHES array.

For each entry: fetch the URL like a browser, follow redirects, and record
status, final URL, the page's canonical/og:url and og:title/<title>. Then flag:
  DEAD      - HTTP 4xx/5xx or network failure
  REDIRECT  - final URL path differs from the one requested
  MISMATCH  - page loads but its canonical URL or title does not match the entry
  BLOCKED   - 403/429/503 (bot wall, cannot judge from here)
  OK        - loads and matches
Writes scripts/link-report.json. Read-only against the sites; no index.html edits.
"""
import json, os, re, sys, time, html, urllib.parse
from concurrent.futures import ThreadPoolExecutor
import requests

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
HDRS = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.9"}

def load_entries():
    # CANDIDATES=<path> checks a JSON list of {headline,url,faculty} instead of DISPATCHES
    import os
    if os.environ.get("CANDIDATES"):
        return json.load(open(os.environ["CANDIDATES"], encoding="utf-8"))
    src = open("index.html", encoding="utf-8").read()
    body = re.search(r"const DISPATCHES\s*=\s*\[(.*?)\n\];", src, re.S).group(1)
    pat = (r'\{\s*headline:"((?:[^"\\]|\\.)*)",\s*url:"([^"]+)",\s*faculty:"([^"]+)"')
    return [{"headline": h.replace('\\"', '"'), "url": u, "faculty": f}
            for h, u, f in re.findall(pat, body)]

def meta(page, key, attr="property"):
    m = re.search(r'<meta[^>]+%s=["\']%s["\'][^>]+content=["\']([^"\']*)["\']' % (attr, re.escape(key)), page, re.I)
    if not m:
        m = re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+%s=["\']%s["\']' % (attr, re.escape(key)), page, re.I)
    return html.unescape(m.group(1)).strip() if m else ""

def canon(page):
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', page, re.I)
    if not m:
        m = re.search(r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']', page, re.I)
    return m.group(1).strip() if m else ""

def words(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if len(w) > 3}

def norm(u):
    p = urllib.parse.urlparse(u)
    return (p.netloc.lower().replace("www.", ""), p.path.rstrip("/"))

def wayback(url):
    """Does the Internet Archive hold a successful (200) capture of this exact URL?"""
    try:
        j = requests.get("https://archive.org/wayback/available",
                         params={"url": url}, timeout=30).json()
        c = j.get("archived_snapshots", {}).get("closest")
        if c and c.get("available"):
            return f'{c.get("status")} {c.get("timestamp")}'
        # no capture of exact URL
        return "none"
    except Exception as ex:
        return f"error {type(ex).__name__}"

def check(e):
    url = e["url"]
    r = {"headline": e["headline"], "url": url, "status": None, "final_url": "",
         "canonical": "", "title": "", "verdict": "", "note": ""}
    try:
        resp = requests.get(url, headers=HDRS, timeout=30, allow_redirects=True)
    except Exception as ex:
        r["verdict"], r["note"] = "DEAD", f"network error: {type(ex).__name__}: {str(ex)[:120]}"
        return r
    r["status"], r["final_url"] = resp.status_code, resp.url
    if resp.status_code in (403, 429, 503):
        r["verdict"], r["note"] = "BLOCKED", f"HTTP {resp.status_code}"
        r["wayback"] = wayback(url)
        if r["wayback"].startswith("200"):
            r["verdict"] = "ARCHIVED_OK"
            r["note"] += " (site blocks us; Internet Archive holds a 200 capture)"
        return r
    if resp.status_code >= 400:
        r["verdict"], r["note"] = "DEAD", f"HTTP {resp.status_code}"
        return r
    page = resp.text[:400000]
    r["canonical"] = meta(page, "og:url") or canon(page)
    t = meta(page, "og:title")
    if not t:
        m = re.search(r"<title[^>]*>(.*?)</title>", page, re.S | re.I)
        t = html.unescape(m.group(1)).strip() if m else ""
    r["title"] = t[:200]
    if norm(resp.url) != norm(url):
        r["verdict"], r["note"] = "REDIRECT", "final URL differs from requested"
    elif r["canonical"] and norm(r["canonical"]) != norm(url):
        r["verdict"], r["note"] = "MISMATCH", "page canonical differs from requested"
    else:
        # headline is often editorially shortened; require some title overlap
        hw, tw = words(e["headline"]), words(t)
        overlap = len(hw & tw) / max(1, len(hw))
        r["note"] = f"title overlap {overlap:.2f}"
        r["verdict"] = "OK" if overlap >= 0.34 or not tw else "MISMATCH"
        if r["verdict"] == "MISMATCH":
            r["note"] += " (served title unrelated to headline)"
    return r

def main():
    entries = load_entries()
    print(f"{len(entries)} entries", flush=True)
    # polite: few threads, small jitter
    def run(e):
        time.sleep(0.2)
        return check(e)
    with ThreadPoolExecutor(max_workers=6) as ex:
        results = list(ex.map(run, entries))
    counts = {}
    for r in results:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print("SUMMARY", json.dumps(counts))
    json.dump({"generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "summary": counts, "results": results},
              open(os.environ.get("REPORT_OUT", "scripts/link-report.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
