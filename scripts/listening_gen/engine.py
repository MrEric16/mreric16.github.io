"""Infinite-variety listening item generator. Templates fill randomised slots (names, prices, times, dates, places, facts),
build a spoken script, and derive questions with plausible distractors from the same slot pools."""
import random, re

ONES = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
TENS = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def words(n):
    if n < 20: return ONES[n]
    if n < 100: return TENS[n // 10] + ('-' + ONES[n % 10] if n % 10 else '')
    if n < 1000: return ONES[n // 100] + ' hundred' + (' and ' + words(n % 100) if n % 100 else '')
    return words(n // 1000) + ' thousand' + ((' and ' + words(n % 1000)) if n % 1000 and n % 1000 < 100 else (' ' + words(n % 1000) if n % 1000 else ''))
ORD = {1:'first',2:'second',3:'third',4:'fourth',5:'fifth',6:'sixth',7:'seventh',8:'eighth',9:'ninth',10:'tenth',11:'eleventh',12:'twelfth',13:'thirteenth',14:'fourteenth',15:'fifteenth',16:'sixteenth',17:'seventeenth',18:'eighteenth',19:'nineteenth',20:'twentieth',21:'twenty-first',22:'twenty-second',23:'twenty-third',24:'twenty-fourth',25:'twenty-fifth',26:'twenty-sixth',27:'twenty-seventh',28:'twenty-eighth',29:'twenty-ninth',30:'thirtieth',31:'thirty-first'}
MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December']
DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
FN = {'F': ['Emma','Sophie','Olivia','Hannah','Priya','Fatima','Chloe','Grace','Maya','Zara','Isabel','Leila','Megan','Nadia','Rachel','Alice','Katie','Ingrid'],
      'M': ['James','Oliver','Daniel','Hassan','Ravi','Callum','Ben','Thomas','Adam','Yusuf','Marcus','Liam','Owen','Declan','Samir','Henry','Jonas','Patrick']}
SN = ['Whitfield','Hargreaves','Kowalski','Patel','Henderson','Okafor','Brennan','Nakamura','Lindqvist','Abbott','Fairweather','Mahmood','Ashworth','Pemberton','Thackeray','Quigley','Szymanski','Mackenzie','Radcliffe','Delaney','Fitzgerald','Hollingworth','Beaumont','Yardley','Underwood','Prendergast','Whittaker','Chaudhry','Lawson','Marlowe','Tennant','Gallagher','Osborne','Rutherford','Blackwood','Hutchinson']
def spell(w): return ', '.join(w.upper())
def tspoken(h, m):
    nxt = h % 12 + 1 if h % 12 else 1; hh = h % 12 or 12
    if m == 0: return words(hh) + " o'clock"
    if m == 15: return 'quarter past ' + words(hh)
    if m == 30: return 'half past ' + words(hh)
    if m == 45: return 'quarter to ' + words(nxt)
    if m < 30: return words(m) + ' past ' + words(hh)
    return words(60 - m) + ' to ' + words(nxt)
def tdisp(h, m): return '%d.%02d %s' % (h % 12 or 12, m, 'am' if h < 12 else 'pm')
class Ctx:
    def __init__(self, rnd): self.r = rnd; self.used = {}
def draw(rnd, kind, a, used):
    """Return a slot value dict."""
    if kind == 'pick':
        pool = [x for x in a if x not in used] or a; v = rnd.choice(pool); return {'s': v, 'd': v, 'k': 'pick', 'pool': a}
    if kind == 'obj':
        pool = [x for x in a if id(x) not in used] or a; v = rnd.choice(pool); o = dict(v); o['_k'] = 'obj'; o['_pool'] = a; o['_id'] = id(v); return o
    if kind == 'num':
        lo, hi = a[0], a[1]; n = rnd.randint(lo, hi); return {'s': words(n), 'd': str(n), 'k': 'num', 'n': n, 'rng': (lo, hi)}
    if kind == 'price':
        lo, hi, st = a[0], a[1], a[2]; n = rnd.randrange(lo, hi + 1, st); return {'s': words(n) + ' pounds', 'd': '£%d' % n, 'k': 'price', 'n': n, 'rng': (lo, hi, st)}
    if kind == 'pence':
        lo, hi = a; n = rnd.randint(lo, hi) * 5; p = n % 100; w = n // 100
        s = words(w) + ' pounds' + (' ' + words(p) if p else ''); return {'s': s, 'd': '£%d.%02d' % (w, p), 'k': 'pence', 'n': n, 'rng': (lo * 5, hi * 5)}
    if kind == 'time':
        lo, hi = a[0], a[1]; h = rnd.randint(lo, hi); m = rnd.choice([0, 0, 15, 30, 30, 45, 10, 20, 40, 50]); return {'s': tspoken(h, m), 'd': tdisp(h, m), 'k': 'time', 'n': h * 60 + m, 'rng': (lo, hi)}
    if kind == 'date':
        mo = rnd.randint(0, 11); dd = rnd.randint(1, 28); return {'s': 'the ' + ORD[dd] + ' of ' + MONTHS[mo], 'd': '%d %s' % (dd, MONTHS[mo]), 'k': 'date', 'n': mo * 31 + dd}
    if kind == 'year':
        lo, hi = a; y = rnd.randint(lo, hi)
        if y < 2000: sp = words(y // 100) + ' ' + (words(y % 100) if y % 100 > 9 else ('oh ' + ONES[y % 100] if y % 100 else 'hundred'))
        elif y < 2010: sp = 'two thousand' + (' and ' + words(y % 100) if y % 100 else '')
        else: sp = 'twenty ' + words(y % 100)
        return {'s': sp, 'd': str(y), 'k': 'year', 'n': y, 'rng': (lo, hi)}
    if kind == 'day':
        v = rnd.choice(DAYS); return {'s': v, 'd': v, 'k': 'pick', 'pool': DAYS}
    if kind == 'phone':
        ds = '07' + ''.join(str(rnd.randint(0, 9)) for _ in range(9)); sp = ' '.join('oh' if c == '0' else ONES[int(c)] for c in ds)
        sp = sp.replace('oh seven', 'oh seven', 1); return {'s': sp, 'd': ds, 'k': 'phone'}
    if kind == 'name':
        g = a if a in ('F', 'M') else rnd.choice('FM'); fn = rnd.choice(FN[g]); sn = rnd.choice(SN)
        return {'s': fn, 'd': fn, 'g': g, 'k': 'name', 'fn': fn, 'sn': sn, 'full': fn + ' ' + sn, 'spell': spell(sn)}
    if kind == 'surname':
        sn = rnd.choice(SN); return {'s': sn, 'd': sn, 'k': 'surname', 'spell': spell(sn)}
    if kind == 'code':
        ls = ''.join(rnd.choice('ABCDEFGHJKLMNPRSTUVWXY') for _ in range(2)); ds = ''.join(str(rnd.randint(1, 9)) for _ in range(3)); c = ls + ds
        return {'s': spell(ls) + ', ' + ', '.join(ONES[int(x)] for x in ds), 'd': c, 'k': 'code'}
    raise ValueError(kind)
def val_key(v): return v['d'] if 'd' in v else None
def perturb(rnd, v, n=3):
    """Plausible wrong values of the same kind as v (display strings)."""
    k = v['k']; out = []; tries = 0
    while len(out) < n and tries < 60:
        tries += 1
        if k == 'num':
            lo, hi = v['rng']; d = str(max(1, v['n'] + rnd.choice([-3, -2, -1, 1, 2, 3, 5, 10])))
            if hi < 15: d = str(rnd.randint(max(1, lo - 1), hi + 2))
        elif k == 'price':
            lo, hi, st = v['rng']; d = '£%d' % max(st, v['n'] + rnd.choice([-3, -2, -1, 1, 2, 3]) * st)
        elif k == 'pence':
            n2 = max(5, v['n'] + rnd.choice([-3, -2, -1, 1, 2, 3, 4]) * 5); d = '£%d.%02d' % (n2 // 100, n2 % 100)
        elif k == 'time':
            h = (v['n'] // 60 + rnd.choice([-2, -1, 0, 0, 1, 2])); m = rnd.choice([0, 15, 30, 45, 10, 20, 40, 50]); h = min(max(h, 6), 22); d = tdisp(h, m)
        elif k == 'date':
            mo = (v['n'] // 31 + rnd.choice([-1, 0, 0, 1])) % 12; dd = rnd.randint(1, 28); d = '%d %s' % (dd, MONTHS[mo])
        elif k == 'year':
            d = str(v['n'] + rnd.choice([-8, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 8]))
        elif k == 'phone':
            d = v['d'][:-2] + ''.join(str(rnd.randint(0, 9)) for _ in range(2))
        elif k == 'code':
            d = v['d'][:-1] + str(rnd.randint(1, 9))
        elif k == 'name':
            d = rnd.choice(FN[v.get('g', 'F')])
        elif k in ('pick', 'surname'):
            pool = v.get('pool') or SN; d = rnd.choice(pool)
        else: d = v['d']
        if d != v['d'] and d not in out: out.append(d)
    return out
PH = re.compile(r'\{(\w+)(?:\.(\w+))?\}')
class Item(Exception): pass
def render(text, slots):
    def f(m):
        n, fld = m.group(1), m.group(2)
        if n not in slots: raise Item('missing slot ' + n)
        v = slots[n]; used_slots.add(n)
        key = fld or 's'
        if key not in v: raise Item('missing field %s.%s' % (n, key))
        return str(v[key])
    return PH.sub(f, text)
used_slots = set()
def norm_ans(s): return re.sub(r'\s+', ' ', re.sub(r'[£$,]|o\'clock|\bpounds?\b|\b(am|pm)\b', '', str(s).lower().replace(':', '.'))).strip()
def make(tpl, rnd, sec):
    """tpl: dict(title, roles, slots, lines, qs, voices?). Returns item dict."""
    used_slots.clear()
    slots = {}; used = {}
    for name, (kind, arg) in tpl['slots'].items():
        v = draw(rnd, kind, arg, used.setdefault(name, set()))
        # avoid duplicate display values across slots of same kind (e.g. two prices)
        for _ in range(20):
            if any(o.get('d') == v.get('d') and o.get('k') == v.get('k') for o in slots.values() if isinstance(o, dict) and 'k' in o): v = draw(rnd, kind, arg, used[name]); continue
            break
        if v.get('_k') == 'obj':
            for _ in range(30):
                if any(o.get('_k') == 'obj' and o['_pool'] is v['_pool'] and o['_id'] == v['_id'] for o in slots.values()): v = draw(rnd, kind, arg, used[name]); continue
                break
        slots[name] = v
    # voices by role
    vm = {'F': ['F1', 'F2'], 'M': ['M1', 'M2']}; rnd.shuffle(vm['F']); rnd.shuffle(vm['M']); take = {'F': 0, 'M': 0}; voices = {}
    for role, s in tpl['roles'].items():
        g = slots[s]['g'] if s and s in slots and 'g' in slots[s] else rnd.choice('FM')
        voices[role] = vm[g][take[g] % 2]; take[g] += 1
    turns = []
    for role, text in tpl['lines']:
        if isinstance(text, list): text = rnd.choice(text)
        turns.append({'v': voices[role], 't': render(text, slots)})
    tx = [{'r': role, 't': t['t']} for (role, _), t in zip(tpl['lines'], turns)]
    qs = []
    for q in tpl['qs']:
        stem = render(q['q'], slots)
        sl = slots[q['slot']]; fld = q.get('field')
        if fld:
            ans = str(sl[fld]); pool = sl.get('_pool'); dis = []
            if pool is not None: others = [str(o[fld]) for o in pool if str(o[fld]) != ans]
            elif fld == 'sn': others = [x for x in SN if x != ans]
            elif fld == 'fn': others = [x for x in FN[sl.get('g', 'F')] if x != ans]
            else: others = []
            rnd.shuffle(others); dis = list(dict.fromkeys(others))[:3]
            if q.get('dis'): dis = [str(x) for x in q['dis'] if str(x) != ans][:3]
        else:
            ans = sl['d']; dis = perturb(rnd, sl)
        if q.get('dis') and not fld: dis = [render(x, slots) for x in q['dis']]
        dis = list(dict.fromkeys(x for x in dis if x != ans))
        if len(dis) < 3 and not fld: dis += [x for x in perturb(rnd, sl, 8) if x not in dis and x != ans]
        if q['mode'] == 'mc':
            opts = [ans] + dis[:3]
            if len(opts) < 3: raise Item('too few distractors: ' + stem)
            rnd.shuffle(opts); qs.append({'t': 'mc', 'q': stem, 'o': opts, 'a': opts.index(ans)})
        else:
            acc = [norm_ans(ans)]
            if fld is None and sl['k'] == 'name': acc = [norm_ans(sl['d'])]
            qs.append({'t': 'type', 'q': stem, 'ans': ans, 'acc': acc})
    for q in tpl['qs']:
        if q['slot'] not in used_slots: raise Item('answer slot not spoken: ' + q['slot'])
    tt = render(tpl['title'], slots) if '{' in tpl['title'] else tpl['title']
    return {'sec': sec, 'title': tt, 'turns': turns, 'tx': tx, 'qs': qs, 'tpl': tpl.get('id', '')}

INTROS = ['{i}', '{i} Please listen carefully, as you will hear this only once.', '{i} I will cover several points, so take notes if you wish.']
def make_lecture(topic, rnd, sec='S4'):
    title, intro, facts = topic
    k = min(len(facts), rnd.choice([5, 6, 6]))
    idx = sorted(rnd.sample(range(len(facts)), k)); fs = [facts[j] for j in idx]
    chunks = [intro] + [f[0] for f in fs]
    paras = []
    cur = []
    for c in chunks:
        cur.append(c)
        if len(cur) == 2: paras.append(' '.join(cur)); cur = []
    if cur: paras.append(' '.join(cur))
    voice = rnd.choice(['M1', 'M2', 'F1', 'F2'])
    turns = [{'v': voice, 't': p} for p in paras]
    qs = []
    for (sent, q, ans, dis) in fs:
        if dis is None:
            qs.append({'t': 'type', 'q': q, 'ans': ans, 'acc': [norm_ans(ans), norm_ans(ans.replace('one', '1'))] if ans == 'one' else [norm_ans(ans)]})
        else:
            opts = [ans] + rnd.sample(dis, 3); rnd.shuffle(opts); qs.append({'t': 'mc', 'q': q, 'o': opts, 'a': opts.index(ans)})
    return {'sec': sec, 'title': title, 'turns': turns, 'tx': [{'r': 'A', 't': t['t']} for t in turns], 'qs': qs, 'tpl': 'lecture:' + title}
