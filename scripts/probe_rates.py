import requests
U = ['https://cbu.uz/en/arkhiv-kursov-valyut/json/','http://cbu.uz/en/arkhiv-kursov-valyut/json/','https://www.cbu.uz/en/arkhiv-kursov-valyut/json/','https://cbu.uz/en/arkhiv-kursov-valyut/json/USD/',
 'https://nbu.uz/en/exchange-rates/json/','https://nbu.uz/exchange-rates/json/','https://bank.uz/uz/currency','https://api.bank.uz/api/v1/currency','https://kun.uz/uz/exchange-rates',
 'https://open.er-api.com/v6/latest/USD','https://api.frankfurter.dev/v1/latest?base=USD','https://uugjyucgeyopyvmhckdg.supabase.co/functions/v1/cbu-rates',
 'https://r.jina.ai/https://cbu.uz/en/arkhiv-kursov-valyut/json/','https://web.archive.org/web/2/https://cbu.uz/en/arkhiv-kursov-valyut/json/',
 'https://api.allorigins.win/get?url=https%3A%2F%2Fcbu.uz%2Fen%2Farkhiv-kursov-valyut%2Fjson%2F','https://thingproxy.freeboard.io/fetch/https://cbu.uz/en/arkhiv-kursov-valyut/json/',
 'https://cors-anywhere.herokuapp.com/https://cbu.uz/en/arkhiv-kursov-valyut/json/','https://yacdn.org/proxy/https://cbu.uz/en/arkhiv-kursov-valyut/json/']
for u in U:
    try:
        r = requests.get(u, timeout=12, headers={'User-Agent':'Mozilla/5.0'})
        print(r.status_code, len(r.content), 'CORS=' + str(r.headers.get('access-control-allow-origin')), u[:80], '|', r.text[:70].replace('\n',' '))
    except Exception as e: print('ERR', u[:80], str(e)[:70])
