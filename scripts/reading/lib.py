"""Authoring helpers for Reading passages. Each helper returns a question group (dict)."""
def ev(l, s): return [l, s]
def tfng(items, yn=False):
    """items: (statement, 'T'|'F'|'NG' (or 'Y'|'N'|'NG'), para, snippet, why)"""
    return {'t': 'tfng', 'yn': yn, 'items': [{'s': a, 'a': b, 'e': [c, d], 'w': (x[0] if (x := e) else '')} for a, b, c, d, *e in items]}
def mcq(items):
    """items: (question, [4 options], answer_index, para, snippet)"""
    return {'t': 'mcq', 'items': [{'q': q, 'o': o, 'a': a, 'e': [p, s]} for q, o, a, p, s in items]}
def multi(q, opts, answers, evs):
    return {'t': 'multi', 'qt': q, 'o': opts, 'a': answers, 'e': [list(x) for x in evs]}
def head(heads, items):
    """heads: list of heading texts (incl. spare ones); items: (para, head_index, snippet)"""
    return {'t': 'head', 'heads': heads, 'items': [{'p': p, 'a': h, 'e': [p, s]} for p, h, s in items]}
def info(items):
    """items: (statement, para, snippet)"""
    return {'t': 'info', 'items': [{'s': s, 'a': p, 'e': [p, sn]} for s, p, sn in items]}
def feat(title, opts, items, cls=False):
    """items: (statement, option_index, para, snippet)"""
    return {'t': 'feat', 'cls': cls, 'title': title, 'opts': opts, 'items': [{'s': s, 'a': a, 'e': [p, sn]} for s, a, p, sn in items]}
def ends(endings, items):
    """items: (stem, ending_index, para, snippet)"""
    return {'t': 'end', 'endings': endings, 'items': [{'s': s, 'a': a, 'e': [p, sn]} for s, a, p, sn in items]}
def sent(lim, items):
    """items: (sentence with ___, [accepted], para, snippet)"""
    return {'t': 'sent', 'lim': lim, 'items': [{'s': s, 'a': a, 'e': [p, sn]} for s, a, p, sn in items]}
def short(lim, items):
    return {'t': 'short', 'lim': lim, 'items': [{'q': q, 'a': a, 'e': [p, sn]} for q, a, p, sn in items]}
def summ(title, text, blanks, lim, bank=None, kind='summary'):
    """blanks: ([accepted], para, snippet) in order of [[1]],[[2]]..."""
    return {'t': 'summ', 'kind': kind, 'title': title, 'text': text, 'lim': lim, 'bank': bank,
            'a': [b[0] for b in blanks], 'e': [[b[1], b[2]] for b in blanks]}
def table(title, headrow, rows, blanks, lim):
    return {'t': 'table', 'title': title, 'head': headrow, 'rows': rows, 'lim': lim,
            'a': [b[0] for b in blanks], 'e': [[b[1], b[2]] for b in blanks]}
def flow(title, steps, blanks, lim):
    return {'t': 'flow', 'title': title, 'steps': steps, 'lim': lim,
            'a': [b[0] for b in blanks], 'e': [[b[1], b[2]] for b in blanks]}
def diag(title, w, h, svg, pts, blanks, lim, bank=None):
    return {'t': 'diag', 'title': title, 'w': w, 'h': h, 'svg': svg, 'pts': pts, 'lim': lim, 'bank': bank,
            'a': [b[0] for b in blanks], 'e': [[b[1], b[2]] for b in blanks]}
def pic(prompt, pics, items):
    """pics: list of (caption_letter_text, svg inner markup, w, h). items: (statement, pic_index, para, snippet)"""
    return {'t': 'pic', 'prompt': prompt, 'pics': [{'svg': p[0], 'w': p[1], 'h': p[2]} for p in pics],
            'items': [{'s': s, 'a': a, 'e': [p, sn]} for s, a, p, sn in items]}
def passage(id, title, topic, lv, intro, paras, groups):
    """paras: list of paragraph strings (lettered A.. automatically)."""
    return {'id': id, 'title': title, 'topic': topic, 'lv': lv, 'intro': intro,
            'paras': [{'l': chr(65 + i), 't': t.strip()} for i, t in enumerate(paras)], 'groups': groups}
