#!/usr/bin/env python3
"""Builds the "Direct & reported speech" group of grammar topics.

Every item is produced by one rule engine (backshift rules, pronoun / time / place shifts, question
word order, to-infinitive commands), and the accepted answers come from the same engine, so the
sentence and its key can never disagree. Run:  python3 scripts/grammar/build_drs.py
Writes data/grammar/drs-*.json and updates data/grammar/index.json.
"""
import json, random, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(ROOT, 'data', 'grammar')
RNG = random.Random(20261126)
PER_LEVEL = 260

# ---------------------------------------------------------------- people
MALE = ['Ali', 'Timur', 'Bobur', 'Aziz', 'Jasur', 'Omar', 'Sardor', 'Rustam', 'Farhod', 'Daniel']
FEM = ['Mina', 'Dilnoza', 'Laylo', 'Aisha', 'Zarina', 'Nodira', 'Maria', 'Sevara', 'Malika', 'Madina']
KIN = [('my brother', 'm'), ('my father', 'm'), ('my uncle', 'm'), ('my sister', 'f'), ('my mother', 'f'), ('my aunt', 'f')]
PRON = {'m': ('he', 'him', 'his'), 'f': ('she', 'her', 'her')}


def cap(s):
    return s[0].upper() + s[1:]


def person(exclude=(), g=None, kin=False):
    while True:
        if kin and RNG.random() < .4:
            n, gg = RNG.choice(KIN)
        else:
            gg = g or RNG.choice('mf')
            n = RNG.choice(MALE if gg == 'm' else FEM)
        if (g is None or gg == g) and n not in exclude:
            return {'n': n, 'g': gg}


# ---------------------------------------------------------------- verbs
# base: (3sg, past, pp, ing)
VERBS = {
    'play': ('plays', 'played', 'played', 'playing'), 'watch': ('watches', 'watched', 'watched', 'watching'),
    'study': ('studies', 'studied', 'studied', 'studying'), 'cook': ('cooks', 'cooked', 'cooked', 'cooking'),
    'read': ('reads', 'read', 'read', 'reading'), 'write': ('writes', 'wrote', 'written', 'writing'),
    'clean': ('cleans', 'cleaned', 'cleaned', 'cleaning'), 'visit': ('visits', 'visited', 'visited', 'visiting'),
    'buy': ('buys', 'bought', 'bought', 'buying'), 'meet': ('meets', 'met', 'met', 'meeting'),
    'learn': ('learns', 'learned', 'learned', 'learning'), 'drink': ('drinks', 'drank', 'drunk', 'drinking'),
    'finish': ('finishes', 'finished', 'finished', 'finishing'), 'repair': ('repairs', 'repaired', 'repaired', 'repairing'),
    'paint': ('paints', 'painted', 'painted', 'painting'), 'walk': ('walks', 'walked', 'walked', 'walking'),
    'travel': ('travels', 'travelled', 'travelled', 'travelling'), 'live': ('lives', 'lived', 'lived', 'living'),
    'work': ('works', 'worked', 'worked', 'working'), 'wait': ('waits', 'waited', 'waited', 'waiting'),
    'sleep': ('sleeps', 'slept', 'slept', 'sleeping'), 'run': ('runs', 'ran', 'run', 'running'),
    'speak': ('speaks', 'spoke', 'spoken', 'speaking'), 'sing': ('sings', 'sang', 'sung', 'singing'),
    'eat': ('eats', 'ate', 'eaten', 'eating'), 'make': ('makes', 'made', 'made', 'making'),
    'go': ('goes', 'went', 'gone', 'going'), 'see': ('sees', 'saw', 'seen', 'seeing'),
    'take': ('takes', 'took', 'taken', 'taking'), 'wash': ('washes', 'washed', 'washed', 'washing'),
    'open': ('opens', 'opened', 'opened', 'opening'), 'bake': ('bakes', 'baked', 'baked', 'baking'),
    'help': ('helps', 'helped', 'helped', 'helping'),
}

# flags: dur = fits for/since, tel = fits already/just/yet, act = fits continuous tenses,
# what = object can be asked about, where = place complement can be asked about, sh = contains here/this
def P(v, obj, **f):
    d = {'v': v, 'obj': obj, 'dur': False, 'tel': False, 'act': True, 'what': False, 'where': False, 'sh': False}
    d.update(f)
    return d


PREDS = [
    P('play', 'tennis', dur=True, what=True), P('play', 'football', dur=True, what=True), P('play', 'chess', dur=True, what=True),
    P('watch', 'a film', tel=True, what=True), P('watch', 'the news', what=True),
    P('study', 'English', dur=True, what=True), P('study', 'for the exam', dur=True),
    P('cook', 'dinner', tel=True, what=True), P('cook', 'plov', tel=True, what=True),
    P('read', '{P} book', tel=True, what=True), P('read', 'this book', tel=True, what=True, sh=True),
    P('write', 'an essay', tel=True, what=True), P('write', 'a letter', tel=True, what=True),
    P('clean', '{P} room', tel=True), P('clean', 'the kitchen', tel=True),
    P('visit', '{P} grandparents'), P('visit', 'the museum', tel=True),
    P('buy', 'a new phone', tel=True, what=True), P('buy', 'some bread', tel=True, what=True),
    P('meet', '{P} friends'),
    P('learn', 'French', dur=True, what=True), P('learn', 'ten new words', tel=True, what=True),
    P('drink', 'tea', what=True), P('drink', 'green tea', what=True),
    P('finish', '{P} project', tel=True, act=False), P('finish', 'the report', tel=True, act=False),
    P('repair', 'the bike', tel=True), P('paint', 'the fence', tel=True),
    P('walk', 'to school'), P('travel', 'to Samarkand', where=True),
    P('live', 'in Tashkent', dur=True, where=True), P('live', 'here', dur=True, where=True, sh=True),
    P('work', 'in a bank', dur=True, where=True), P('work', 'at a hospital', dur=True, where=True),
    P('wait', 'for the bus', dur=True), P('sleep', 'late'),
    P('run', 'in the park', dur=True, where=True), P('speak', 'three languages', dur=True),
    P('sing', 'in the choir', dur=True, where=True), P('eat', 'lunch', what=True),
    P('make', 'a cake', tel=True, what=True), P('go', 'to the gym', where=True), P('go', 'to school', where=True),
    P('see', 'a doctor'), P('take', 'photos', what=True), P('wash', 'the car', tel=True),
    P('open', 'the shop', tel=True), P('bake', 'bread', tel=True, what=True), P('help', '{P} brother'),
]
BE = [{'be': True, 'adj': a, 'dur': True, 'tel': False, 'act': False, 'what': False, 'where': False, 'sh': False, 'v': 'be', 'obj': ''}
      for a in ['tired', 'hungry', 'busy', 'late', 'ready', 'upset', 'nervous']]

# ---------------------------------------------------------------- adverbials
# D = direct wording(s), R = reported wording(s), ok = direct tenses that can carry it, need = verb flag
def A(ts, D, R, pos='end', ok=None, pols=('aff', 'neg', 'q'), need=None, shift=False):
    return {'ts': ts, 'D': D, 'R': R, 'pos': pos, 'ok': ok or ts, 'pols': pols, 'need': need, 'shift': shift}


