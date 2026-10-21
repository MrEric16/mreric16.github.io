#!/usr/bin/env python3
"""Usage: contrast_clicks.py OUTDIR THEME...  Clicks through interactive states (answers, buttons, modals) on each route and re-checks contrast after every click."""
import json, sys, re, os
from playwright.sync_api import sync_playwright
OUT = sys.argv[1]; THEMES = sys.argv[2:]
B = os.environ.get('AUDIT_BASE', 'http://localhost:8790/')
SEASONAL = ['firstday', 'christmas', 'newyear', 'ramadan', 'eidfitr', 'nowruz', 'eidadha']
JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'contrast_check.js')).read()
routes = [r for r in json.load(open(os.path.join(OUT, 'routes.json'))) if not r.startswith('globe')]
CLICKS = int(os.environ.get('CLICKS', '10'))
PICK = """() => {
  const ok = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width > 8 && r.height > 8 && r.top >= 0 && r.bottom <= innerHeight + 400 && cs.visibility !== 'hidden' && cs.pointerEvents !== 'none' && !e.disabled; };
  const els = [...document.querySelectorAll('button, [role=button], .opt, .option, .choice, .answer, .tile, .card[data-i], input[type=checkbox], input[type=radio], summary, label')].filter(e => ok(e) && !e.closest('a[href]') && !e.closest('nav,.bottom-tabs,.tabbar') && !/^(theme|back|home|reset|clear|delete|remove|logout|sign|share|download|print)/i.test((e.innerText || '').trim()));
  return els.length;
}"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for th in THEMES:
        res = {}
        init = "localStorage.setItem('themeChoice','%s');localStorage.setItem('elDihlDefaultMigrationDone','1');localStorage.setItem('themePickerShown','1');" % ('default' if th in SEASONAL else th)
        ctx = b.new_context(viewport={'width': 420, 'height': 900}, service_workers='block'); ctx.add_init_script(init)
        ctx.add_init_script("document.addEventListener('DOMContentLoaded',function(){var s=document.createElement('style');s.textContent='*,*::before,*::after{transition:none!important;animation-duration:0s!important;animation-delay:0s!important}';document.head.appendChild(s)})")
        pg = ctx.new_page(); pg.route(re.compile(r'^https?://(?!localhost)'), lambda r: r.abort())
        pg.on('dialog', lambda d: d.dismiss())
        for r in routes:
            found = {}
            try:
                pg.goto(B + r)
                if '#' in r: pg.reload()
                pg.wait_for_timeout(400)
                if th in SEASONAL: pg.evaluate("t=>{document.body.classList.add('theme-'+t)}", th); pg.wait_for_timeout(1000)
                base = pg.url
                for n in range(CLICKS):
                    idx = pg.evaluate("""(n) => {
                      const ok = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width > 8 && r.height > 8 && r.top >= 0 && r.bottom <= innerHeight && cs.visibility !== 'hidden' && cs.pointerEvents !== 'none' && !e.disabled; };
                      const els = [...document.querySelectorAll('button:not([id*=theme i]):not([class*=theme i]):not([aria-label*=theme i]):not([aria-label*=mode i]), [role=button], [data-action], .opt, .option, .choice, .answer, summary, label, input[type=checkbox], input[type=radio], .key, .tab, .chip, .pill')].filter(e => ok(e) && !e.closest('a[href]') && !e.closest('.bottom-tabs,.tabbar,nav') && !/^(theme|back|home|reset|clear|delete|remove|logout|sign|share|download|print|erase|new)/i.test((e.innerText || '').trim()));
                      if (!els.length) return -1;
                      const e = els[(n * 7 + 3) % els.length]; e.setAttribute('data-clicktmp', '1'); return els.length;
                    }""", n)
                    if idx < 0: break
                    try: pg.click('[data-clicktmp]', timeout=1500, no_wait_after=True)
                    except Exception: pass
                    pg.evaluate("document.querySelectorAll('[data-clicktmp]').forEach(e=>e.removeAttribute('data-clicktmp'))")
                    pg.wait_for_timeout(260)
                    if pg.url.split('#')[0] != base.split('#')[0]:
                        break
                    for i in pg.evaluate('(' + JS + ')({})'):
                        found[i['sel'] + '|' + i['text'][:20]] = dict(i, step=n)
                # hover states: move over the first interactive controls and re-check
                pg.evaluate("document.querySelectorAll('#dsurpriseOverlay,[data-egg-popup]').forEach(e=>e.remove())")
                hov = pg.locator('a, button, summary, [role=button], .tile, [class*=tile], [class*=card]')
                cnt = min(hov.count(), 14)
                for n in range(cnt):
                    try:
                        hov.nth((n * 5) % max(1, hov.count())).hover(timeout=800, force=True)
                    except Exception: continue
                    pg.wait_for_timeout(120)
                    for i in pg.evaluate('(' + JS + ')({})'):
                        found['H' + i['sel'] + '|' + i['text'][:20]] = dict(i, step='hover%d' % n)
            except Exception as e:
                found['ERR'] = {'error': str(e)[:120]}
            res[r] = list(found.values())
        ctx.close()
        json.dump(res, open(os.path.join(OUT, 'clk-%s.json' % th), 'w'))
        print(th, sum(len(v) for v in res.values()), flush=True)
    b.close()
