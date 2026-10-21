#!/usr/bin/env python3
"""Usage: contrast_audit.py OUTDIR THEME [THEME ...]  (needs a server on :8790 and routes.json from contrast_crawl.py)"""
import json, sys, re, os, time
from playwright.sync_api import sync_playwright
OUT = sys.argv[1]; THEMES = sys.argv[2:]
B = os.environ.get('AUDIT_BASE', 'http://localhost:8790/')
SEASONAL = ['firstday', 'christmas', 'newyear', 'ramadan', 'eidfitr', 'nowruz', 'eidadha']
JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'contrast_check.js')).read()
routes = json.load(open(os.path.join(OUT, 'routes.json')))
W = int(os.environ.get('VW', '420'))
with sync_playwright() as p:
    b = p.chromium.launch()
    for th in THEMES:
        res = {}
        init = "localStorage.setItem('themeChoice','%s');localStorage.setItem('elDihlDefaultMigrationDone','1');localStorage.setItem('themePickerShown','1');" % ('default' if th in SEASONAL else th)
        ctx = b.new_context(viewport={'width': W, 'height': 900}, service_workers='block'); ctx.add_init_script(init)
        ctx.add_init_script("document.addEventListener('DOMContentLoaded',function(){var s=document.createElement('style');s.textContent='*,*::before,*::after{transition:none!important;animation-duration:0s!important;animation-delay:0s!important}';document.head.appendChild(s)})")
        pg = ctx.new_page(); pg.route(re.compile(r'^https?://(?!localhost)'), lambda r: r.abort())
        for r in routes:
            try:
                pg.goto(B + r); 
                if '#' in r: pg.reload()
                pg.wait_for_timeout(450)
                if th in SEASONAL: pg.evaluate("t=>{document.body.classList.add('theme-'+t)}", th); pg.wait_for_timeout(150)
                res[r] = pg.evaluate('(' + JS + ')({})')
            except Exception as e:
                res[r] = [{'error': str(e)[:120]}]
        ctx.close()
        json.dump(res, open(os.path.join(OUT, 'res-%s-%d.json' % (th, W)), 'w'))
        print(th, sum(len(v) for v in res.values()), flush=True)
    b.close()
