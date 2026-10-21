#!/usr/bin/env python3
"""Validates scripts/reading/passages/*.py and writes data/reading/<id>.json + index.json.
Every evidence snippet must occur verbatim in the paragraph it cites; every completion answer must sit inside its snippet."""
import sys, os, re, json, glob, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
BAD = ['--', '\u2014', '\u2013']
def banned(s):
    return [b for b in BAD if b in s] + (['gotten'] if re.search(r'\bgotten\b', s, re.I) else [])
errs = []
def err(pid, m): errs.append('%s: %s' % (pid, m))
def words(s): return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*", s))
def walk(o):
    if isinstance(o, str): yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)
def check(p):
    pid = p['id']; P = {x['l']: x['t'] for x in p['paras']}
    for s in walk({k: v for k, v in p.items() if k != 'groups'}) :
        for b in banned(s): err(pid, 'banned %r in passage text' % b)
    wc = sum(words(x['t']) for x in p['paras'])
    if wc < 600 or wc > 950: err(pid, 'passage length %d words' % wc)
    seen_ids = set()
    for gi, g in enumerate(p['groups']):
        t = g['t']; tag = '%s g%d(%s)' % (pid, gi, t)
        for s in walk(g):
            for b in banned(s): err(tag, 'banned %r in %r' % (b, s[:50]))
        def ec(e, ans=None):
            l, sn = e
            if l not in P: err(tag, 'bad para %s' % l); return
            if sn not in P[l]: err(tag, 'snippet not in para %s: %r' % (l, sn[:60]))
            if ans:
                if not any(a.lower() in sn.lower() for a in ans): err(tag, 'answer %r not inside snippet %r' % (ans[0], sn[:60]))
        if t == 'tfng':
            ok = ('T', 'F', 'NG') if not g['yn'] else ('Y', 'N', 'NG')
            for it in g['items']:
                if it['a'] not in ok: err(tag, 'bad answer %r' % it['a'])
                ec(it['e'])
            if len(g['items']) < 4: err(tag, 'few items')
            from collections import Counter
            c = Counter(i['a'] for i in g['items'])
            if len(c) < 3: err(tag, 'tfng group needs all three answers: %s' % dict(c))
        elif t == 'mcq':
            for it in g['items']:
                if len(it['o']) != 4 or not (0 <= it['a'] < 4): err(tag, 'mcq shape')
                ec(it['e'])
        elif t == 'multi':
            if len(g['o']) != 5 or len(g['a']) != 2 or len(g['e']) != 2: err(tag, 'multi shape')
            for e in g['e']: ec(e)
        elif t == 'head':
            if len(g['heads']) < len(g['items']) + 2: err(tag, 'need 2+ spare headings')
            used = [i['a'] for i in g['items']]
            if len(set(used)) != len(used): err(tag, 'heading reused')
            for i in g['items']:
                if i['a'] >= len(g['heads']): err(tag, 'heading idx')
                ec(i['e'])
        elif t == 'info':
            for i in g['items']:
                if i['e'][0] != i['a']: err(tag, 'info evidence para must equal answer')
                ec(i['e'])
        elif t in ('feat', 'end'):
            ol = g['opts'] if t == 'feat' else g['endings']
            if t == 'end' and len(ol) < len(g['items']) + 2: err(tag, 'too few endings')
            for i in g['items']:
                if i['a'] >= len(ol): err(tag, 'option idx')
                ec(i['e'])
            if t == 'feat' and len(ol) > 7: err(tag, 'too many options')
        elif t in ('sent', 'short'):
            for i in g['items']:
                if t == 'sent' and i['s'].count('___') != 1: err(tag, 'need one ___')
                for a in i['a']:
                    if words(a) > g['lim']: err(tag, 'answer %r over limit' % a)
                ec(i['e'], i['a'])
        elif t in ('summ', 'table', 'flow', 'diag'):
            n = len(g['a'])
            txt = ' '.join(walk({'x': g.get('text', ''), 'r': g.get('rows', []), 's': g.get('steps', [])}))
            ms = sorted(int(m) for m in re.findall(r'\[\[(\d+)\]\]', txt))
            if t != 'diag' and ms != list(range(1, n + 1)): err(tag, 'markers %s vs %d answers' % (ms, n))
            if t == 'diag' and len(g['pts']) != n: err(tag, 'pts vs answers')
            if len(g['e']) != n: err(tag, 'evidence count')
            for a, e in zip(g['a'], g['e']):
                if g.get('bank'):
                    if a[0] not in g['bank']: err(tag, 'bank missing %r' % a[0])
                for x in a:
                    if words(x) > g['lim']: err(tag, 'answer %r over limit' % x)
                ec(e, a)
            if g.get('bank') and len(g['bank']) < n + 2: err(tag, 'bank needs 2+ spare words')
        elif t == 'pic':
            for i in g['items']:
                if i['a'] >= len(g['pics']): err(tag, 'pic idx')
                ec(i['e'])
        else: err(tag, 'unknown type')
def main():
    out = os.path.join(ROOT, 'data', 'reading'); os.makedirs(out, exist_ok=True)
    idx = []
    for f in sorted(glob.glob(os.path.join(HERE, 'passages', 'p*.py'))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        p = m.P; check(p)
        for gi, g in enumerate(p['groups']): g['id'] = '%s-%d' % (p['id'], gi)
        json.dump(p, open(os.path.join(out, p['id'] + '.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
        types = sorted({g['t'] for g in p['groups']})
        cap = {'tfng': 0, 'mcq': 0}
        idx.append({'id': p['id'], 'title': p['title'], 'topic': p['topic'], 'lv': p['lv'], 'types': types,
                    'n': sum(len(g['items']) if 'items' in g else len(g['a']) for g in p['groups'])})
    json.dump({'v': 1, 'passages': idx}, open(os.path.join(out, 'index.json'), 'w'), separators=(',', ':'))
    for e in errs: print('ERR', e)
    print(len(idx), 'passages,', len(errs), 'errors')
    sys.exit(1 if errs else 0)
main()