ADVS = [
    A(['ps'], ['every day'], ['every day'], ok=['ps', 'pas']), A(['ps'], ['every morning'], ['every morning'], ok=['ps', 'pas']),
    A(['ps'], ['on Sundays'], ['on Sundays'], ok=['ps', 'pas']), A(['ps'], ['after school'], ['after school'], ok=['ps', 'pas']),
    A(['ps'], ['at the weekend'], ['at the weekend'], ok=['ps', 'pas']), A(['ps'], ['twice a week'], ['twice a week'], ok=['ps', 'pas']),
    A(['ps'], ['usually'], ['usually'], pos='mid', ok=['ps', 'pas']), A(['ps'], ['always'], ['always'], pos='mid', ok=['ps', 'pas'], pols=('aff',)),
    A(['ps'], ['never'], ['never'], pos='mid', ok=['ps', 'pas'], pols=('aff',)),
    A(['pc'], ['now', 'right now', 'at the moment'], ['then', 'at that moment', 'at that time'], ok=['pc'], shift=True),
    A(['pc'], ['today'], ['that day'], ok=['pc', 'pac'], shift=True), A(['pc'], ['this week'], ['that week'], ok=['pc', 'pac'], shift=True),
    A(['pc'], ['this morning'], ['that morning'], ok=['pc', 'pac'], shift=True),
    A(['pp'], ['already'], ['already'], pos='mid', ok=['pp', 'pap', 'pas'], pols=('aff',), need='tel'),
    A(['pp'], ['just'], ['just'], pos='mid', ok=['pp', 'pap'], pols=('aff',), need='tel'),
    A(['pp'], ['never'], ['never'], pos='mid', ok=['pp', 'pap', 'pas'], pols=('aff',)),
    A(['pp'], ['ever'], ['ever'], pos='mid', ok=['pp', 'pap', 'pas'], pols=('q',)),
    A(['pp'], ['yet'], ['yet'], ok=['pp', 'pap'], pols=('neg', 'q'), need='tel'),
    A(['pp'], ['for two years'], ['for two years'], ok=['pp', 'pap', 'pas'], need='dur'),
    A(['pp'], ['for six months'], ['for six months'], ok=['pp', 'pap', 'pas'], need='dur'),
    A(['pp'], ['since Monday'], ['since Monday'], ok=['pp', 'pap'], need='dur'),
    A(['pp'], ['since 2020'], ['since 2020'], ok=['pp', 'pap'], need='dur'),
    A(['pp'], ['this week'], ['that week'], ok=['pp', 'pas', 'pap'], shift=True),
    A(['pp'], ['today'], ['that day'], ok=['pp', 'pas', 'pap'], shift=True),
    A(['pp'], ['this year'], ['that year'], ok=['pp', 'pas', 'pap'], shift=True),
    A(['ppc'], ['for two hours'], ['for two hours'], ok=['ppc', 'papc', 'pac'], need='dur'),
    A(['ppc'], ['since morning'], ['since morning'], ok=['ppc', 'papc'], need='dur'),
    A(['ppc'], ['all day'], ['all day'], ok=['ppc', 'papc', 'pac'], need='dur'),
    A(['ppc'], ['since eight o\'clock'], ['since eight o\'clock'], ok=['ppc', 'papc'], need='dur'),
    A(['ppc'], ['lately'], ['lately'], ok=['ppc', 'papc'], need='dur'),
    A(['ppc'], ['this week'], ['that week'], ok=['ppc', 'papc', 'pac'], need='dur', shift=True),
    A(['ppc'], ['today'], ['that day'], ok=['ppc', 'papc', 'pac'], need='dur', shift=True),
    A(['pas'], ['yesterday'], ['the day before', 'the previous day'], ok=['pas', 'pap'], shift=True),
    A(['pas'], ['last week'], ['the week before', 'the previous week'], ok=['pas', 'pap'], shift=True),
    A(['pas'], ['last night'], ['the night before', 'the previous night'], ok=['pas', 'pap'], shift=True),
    A(['pas'], ['last year'], ['the year before', 'the previous year'], ok=['pas', 'pap'], shift=True),
    A(['pas'], ['last month'], ['the month before', 'the previous month'], ok=['pas', 'pap'], shift=True),
    A(['pas'], ['two days ago'], ['two days before', 'two days earlier'], ok=['pas', 'pap'], shift=True),
    A(['pas'], ['three weeks ago'], ['three weeks before', 'three weeks earlier'], ok=['pas', 'pap'], shift=True),
    A(['pas'], ['in 2019'], ['in 2019'], ok=['pas', 'pap']), A(['pas'], ['in July'], ['in July'], ok=['pas', 'pap']),
    A(['pas'], ['at the weekend'], ['at the weekend'], ok=['pas', 'pap']),
    A(['pac'], ['all morning'], ['all morning'], ok=['pac', 'papc']), A(['pac'], ['at eight o\'clock'], ['at eight o\'clock'], ok=['pac', 'papc']),
    A(['pac'], ['yesterday morning'], ['the morning before', 'the previous morning'], ok=['pac', 'papc'], shift=True),
    A(['pac'], ['at ten last night'], ['at ten the night before', 'at ten the previous night'], ok=['pac', 'papc'], shift=True),
    A(['pap'], ['before the lesson'], ['before the lesson'], ok=['pap', 'pas']), A(['pap'], ['before breakfast'], ['before breakfast'], ok=['pap', 'pas']),
    A(['pap'], ['by nine o\'clock'], ['by nine o\'clock'], ok=['pap', 'pas']),
    A(['pap'], ['already'], ['already'], pos='mid', ok=['pp', 'pap', 'pas'], pols=('aff',), need='tel'),
    A(['pap'], ['just'], ['just'], pos='mid', ok=['pp', 'pap'], pols=('aff',), need='tel'),
    A(['papc'], ['for an hour'], ['for an hour'], ok=['ppc', 'papc'], need='dur'),
    A(['papc'], ['since morning'], ['since morning'], ok=['ppc', 'papc'], need='dur'),
    A(['papc'], ['all day'], ['all day'], ok=['ppc', 'papc'], need='dur'),
    A(['fs'], ['tomorrow'], ['the next day', 'the following day'], ok=['fs'], shift=True),
    A(['fs'], ['tonight'], ['that night'], ok=['fs'], shift=True),
    A(['fs'], ['next week'], ['the following week', 'the week after', 'the next week'], ok=['fs'], shift=True),
    A(['fs'], ['next month'], ['the following month', 'the month after', 'the next month'], ok=['fs'], shift=True),
    A(['fs'], ['next year'], ['the following year', 'the year after', 'the next year'], ok=['fs'], shift=True),
    A(['fs'], ['next Monday'], ['the following Monday', 'the Monday after', 'the next Monday'], ok=['fs'], shift=True),
    A(['fs'], ['soon'], ['soon'], ok=['fs']), A(['fs'], ['after school'], ['after school'], ok=['fs']),
    A(['fc'], ['tomorrow'], ['the next day', 'the following day'], ok=['fc'], shift=True),
    A(['fc'], ['tonight'], ['that night'], ok=['fc'], shift=True),
    A(['fc'], ['next week'], ['the following week', 'the week after', 'the next week'], ok=['fc'], shift=True),
    A(['fc'], ['at ten tomorrow'], ['at ten the next day', 'at ten the following day'], ok=['fc'], shift=True),
    A(['fc'], ['all day tomorrow'], ['all day the next day', 'all day the following day'], ok=['fc'], shift=True),
    A(['fc'], ['at eight o\'clock'], ['at eight o\'clock'], ok=['fc']), A(['fc'], ['this evening'], ['that evening'], ok=['fc'], shift=True),
    A(['fp'], ['by Friday'], ['by Friday'], ok=['fp'], need='tel'), A(['fp'], ['by the end of the month'], ['by the end of the month'], ok=['fp'], need='tel'),
    A(['fp'], ['by 2030'], ['by 2030'], ok=['fp'], need='tel'),
    A(['fp'], ['by tomorrow'], ['by the next day', 'by the following day'], ok=['fp'], need='tel', shift=True),
    A(['fp'], ['by next week'], ['by the following week', 'by the next week'], ok=['fp'], need='tel', shift=True),
    A(['fp'], ['by next June'], ['by the following June', 'by the next June'], ok=['fp'], need='tel', shift=True),
]

