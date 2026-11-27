"""Tap-gloss map for the Chinese reading passages: data/lang/gloss/zh.json  {segment: [[meaning, pinyin], ...]}"""
import sys, json, re
sys.path.insert(0, 'scripts/zh')
import jieba, pypinyin, hsk, words
W = hsk.index()
d = json.load(open('data/lang/zh.json', encoding='utf-8'))
MAN = json.load(open('scripts/zh/gloss_manual.json', encoding='utf-8')) if __import__('os').path.exists('scripts/zh/gloss_manual.json') else {}

def entry(h):
    if h in MAN: return MAN[h]
    e = W.get(h)
    if not e: return None
    want = ''.join(pypinyin.lazy_pinyin(h, style=pypinyin.NORMAL)).lower()
    fs = sorted(e['e']['forms'], key=lambda f: 0 if re.sub(r'[^a-z]', '', __import__('unicodedata').normalize('NFD', f['transcriptions']['pinyin'].lower()).encode('ascii', 'ignore').decode()) == want else 1)
    for f in fs:
        p = f['transcriptions']['pinyin']
        if p != p.lower(): continue
        e2 = {'forms': [f]}
        g = words.gloss(e2)
        if g:
            syl = p.split(); out = syl[0]
            for s in syl[1:]: out += ("'" if s[0] in 'aoeāáǎàōóǒòēéěè' else '') + s
            return [g, out]
    return None

def pieces(w):
    out = []; i = 0
    while i < len(w):
        for j in range(min(len(w), i + 4), i, -1):
            x = w[i:j]
            if entry(x): out.append(entry(x)); i = j; break
        else:
            out.append(['', ''.join(pypinyin.lazy_pinyin(w[i], style=pypinyin.TONE))]); i += 1
    return out

segs = set()
for P in d['reading']:
    for t in [p['t'] for p in P['paras']] + [x for f in P['f'] for x in f['s']]:
        for w in jieba.cut(re.sub(r'\{\d\}', '', t)):
            if re.search(r'[一-鿿]', w): segs.add(w)
G = {}
for w in sorted(segs):
    e = entry(w)
    G[w] = [e] if e else pieces(w)
json.dump(G, open('data/lang/gloss/zh.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
if '--show' in sys.argv:
    for w, v in G.items(): print(w, ' | '.join(a + ' (' + b + ')' for a, b in v))
