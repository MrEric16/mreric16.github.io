#!/usr/bin/env python3
"""Adds a level band (a/b/c) as the 8th element of every Chinese item in data/lang/zh.json, from the official HSK lists."""
import sys, json, re, collections
sys.path.insert(0, 'scripts/zh')
import hsk, jieba
W = hsk.index()
for w in W:
    if len(w) > 1:
        jieba.add_word(w, 100000)
RANK = {'a': 0, 'b': 1, 'c': 2}
# character -> easiest band among HSK words containing it
CH = {}
for w, v in W.items():
    if v['band'] is None:
        continue
    for ch in w:
        if ch not in CH or RANK[v['band']] < RANK[CH[ch]]:
            CH[ch] = v['band']
PUNCT = re.compile(r'[^一-鿿]')


def band_item(h):
    h = PUNCT.sub('', h)
    if not h:
        return None
    if h in W and W[h]['band']:
        return W[h]['band']
    segs = [s for s in jieba.cut(h) if s.strip()]
    out = []
    for s in segs:
        if s in W and W[s]['band']:
            out.append(W[s]['band'])
        elif len(s) == 1 and s in CH:
            out.append(CH[s])
        elif len(s) > 1 and all(c in CH for c in s):
            out.append(max((CH[c] for c in s), key=lambda b: RANK[b]))
    return max(out, key=lambda b: RANK[b]) if out else None


def hsk_num(h):
    """HSK 2.0 level (1-6) shown on a card: only for items that are exactly one word in the official list; otherwise 0."""
    h = PUNCT.sub('', h)
    return W[h]['old'] if h in W and W[h]['old'] else 0


def main():
    p = 'data/lang/zh.json'
    d = json.load(open(p, encoding='utf-8'))
    stats = collections.Counter()
    unknown = []
    for sec in ('numbers', 'greetings', 'phrases', 'vocab', 'writing'):
        for g in d[sec]:
            bands = [band_item(it[3]) for it in g['items']]
            known = [b for b in bands if b]
            maj = collections.Counter(known).most_common(1)[0][0] if known else 'b'
            for it, b in zip(g['items'], bands):
                if sec in ('numbers', 'greetings'):
                    b = 'a'
                elif b is None:
                    unknown.append((sec, g['id'], it[3], it[0]))
                    b = maj
                while len(it) < 7:
                    it.append(None)
                it[:] = it[:7] + [b, hsk_num(it[3])]
                stats[(sec, b)] += 1
    for sec in ('numbers', 'greetings', 'phrases', 'vocab', 'writing'):
        print(sec, {b: stats[(sec, b)] for b in 'abc'})
    print('unknown inherited:', len(unknown))
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    json.dump(unknown, open('/tmp/zh_unknown.json', 'w', encoding='utf-8'), ensure_ascii=False)


if __name__ == '__main__':
    main()