# tense maps -------------------------------------------------------------
RT_FROM = {  # direct tense -> accepted reported tenses (first = standard)
    'ps': ['rps'], 'pc': ['rpc'], 'pp': ['rpp'], 'ppc': ['rppc'],
    'pas': ['rpp', 'rps'], 'pac': ['rppc', 'rpc'], 'pap': ['rpp'], 'papc': ['rppc'],
    'fs': ['rfs'], 'fc': ['rfc'], 'fp': ['rfp'],
}
D_FROM_R = {  # reported tense -> possible direct tenses (first = standard for the shown tense)
    'rps': ['ps', 'pas'], 'rpc': ['pc', 'pac'], 'rpp': ['pp', 'pap', 'pas'], 'rppc': ['ppc', 'papc', 'pac'],
    'rfs': ['fs'], 'rfc': ['fc'], 'rfp': ['fp'],
}
BE_OK = {'ps', 'pas', 'pp', 'pap', 'fs'}
WHEN_OK = {'pas', 'pac', 'fs', 'fc', 'fp'}
TENSE_NAME = {'ps': 'present simple', 'pc': 'present continuous', 'pp': 'present perfect', 'ppc': 'present perfect continuous',
              'pas': 'past simple', 'pac': 'past continuous', 'pap': 'past perfect', 'papc': 'past perfect continuous',
              'fs': 'future simple', 'fc': 'future continuous', 'fp': 'future perfect'}

NEG = {'am': 'am not', 'is': "isn't", 'are': "aren't", 'was': "wasn't", 'were': "weren't", 'have': "haven't", 'has': "hasn't",
       'had': "hadn't", 'will': "won't", 'would': "wouldn't", 'do': "don't", 'does': "doesn't", 'did': "didn't"}


def be_pres(p):
    return {'1s': 'am', '3s': 'is'}.get(p, 'are')


def be_past(p):
    return 'was' if p in ('1s', '3s') else 'were'


def have_pres(p):
    return 'has' if p == '3s' else 'have'


def chain(t, pol, p, pr, q=False):
    """Direct-speech verb chain -> (aux list, main verb or None)."""
    be = pr.get('be')
    V = VERBS.get(pr['v'])
    base = pr['v']
    if t == 'ps':
        if be:
            aux, main = [be_pres(p)], None
        elif pol == 'aff' and not q:
            aux, main = [], (V[0] if p == '3s' else base)
        else:
            aux, main = ['does' if p == '3s' else 'do'], base
    elif t == 'pc':
        aux, main = [be_pres(p)], V[3]
    elif t == 'pp':
        aux, main = [have_pres(p)] + (['been'] if be else []), (None if be else V[2])
    elif t == 'ppc':
        aux, main = [have_pres(p), 'been'], V[3]
    elif t == 'pas':
        if be:
            aux, main = [be_past(p)], None
        elif pol == 'aff' and not q:
            aux, main = [], V[1]
        else:
            aux, main = ['did'], base
    elif t == 'pac':
        aux, main = [be_past(p)], V[3]
    elif t == 'pap':
        aux, main = ['had'] + (['been'] if be else []), (None if be else V[2])
    elif t == 'papc':
        aux, main = ['had', 'been'], V[3]
    elif t == 'fs':
        aux, main = ['will'] + (['be'] if be else []), (None if be else base)
    elif t == 'fc':
        aux, main = ['will', 'be'], V[3]
    elif t == 'fp':
        aux, main = ['will', 'have'] + (['been'] if be else []), (None if be else V[2])
    else:
        raise ValueError(t)
    if pol == 'neg' and aux:
        aux = [NEG[aux[0]]] + aux[1:]
    return aux, main


def rchain(rt, pol, p, pr):
    be = pr.get('be')
    V = VERBS.get(pr['v'])
    base = pr['v']
    if rt == 'rps':
        if be:
            aux, main = [be_past(p)], None
        elif pol == 'aff':
            aux, main = [], V[1]
        else:
            aux, main = ['did'], base
    elif rt == 'rpc':
        aux, main = [be_past(p)], V[3]
    elif rt == 'rpp':
        aux, main = ['had'] + (['been'] if be else []), (None if be else V[2])
    elif rt == 'rppc':
        aux, main = ['had', 'been'], V[3]
    elif rt == 'rfs':
        aux, main = ['would'] + (['be'] if be else []), (None if be else base)
    elif rt == 'rfc':
        aux, main = ['would', 'be'], V[3]
    elif rt == 'rfp':
        aux, main = ['would', 'have'] + (['been'] if be else []), (None if be else V[2])
    else:
        raise ValueError(rt)
    if pol == 'neg' and aux:
        aux = [NEG[aux[0]]] + aux[1:]
    return aux, main


def assemble(subj, aux, main, body, mid, end, q):
    if q:
        w = [aux[0], subj] + ([mid] if mid else []) + aux[1:] + ([main] if main else []) + [body]
    else:
        w = [subj]
        if aux:
            w += [aux[0]] + ([mid] if mid else []) + aux[1:]
        elif mid:
            w += [mid]
        if main:
            w.append(main)
        w.append(body)
    if end:
        w.append(end)
    return ' '.join(x for x in w if x)


# ---------------------------------------------------------------- subjects
def poss_of(subj_key, g=None):
    return {'I': 'my', 'we': 'our', 'you': 'your', 'they': 'their'}.get(subj_key) or (PRON[g][2] if g else 'their')


def shift_obj(obj):
    return re.sub(r'\bhere\b', 'there', re.sub(r'\bthis\b', 'that', obj))


def fill_obj(obj, poss):
    return obj.replace('{P}', poss)


class Spec(dict):
    pass


def d_subject_variants(sp):
    """Direct subject texts (for the key). 'we' can come back from 'they'."""
    k = sp['dsub']
    if k == 'we':
        return [('we', 'we', 'our', '1p'), ('they', 'they', 'their', '3p')]
    if k == 'I':
        return [('I', 'I', 'my', '1s')]
    if k == 'you':
        return [('you', 'you', 'your', '2')]
    return [(sp['third']['n'], sp['third']['n'], poss_of(None, sp['third'].get('g')) if sp['third'].get('g') else 'their', '3p' if sp['third'].get('pl') else '3s')]


