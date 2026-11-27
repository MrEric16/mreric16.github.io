"""Clean dictionary data for HSK words: pinyin with tone marks (syllables joined per word) and a short English gloss."""
import re, sys
sys.path.insert(0, 'scripts/zh')

BAD_START = re.compile(r'^(surname|variant of|old variant|erhua variant|abbr\.|see |used in|CL:|also written|archaic|literary|interjection|onom|short for|prefix|suffix|classifier)', re.I)
SKIP = set('把 被 啊 吧 吗 呢 的 了 过 着 得 地 就 才 都 也 还 又 再 将 向 往 从 对 给 让 叫 使 跟 和 与 及 而 并 或 但 却 因 所 为 以 之 其 么 们 个 位 次 种 张 本 件 条 只 双 套 些 点 哪'.split())


def pinyin(e):
    syl = e['forms'][0]['transcriptions']['pinyin'].split()
    out = syl[0]
    for s in syl[1:]:
        out += ("'" if s[0].lower() in 'aoeāáǎàōóǒòēéěè' else '') + s
    return out[0].lower() + out[1:] if out[0].isupper() and False else out


def clean_piece(m):
    m = re.sub(r'\s*\([^)]*\)', '', m).strip()
    m = re.sub(r'\s+', ' ', m)
    return m


def gloss(e):
    ms = e['forms'][0]['meanings']
    pieces = []
    for m in ms:
        if BAD_START.match(m):
            continue
        for p in m.split(';'):
            p = clean_piece(p)
            if p and not BAD_START.match(p) and len(p) <= 34 and p not in pieces:
                pieces.append(p)
        if len(pieces) >= 2:
            break
    if not pieces:
        return ''
    g = ', '.join(pieces[:2])
    return g if len(g) <= 46 else pieces[0]
