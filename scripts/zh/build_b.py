"""Build the B1-B2 content for Chinese: vocabulary groups, writing groups (+ stroke files), grammar lessons, reading passages, tap-gloss map.
Run from the repo root: python3 scripts/zh/build_b.py   (idempotent)"""
import json, re, sys, os
sys.path.insert(0, 'scripts/zh')
import jieba, pypinyin
import hsk, b_vocab, b_text
W = hsk.index()
ZH = 'data/lang/zh.json'
d = json.load(open(ZH, encoding='utf-8'))

# ---- reset previous B content (idempotent)
d['vocab'] = [g for g in d['vocab'] if not g['id'].startswith('b-')]
d['writing'] = [g for g in d['writing'] if not g['id'].startswith('b-')]
d['grammar'] = [g for g in d['grammar'] if g.get('lv') != 'b']
for g in d['grammar']:
    g['lv'] = 'a'

have = set(it[3] for sec in ('numbers', 'greetings', 'phrases', 'vocab', 'writing') for g in d[sec] for it in g['items'])

OVR = {}  # manual pinyin overrides
import unicodedata
def _norm(p): return re.sub(r'[^a-z]', '', unicodedata.normalize('NFD', p.lower()).encode('ascii', 'ignore').decode())
def _tone(h): return ''.join(pypinyin.lazy_pinyin(h, style=pypinyin.TONE))
OVR.update({'哪儿': 'nǎr', '快点儿': 'kuài diǎnr', '点儿': 'diǎnr', '一点儿': 'yìdiǎnr', '这儿': 'zhèr', '那儿': 'nàr', '一会儿': 'yíhuìr'})
def py(h):
    if h in OVR: return OVR[h]
    want = _tone(h)
    e = W.get(h)
    if e:
        for f in e['e']['forms']:
            p = f['transcriptions']['pinyin']
            if p == p.lower() and _norm(p) == _norm(want):
                if re.sub(r'[\s\']', '', p) == want or True:
                    # same toneless letters: require same tone marks too, neutral tones in the dictionary are fine
                    a_, b_ = re.sub(r"[\s']", '', p), want
                    if a_ == b_ or all(x == y or x not in 'āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ' for x, y in zip(a_, b_)):
                        syl = p.split(); out = syl[0]
                        for s in syl[1:]:
                            out += ("'" if s[0] in 'aoeāáǎàōóǒòēéěè' else '') + s
                        return out
    return want

for a, b in [('连', '饭'), ('把', '门'), ('说', '汉语'), ('说', '得'), ('跑', '得'), ('写', '得'), ('吃', '得'), ('唱', '得'), ('起', '得'), ('睡', '得'), ('是', '在'), ('是', '坐'), ('的', '话'), ('风', '吹'), ('坐', '飞机'), ('还', '学'), ('太', '少'), ('很', '快'), ('很', '早'), ('很', '好听')]:
    jieba.suggest_freq((a, b), True)

def sent_py(t):
    out = []
    for w in jieba.cut(t):
        if re.search(r'[一-鿿]', w):
            out.append(py(w))
        elif w.strip() and not re.fullmatch(r'[,。?!、;:\s]+', w):
            out.append(w)
    return re.sub(r'(?<![a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ])dé(?![a-z])', 'de', ' '.join(out))

# ---- vocabulary
seen = set(have); first = {}
for gid, title, lv, s in b_vocab.G:
    items = []
    for p in s.split('|'):
        h, e = p.split(' ', 1)
        w = W.get(h)
        if h in seen or not w or w['old'] not in (3, 4): continue
        seen.add(h)
        items.append([e, py(h), '', h, None, None, None, 'b', w['old']])
    title = title.split(' \u00b7 ')[-1].replace('Linking words and grammar', 'More words') + (' (B1)' if lv == 3 else ' (B2)')
    d['vocab'].append({'id': 'b-' + gid, 'title': title, 'items': items})
print('vocab groups', [(g['id'], len(g['items'])) for g in d['vocab'] if g['id'].startswith('b-')])

# ---- writing
WD = '/tmp/hzw/node_modules/hanzi-writer-data/'
def two(gid): return [it for g in d['vocab'] if g['id'] == 'b-' + gid for it in g['items'] if len(it[3]) == 2]
WSETS = [('b-places', 'Places and time', 'Intermediate words. Each character has its own box.', two('hsk3-people-places')[:8] + two('hsk3-time-seasons')[:6]),
         ('b-verbs', 'Everyday verbs', 'Intermediate words. Each character has its own box.', two('hsk3-verbs')[:14]),
         ('b-feelings', 'Feelings and character', 'Intermediate words. Each character has its own box.', two('hsk4-feelings')[:14]),
         ('b-society', 'Society and work', 'Intermediate words. Each character has its own box.', two('hsk4-society')[:14])]
for gid, title, note, its in WSETS:
    sd = {}; items = []
    for it in its:
        h = it[3]
        if not all(os.path.exists(WD + c + '.json') for c in h): continue
        cnt = []
        for c in h:
            j = json.load(open(WD + c + '.json'))
            sd[c] = {'strokes': j['strokes'], 'medians': j['medians']}; cnt.append(len(j['strokes']))
        items.append([it[0], it[1], '', h, cnt, None, None, 'b', it[8]])
    json.dump(sd, open('data/lang/zh-w-%s.json' % gid, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    d['writing'].append({'id': gid, 'title': title, 'note': note, 'items': items})
print('writing', [(g['id'], len(g['items'])) for g in d['writing'] if g['id'].startswith('b-')])

# ---- grammar
for gid, title, text, rows, ex in b_text.GRAMMAR:
    d['grammar'].append({'id': gid, 'title': title, 'lv': 'b', 'text': text,
        'rows': [[r[0], sent_py(r[2]) if re.search(r'[一-鿿]', r[2]) else r[2], r[1] if False else r[1]] for r in rows],
        'ex': [[en, sent_py(zh), '', zh] for en, zh in ex]})

# ---- reading
R = []; gl = {}
cc = {}
for gid, title, en, lv, paras, qs in b_text.READING:
    P = {'id': gid, 'title': title, 'en': en, 'lv': lv, 'paras': [], 'f': []}
    for i, t in enumerate(paras): P['paras'].append({'l': 'AB'[i], 't': t})
    for q, o, s in qs: P['f'].append({'q': q, 'o': o, 's': s})
    R.append(P)
d['reading'] = R
json.dump(d, open(ZH, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('reading', len(R))
