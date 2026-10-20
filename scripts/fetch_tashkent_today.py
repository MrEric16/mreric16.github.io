#!/usr/bin/env python3
"""Fetches CBU exchange rates, Tashkent air quality (Open-Meteo) and prayer times (Aladhan) into data/tashkent-today.json.
A source that fails keeps its previous value and records the failure, so the page can show how stale it is."""
import requests, json, os, datetime, sys
OUT = 'data/tashkent-today.json'
try: old = json.load(open(OUT, encoding='utf8'))
except Exception: old = {}
H = {'User-Agent': 'mreric16-lounge/1.0', 'Accept': 'application/json'}
now = datetime.datetime.utcnow()
res = dict(old); log = []
def stamp(k): res.setdefault('stamps', {})[k] = now.strftime('%Y-%m-%dT%H:%M:%SZ')
# --- CBU rates
for u in ['https://cbu.uz/en/arkhiv-kursov-valyut/json/', 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/', 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/']:
    try:
        r = requests.get(u, headers=H, timeout=30); r.raise_for_status(); js = r.json()
        want = ['USD', 'EUR', 'RUB', 'GBP', 'KZT', 'TRY', 'CNY', 'AED', 'KRW', 'JPY', 'CHF', 'KGS']
        rates = {}
        for x in js:
            if x.get('Ccy') in want: rates[x['Ccy']] = {'rate': float(x['Rate']), 'nominal': float(x.get('Nominal') or 1), 'diff': float(x.get('Diff') or 0)}
        if 'USD' not in rates: raise ValueError('no USD')
        res['rates'] = {'date': js[0].get('Date'), 'source': 'Central Bank of Uzbekistan', 'items': rates}; stamp('rates'); log.append('rates ok ' + u); break
    except Exception as e: log.append('rates FAIL %s %s' % (u, str(e)[:100]))
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
    res['prayer'] = {'days': days, 'method': 'Karachi (University of Islamic Sciences), Hanafi Asr', 'source': 'Aladhan'}; stamp('prayer'); log.append('prayer ok %d days' % len(days))
except Exception as e: log.append('prayer FAIL ' + str(e)[:120])
res['updated'] = now.strftime('%Y-%m-%dT%H:%M:%SZ')
json.dump(res, open(OUT, 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
print('\n'.join(log))
if all('FAIL' in l for l in log if not l.endswith('ok')) and not any(' ok' in l for l in log): sys.exit(1)
