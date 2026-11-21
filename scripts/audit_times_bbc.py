#!/usr/bin/env python3
"""Cross-checks every upcoming fixture time in data/football-full.json against BBC Sport's
scores-fixtures pages (an independent source, UTC timestamps). Prints mismatches; exit 1 if any
(unless --warn). Usage: audit_times_bbc.py [--days 60] [--json out.json]"""
import re, json, sys, datetime as dt, urllib.request
COMP = {'PL':'premier-league','PD':'la-liga','BL1':'bundesliga','SA':'italian-serie-a','FL1':'french-ligue-1','CL':'champions-league'}
def fetch_day(ymd):
    req=urllib.request.Request(f'https://www.bbc.com/sport/football/scores-fixtures/{ymd}',headers={'User-Agent':'Mozilla/5.0'})
    s=urllib.request.urlopen(req,timeout=40).read().decode('utf-8','replace')
    m=re.search(r'window\.__INITIAL_DATA__="(.*?)";</script>',s,re.S)
    if not m: return []
    raw=json.loads('"'+m.group(1)+'"')
    out=[]
    for mm in re.finditer(r'"home":\{"id":"[^"]+","fullName":"([^"]+)","shortName":"([^"]+)".*?"away":\{"id":"[^"]+","fullName":"([^"]+)","shortName":"([^"]+)".*?"eventGroupingLabel":"([^"]+)","startDateTime":"([^"]+)"',raw):
        out.append((mm.group(1),mm.group(2),mm.group(3),mm.group(4),mm.group(6),mm.group(5)))
    return out
def norm(t):
    t=t.lower()
    for a in ('fc','afc','ac','as','sc','cf','ud','rc','rcd','cd','1.','1899','sv','vfl','vfb','fsv','tsg','hotspur','and','hove','albion','de','the'): t=re.sub(r'\b'+re.escape(a)+r'\b',' ',t)
    t=t.replace('manchester','man').replace('internazionale','inter').replace('paris saint-germain','psg').replace('atlético','atletico')
    t=re.sub(r'[^a-z0-9 ]',' ',t); return ' '.join(t.split())
def same(a,b):
    a,b=norm(a),norm(b)
    return bool(a and b) and (a==b or a in b or b in a or a.split()[0]==b.split()[0])
def main():
    days=60; warn='--warn' in sys.argv
    if '--days' in sys.argv: days=int(sys.argv[sys.argv.index('--days')+1])
    d=json.load(open('data/football-full.json',encoding='utf-8'))
    now=dt.datetime.now(dt.timezone.utc); end=now+dt.timedelta(days=days)
    from concurrent.futures import ThreadPoolExecutor
    ds=[(now+dt.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(-1,days+2)]
    def safe(x):
        for _ in range(3):
            try: return fetch_day(x)
            except Exception: pass
        print('fetch fail',x,file=sys.stderr); return []
    with ThreadPoolExecutor(8) as ex: bbc=[e for r in ex.map(safe,ds) for e in r]
    from functools import lru_cache
    nm=lru_cache(None)(norm)
    def same2(a,b):
        a,b=nm(a),nm(b)
        return bool(a and b) and (a==b or a in b or b in a or a.split()[0]==b.split()[0])
    byday={}
    for e in bbc: byday.setdefault(e[4][:10],[]).append(e)
    bad=[];checked=0;nobbc=[]
    for code in COMP:
        for m in d['matches'][code]['fixtures']:
            t=dt.datetime.fromisoformat(m['utcDate'].replace('Z','+00:00'))
            if not(now<=t<=end): continue
            h=m['homeTeam'];a=m['awayTeam']
            cand=[]
            for k in range(-2,3): cand+=byday.get((t+dt.timedelta(days=k)).strftime('%Y-%m-%d'),[])
            c=[b for b in cand if (same2(h['name'],b[0]) or same2(h['shortName'],b[1])) and (same2(a['name'],b[2]) or same2(a['shortName'],b[3]))]
            if not c: nobbc.append((code,h['shortName'],a['shortName'],m['utcDate']));continue
            checked+=1
            bt=dt.datetime.fromisoformat(c[0][4].replace('Z','+00:00'))
            if bt.tzinfo is None: bt=bt.replace(tzinfo=dt.timezone.utc)
            if abs((bt-t).total_seconds())>60: bad.append((code,h['shortName'],a['shortName'],m['utcDate'],c[0][4]))
    print(f'checked {checked}, mismatches {len(bad)}, not on BBC {len(nobbc)}')
    for b in bad: print('MISMATCH',b)
    for n in nobbc[:20]: print('NOBBC',n)
    if '--json' in sys.argv: json.dump({'bad':bad,'nobbc':nobbc},open(sys.argv[sys.argv.index('--json')+1],'w'))
    sys.exit(1 if bad and not warn else 0)
main()
