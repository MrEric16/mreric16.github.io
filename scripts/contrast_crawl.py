#!/usr/bin/env python3
"""Discovers every reachable hash route and standalone page by following links in the default theme."""
import json, sys, re
from playwright.sync_api import sync_playwright
B = 'http://localhost:8790/'
INIT = "localStorage.setItem('themeChoice','default');localStorage.setItem('elDihlDefaultMigrationDone','1');localStorage.setItem('themePickerShown','1');"
seen = set(); queue = ['index.html#']; pages = set(); out = []
with sync_playwright() as p:
    b = p.chromium.launch(); ctx = b.new_context(viewport={'width': 420, 'height': 900}, service_workers='block'); ctx.add_init_script(INIT)
    pg = ctx.new_page()
    pg.route(re.compile(r'^https?://(?!localhost)'), lambda r: r.abort())
    while queue and len(seen) < 700:
        u = queue.pop(0)
        if u in seen: continue
        seen.add(u)
        try:
            pg.goto(B + u); pg.reload(); pg.wait_for_timeout(500)
        except Exception as e:
            continue
        out.append(u)
        links = pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))")
        base = u.split('#')[0] or 'index.html'
        for h in links:
            if not h or h.startswith('http') or h.startswith('mailto') or h.startswith('tel') or h.startswith('javascript'): continue
            if h.startswith('#'):
                if h in ('#', '#top'): continue
                n = base + h
            else:
                n = h
                if not re.match(r'^[a-z0-9_.-]+\.html(#.*)?$', n, re.I): continue
                if re.match(r'^(v\d|appsandbox|sandbox|404|dashboard|review)', n): continue
            if n not in seen: queue.append(n)
    b.close()
json.dump(out, open('/tmp/claude-0/-home-claude/d96aaad4-8cdd-50a3-8e28-2c8ceae400d1/scratchpad/audit/routes.json', 'w'))
print(len(out)); print('\n'.join(out[:400]))