def r_subject(sp):
    """(text, possessive, agreement key) of the reported subject."""
    S, Ad, k = sp['S'], sp['A'], sp['dsub']
    if k == 'I':
        t = PRON[S['g']]
        return t[0], t[2], '3s'
    if k == 'we':
        return 'they', 'their', '3p'
    if k == 'you':
        if Ad == 'me':
            return 'I', 'my', '1s'
        t = PRON[Ad['g']]
        return t[0], t[2], '3s'
    th = sp['third']
    if th.get('pl'):
        return th['n'], 'their', '3p'
    return th['n'], PRON[th['g']][2], '3s'


def obj_text(sp, pr, poss, shift):
    if pr.get('be'):
        return pr['adj']
    o = fill_obj(pr['obj'], poss)
    return shift_obj(o) if shift else o


def build_direct(sp, t, subj_v=None, advD=None, pr=None, wh=None, pol=None):
    """Direct-speech sentence for spec sp in tense t."""
    pr = pr or sp['pred']
    pol = pol or sp['pol']
    kind = sp['kind']
    subj_v = subj_v or d_subject_variants(sp)[0]
    stext, _, sposs, p = subj_v[0], subj_v[1], subj_v[2], subj_v[3]
    advs = advD if advD is not None else [(a['pos'], a['D'][0]) for a in sp['advs']]
    mid = next((x for pos, x in advs if pos == 'mid'), None)
    end = next((x for pos, x in advs if pos == 'end'), None)
    wh = wh if wh is not None else sp.get('wh')
    body = obj_text(sp, pr, sposs, False)
    q = kind in ('yn', 'wh')
    if kind == 'wh':
        if wh == 'what':
            body = ''
        elif wh == 'where':
            body = ''
        elif wh == 'when':
            end = None
    aux, main = chain(t, pol, p, pr, q)
    s = assemble(stext, aux, main, body, mid, end, q)
    if kind == 'wh':
        s = wh + ' ' + s
    s = cap(s) if kind != 'wh' else cap(s)
    if stext == 'I':
        pass
    return s + ('?' if q else '')


def build_reported(sp, rt, advR=None, pr=None, pol=None, with_sub=True):
    pr = pr or sp['pred']
    pol = pol or sp['pol']
    stext, sposs, p = r_subject(sp)
    advs = advR if advR is not None else [(a['pos'], a['R'][0]) for a in sp['advs']]
    mid = next((x for pos, x in advs if pos == 'mid'), None)
    end = next((x for pos, x in advs if pos == 'end'), None)
    kind = sp['kind']
    body = obj_text(sp, pr, sposs, True)
    if kind == 'wh':
        wh = sp['wh']
        if wh in ('what', 'where'):
            body = ''
        elif wh == 'when':
            end = None
    aux, main = rchain(rt, pol, p, pr)
    s = assemble(stext, aux, main, body, mid, end, False)
    if kind == 'wh':
        s = sp['wh'] + ' ' + s
    return s


def elide(clause1, clause2_full, stext):
    return clause2_full[len(stext) + 1:] if clause2_full.startswith(stext + ' ') else None


def rep_end_variants(sp):
    """All reported wordings for each adverbial, as lists of (pos, text) combos."""
    combos = [[]]
    for a in sp['advs']:
        combos = [c + [(a['pos'], r)] for c in combos for r in a['R']]
    return combos


def d_end_variants(sp):
    combos = [[]]
    for a in sp['advs']:
        combos = [c + [(a['pos'], d)] for c in combos for d in a['D']]
    return combos


# ---------------------------------------------------------------- reporting clauses
STMT_VERBS = ['said', 'said', 'said', 'shouted', 'yelled', 'whispered', 'explained', 'added', 'replied', 'announced', 'admitted', 'complained', 'mentioned', 'remarked']
STMT_EASY = ['said', 'said', 'said', 'told', 'shouted', 'yelled']
Q_VERBS = ['asked', 'asked', 'asked', 'wanted to know', 'wondered']
CMD_VERBS = ['told', 'told', 'told', 'ordered', 'asked', 'begged', 'warned', 'instructed']


def addr_obj(Ad):
    if Ad is None:
        return ''
    return 'me' if Ad == 'me' else Ad['n']


def speaker_text(S, start=True):
    return cap(S['n']) if start else S['n']


def clause_head(sp, start=True):
    s = speaker_text(sp['S'], start) + ' ' + sp['rv']
    a = addr_obj(sp['A'])
    if a:
        s += ' ' + a
    return s


def render_direct_quote(sp, dtext, order):
    head = clause_head(sp)
    inner = dtext
    if order == 'A':
        if inner[-1] in '.?!':
            q = inner[:-1] if inner[-1] == '.' else inner
        else:
            q = inner
        mark = '' if q[-1] in '?!' else ','
        return '"' + q + mark + '" ' + clause_head(sp, False) + '.'
    else:
        end = inner if inner[-1] in '?!.' else inner + '.'
        if sp['rv'] in ('shouted', 'yelled') and end[-1] == '.':
            end = end[:-1] + '!'
        return head + ', "' + end + '"'


def blank_direct(sp, order):
    head = clause_head(sp)
    if order == 'A':
        return '"___," ' + clause_head(sp, False) + '.'
    return head + ', "___"'


# ---------------------------------------------------------------- spec generation
def adv_ok(a, tense, pol_key, pr, level, allow_shift=True):
    if tense not in a['ts'] or pol_key not in a['pols']:
        return False
    if a['need'] and not pr.get(a['need']):
        return False
    if a['shift'] and not allow_shift:
        return False
    return True


def pred_ok(pr, tense, level, allow_sh):
    if pr.get('be'):
        return tense in BE_OK
    if pr['sh'] and not allow_sh:
        return False
    if tense in ('pc', 'pac', 'ppc', 'papc', 'fc') and not pr['act']:
        return False
    if tense in ('ppc', 'papc') and not pr['dur']:
        return False
    if tense == 'fp' and not pr['tel']:
        return False
    return True


def choose_subject(kind, level, A_present):
    r = RNG.random()
    opts = ['I', 'we', 'third']
    if A_present:
        opts += ['you', 'you']
    if kind in ('yn', 'wh'):
        opts = ['you', 'you', 'you', 'I', 'third'] if A_present else ['I', 'third', 'third']
    return RNG.choice(opts)


