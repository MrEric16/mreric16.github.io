#!/usr/bin/env python3
"""Compile scripts/grammar-bank-src/t*.txt into data/grammar/ (index.json + one JSON per topic) (Grammar Practice).
Format per line:  question with ___ per blank => accepted|alt ;; accepted for blank 2
A line with no ___ is a whole-sentence answer (rewrite / correct the mistake). Contractions,
capitalisation, punctuation and American spellings are forgiven by the app's checker."""
import glob, json, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
topics, bad = [], 0
files = sorted(glob.glob(os.path.join(root, 'scripts/grammar-bank-src/t*.txt'))) + sorted(glob.glob(os.path.join(root, 'scripts/grammar-bank-src/g_*.txt')))
byid = {}
for f in files:
    cur = lvl = None
    for ln, l in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
        l = l.strip()
        if not l: continue
        if l.startswith('@topic'):
            i, n = [x.strip() for x in l[6:].split('|')]
            if i in byid: cur = byid[i]; continue
            cur = {'id': i, 'name': n, 'levels': {'easy': [], 'medium': [], 'hard': []}}; topics.append(cur); byid[i] = cur; continue
        if l in ('@easy', '@medium', '@hard'): lvl = l[1:]; continue
        if ' => ' not in l: print('NO =>', f, ln); bad += 1; continue
        q, a = l.rsplit(' => ', 1)
        groups = [[x.strip() for x in g.split('|') if x.strip()] for g in a.split(' ;; ')]
        if (q.count('___') or 1) != len(groups) or any(not g for g in groups): print('BAD', f, ln, l); bad += 1; continue

        cur['levels'][lvl].append({'q': q, 'a': groups})
for t in topics:
    for k, arr in t['levels'].items():
        seen, out = set(), []
        for it in arr:
            if it['q'] in seen: continue
            seen.add(it['q']); out.append(it)
        t['levels'][k] = out
if bad: sys.exit(1)
import hashlib, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gg_tag, gg_pools
ntag = 0
for t in topics:
    for k, arr in t['levels'].items():
        seen, out = set(), []
        for it in arr:
            q, a = gg_tag.tag(it['q'], it['a'])
            if q != it['q']: ntag += 1
            key = q + '\u0001' + json.dumps(a, ensure_ascii=False)
            if key in seen: continue
            seen.add(key); out.append({'q': q, 'a': a})
        t['levels'][k] = out
print(ntag, 'items carry random-name/place/job slots')
ORDER = '''present-simple-be present-simple-other present-continuous present-simple-vs-continuous past-simple-be past-simple-other past-continuous past-simple-vs-continuous
present-perfect-simple present-perfect-continuous present-perfect-simple-vs-continuous present-perfect-vs-past-simple
past-perfect past-perfect-continuous past-perfect-simple-vs-continuous past-perfect-vs-past-simple present-perfect-vs-past-perfect narrative-tenses
future-will future-going-to future-present-continuous future-will-vs-going-to future-all-forms future-perfect future-perfect-continuous future-perfect-simple-vs-continuous
zero-conditional first-conditional second-conditional third-conditional conditionals-which-type conditional-connectors wish-and-if-only
passive-present-simple passive-past-simple passive-continuous passive-perfect passive-future passive-modals passive-reporting-verbs active-or-passive causative-have-something-done
reported-statements reported-questions reported-commands reporting-verbs reported-speech-all indirect-questions
modals-ability modals-obligation modals-advice modals-possibility modals-perfect modals-all
stative-verbs used-to-would-and-be-used-to gerunds-and-infinitives
comparatives superlatives comparatives-or-superlatives as-as-too-and-enough articles quantifiers determiners possessives this-that-these-those reflexive-pronouns-and-each-other indefinite-pronouns adverbs-of-frequency adjectives-or-adverbs adjective-order
dependent-prepositions collocations-make-do-take-get-have word-formation key-word-transformations error-correction
relative-clauses-defining relative-clauses-non-defining participle-clauses linkers inversion question-tags so-neither-too-and-either
prepositions-of-time prepositions-of-place prepositions-of-movement phrasal-verbs-separable-and-inseparable irregular-verbs subject-verb-agreement time-clauses for-since-ago-already-yet-still-just purpose-and-result wh-questions verbs-that-change-meaning verb-object-infinitive participle-adjectives commonly-confused-words would-rather-had-better-its-time-prefer future-in-the-past countable-and-uncountable-nouns'''.split()
topics.sort(key=lambda t: ORDER.index(t['id']) if t['id'] in ORDER else len(ORDER))
outdir = os.path.join(root, 'data/grammar')
os.makedirs(outdir, exist_ok=True)
for f in os.listdir(outdir):
    if f.endswith('.json'): os.remove(os.path.join(outdir, f))
dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':')) + '\n'
for t in topics:
    open(os.path.join(outdir, t['id'] + '.json'), 'w', encoding='utf-8').write(dump(t))
open(os.path.join(outdir, 'index.json'), 'w', encoding='utf-8').write(dump({'topics': [{'id': t['id'], 'name': t['name']} for t in topics]}))
pools = gg_pools.build()
open(os.path.join(outdir, 'pools.json'), 'w', encoding='utf-8').write(dump(pools))
h = hashlib.sha1()
for f in sorted(os.listdir(outdir)): h.update(open(os.path.join(outdir, f), 'rb').read())
ver = h.hexdigest()[:10]
gp = os.path.join(root, 'grammar.html')
g = open(gp, encoding='utf-8').read()
g2 = re.sub(r"var DATA_V = '[^']*';", "var DATA_V = '" + ver + "';", g, count=1)
if g2 != g: open(gp, 'w', encoding='utf-8').write(g2)
print(len(topics), 'topics written to data/grammar/ (one file each + index.json)')
