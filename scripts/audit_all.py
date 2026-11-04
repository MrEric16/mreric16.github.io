#!/usr/bin/env python3
"""Audit every article (DISPATCHES), instrument (EXPLORE_SITES) and video (WATCH_VIDEOS) in index.html.
Runs on a GitHub runner (open internet). Writes scripts/audit-all.json. Report only."""
import re, json, html, time, urllib.parse, collections
from concurrent.futures import ThreadPoolExecutor
import requests
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
H = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml", "Accept-Language": "en-US,en;q=0.9"}
src = open("index.html", encoding="utf-8").read()
def block(name):
    return re.search(r"const %s\s*=\s*\[(.*?)\n\];" % name, src, re.S).group(1)
def unq(s): return s.replace('\\"', '"').replace("\\'", "'")
arts = [{"title": unq(h), "url": u} for h, u in re.findall(r'headline:"((?:[^"\\]|\\.)*)",\s*url:"([^"]+)"', block("DISPATCHES"))]
inst = [{"title": unq(n), "url": u} for n, u in re.findall(r'name:"((?:[^"\\]|\\.)*)",\s*desc:"(?:[^"\\]|\\.)*",\s*url:"([^"]+)"', block("EXPLORE_SITES"))]
vids = [{"title": unq(t), "id": v} for t, v in re.findall(r'title:"((?:[^"\\]|\\.)*)",\s*channel:"(?:[^"\\]|\\.)*",\s*videoId:"([^"]+)"', block("WATCH_VIDEOS"))]
print(len(arts), len(inst), len(vids), flush=True)
SOFT = re.compile(r"(page not found|404 not found|not found|no longer available|has been removed|domain (is )?for sale|this domain|buy this domain|account suspended|site not found|coming soon|under construction|expired)", re.I)
def words(s): return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if len(w) > 3}
def norm(u):
    p = urllib.parse.urlparse(u); return (p.netloc.lower().replace("www.", ""), p.path.rstrip("/"))
def meta(page, key):
    m = re.search(r'<meta[^>]+(?:property|name)=["\']%s["\'][^>]+content=["\']([^"\']*)["\']' % re.escape(key), page, re.I) or \
        re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+(?:property|name)=["\']%s["\']' % re.escape(key), page, re.I)
    return html.unescape(m.group(1)).strip() if m else ""
def wayback(url):
    try:
        c = requests.get("https://archive.org/wayback/available", params={"url": url}, timeout=30).json().get("archived_snapshots", {}).get("closest")
        return bool(c and c.get("available") and str(c.get("status")).startswith("2"))
    except Exception: return None
def page_check(e, kind):
    url = e["url"]; r = {"title": e["title"], "url": url, "kind": kind}
    resp = None
    for i in range(3):
        try:
            resp = requests.get(url, headers=H, timeout=30, allow_redirects=True); break
        except requests.exceptions.SSLError as ex:
            r.update(v="DEAD", note="ssl: " + str(ex)[:80]); return r
        except Exception as ex:
            err = type(ex).__name__ + ": " + str(ex)[:100]; time.sleep(1.5)
    if resp is None:
        r.update(v="DEAD", note="network: " + err); return r
    r["status"] = resp.status_code; r["final"] = resp.url
    if resp.status_code in (404, 410): r.update(v="DEAD", note="HTTP %d" % resp.status_code); return r
    if resp.status_code >= 500: r.update(v="DEAD", note="HTTP %d" % resp.status_code); return r
    if resp.status_code in (401, 403, 429, 451, 400):
        wb = wayback(url); r.update(v="BLOCKED", note="HTTP %d wayback=%s" % (resp.status_code, wb)); return r
    p = resp.text[:400000]
    t = meta(p, "og:title")
    m = re.search(r"<title[^>]*>(.*?)</title>", p, re.S | re.I)
    pt = html.unescape(m.group(1)).strip() if m else ""
    r["page_title"] = (t or pt)[:160]
    ov = len(words(e["title"]) & words(t + " " + pt)) / max(1, len(words(e["title"])))
    r["overlap"] = round(ov, 2)
    sp, pp = norm(url), norm(resp.url)
    r["v"] = "OK"
    if sp[1] and not pp[1] and sp[0].split(".")[-2:] == pp[0].split(".")[-2:]: r.update(v="DEAD", note="redirects to homepage")
    elif sp[0].split(".")[-2:] != pp[0].split(".")[-2:]: r.update(v="CHECK", note="redirects to another domain")
    elif SOFT.search(pt) and ov < 0.5 and len(re.sub(r"<[^>]+>", " ", p)) < 20000: r.update(v="DEAD", note="soft 404: " + pt[:60])
    elif kind == "article" and ov < 0.25: r.update(v="MISMATCH", note="title unrelated")
    return r
def vid_check(e):
    r = {"title": e["title"], "id": e["id"], "kind": "video"}
    for _ in range(3):
        try:
            o = requests.get("https://www.youtube.com/oembed", params={"url": "https://www.youtube.com/watch?v=" + e["id"], "format": "json"}, headers=H, timeout=20)
            r["status"] = o.status_code
            if o.status_code == 200:
                j = o.json(); r["real_title"] = j.get("title"); r["channel"] = j.get("author_name")
                r["overlap"] = round(len(words(e["title"]) & words(j.get("title", ""))) / max(1, len(words(e["title"]))), 2)
                r["v"] = "OK" if r["overlap"] >= 0.3 else "MISMATCH"
            elif o.status_code == 404: r["v"] = "DEAD"
            elif o.status_code == 401: r["v"] = "NOEMBED"
            else: r["v"] = "BLOCKED"
            if o.status_code in (200, 401, 404): break
        except Exception as ex:
            r["v"] = "BLOCKED"; r["status"] = type(ex).__name__
        time.sleep(1)
    return r
def run(f, items):
    def g(e):
        time.sleep(0.1); return f(e)
    with ThreadPoolExecutor(8) as ex: return list(ex.map(g, items))
out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
out["videos"] = run(vid_check, vids)
out["articles"] = run(lambda e: page_check(e, "article"), arts)
out["instruments"] = run(lambda e: page_check(e, "instrument"), inst)
for k in ("articles", "instruments", "videos"):
    print(k, dict(collections.Counter(x["v"] for x in out[k])), flush=True)
json.dump(out, open("scripts/audit-all.json", "w"), indent=1)