def gen_spec(level, tense, kind=None, shift_only=False, allow_compound=True):
    for _ in range(200):
        r = RNG.random()
        if kind is None:
            if level == 'easy':
                k, pol = (('s', 'aff') if r < .5 else ('s', 'neg') if r < .75 else ('yn', 'aff'))
            elif level == 'medium':
                k, pol = (('s', 'aff') if r < .30 else ('s', 'neg') if r < .52 else ('yn', 'aff') if r < .75 else ('wh', 'aff'))
            else:
                k, pol = (('s', 'aff') if r < .22 else ('s', 'neg') if r < .42 else ('yn', 'aff') if r < .62 else ('wh', 'aff'))
        else:
            k, pol = kind
        if k == 'wh' and RNG.random() < .2:
            pol = 'neg'
        kd = {'s': 's', 'yn': 'yn', 'wh': 'wh'}[k]
        # people
        S = person(kin=True)
        need_A = kd != 's' and RNG.random() < .6 or RNG.random() < .3
        A_ = None
        if need_A:
            A_ = 'me' if (level != 'easy' and RNG.random() < .3) else person(exclude=[S['n']], g=('f' if S['g'] == 'm' else 'm'))
        dsub = choose_subject(kd, level, A_ is not None)
        if dsub == 'we' and A_ == 'me':
            continue
        if dsub == 'you' and A_ is None:
            A_ = person(exclude=[S['n']], g=('f' if S['g'] == 'm' else 'm'))
        if kd != 's' and dsub == 'you' and A_ == 'me' and False:
            continue
        third = None
        if dsub == 'third':
            ex = [S['n']] + ([A_['n']] if isinstance(A_, dict) else [])
            if RNG.random() < .2:
                third = {'n': RNG.choice(['my parents', 'the students', 'my friends', 'the boys', 'the girls']), 'pl': True}
            else:
                third = person(exclude=ex)
        allow_sh = level != 'easy'
        pr = RNG.choice(PREDS + BE * 2)
        if not pred_ok(pr, tense, level, allow_sh):
            continue
        # question words
        wh = None
        if kd == 'wh':
            opts = ['why']
            if pr['what']:
                opts += ['what', 'what']
            if pr['where']:
                opts += ['where', 'where']
            if tense in WHEN_OK and not pr.get('be'):
                opts += ['when']
            wh = RNG.choice(opts)
            if pol == 'neg' and wh != 'why':
                pol = 'aff'
            if pol == 'neg' and dsub == 'I' and pr.get('be') and tense in ('ps',):
                continue  # "Why am not I" is not possible
            if pol == 'neg' and dsub == 'I' and tense in ('ps',) and False:
                continue
        # adverbials
        polkey = 'q' if kd in ('yn', 'wh') else pol
        cands = [a for a in ADVS if adv_ok(a, tense, polkey, pr, level, allow_sh)]
        if shift_only:
            cands_s = [a for a in cands if a['shift']]
            if not cands_s and not pr['sh']:
                continue
            cands = cands_s
        advs = []
        if cands:
            roll = RNG.random()
            want = 1 if roll < (.55 if level == 'easy' else .8) else 0
            if shift_only:
                want = 1
            if level == 'hard' and tense in ('pp', 'pap') and RNG.random() < .3:
                want = 2
            pool = [a for a in cands if (level != 'easy' or not a['shift'])]
            if level == 'medium' and not shift_only:
                sh = [a for a in pool if a['shift']]
                if sh and RNG.random() < .55:
                    pool = sh
            if want and pool:
                first = RNG.choice(pool)
                advs.append(first)
                if want == 2:
                    other = [a for a in pool if a['pos'] != first['pos'] and a is not first and (first['need'] == 'tel' or a['need'] == 'tel') and (a['shift'] or first['shift'] or a['need'] == 'dur')]
                    if other:
                        advs.append(RNG.choice(other))
        if kd == 'wh' and wh == 'when':
            advs = [a for a in advs if a['pos'] == 'mid']
        if shift_only and not any(a['shift'] for a in advs) and not pr['sh']:
            continue
        # wh with what/where removes the object: a "this/here" object then adds nothing to shift
        if shift_only and kd == 'wh' and wh in ('what', 'where') and not any(a['shift'] for a in advs):
            continue
        # 'for/since' with 'when' questions, and 'ever' only in yn
        sp = Spec(level=level, tense=tense, S=S, A=A_, dsub=dsub, third=third, pol=pol, kind=kd, wh=wh, pred=pr,
                  advs=advs, comp=None, rv='')
        # verbs
        if kd == 's':
            if sp['A'] is not None:
                sp['rv'] = 'told'
            else:
                sp['rv'] = RNG.choice(STMT_EASY if level == 'easy' else STMT_VERBS)
                if sp['rv'] == 'told':
                    sp['A'] = person(exclude=[S['n']], g=('f' if S['g'] == 'm' else 'm'))
                    if dsub == 'we' or dsub == 'you':
                        pass
        else:
            if sp['A'] is None:
                sp['rv'] = RNG.choice(['asked', 'wanted to know', 'wondered'] if level != 'easy' else ['asked', 'wanted to know'])
                if dsub == 'you':
                    sp['rv'] = 'asked'
            else:
                sp['rv'] = 'asked'
            if sp['A'] is None and sp['rv'] == 'asked' and RNG.random() < .5:
                sp['A'] = person(exclude=[S['n']] + ([third['n']] if third else []), g=('f' if S['g'] == 'm' else 'm'))
        if sp['rv'] in ('told',) and sp['A'] is None:
            continue
        if sp['dsub'] == 'you' and sp['A'] is None:
            continue
        # an addressee appearing in the sentence for a third-person subject must differ from 'third'
        if third and isinstance(sp['A'], dict) and third['n'] == sp['A']['n']:
            continue
        # compound (hard): affirmative + negative, same subject, same tense
        if level == 'hard' and allow_compound and kd == 's' and RNG.random() < .22 and not advs and tense in ('ps', 'pas', 'pc', 'pac', 'fs', 'fc', 'pp', 'pap'):
            pr2 = RNG.choice(PREDS + BE)
            if pr2['v'] != pr['v'] and pred_ok(pr2, tense, level, False) and not pr2['sh'] and not pr['sh'] and bool(pr2.get('be')) == bool(pr.get('be')):
                sp['pol'] = 'aff'
                sp['comp'] = pr2
        return sp
    raise RuntimeError('no spec')


# ---------------------------------------------------------------- items from specs
def that_variants(sp):
    return ['', 'that '] if sp['kind'] == 's' else (['if ', 'whether '] if sp['kind'] == 'yn' else [''])


def direct_valid(sp, t):
    """Is direct tense t a sensible reading of this spec's reported sentence?"""
    pr = sp['pred']
    if pr.get('be') and t not in BE_OK:
        return False
    if t in ('pc', 'pac', 'ppc', 'papc', 'fc') and not pr.get('be') and not pr['act']:
        return False
    if t in ('ppc', 'papc') and not pr['dur']:
        return False
    if sp['comp'] is not None:
        pr2 = sp['comp']
        if pr2.get('be') and t not in BE_OK:
            return False
        if t in ('pc', 'pac') and not pr2.get('be') and not pr2['act']:
            return False
    for a in sp['advs']:
        if t not in a['ok']:
            return False
    if sp['kind'] == 'wh' and sp['wh'] == 'when' and t not in WHEN_OK:
        return False
    return True


