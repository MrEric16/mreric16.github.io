"""Build per-language word glosses for tap-to-translate in the Languages reading texts.
Source: English Wiktionary via kaikki.org (Wiktextract JSONL). Only words that occur in
data/lang/<id>.json reading texts are kept, so the output is tiny.
usage: build_gloss.py <lang_id> <path-to-kaikki.jsonl>"""
import json, re, sys, os
lid, src = sys.argv[1], sys.argv[2]
ROOT = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'lang')
SRC_ID = {'den': 'de', 'no': 'nb'}.get(lid, lid)
TOK = re.compile(r"[^\W\d_]+(?:[-][^\W\d_]+)*['’]?", re.U)
def toks(s):
    return [m.group(0).replace('’', "'") for m in TOK.finditer(re.sub(r'\{\d\}', ' ', s))]
d = json.load(open(os.path.join(ROOT, lid + '.json')))
need = set()
for r in d.get('reading', []):
    for p in r['paras']: need.update(toks(p['t']))
    for f in r['f']:
        for s in f['s']: need.update(toks(s))
keys = set()
for w in need:
    keys.add(w); keys.add(w.lower())
    if w.endswith("'"): keys.add(w[:-1]); keys.add(w[:-1].lower())
entries = {}      # word -> list of entries
lemmas_needed = set()
BAD = re.compile(r'(letter of the|^the .{0,25}letter|alphabet|^(first|second|third)-person|^(masculine|feminine|neuter|plural|singular|genitive|dative|accusative|nominative|inflection|past|present|comparative|superlative)\b)', re.I)
VULG = re.compile(r'prostitut|whore|slut|fuck|\bcock\b|\bdick\b|cunt|penis|vagina|vulgar|sexual', re.I)
def short(g):
    g = g.replace('\u0301', '')
    prev = None
    while prev != g:                      # drop (nested) parentheticals, innermost first
        prev = g
        g = re.sub(r'\s*\([^()]*\)', '', g)
    g = re.sub(r'\s*\(.*$', '', g)          # unbalanced opener: cut the rest
    g = g.replace(')', '')
    g = g.split(';')[0].strip(' ,:')
    return g[:70]
WRE = re.compile(r'"word": "([^"]*)", "lang": "[^"]*", "lang_code"')
def scan(final):
    with open(src, encoding='utf-8') as fh:
        for line in fh:
            # cheap prefilter on the word before parsing
            m = WRE.search(line)
            if not m: continue
            w = m.group(1)
            wl = w.lower()
            want = keys if not final else lemmas_needed
            if w not in want and wl not in want: continue
            e = json.loads(line)
            if e.get('lang_code') != SRC_ID: continue
            yield e
def sense_info(e):
    out = []
    for s in e.get('senses', []):
        gl = s.get('glosses') or []
        if not gl: continue
        fo = s.get('form_of') or s.get('alt_of') or []
        lem = (fo[0].get('word') if fo else '').replace('\u0301', '')
        if not lem:
            mm = re.search(r' of ([^\s,;:()]+)$', gl[0])
            if mm and BAD.search(gl[0]): lem = mm.group(1).replace('\u0301', '')
        out.append((gl[-1] if len(gl) > 1 and not fo else gl[0], lem, s.get('tags', [])))
    return out
for e in scan(False):
    entries.setdefault(e['word'], []).append(e)
    for g, lem, t in sense_info(e):
        if lem: lemmas_needed.add(lem); lemmas_needed.add(lem.lower())
lem_entries = {}
for e in scan(True):
    lem_entries.setdefault(e['word'], []).append(e)
def lemma_gloss(lem):
    for e in lem_entries.get(lem, []) + lem_entries.get(lem.lower(), []):
        for g, l, t in sense_info(e):
            if not l: return short(g)
    return ''
SKIP = ('obsolete', 'archaic', 'dated', 'rare', 'dialectal', 'historical')
out = {}
for w in sorted(need):
    cand = entries.get(w, []) + ([] if w == w.lower() else entries.get(w.lower(), []))
    if w.endswith("'"): cand += entries.get(w[:-1], [])
    res, seen, late = [], set(), []
    for e in cand:
        pos = e.get('pos', '')
        if pos in ('name',) and w == w.lower(): continue
        for g, lem, tags in sense_info(e):
            if any(t in SKIP for t in tags): continue
            if lem:
                lg = lemma_gloss(lem)
                item = [lg or short(g), lem if lem.lower() != w.lower() else '']
                if not lg: item = [short(g), '']
            else:
                item = [short(g), '']
            if not item[0] or item[0] in seen or VULG.search(item[0]): continue
            if BAD.search(item[0]) and not item[1]:
                late.append(item); continue
            if len(item[0]) > 40 and res: continue
            seen.add(item[0]); res.append(item)
            break      # first usable sense per entry
        if len(res) >= 2: break
    if not res and late: res = late[:1]
    if res: out[w] = res
# fallback: the app's own single-word pairs (human-written), only for words Wiktionary lacks
def pairs(o):
    if isinstance(o, list):
        if len(o) >= 2 and isinstance(o[0], str) and isinstance(o[1], str):
            yield o[0], o[1]
        for x in o: yield from pairs(x)
    elif isinstance(o, dict):
        for v in o.values(): yield from pairs(v)
own = {}
for k in ('numbers', 'greetings', 'phrases', 'vocab', 'grammar'):
    for en, tg in pairs(d.get(k, [])):
        t = toks(tg)
        if len(t) == 1 and len(en) <= 40 and '/' not in en:
            own.setdefault(t[0].lower(), re.sub(r'^(the|a|an|to) ', '', en.split(' (')[0]) if False else en)
added = 0
for w in need:
    if w not in out and w.lower() in own:
        out[w] = [[own[w.lower()], '']]; added += 1
print('  own-pair fallback added', added)
os.makedirs(os.path.join(ROOT, 'gloss'), exist_ok=True)
json.dump(out, open(os.path.join(ROOT, 'gloss', lid + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(lid, 'needed', len(need), 'glossed', len(out), 'missing', sorted(need - set(out))[:25])
