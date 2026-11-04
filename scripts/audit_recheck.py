#!/usr/bin/env python3
"""Second pass: load every URL the first audit could not settle in a real headless Chromium."""
import json, re, time
from playwright.sync_api import sync_playwright
d = json.load(open("scripts/audit-all.json"))
todo = []
for k in ("articles", "instruments"):
    for x in d[k]:
        if x["v"] in ("BLOCKED", "DEAD", "CHECK") or x.get("status") in (202, 406) or (x["v"] == "MISMATCH" and not x.get("page_title")):
            todo.append(x)
print(len(todo), flush=True)
CH = re.compile(r"(just a moment|verify you are human|checking your browser|access denied|attention required|enable javascript and cookies|are you a robot|pardon our interruption|request blocked)", re.I)
NF = re.compile(r"(page not found|404|not found|no longer available|domain.{0,20}for sale|site can.t be reached|this site can.t)", re.I)
out = []
with sync_playwright() as pw:
    b = pw.chromium.launch(args=["--disable-blink-features=AutomationControlled"])
    ctx = b.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", viewport={"width": 1280, "height": 800}, locale="en-US")
    for i, x in enumerate(todo):
        r = {"title": x["title"], "url": x["url"], "kind": x["kind"], "first": x["v"]}
        pg = ctx.new_page()
        try:
            resp = pg.goto(x["url"], wait_until="domcontentloaded", timeout=35000)
            pg.wait_for_timeout(4500)
            r["status"] = resp.status if resp else None
            r["final"] = pg.url
            r["page_title"] = (pg.title() or "")[:160]
            body = pg.evaluate("document.body ? document.body.innerText.slice(0,3000) : ''")
            r["body_len"] = len(body)
            r["challenge"] = bool(CH.search(r["page_title"] + " " + body[:400]))
            r["notfound"] = bool(NF.search(r["page_title"])) or bool(NF.search(body[:300]))
            r["snippet"] = re.sub(r"\s+", " ", body)[:160]
        except Exception as ex:
            r["err"] = type(ex).__name__ + ": " + str(ex)[:140]
        pg.close(); out.append(r)
        if i % 20 == 0: print(i, flush=True)
    b.close()
json.dump(out, open("scripts/audit-recheck.json", "w"), indent=1)