def key_for_d2r(sp):
    """All accepted reported renderings for the spec's direct tense."""
    out = []
    pred_pairs = [(sp['pred'], sp['pol'])]
    for rt in RT_FROM[sp['tense']]:
        for combo in rep_end_variants(sp):
            if sp['comp'] is not None:
                c1 = build_reported(sp, rt, advR=combo, pr=sp['pred'], pol='aff')
                c2 = build_reported(sp, rt, advR=combo, pr=sp['comp'], pol='neg')
                stext = r_subject(sp)[0]
                forms = [c1 + ' but ' + c2]
                e = elide(c1, c2, stext)
                if e:
                    forms.append(c1 + ' but ' + e)
                forms += [f.replace(' but ', ', but ') for f in list(forms)]
                for f in forms:
                    for pre in ['', 'that ']:
                        out.append(pre + f)
                        if pre == 'that ':
                            out.append('that ' + c1 + ' but that ' + c2)
                continue
            core = build_reported(sp, rt, advR=combo)
            for pre in that_variants(sp):
                out.append(pre + core)
    seen, res = set(), []
    for x in out:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res


def shown_reported(sp):
    """The canonical reported sentence (after the reporting verb) shown in reported -> direct items."""
    rt = RT_FROM[sp['tense']][0]
    # choose reported wording at random for adverbials
    advR = [(a['pos'], RNG.choice(a['R'])) for a in sp['advs']]
    if sp['comp'] is not None:
        stext = r_subject(sp)[0]
        c1 = build_reported(sp, rt, advR=advR, pr=sp['pred'], pol='aff')
        c2 = build_reported(sp, rt, advR=advR, pr=sp['comp'], pol='neg')
        core = c1 + ' but ' + c2
    else:
        core = build_reported(sp, rt, advR=advR)
    pre = ''
    if sp['kind'] == 's':
        pre = RNG.choice(['', 'that '])
    elif sp['kind'] == 'yn':
        pre = RNG.choice(['if ', 'whether '])
    return pre + core, rt, advR


def key_for_r2d(sp, rt, advR):
    """All accepted direct renderings."""
    texts = set()
    cand = [t for t in D_FROM_R[rt] if direct_valid(sp, t)]
    # tenses must also respect the adverbial wording that was shown
    shown = {pos + '|' + x for pos, x in advR}
    # direct wording alternatives for every shown reported wording
    d_alts = []
    for a, (pos, rtext) in zip(sp['advs'], advR):
        d_alts.append([(pos, d) for d in a['D']])
    combos = [[]]
    for alts in d_alts:
        combos = [c + [x] for c in combos for x in alts]
    for t in cand:
        for sv in d_subject_variants(sp):
            for combo in combos:
                if sp['comp'] is not None:
                    c1 = build_direct(sp, t, subj_v=sv, advD=combo, pr=sp['pred'], pol='aff')
                    c2 = build_direct(sp, t, subj_v=sv, advD=combo, pr=sp['comp'], pol='neg')
                    c1 = c1.rstrip('.?')
                    c2 = c2.rstrip('.?')
                    texts.add(c1 + ' but ' + c2)
                    texts.add(c1 + ' but ' + c2[len(sv[0]) + 1:])
                    texts.add(c1 + ', but ' + c2)
                    texts.add(c1 + ', but ' + c2[len(sv[0]) + 1:])
                else:
                    texts.add(build_direct(sp, t, subj_v=sv, advD=combo))
    return sorted(texts)


def item_d2r(sp):
    order = RNG.choice('AB')
    if sp['comp'] is not None:
        c1 = build_direct(sp, sp['tense'], pr=sp['pred'], pol='aff').rstrip('.')
        c2 = build_direct(sp, sp['tense'], pr=sp['comp'], pol='neg').rstrip('.')
        sv = d_subject_variants(sp)[0]
        dtext = c1 + ', but ' + c2
    else:
        dtext = build_direct(sp, sp['tense'])
    ans = key_for_d2r(sp)
    head = clause_head(sp)
    q = 'Direct → reported: ' + render_direct_quote(sp, dtext, order) + ' ' + head + ' ___.'
    return {'q': q, 'a': [ans]}


def item_r2d(sp):
    core, rt, advR = shown_reported(sp)
    order = RNG.choice('AB')
    head = clause_head(sp)
    q = 'Reported → direct: ' + head + ' ' + core + '. ' + blank_direct(sp, order)
    ans = key_for_r2d(sp, rt, advR)
    return {'q': q, 'a': [ans]}


# ---------------------------------------------------------------- mistakes (hard): wrong word order etc.
def item_fix(sp):
    """Correct the mistake: a reported question with direct word order."""
    if sp['kind'] not in ('yn', 'wh') or sp['comp'] is not None:
        return None
    rt = RT_FROM[sp['tense']][0]
    stext, sposs, p = r_subject(sp)
    advR = [(a['pos'], a['R'][0]) for a in sp['advs']]
    good = build_reported(sp, rt, advR=advR)
    mid = next((x for pos, x in advR if pos == 'mid'), None)
    end = next((x for pos, x in advR if pos == 'end'), None)
    if sp['wh'] in ('what', 'where') and sp['kind'] == 'wh':
        body = ''
    else:
        body = obj_text(sp, sp['pred'], sposs, True)
    if sp['kind'] == 'wh' and sp['wh'] == 'when':
        end = None
    aux, main = rchain(rt, sp['pol'], p, sp['pred'])
    if not aux:
        aux2, main2 = rchain('rps', 'neg', p, sp['pred']) if False else (['did'], sp['pred']['v'])
        if sp['pred'].get('be'):
            return None
        bad_body = assemble(stext, ['did'], sp['pred']['v'], body, mid, end, True)
        # only a plain past simple with inverted do-support
        if rt != 'rps' or sp['pol'] != 'aff':
            return None
    else:
        if aux[0] in ("didn't", "wouldn't", "wasn't", "weren't", "hadn't") and not sp['pol'] == 'aff':
            bad_aux0 = aux[0]
        bad_body = assemble(stext, aux, main, body, mid, end, True)
    if sp['pol'] == 'neg':
        return None  # the inverted form of a negative reported question is ambiguous to mark
    if sp['kind'] == 'wh':
        bad = sp['wh'] + ' ' + bad_body
    else:
        bad = bad_body  # no if/whether at all
    head = clause_head(sp)
    wrong = head + ' ' + bad + '.'
    answers = []
    for pre in that_variants(sp):
        for combo in rep_end_variants(sp):
            answers.append(pre + build_reported(sp, rt, advR=combo))
    return {'q': 'Correct the mistake: ' + wrong, 'a': [[head + ' ' + x + '.' for x in dict.fromkeys(answers)]]}


# ---------------------------------------------------------------- commands and requests
def C(base, aff=True, neg=True, warn=False, beg=False, obj_m=False, **kw):
    d = {'base': base, 'aff': aff, 'neg': neg, 'warn': warn, 'beg': beg, 'sh': False}
    d.update(kw)
    return d


