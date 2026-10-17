import random, re
from verbs import VERBS, FORMS, Verb

class Subj:
    def __init__(s, text, kind, pron, proper=False, objp=None):
        s.text, s.kind, s.pron, s.proper = text, kind, pron, proper
        s.objp = objp or {'i':'me','you':'you','he':'him','she':'her','we':'us','they':'them'}[pron]
    @property
    def mid(s):
        if s.proper or s.text == 'I': return s.text
        return s.text[0].lower() + s.text[1:]
    @property
    def sg(s): return s.kind == 'sg'

SUBJ = [Subj('I','i','i'), Subj('You','you','you'), Subj('He','sg','he'), Subj('She','sg','she'),
        Subj('We','pl','we'), Subj('They','pl','they'),
        Subj('Aziz','sg','he',True), Subj('Dilnoza','sg','she',True), Subj('Tom','sg','he',True), Subj('Anna','sg','she',True),
        Subj('Jasur','sg','he',True), Subj('Malika','sg','she',True),
        Subj('My brother','sg','he'), Subj('My sister','sg','she'), Subj('My mum','sg','she'), Subj('My dad','sg','he'),
        Subj('Our teacher','sg','she'), Subj('The students','pl','they'), Subj('My parents','pl','they'),
        Subj('My friends','pl','they'), Subj('The children','pl','they'), Subj('Mr Karimov','sg','he',True)]
SUBJ_PRON = [s for s in SUBJ if s.text in ('I','You','He','She','We','They')]

def cap(s): return s[0].upper() + s[1:] if s else s
def be_pres(S): return 'am' if S.kind == 'i' else ('is' if S.kind == 'sg' else 'are')
def be_past(S): return 'was' if S.kind in ('i','sg') else 'were'
def have_pres(S): return 'has' if S.kind == 'sg' else 'have'
def do_pres(S): return 'does' if S.kind == 'sg' else 'do'

# ---- tenses: group(S,V,neg) -> list of accepted strings; q(S,V) -> (aux, rest)
def _alts(full):  # add contracted accepted forms is handled by the checker; return as list
    return full if isinstance(full, list) else [full]
class T:
    pass
def g_ps(S,V,neg=False):
    if neg: return [f"{do_pres(S)}n't {V.base}" if do_pres(S)=='does' else f"don't {V.base}", f"{do_pres(S)} not {V.base}"]
    return [V.s if S.kind == 'sg' else V.base]
def q_ps(S,V): return (cap(do_pres(S)), V.base)
def g_pc(S,V,neg=False):
    b = be_pres(S)
    if neg: return ([f"'m not {V.ing}", f"am not {V.ing}"] if b=='am' else [f"{b}n't {V.ing}", f"{b} not {V.ing}"])
    return [f"{b} {V.ing}"]
def q_pc(S,V): return (cap(be_pres(S)), V.ing)
def g_pas(S,V,neg=False):
    return [f"didn't {V.base}", f"did not {V.base}"] if neg else [V.past]
def q_pas(S,V): return ('Did', V.base)
def g_pac(S,V,neg=False):
    b = be_past(S)
    return [f"{b}n't {V.ing}", f"{b} not {V.ing}"] if neg else [f"{b} {V.ing}"]
def q_pac(S,V): return (cap(be_past(S)), V.ing)
def g_pp(S,V,neg=False):
    h = have_pres(S)
    return [f"{h}n't {V.pp}", f"{h} not {V.pp}"] if neg else [f"{h} {V.pp}"]
def q_pp(S,V): return (cap(have_pres(S)), V.pp)
def g_ppc(S,V,neg=False):
    h = have_pres(S)
    return [f"{h}n't been {V.ing}", f"{h} not been {V.ing}"] if neg else [f"{h} been {V.ing}"]
def q_ppc(S,V): return (cap(have_pres(S)), f"been {V.ing}")
def g_pap(S,V,neg=False):
    return [f"hadn't {V.pp}", f"had not {V.pp}"] if neg else [f"had {V.pp}"]
def q_pap(S,V): return ('Had', V.pp)
def g_fw(S,V,neg=False):
    return [f"won't {V.base}", f"will not {V.base}"] if neg else [f"will {V.base}", f"'ll {V.base}"]
def q_fw(S,V): return ('Will', V.base)
def g_fg(S,V,neg=False):
    b = be_pres(S)
    if neg: return ([f"'m not going to {V.base}", f"am not going to {V.base}"] if b=='am' else [f"{b}n't going to {V.base}", f"{b} not going to {V.base}"])
    return [f"{b} going to {V.base}"] + ([f"'m going to {V.base}"] if b=='am' else ([f"'re going to {V.base}"] if b=='are' else []))
def q_fg(S,V): return (cap(be_pres(S)), f"going to {V.base}")

TENSES = {
 'ps': (g_ps,q_ps,'do'), 'pc': (g_pc,q_pc,'be'), 'pas': (g_pas,q_pas,'did'), 'pac': (g_pac,q_pac,'bepast'),
 'pp': (g_pp,q_pp,'have'), 'ppc': (g_ppc,q_ppc,'have'), 'pap': (g_pap,q_pap,'had'), 'fw': (g_fw,q_fw,'will'),
 'fg': (g_fg,q_fg,'be'), 'fpc': (g_pc,q_pc,'be'),
}
def grp(t,S,V,neg=False): return TENSES[t][0](S,V,neg)
def qp(t,S,V): return TENSES[t][1](S,V)
def display(t,S,V,neg=False): return grp(t,S,V,neg)[0] if not (neg and grp(t,S,V,neg)[0].startswith("'m")) else grp(t,S,V,neg)[1]
def full_group(t,S,V,neg=False):
    # a presentable full-form string (for building whole sentences); never starts with an apostrophe
    for g in grp(t,S,V,neg):
        if not g.startswith("'"): return g
def short_aux(t,S,neg=False):
    k = TENSES[t][2]
    if k == 'do': a = do_pres(S)
    elif k == 'be': a = be_pres(S)
    elif k == 'did': a = 'did'
    elif k == 'bepast': a = be_past(S)
    elif k == 'have': a = have_pres(S)
    elif k == 'had': a = 'had'
    else: a = 'will'
    if not neg: return a
    return {'am':'am not','will':"won't"}.get(a, a + "n't")
def pron_ans(S):  # subject pronoun used in short answers to a question about S
    return {'you':'I','i':'you'}.get(S.pron, S.pron if S.pron not in ('you',) else 'I')

def sentence(S, group, comp='', cue_end='', pre=''):
    parts = [S.text]
    if pre: parts.append(pre)
    parts.append(group)
    if comp: parts.append(comp)
    if cue_end: parts.append(cue_end)
    return ' '.join(parts) + '.'

def line(q, *groups):
    gs = []
    for g in groups:
        g = [x for x in (g if isinstance(g, list) else [g])]
        seen = []
        for x in g:
            if x not in seen: seen.append(x)
        assert seen and all('|' not in x and ';;' not in x and '=>' not in x for x in seen), (q, g)
        gs.append('|'.join(seen))
    assert ' => ' not in q and '|' not in q, q
    return q + ' => ' + ' ;; '.join(gs)

def blank_count(q): return q.count('___')

class Rng:
    def __init__(s, seed): s.r = random.Random(seed)
    def pick(s, seq): return s.r.choice(seq)
    def shuffle(s, seq): s.r.shuffle(seq); return seq

def vcomp(rng, V=None):
    V = V or rng.pick(VERBS)
    return V, rng.pick(V.comps)
