// Regression tests: run with `node tests/smoke.js` (needs `npm i playwright` and a chromium install).
// Serves the repo on localhost, loads the app at phone size with all external requests blocked.
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.css': 'text/css', '.png': 'image/png', '.svg': 'image/svg+xml' };
const server = http.createServer((q, r) => {
  let f = path.join(root, decodeURIComponent(q.url.split('?')[0])); if (f.endsWith('/')) f += 'index.html';
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'Content-Type': mime[path.extname(f)] || 'application/octet-stream' }); r.end(d); } });
});
let fails = 0; const ok = (c, m) => { if (!c) { fails++; console.log('FAIL', m); } else console.log('ok  ', m); };
(async () => {
  await new Promise(r => server.listen(0, r)); const base = 'http://localhost:' + server.address().port;
  const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
  const routes = [...new Set([...html.matchAll(/url\s*:\s*"#([a-z0-9][a-z0-9-]*)"/g)].map(m => m[1]))];
  const b = await chromium.launch(); const c = await b.newContext({ viewport: { width: 390, height: 800 }, hasTouch: true, isMobile: true });
  await c.route('**/*', r => r.request().url().startsWith(base) ? r.continue() : r.abort());
  const p = await c.newPage(); p.setDefaultTimeout(8000); let errs = [];
  p.on('pageerror', e => errs.push(e.message.slice(0, 160)));
  await p.addInitScript(() => document.addEventListener('DOMContentLoaded', () => { const s = document.createElement('style'); s.textContent = '.theme-picker-backdrop,.dsurprise-overlay{display:none !important}'; document.head.appendChild(s); }));
  await p.goto(base + '/index.html', { waitUntil: 'domcontentloaded' }); await p.waitForTimeout(1500);
  ok(errs.length === 0, 'home loads without page errors ' + errs.join('|'));
  // Daily Challenge tile is the first home section
  ok(await p.evaluate(() => { const s = document.querySelector('#app > section'); return !!(s && s.querySelector('a.random-tile[href="#daily-challenge"]')); }), 'Daily Challenge tile is first on home');
  // every route renders, no overflow, no errors
  for (const r of ['', ...routes]) {
    errs = []; await p.evaluate(h => { location.hash = h ? '#' + h : '#'; }, r); await p.waitForTimeout(600);
    const i = await p.evaluate(() => ({ len: document.getElementById('app').innerText.trim().length, ov: document.documentElement.scrollWidth - innerWidth }));
    ok(i.len > 20 && i.ov <= 2 && !errs.length, 'route #' + r + ' renders (' + i.len + ' chars, overflow ' + i.ov + ') ' + errs.join('|'));
  }
  // Unit converter maths
  const u = await p.evaluate(() => {
    const idx = (cat, s) => window.UNITCONV.cats[cat].units.findIndex(x => x[0] === s);
    const conv = (cat, a, b, v) => window.UNITCONV.fromBase(cat, idx(cat, b), window.UNITCONV.toBase(cat, idx(cat, a), v));
    return { mi: conv('length', 'mi', 'km', 1), ft: conv('length', 'ft', 'in', 1), f: conv('temp', '°F', '°C', 212), c: conv('temp', '°C', '°F', 100) };
  }).catch(e => ({ err: e.message }));
  ok(u.mi && Math.abs(u.mi - 1.609344) < 1e-9, '1 mile = 1.609344 km ' + JSON.stringify(u));
  ok(u.ft && Math.abs(u.ft - 12) < 1e-9, '1 foot = 12 inches');
  // Team maker
  const t = await p.evaluate(() => { const n = window.TEAMMAKER.names('a, b\nc;d,e'); const d = window.TEAMMAKER.deal(n, 2); return { n, sizes: d.map(x => x.length), all: d.flat().sort().join('') }; });
  ok(t.n.length === 5 && t.sizes.join() === '3,2' && t.all === 'abcde', 'team maker splits 5 names into 3+2 with nobody lost');
  // Daily Challenge: deterministic, ten questions, rollover at 23:59 Tashkent
  const d = await p.evaluate(() => { const D = window.DAILY; const a = JSON.stringify(D.build('2026-11-10')), b = JSON.stringify(D.build('2026-11-10')), c = JSON.stringify(D.build('2026-11-11')); return { same: a === b, diff: a !== c, keys: Object.keys(D.build('2026-11-10')).length, order: D.order.length, names: ['Sardor', 'Aziza', "D'Arcy", 'Ali99', 'Fuck', 'sh1t'].map(n => D.nameOk(n)) }; });
  ok(d.same && d.diff, 'daily questions identical for the same day, different next day');
  ok(d.keys === 10 && d.order === 10, 'daily challenge has ten questions');
  ok(d.names.join() === 'true,true,true,false,false,false', 'name filter: ' + d.names.join());
  const rollover = await p.evaluate(() => { const real = Date.now; const day = t => { Date.now = () => t; const k = window.DAILY.dayKey(); Date.now = real; return k; }; return [day(Date.UTC(2026, 10, 10, 18, 57)), day(Date.UTC(2026, 10, 10, 18, 59))]; });
  ok(rollover[0] === '2026-11-10' && rollover[1] === '2026-11-11', 'rollover at 23:59 Tashkent ' + rollover.join());
  await b.close(); server.close();
  console.log(fails ? fails + ' FAILED' : 'ALL PASSED'); process.exit(fails ? 1 : 0);
})().catch(e => { console.log('CRASH', e.message); process.exit(1); });