CMDS = [
    C('close the door'), C('open the window'), C('switch off the light'), C('turn off {P} phone', warn=False),
    C('tidy {P} room'), C('clean the board'), C('do {P} homework'), C('bring {P} books'), C('write {P} name'),
    C('sit down'), C('stand up'), C('be quiet', neg=False), C('be careful', neg=False, warn=True), C('be on time', neg=False),
    C('be late', aff=False, warn=True), C('listen carefully', neg=False), C('read the text'), C('wash {P} hands'),
    C('help {M} with {MP} bags', beg=True), C('wait for {M}', beg=True), C('pass {M} the salt', beg=True),
    C('call {M}', beg=True), C('forgive {M}', beg=True, neg=False),
    C('touch the wire', aff=False, warn=True), C('run in the corridor', aff=False, warn=True), C('open the box', warn=False),
    C('stay away from the fire', neg=False, warn=True), C('watch out', neg=False, warn=True),
    C('speak English', neg=True), C('turn off the TV'), C('finish {P} work'), C('take {P} seat', neg=False),
    C('use {P} dictionaries'), C('copy the answers', aff=False, warn=True), C('talk during the test', aff=False, warn=True),
    C('answer the question'), C('open {P} books'), C('feed the cat'), C('lock the door'),
]
CMD_ADV = [  # (D, [R alts]); the shifted time words
    ('tomorrow', ['the next day', 'the following day']), ('today', ['that day']), ('tonight', ['that night']),
    ('next week', ['the following week', 'the week after', 'the next week']), ('this evening', ['that evening']),
    ('now', ['then', 'at that moment']),
]
VERB_CAP = {
    'told': 'told', 'ordered': 'ordered', 'asked': 'asked', 'begged': 'begged', 'warned': 'warned', 'instructed': 'instructed',
}


def cmd_fill(base, D=True, sp=None):
    A_, S = sp['A'], sp['S']
    if D:
        return base.replace('{P}', 'your').replace('{M}', 'me').replace('{MP}', 'my')
    P_ = 'my' if A_ == 'me' else PRON[A_['g']][2]
    M_ = PRON[S['g']][1]
    MP_ = PRON[S['g']][2]
    return base.replace('{P}', P_).replace('{M}', M_).replace('{MP}', MP_)


def gen_cmd(level, shift_only=False):
    for _ in range(200):
        S = person(kin=True)
        A_ = 'me' if RNG.random() < .35 else person(exclude=[S['n']], g=('f' if S['g'] == 'm' else 'm'))
        rv = RNG.choice(CMD_VERBS if level != 'easy' else ['told', 'told', 'asked', 'ordered'])
        c = RNG.choice(CMDS)
        pol = 'neg' if (level != 'easy' or RNG.random() < .25) and RNG.random() < .45 else 'aff'
        if pol == 'neg' and not c['neg']:
            pol = 'aff'
        if pol == 'aff' and not c['aff']:
            pol = 'neg'
        if pol == 'neg' and not c['neg']:
            continue
        if rv == 'warned' and not c['warn']:
            continue
        if rv == 'begged' and not c['beg'] and RNG.random() < .7:
            continue
        adv = None
        if shift_only or (level != 'easy' and RNG.random() < (.45 if level == 'medium' else .5)):
            adv = RNG.choice(CMD_ADV)
        if shift_only and not adv:
            continue
        if adv and adv[0] == 'now' and c['base'].startswith(('be ', 'sit', 'stand')) is False and rv in ('begged',) and False:
            continue
        # polite request shape for asked / begged
        form = 'imp'
        if rv in ('asked', 'begged'):
            form = RNG.choice(['please', 'please2', 'could', 'can', 'would'] if rv == 'asked' else ['please', 'please2', 'pleasecomma'])
            if pol == 'neg' and form in ('could', 'can', 'would'):
                form = 'please'
        sp = Spec(level=level, S=S, A=A_, rv=rv, cmd=c, pol=pol, adv=adv, form=form)
        return sp
    raise RuntimeError('no cmd')


def cmd_direct(sp):
    c = sp['cmd']
    base = cmd_fill(c['base'], True, sp)
    tail = (' ' + sp['adv'][0]) if sp['adv'] else ''
    f = sp['form']
    if sp['pol'] == 'neg':
        imp = "don't " + base + tail
        if f in ('please', 'pleasecomma'):
            return 'Please ' + imp + '.' if f == 'please' else cap(imp) + ', please.'
        if f == 'please2':
            return cap(imp) + ', please.'
        return cap(imp) + ('!' if sp['rv'] in ('warned', 'ordered') else '.')
    if f == 'imp':
        return cap(base + tail) + ('!' if sp['rv'] in ('warned', 'ordered') else '.')
    if f == 'please':
        return 'Please ' + base + tail + '.'
    if f in ('please2', 'pleasecomma'):
        return cap(base + tail) + ', please.'
    return {'could': 'Could', 'can': 'Can', 'would': 'Would'}[f] + ' you ' + base + tail + '?'


def cmd_direct_variants(sp):
    """Accepted direct wording for a reported command."""
    c = sp['cmd']
    base = cmd_fill(c['base'], True, sp)
    tails = [(' ' + x) for x in [sp['adv'][0]]] if sp['adv'] else ['']
    out = []
    for tl in tails:
        b = base + tl
        if sp['pol'] == 'neg':
            imps = ["don't " + b, 'do not ' + b]
            out += imps + ['please ' + x for x in imps] + [x + ', please' for x in imps]
            if sp['rv'] in ('told', 'ordered', 'warned', 'instructed'):
                out += ['you must not ' + b, "you mustn't " + b, "you can't " + b, 'you should not ' + b]
                if sp['rv'] == 'warned':
                    out += ['you should not ' + b]
        else:
            out += [b, 'please ' + b, b + ', please']
            if sp['rv'] in ('asked', 'begged'):
                out += [w + ' you ' + b for w in ('could', 'can', 'would', 'will')]
                out += ['please ' + w + ' you ' + b for w in ('could', 'can', 'would')]
            if sp['rv'] in ('told', 'ordered', 'warned', 'instructed'):
                out += ['you must ' + b, 'you have to ' + b, 'you need to ' + b]
        if sp['rv'] in ('asked', 'begged') and sp['pol'] == 'neg':
            out += ['please ' + x for x in ["don't " + b]]
    return list(dict.fromkeys(out))


def cmd_reported_variants(sp):
    c = sp['cmd']
    base = cmd_fill(c['base'], False, sp)
    advs = [sp['adv'][1]] if False else (sp['adv'][1] if sp['adv'] else [None])
    outs = []
    for a in advs:
        tail = (' ' + a) if a else ''
        neg = 'not ' if sp['pol'] == 'neg' else ''
        outs.append('to ' + neg + base + tail)
        if sp['pol'] == 'neg':
            outs.append('not to ' + base + tail)
    return list(dict.fromkeys(outs))


def cmd_reported_shown(sp):
    c = sp['cmd']
    base = cmd_fill(c['base'], False, sp)
    a = RNG.choice(sp['adv'][1]) if sp['adv'] else None
    neg = 'not ' if sp['pol'] == 'neg' else ''
    return ('not to ' if neg else 'to ') + base + ((' ' + a) if a else ''), a


def item_cmd_d2r(sp):
    order = RNG.choice('AB')
    head = clause_head(sp)
    d = cmd_direct(sp)
    q = 'Direct → reported: ' + render_direct_quote(sp, d, order) + ' ' + head + ' ___.'
    return {'q': q, 'a': [cmd_reported_variants(sp)]}


