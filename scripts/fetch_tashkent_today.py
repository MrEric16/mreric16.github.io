#!/usr/bin/env python3
"""Fetches CBU exchange rates (validated, cross-checked), Tashkent air quality (Open-Meteo) and prayer times (Aladhan) into data/tashkent-today.json.
A source that fails keeps its previous value and records the failure, so the page can show how stale it is."""
import requests, json, os, datetime, sys
OUT = 'data/tashkent-today.json'
try: old = json.load(open(OUT, encoding='utf8'))
except Exception: old = {}
H = {'User-Agent': 'mreric16-lounge/1.0', 'Accept': 'application/json'}
now = datetime.datetime.utcnow()
res = dict(old); log = []
def stamp(k): res.setdefault('stamps', {})[k] = now.strftime('%Y-%m-%dT%H:%M:%SZ')
# --- CBU rates (official), validated before anything is written
WANT = ['USD', 'EUR', 'GBP', 'RUB', 'AED', 'KZT', 'CNY', 'KGS']
MAX_STEP = 0.05    # a single currency moving more than 5 percent between fetches is suspicious
MAX_DEV = 0.05     # CBU vs independent market source may differ by up to 5 percent
def per_uzs(r): return r['rate'] / r['nominal']
def xcheck(items):
    """Compare CBU-implied units of X per USD with an independent source. Returns (source, worst_pct, detail)."""
    srcs = [('open.er-api.com', 'https://open.er-api.com/v6/latest/USD', lambda j: j['rates']),
            ('fawazahmed0 currency-api', 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json', lambda j: {k.upper(): v for k, v in j['usd'].items()}),
            ('frankfurter (ECB)', 'https://api.frankfurter.dev/v1/latest?base=USD', lambda j: j['rates'])]
    for name, u, get in srcs:
        try:
            r = requests.get(u, headers=H, timeout=30); r.raise_for_status(); ref = get(r.json())
            worst, det = 0.0, []
            for c in WANT:
                if c == 'USD' or c not in ref: continue
                implied = per_uzs(items['USD']) / per_uzs(items[c])     # units of c per USD according to CBU
                dev = abs(implied - ref[c]) / ref[c]; worst = max(worst, dev); det.append('%s %.2f%%' % (c, dev * 100))
            if len(det) >= 3: return name, worst, ', '.join(det)
        except Exception as e: log.append('xcheck source %s unavailable: %s' % (name, str(e)[:80]))
    return None, None, ''
def _age0():
    try: return (now - datetime.datetime.strptime((old.get('stamps') or {})['rates'], '%Y-%m-%dT%H:%M:%SZ')).total_seconds() / 3600
    except Exception: return 1e9
rates_ok = False
import urllib.parse
CBU = 'https://cbu.uz/en/arkhiv-kursov-valyut/json/'
EDGE = 'https://uugjyucgeyopyvmhckdg.supabase.co/functions/v1/cbu-rates'
def q(u): return urllib.parse.quote(u, safe='')
# The GitHub runner often cannot reach cbu.uz directly (connect timeouts), so the same official JSON is also tried through
# other routes: our own Supabase edge function, then public relays. The data is still CBU's; only the road differs.
CANDS = [
    ('direct', CBU, lambda j: j), ('direct oz', 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/', lambda j: j),
    ('direct ru', 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/', lambda j: j),
    ('supabase edge', EDGE, lambda j: j['rates']),
    ('corsproxy.io', 'https://corsproxy.io/?url=' + q(CBU), lambda j: j),
    ('allorigins', 'https://api.allorigins.win/raw?url=' + q(CBU), lambda j: j),
    ('codetabs', 'https://api.codetabs.com/v1/proxy?quest=' + q(CBU), lambda j: j),
]
for label, u, getrows in CANDS:
    try:
        r = requests.get(u, headers=H, timeout=20); r.raise_for_status(); js = getrows(r.json())
        rates = {}
        for x in js:
            if x.get('Ccy') in WANT: rates[x['Ccy']] = {'rate': float(x['Rate']), 'nominal': float(x.get('Nominal') or 1), 'diff': float(x.get('Diff') or 0)}
        miss = [c for c in WANT if c not in rates]
        if miss: raise ValueError('missing ' + ','.join(miss))
        if any(v['rate'] <= 0 or v['nominal'] <= 0 for v in rates.values()): raise ValueError('non-positive rate')
        date = js[0].get('Date'); dd = datetime.datetime.strptime(date, '%d.%m.%Y')
        if (now + datetime.timedelta(hours=5) - dd).days > 3 or (dd - now).days > 2: raise ValueError('CBU date out of range ' + date)
        prev = (old.get('rates') or {}).get('items') or {}
        jumps = ['%s %.1f%%' % (c, abs(per_uzs(rates[c]) / per_uzs(prev[c]) - 1) * 100) for c in WANT if c in prev and abs(per_uzs(rates[c]) / per_uzs(prev[c]) - 1) > MAX_STEP]
        src, worst, det = xcheck(rates)
        if src is None:
            if jumps: raise ValueError('no cross-check source and large jump: ' + ', '.join(jumps))
            xc = {'source': None}; log.append('WARNING rates: no cross-check source reachable, accepted (no jumps)')
        else:
            if worst > MAX_DEV: raise ValueError('CBU disagrees with %s by %.1f%% (%s)' % (src, worst * 100, det))
            xc = {'source': src, 'worstPct': round(worst * 100, 2)}; log.append('rates cross-check vs %s ok, worst %.2f%% (%s)' % (src, worst * 100, det))
        res['rates'] = {'date': date, 'source': 'Central Bank of Uzbekistan', 'items': rates, 'xcheck': xc}; stamp('rates'); log.append('rates ok via ' + label + ' ' + date); rates_ok = True; break
    except Exception as e: log.append('rates FAIL %s %s' % (label, str(e)[:120]))
# Last resort: CBU unreachable by every route and the saved rates are over 20 h old -> market rates (clearly labelled, not official)
if not rates_ok and _age0() > 20:
    try:
        ref = None
        for name, u2, get in [('open.er-api.com', 'https://open.er-api.com/v6/latest/USD', lambda j: j['rates']),
                              ('fawazahmed0', 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json', lambda j: {k.upper(): v for k, v in j['usd'].items()})]:
            try:
                rr = requests.get(u2, headers=H, timeout=20); rr.raise_for_status(); ref = get(rr.json()); break
            except Exception as e: log.append('market source %s unavailable: %s' % (name, str(e)[:80]))
        if ref and ref.get('UZS'):
            prev = (old.get('rates') or {}).get('items') or {}
            mk_items = {c: {'rate': round(ref['UZS'] / ref[c], 2), 'nominal': 1.0, 'diff': 0.0} for c in WANT if c in ref}
            if len(mk_items) == len(WANT) and all(c not in prev or abs(per_uzs(mk_items[c]) / per_uzs(prev[c]) - 1) < 0.15 for c in WANT):
                res['rates'] = {'date': (now + datetime.timedelta(hours=5)).strftime('%d.%m.%Y'), 'source': 'Market rates (CBU unreachable)', 'items': mk_items, 'xcheck': {'source': None}, 'approx': True}
                stamp('rates'); rates_ok = True; log.append('rates MARKET fallback used')
    except Exception as e: log.append('market fallback FAIL ' + str(e)[:100])
# --- Air quality
try:
    u = 'https://air-quality-api.open-meteo.com/v1/air-quality?latitude=41.3111&longitude=69.2797&current=us_aqi,pm2_5,pm10,ozone,nitrogen_dioxide&hourly=us_aqi&timezone=Asia%2FTashkent&forecast_days=2'
    r = requests.get(u, headers=H, timeout=30); r.raise_for_status(); js = r.json()
    hr = js['hourly']; res['air'] = {'current': js['current'], 'hours': list(zip(hr['time'], hr['us_aqi'])), 'source': 'Open-Meteo (CAMS model)'}; stamp('air'); log.append('air ok')
except Exception as e: log.append('air FAIL ' + str(e)[:120])
# --- Prayer times (Karachi angles, Hanafi Asr) for this and next month
try:
    days = {}
    for k in range(2):
        y, m = now.year, now.month + k
        if m > 12: y, m = y + 1, 1
        u = 'https://api.aladhan.com/v1/calendarByCity/%d/%d?city=Tashkent&country=Uzbekistan&method=1&school=1&timezonestring=Asia/Tashkent' % (y, m)
        r = requests.get(u, headers=H, timeout=30); r.raise_for_status()
        for d in r.json()['data']:
            iso = datetime.datetime.strptime(d['date']['gregorian']['date'], '%d-%m-%Y').strftime('%Y-%m-%d')
            t = d['timings']; days[iso] = {n: t[n][:5] for n in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']}
    tk = now + datetime.timedelta(hours=5)
    need = [(tk + datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(0, 3)]
    miss = [d for d in need if d not in days]
    if miss: raise ValueError('prayer days missing ' + ','.join(miss))
    for d in need:
        t = [days[d][k] for k in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']]
        mins = [int(x[:2]) * 60 + int(x[3:]) for x in t]
        if mins != sorted(mins) or len(set(mins)) != 6: raise ValueError('prayer order invalid ' + d)
    res['prayer'] = {'days': days, 'method': 'Karachi (University of Islamic Sciences), Hanafi Asr', 'source': 'Aladhan'}; stamp('prayer'); log.append('prayer ok %d days' % len(days))
    try:
        r2 = requests.get('https://islomapi.uz/api/present/day?region=Toshkent', headers=H, timeout=20); r2.raise_for_status(); t2 = r2.json()['times']
        mp = {'Fajr': 'tong_saharlik', 'Sunrise': 'quyosh', 'Dhuhr': 'peshin', 'Asr': 'asr', 'Maghrib': 'shom_iftor', 'Isha': 'hufton'}
        td = days[need[0]]; diffs = {k: abs(int(td[k][:2]) * 60 + int(td[k][3:]) - int(t2[v][:2]) * 60 - int(t2[v][3:])) for k, v in mp.items()}
        log.append('prayer cross-check vs islomapi.uz (minutes apart): ' + ', '.join('%s %d' % kv for kv in diffs.items()))
    except Exception as e: log.append('prayer cross-check unavailable: ' + str(e)[:80])
except Exception as e: log.append('prayer FAIL ' + str(e)[:120])
res['updated'] = now.strftime('%Y-%m-%dT%H:%M:%SZ')
res['rates_ok'] = rates_ok
json.dump(res, open(OUT, 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
print('\n'.join(log))
def _rates_age_h():
    try: return (now - datetime.datetime.strptime(res['stamps']['rates'], '%Y-%m-%dT%H:%M:%SZ')).total_seconds() / 3600
    except Exception: return 1e9
# CBU publishes once a day and its host sometimes times out from GitHub runners: keep the last good rates and only fail once they are >30h old
rates_bad = any('rates FAIL' in l for l in log) and not rates_ok and _rates_age_h() > 30
if rates_bad or any('prayer FAIL' in l for l in log): sys.exit(1)
