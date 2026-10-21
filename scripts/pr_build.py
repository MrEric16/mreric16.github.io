#!/usr/bin/env python3
"""Builds data/writing/practice.json (typed writing exercises) and checks every model answer against its own rules."""
import sys, os, re, json
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from wm_src_pr import SKILLS
from wm_src_pr2 import T1_INTROS, T1_OVERVIEWS, T2_INTROS, T2_CONCL, T2_BODY
TOK = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)*|\d[\d,.]*")
FUNC = sorted(set('the of and to in a an is are was were that it for as with on by be this which have has had from at or not but their they these its who can more than will do does did so if no all any only never been would should there between while although also'.split()))
CONTR = re.compile(r"\b\w+n['’]t\b|\b\w+['’](re|ve|ll|d|m)\b", re.I)
AMER = re.compile(r'\b(colors?|colored|favorites?|organiz\w*|centers?|behaviors?|realiz\w*|analyz\w*|gotten|neighbors?|labor|defense|traveled|traveling|labeled|catalog)\b', re.I)
def words(t): return TOK.findall(t)
def sents(t): return [s for s in re.sub(r'([.!?])\s+', r'\1\n', t.strip()).split('\n') if s.strip()]
def common(ex, text):
    bad = []
    w = [x.lower() for x in words(text)]
    if not (ex['min'] <= len(w) <= ex['max']): bad.append('words %d not in %d-%d' % (len(w), ex['min'], ex['max']))
    ss = sents(text)
    if not (ex['smin'] <= len(ss) <= ex['smax']): bad.append('sentences %d' % len(ss))
    if not re.search(r'[.!?]$', text.strip()): bad.append('no end punct')
    for s in ss:
        if not re.match(r'[A-Z0-9$\']', s.strip()): bad.append('no capital: ' + s[:20])
    if CONTR.search(text): bad.append('contraction')
    if AMER.search(text): bad.append('american: ' + AMER.search(text).group(0))
    if len(w) >= 12 and sum(1 for x in w if x in FUNC) / len(w) < 0.15: bad.append('function-word ratio')
    if ex.get('source'):
        n = ex['n']; sw = [x.lower() for x in words(ex['source'])]
        grams = set(tuple(sw[i:i + n]) for i in range(len(sw) - n + 1))
        for i in range(len(w) - n + 1):
            if tuple(w[i:i + n]) in grams: bad.append('copy: ' + ' '.join(w[i:i + n]))
    if ex.get('noDigits') and re.search(r'\d', text): bad.append('digits')
    for lab, rx, mode in ex['checks']:
        hit = re.search(rx, text, re.I) is not None
        if (mode == 'must') != hit: bad.append('check: ' + lab)
    return bad
def mk(set_key, group, title, d, i, ex):
    return ex
out = []; problems = 0; total = 0; ids = set()
def add(key, group, title, blurb, task, why, formula, hint, exs):
    global problems, total
    out.append({'key': key, 'group': group, 'title': title, 'blurb': blurb, 'task': task, 'why': why, 'formula': formula, 'hint': hint, 'items': exs})
    for e in exs:
        total += 1
        assert e['id'] not in ids, e['id']; ids.add(e['id'])
        b = common(e, e['model'])
        if b: print('PROBLEM', e['id'], b); problems += 1
        s = json.dumps(e, ensure_ascii=False)
        if re.search('—|–|--', s) or re.search('gotten', s, re.I): print('STYLE', e['id']); problems += 1
def kwchecks(kws):
    return [('uses the information: ' + ' / '.join(k.split('|')), r'\b(' + k + ')', 'must') for k in kws]
def norm(e):
    e = dict(e); e['checks'] = [list(c) for c in kwchecks(e.get('kw', [])) + e.get('checks', [])]; e.pop('kw', None); return e
for s in SKILLS:
    exs = []
    for n, it in enumerate(s['items'], 1):
        facts, kw, model = it[0], it[1], it[2]
        task = it[3] if len(it) > 3 and it[3] else None
        extra = it[4] if len(it) > 4 else []
        mw = len(words(model))
        e = {'id': 'sk-%s-%d' % (s['key'], n), 'facts': facts, 'kw': kw, 'checks': list(s['checks']) + extra, 'task': task, 'min': max(4, int(mw * 0.6)), 'max': int(mw * 2.2) + 12, 'smin': 1, 'smax': 2, 'model': model}
        exs.append(norm(e))
    add(s['key'], 'build', s['title'], '%d sentences' % len(exs), s['task'], None, s['formula'], s['hint'], exs)
def plain(d, key, group, blurb):
    exs = []
    for e in d['items']:
        exs.append(norm(e))
    add(key, group, d['title'].split(': ', 1)[1], blurb % len(exs), d['task'], d['why'], None, None, exs)
plain(T1_INTROS, 't1-intro', 'task1', '%d introductions')
plain(T1_OVERVIEWS, 't1-overview', 'task1', '%d overviews')
plain(T2_INTROS, 't2-intro', 'task2', '%d introductions')
plain(T2_CONCL, 't2-concl', 'task2', '%d conclusions')
plain(T2_BODY, 't2-body', 'task2', '%d paragraphs')
os.makedirs(os.path.join(here, '..', 'data', 'writing'), exist_ok=True)
json.dump({'v': 1, 'func': FUNC, 'sets': out}, open(os.path.join(here, '..', 'data', 'writing', 'practice.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
print(total, 'exercises in', len(out), 'sets,', problems, 'problems'); sys.exit(1 if problems else 0)