def item_cmd_r2d(sp):
    order = RNG.choice('AB')
    head = clause_head(sp)
    shown, a = cmd_reported_shown(sp)
    ans_sp = sp
    # the shown time word decides which direct word is expected
    if sp['adv']:
        idx = sp['adv'][1].index(a)
        ans_sp = dict(sp)
    q = 'Reported → direct: ' + head + ' ' + shown + '. ' + blank_direct(sp, order)
    return {'q': q, 'a': [cmd_direct_variants(sp)]}


def item_cmd_fix(sp):
    head = clause_head(sp)
    c = sp['cmd']
    base = cmd_fill(c['base'], False, sp)
    if sp['adv'] or sp['pol'] == 'neg':
        return None
    wrong = head + ' ' + base + '.'
    return {'q': 'Correct the mistake: ' + wrong, 'a': [[head + ' ' + x + '.' for x in cmd_reported_variants(sp)]]}


# ---------------------------------------------------------------- assembling the topics
def uniq(items, n):
    seen, out = set(), []
    for it in items:
        if it is None or it['q'] in seen:
            continue
        seen.add(it['q'])
        out.append(it)
    return out[:n]


def pool_for(level, tenses, mode, cmds=0.0, kinds=None, shift_only=False, fixes=True, n=PER_LEVEL):
    items = []
    tries = 0
    while len(items) < n * 2 and tries < n * 40:
        tries += 1
        r = RNG.random()
        d = mode if mode in ('d2r', 'r2d') else RNG.choice(['d2r', 'r2d'])
        if cmds and r < cmds:
            try:
                sp = gen_cmd(level, shift_only)
            except RuntimeError:
                continue
            if level == 'hard' and RNG.random() < .12:
                it = item_cmd_fix(sp)
                if it:
                    items.append(it)
                    continue
            items.append(item_cmd_d2r(sp) if d == 'd2r' else item_cmd_r2d(sp))
            continue
        t = RNG.choice(tenses)
        try:
            sp = gen_spec(level, t, kind=kinds, shift_only=shift_only)
        except RuntimeError:
            continue
        if level == 'hard' and fixes and RNG.random() < .12:
            it = item_fix(sp)
            if it:
                items.append(it)
                continue
        items.append(item_d2r(sp) if d == 'd2r' else item_r2d(sp))
    items = uniq(items, n)
    RNG.shuffle(items)
    return items


ALLT = ['ps', 'pc', 'pp', 'ppc', 'pas', 'pac', 'pap', 'papc', 'fs', 'fc', 'fp']

TOPICS = [
    # id, name, section, kwargs
    ('drs-present-simple', 'Present simple', 'Present', dict(tenses=['ps'], mode='both')),
    ('drs-present-continuous', 'Present continuous', 'Present', dict(tenses=['pc'], mode='both')),
    ('drs-present-perfect', 'Present perfect', 'Present', dict(tenses=['pp'], mode='both')),
    ('drs-present-perfect-continuous', 'Present perfect continuous', 'Present', dict(tenses=['ppc'], mode='both')),
    ('drs-past-simple', 'Past simple', 'Past', dict(tenses=['pas'], mode='both')),
    ('drs-past-continuous', 'Past continuous', 'Past', dict(tenses=['pac'], mode='both')),
    ('drs-past-perfect', 'Past perfect', 'Past', dict(tenses=['pap'], mode='both')),
    ('drs-past-perfect-continuous', 'Past perfect continuous', 'Past', dict(tenses=['papc'], mode='both')),
    ('drs-future-simple', 'Future simple (will)', 'Future', dict(tenses=['fs'], mode='both')),
    ('drs-future-continuous', 'Future continuous', 'Future', dict(tenses=['fc'], mode='both')),
    ('drs-future-perfect', 'Future perfect', 'Future', dict(tenses=['fp'], mode='both')),
    ('drs-questions', 'Reported questions (if, whether, wh-)', 'Questions, commands, time words', dict(tenses=ALLT, mode='both', kinds='Q')),
    ('drs-commands', 'Commands and requests', 'Questions, commands, time words', dict(tenses=ALLT, mode='both', cmds=1.0)),
    ('drs-time-place', 'Time and place words', 'Questions, commands, time words', dict(tenses=ALLT, mode='both', shift_only=True, cmds=.25)),
    ('drs-direct-to-reported', 'Direct to reported (all tenses)', 'Mixed', dict(tenses=ALLT, mode='d2r', cmds=.2)),
    ('drs-reported-to-direct', 'Reported to direct (all tenses)', 'Mixed', dict(tenses=ALLT, mode='r2d', cmds=.2)),
    ('drs-mixed', 'Everything mixed', 'Mixed', dict(tenses=ALLT, mode='both', cmds=.2)),
]
GROUP_ID = 'direct-reported-speech'
GROUP_NAME = 'Direct and reported speech (all tenses)'


def build_topic(tid, name, kw):
    levels = {}
    for lv in ('easy', 'medium', 'hard'):
        kinds = None
        if kw.get('kinds') == 'Q':
            # questions only: alternate yes/no and wh
            items = []
            tries = 0
            while len(items) < PER_LEVEL * 2 and tries < PER_LEVEL * 40:
                tries += 1
                k = ('yn', 'aff') if (lv == 'easy' or RNG.random() < .45) else ('wh', 'aff')
                if lv != 'easy' and k[0] == 'wh' and RNG.random() < .2:
                    k = ('wh', 'neg')
                t = RNG.choice(kw['tenses'])
                try:
                    sp = gen_spec(lv, t, kind=k)
                except RuntimeError:
                    continue
                if lv == 'hard' and RNG.random() < .15:
                    it = item_fix(sp)
                    if it:
                        items.append(it)
                        continue
                items.append(item_d2r(sp) if RNG.random() < .5 else item_r2d(sp))
            items = uniq(items, PER_LEVEL)
            RNG.shuffle(items)
            levels[lv] = items
        else:
            levels[lv] = pool_for(lv, kw['tenses'], kw['mode'], cmds=kw.get('cmds', 0.0), shift_only=kw.get('shift_only', False))
    return {'id': tid, 'name': 'Direct and reported speech: ' + name.lower() if False else name, 'levels': levels}


def main():
    topics_meta = []
    for tid, name, sec, kw in TOPICS:
        t = build_topic(tid, name, kw)
        full = 'Speech: ' + name[0].lower() + name[1:] if sec in ('Present', 'Past', 'Future') else name
        t['name'] = full
        counts = {k: len(v) for k, v in t['levels'].items()}
        print(tid, counts)
        with open(os.path.join(OUT, tid + '.json'), 'w', encoding='utf-8') as f:
            json.dump(t, f, ensure_ascii=False, separators=(',', ':'))
        topics_meta.append({'id': tid, 'name': full, 'parent': GROUP_ID, 'sec': sec})
    ix_path = os.path.join(OUT, 'index.json')
    ix = json.load(open(ix_path, encoding='utf-8'))
    ix['topics'] = [t for t in ix['topics'] if t['id'] != GROUP_ID and not t['id'].startswith('drs-')]
    ix['topics'].append({'id': GROUP_ID, 'name': GROUP_NAME, 'group': True})
    ix['topics'] += topics_meta
    with open(ix_path, 'w', encoding='utf-8') as f:
        json.dump(ix, f, ensure_ascii=False, separators=(',', ':'))
    print('index topics:', len(ix['topics']))


if __name__ == '__main__':
    main()
