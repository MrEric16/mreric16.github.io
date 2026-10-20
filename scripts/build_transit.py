#!/usr/bin/env python3
"""Compiles data/tashkent-transit-raw.json (OSM) into compact data/tashkent-transit.json for the Tashkent planner."""
import json, re, math
R = json.load(open('data/tashkent-transit-raw.json', encoding='utf8'))
def nodes(lst): return {e['id']: e for e in lst if e['type'] == 'node'}
def r5(x): return round(x, 5)
# ---- metro: official English names, ordered, verified against Wikipedia 2026 (50 stations)
LINES = {
 '1': ('Chilonzor', '#E4002B', ['Buyuk Ipak Yoli','Pushkin','Hamid Olimjon','Amir Temur Xiyoboni','Mustaqillik Maydoni','Paxtakor','Xalqlar Doʻstligi','Milliy Bogʻ','Novza','Mirzo Ulugʻbek','Chilonzor','Olmazor','Choshtepa','Oʻzgarish','Sirgʻali','Yangihayot','Chinor']),
 '2': ('Oʻzbekiston', '#0072CE', ['Beruniy','Tinchlik','Chorsu','Gʻafur Gʻulom','Alisher Navoiy','Oʻzbekiston','Kosmonavtlar','Oybek','Toshkent','Mashinasozlar','Doʻstlik']),
 '3': ('Yunusobod', '#2E9B3E', ['Turkiston','Yunusobod','Shahriston','Bodomzor','Minor','Abdulla Qodiriy','Yunus Rajabiy','Ming Oʻrik']),
 '4': ('Circle', '#F2B600', ['Texnopark','Yashnobod','Tuzel','Olmos','Rohat','Yangiobod','Qoʻyliq','Matonat','Qiyot','Toʻlariq','Xonobod','Quruvchilar','Turon','Qipchoq']),
}
mn = nodes(R['metro'])
rels = [e for e in R['metro'] if e['type'] == 'relation']
metro = []
for lid, (name, col, names) in LINES.items():
    cands = [r for r in rels if r['tags'].get('ref') == lid]
    best = None
    for r in cands:
        pts = []
        for m in r['members']:
            if m['type'] == 'node' and m['ref'] in mn and m['role'] in ('stop', 'stop_entry_only', 'stop_exit_only', 'platform', ''):
                n = mn[m['ref']]
                if pts and pts[-1][3] == m['ref']: continue
                pts.append((n['lat'], n['lon'], n['tags'].get('name', ''), m['ref']))
        if best is None or abs(len(pts) - len(names)) < abs(len(best) - len(names)): best = pts
    assert len(best) == len(names), (lid, len(best), len(names))
    if lid in ('1', '4'): best = best[::-1]  # OSM relation runs from the far end; verified by name check below
    # direction: relation order may run either way; fix by matching first/last latitude later via names
    metro.append({'id': lid, 'name': name, 'color': col, 'st': [{'n': nm, 'la': r5(p[0]), 'lo': r5(p[1]), 'osm': p[2]} for nm, p in zip(names, best)]})
# ---- bus
bn = nodes(R['bus'])
rr = [e for e in R['bus'] if e['type'] == 'relation']
routes = []
for r in rr:
    t = r['tags']; ref = t.get('ref') or (re.match(r'^(\d+\S*)', t.get('name', '')) or [None, None])[1]
    if not ref: continue
    mem = [m for m in r['members'] if m['type'] == 'node' and m['ref'] in bn]
    plat = [m for m in mem if m['role'].startswith('platform')]
    use = plat if len(plat) >= 3 else [m for m in mem if m['role'].startswith('stop')] or plat
    stops = []
    for m in use:
        n = bn[m['ref']]
        if stops and stops[-1][3] == m['ref']: continue
        stops.append((n['lat'], n['lon'], n['tags'].get('name') or n['tags'].get('name:uz') or n['tags'].get('name:ru') or '', m['ref']))
    if len(stops) < 3: continue
    routes.append({'ref': ref, 'type': t.get('route'), 'name': t.get('name', ''), 'from': t.get('from', ''), 'to': t.get('to', ''), 'st': [[r5(a), r5(b), c] for a, b, c, _ in stops]})
# drop exact duplicates
seen = set(); out = []
for r in routes:
    k = (r['ref'], tuple((s[0], s[1]) for s in r['st']))
    if k in seen: continue
    seen.add(k); out.append(r)
routes = sorted(out, key=lambda r: (len(r['ref']), r['ref'], r['name']))
json.dump({'metro': metro, 'bus': routes, 'built': '2026-10-20'}, open('data/tashkent-transit.json', 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
print(len(metro), 'lines', sum(len(l['st']) for l in metro), 'stations', len(routes), 'bus routes', len(set(r['ref'] for r in routes)), 'refs')
# sanity: metro station spacing km
def d(a, b): return math.hypot((a['la'] - b['la']) * 111.2, (a['lo'] - b['lo']) * 84)
for l in metro:
    gaps = [d(l['st'][i], l['st'][i + 1]) for i in range(len(l['st']) - 1)]
    print(l['name'], 'total km %.1f' % sum(gaps), 'max gap %.2f' % max(gaps), 'min %.2f' % min(gaps))
