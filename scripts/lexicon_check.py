#!/usr/bin/env python3
"""Lexicon source format (scripts/content/lex_<pos>.txt), one concept per line:
   domain|a1,a2,a3 ~ b1,b2,b3     two opposite clusters (each word means the same as its side-mates, opposite to the other side)
   domain|a1,a2,a3                a cluster with no opposite
Every word may appear once in the whole lexicon. Prints problems; use load() from the builder."""
import glob, re, sys, collections
def load(verbose=True):
    cl = []; seen = collections.defaultdict(list); bad = 0
    for f in sorted(glob.glob('scripts/content/lex_*.txt')):
        pos = re.search(r'lex_(\w+)\.txt', f).group(1)
        for n, line in enumerate(open(f, encoding='utf8'), 1):
            line = line.strip()
            if not line or line.startswith('#'): continue
            p = line.split('|')
            if len(p) != 2: print('BAD LINE', f, n, line[:60]); bad += 1; continue
            dom, body = p; sides = [s.strip() for s in body.split('~')]
            if len(sides) > 2: print('TOO MANY SIDES', f, n); bad += 1; continue
            ids = []
            for s in sides:
                ws = [w.strip() for w in s.split(',') if w.strip()]
                c = {'id': ws[0] if ws else '?', 'pos': pos, 'dom': dom.strip(), 'w': ws, 'file': f, 'line': n, 'opp': []}
                cl.append(c); ids.append(c)
                if len(ws) < 2: print('TOO SMALL', f, n, ws); bad += 1
                if len(set(w.lower() for w in ws)) != len(ws): print('DUPWORD', f, n, ws); bad += 1
                for w in ws: seen[(pos, w.lower())].append(n)
            if len(ids) == 2: ids[0]['opp'].append(ids[1]['id']); ids[1]['opp'].append(ids[0]['id'])
    for w, where in seen.items():
        if len(where) > 1 and verbose: print('REPEATED', w, where); bad += 1
    byid = collections.Counter((c['pos'], c['id']) for c in cl)
    for i, k in byid.items():
        if k > 1 and verbose: print('ID CLASH', i); bad += 1
    if verbose: print(len(cl), 'clusters,', sum(len(c['w']) for c in cl), 'words,', sum(1 for c in cl if c['opp']), 'with an opposite;', bad, 'problems')
    return cl
if __name__ == '__main__': load()
