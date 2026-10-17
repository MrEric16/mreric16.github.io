from lib import *
from tense import PS_END, PAS_E, PAS_D, negs
from passive import gen_topic

SPEAKERS = [('Tom','he'),('Anna','she'),('Aziz','he'),('Dilnoza','she'),('My brother','he'),('My sister','she'),('Our teacher','she'),('Jasur','he'),('Malika','she'),('My dad','he'),('My mum','she'),('The manager','he')]
def spk_subj(pr, pl=False):
    return Subj('they','pl','they',True) if pl else Subj(pr, 'sg', pr, True)
CUEMAP = {
 'now':['then','at that moment'], 'at the moment':['at that moment','then'], 'right now':['then','at that moment'],
 'today':['that day'], 'tonight':['that night'], 'tomorrow':['the next day','the following day','the day after'],
 'yesterday':['the day before','the previous day'], 'last week':['the week before','the previous week'], 'last night':['the night before','the previous night'],
 'last month':['the month before','the previous month'], 'next week':['the following week','the week after','the next week'],
 'next month':['the following month','the month after','the next month'], 'two days ago':['two days before'], 'three days ago':['three days before'],
 'last year':['the year before','the previous year'], 'next year':['the following year','the year after','the next year'],
 'this week':['that week'], 'this month':['that month'], 'last Monday':['the Monday before','the previous Monday'], 'on Friday':['on Friday'],
}
TCUES = {
 'ps': PS_END[:8], 'pc': ['now','at the moment','right now'], 'pas': ['yesterday','last week','last night','two days ago','last month','last year','three days ago'],
 'pp': ['already','twice','many times','three times'], 'fw': ['tomorrow','next week','next month','next year','tonight'], 'fg': ['tomorrow','next week','next month','next year','tonight'],
 'can': [''], 'must': ['today','tomorrow'],
}
def cue_rep(c):
    return CUEMAP.get(c, [c]) if c else ['']

def direct_group(tn, S, V, neg=False):
    if tn in ('ps','pc','pas','pp'): return full_group(tn,S,V,neg)
    if tn == 'fw': return f"won't {V.base}" if neg else f"will {V.base}"
    if tn == 'fg': return full_group('fg',S,V,neg)
    if tn == 'can': return f"can't {V.base}" if neg else f"can {V.base}"
    if tn == 'must': return f"must {V.base}"
def rep_group(tn, Sr, V, neg=False):
    if tn == 'ps': return ([f"didn't {V.base}", f"did not {V.base}"] if neg else [V.past])
    if tn == 'pc': return grp('pac',Sr,V,neg)
    if tn == 'pas': return grp('pap',Sr,V,neg) + grp('pas',Sr,V,neg)
    if tn == 'pp': return grp('pap',Sr,V,neg)
    if tn == 'fw': return ([f"wouldn't {V.base}", f"would not {V.base}"] if neg else [f"would {V.base}", f"'d {V.base}"])
    if tn == 'fg':
        b = be_past(Sr); return ([f"{b}n't going to {V.base}", f"{b} not going to {V.base}"] if neg else [f"{b} going to {V.base}"])
    if tn == 'can': return ([f"couldn't {V.base}", f"could not {V.base}"] if neg else [f"could {V.base}"])
    if tn == 'must': return [f"had to {V.base}", f"must {V.base}"]
def rep_full(tn, Sr, V, neg=False):
    for g in rep_group(tn,Sr,V,neg):
        if not g.startswith("'"): return g

def make_dir(rng, tn=None, allow_neg=True):
    tn = tn or rng.pick(['ps','ps','pc','pas','pp','fw','fg','can','must'])
    V = rng.pick(VERBS)
    if tn == 'pp' and False: pass
    comp = rng.pick(V.comps)
    r = rng.r.random()
    sp_name, sp_pr = rng.pick(SPEAKERS)
    # direct subject
    k = rng.pick(['I','I','I','We','third'])
    if k == 'I': Sd = SUBJ[0]; Sr = spk_subj(sp_pr)
    elif k == 'We': Sd = SUBJ[4]; Sr = spk_subj('they', True)
    else:
        Sd = rng.pick([x for x in SUBJ if x.kind in ('sg','pl') and x.text not in ('He','She','We','They',sp_name)]); Sr = Sd
    neg = allow_neg and tn != 'must' and rng.pick([False,False,True])
    if tn == 'must' and k != 'third': pass
    cues = TCUES[tn]
    cue = rng.pick(cues) if cues else ''
    if tn == 'pp' and neg: cue = ''  # keep simple
    if V.dur and tn == 'pas': cue = rng.pick(PAS_D)
    if tn == 'pp' and cue in ('three times','twice','many times') and neg: cue = ''
    if tn == 'ps' and V.ach and False: pass
    return dict(tn=tn,V=V,comp=comp,Sd=Sd,Sr=Sr,k=k,neg=neg,cue=cue,sp=sp_name,sp_pr=sp_pr)

def dsent(d):
    g = direct_group(d['tn'], d['Sd'], d['V'], d['neg'])
    return cap(' '.join(x for x in [d['Sd'].text, g, d['comp'], d['cue']] if x)) + '.'
def dsent_third(d):
    return dsent(d)
def rep_subject_text(d):
    if d['k'] == 'third': return d['Sd'].mid
    return d['sp_pr'] if d['k'] == 'I' else 'they'
def rest_cue(d, alt=None):
    cl = cue_rep(d['cue'])
    return cl if alt is None else [cl[alt]]

def intro(d, rng, verb=None):
    verb = verb or rng.pick(['said','told me'])
    return verb

def say_pre(d, verb):
    return f"{d['sp']} {verb}"

def gen_statement(level, rng, tn=None):
    d = make_dir(rng, tn)
    V = d['V']; verb = rng.pick(['said','said','told me'])
    ds = dsent(d)
    quote = f'{d["sp"]} {"said" if verb=="said" else "told me"}, "{ds[:-1]}."'
    rs = rep_subject_text(d)
    group_ans = rep_group(d['tn'], d['Sr'], V, d['neg'])
    cues_a = cue_rep(d['cue'])
    pre = f"{d['sp']} {verb} {rs}" if rs != 'they' else f"{d['sp']} {verb} they"
    if rs.lower() in ('he','she','they') or d['k'] != 'third': pre = f"{d['sp']} {verb} {rs}"
    hint = f"(not / {V.base})" if d['neg'] else f"({V.base})"
    cuet = cues_a[0] if len(cues_a) == 1 else None
    if level == 'easy':
        if len(cues_a) > 1: cue_txt = cues_a[0]
        else: cue_txt = cues_a[0]
        q = f"{quote} {pre} ___ {hint} {d['comp']}{(' ' + cue_txt) if cue_txt else ''}."
        return line(q, group_ans)
    if level == 'medium':
        k = rng.pick(['cue','both','cue','verb'])
        if d['cue'] in CUEMAP and k != 'verb':
            if k == 'cue':
                gfull = rep_full(d['tn'], d['Sr'], V, d['neg'])
                q = f"{quote} {pre} {gfull} {d['comp']} ___."
                return line(q, cues_a)
            q = f"{quote} {pre} ___ {hint} {d['comp']} ___."
            return line(q, group_ans, cues_a)
        q = f"{quote} {pre} ___ {hint} {d['comp']}{(' ' + cues_a[0]) if cues_a[0] else ''}."
        return line(q, group_ans)
    # hard
    k = rng.pick(['report','report','fix','fix','fixcue'])
    base_ok = []
    gs = rep_group(d['tn'], d['Sr'], V, d['neg'])
    pre_alts = [f"{d['sp']} {verb} {rs}", f"{d['sp']} {verb} that {rs}"] if verb == 'said' else [f"{d['sp']} {verb} {rs}", f"{d['sp']} {verb} that {rs}"]
    full_ans = []
    for pa in pre_alts:
        for g in gs:
            if g.startswith("'"): continue
            for c in cues_a:
                full_ans.append(cap(' '.join(x for x in [pa, g, d['comp'], c] if x)) + '.')
    if k == 'report':
        return line(f"Report it: {quote}", full_ans[:24])
    if k == 'fix':
        # no backshift (keep direct tense) -> wrong
        wrong_g = direct_group(d['tn'], d['Sr'] if d['k']!='I' or True else d['Sd'], V, d['neg'])
        if d['tn'] in ('ps','pc','pas','pp','fg'):
            # compute wrong by using the present forms with the reported subject
            wt = {'ps':'ps','pc':'pc','pas':'pas','pp':'pp','fg':'fg'}[d['tn']]
            wg = full_group(wt, d['Sr'], V, d['neg'])
        elif d['tn'] == 'fw': wg = f"will {V.base}" if not d['neg'] else f"won't {V.base}"
        elif d['tn'] == 'can': wg = f"can {V.base}" if not d['neg'] else f"can't {V.base}"
        else: wg = f"must {V.base}"
        if d['tn'] == 'pas': wg = V.past if not d['neg'] else f"didn't {V.base}"
        bad = cap(' '.join(x for x in [f"{d['sp']} {verb} {rs}", wg, d['comp'], cues_a[0]] if x)) + '.'
        if bad in full_ans or d['tn'] in ('must','pas'): return None
        return line(f"Correct the mistake: {bad}", full_ans[:24])
    # fixcue: wrong time word
    if d['cue'] in CUEMAP and d['cue'] not in ('on Friday',):
        g = rep_full(d['tn'], d['Sr'], V, d['neg'])
        bad = cap(' '.join(x for x in [f"{d['sp']} {verb} {rs}", g, d['comp'], d['cue']] if x)) + '.'
        good = [cap(' '.join(x for x in [f"{d['sp']} {verb} {rs}", g, d['comp'], c] if x)) + '.' for c in cues_a]
        if bad in good: return None
        return line(f"Correct the mistake: {bad}", good)
    return None

# --------- questions -------------
def gen_question(level, rng):
    V = rng.pick(VERBS); comp = rng.pick(V.comps)
    sp_name, sp_pr = rng.pick(SPEAKERS); verb = rng.pick(['asked me','asked'])
    tn = rng.pick(['ps','ps','pc','pas','pp','fw','can'])
    third = rng.pick([False,False,True])
    Sd = SUBJ[1] if not third else rng.pick([x for x in SUBJ if x.kind in ('sg','pl') and x.text not in ('He','She','We','They',sp_name,'You','I')])
    Sr = SUBJ[0] if not third else Sd
    rs = 'I' if not third else Sd.mid
    kind = rng.pick(['yn','yn','wh'])
    cue_d = rng.pick(TCUES[tn]) if tn not in ('can',) else ''
    if tn == 'pp': cue_d = rng.pick(['yet','already']) if kind == 'yn' else ''
    if tn == 'pp' and kind == 'yn': cue_d = 'yet'
    if V.dur and tn == 'pas': cue_d = rng.pick(PAS_D)
    cues_a = cue_rep(cue_d) if cue_d != 'yet' else ['yet']
    # direct question text
    if kind == 'yn':
        a,r = qp(tn,Sd,V) if tn in ('ps','pc','pas','pp','fw') else ('Can', V.base)
        dq = cap(' '.join(x for x in [a, Sd.mid, r, comp, cue_d] if x)) + '?'
        grp_ans = rep_group(tn if tn != 'pp' else 'pp', Sr, V, False)
        rep_ans_group = grp_ans
        if tn == 'can': rep_ans_group = [f"could {V.base}"]
        opener = f'{sp_name} {verb}, "{dq[:-1]}?"'
        pre = f"{sp_name} {verb}"
        q = None
        if level == 'easy':
            q = f"{opener} {pre} if {rs} ___ ({V.base}) {comp}{(' ' + cues_a[0]) if cues_a[0] else ''}."
            return line(q, rep_ans_group)
        if level == 'medium':
            k = rng.pick(['one','two'])
            if k == 'one': return line(f"{opener} {pre} ___ {rs} ___ ({V.base}) {comp}{(' ' + cues_a[0]) if cues_a[0] else ''}.", ['if','whether'], rep_ans_group)
            return line(f"{opener} {pre} ___ {rs} {rep_full(tn,Sr,V) if tn!='can' else 'could '+V.base} {comp}{(' ' + cues_a[0]) if cues_a[0] else ''}.", ['if','whether'])
        full = []
        for w in ['if','whether']:
            for g in rep_ans_group:
                if g.startswith("'"): continue
                for c in cues_a:
                    full.append(cap(' '.join(x for x in [pre, w, rs, g, comp, c] if x)) + '.')
        k = rng.pick(['report','report','fix','fix'])
        if k == 'report': return line(f"Report it: {opener}", full[:24])
        wrongs = [cap(' '.join(x for x in [pre, 'if', rs, (full_group(tn,Sr,V) if tn!='can' else 'can '+V.base) if tn not in ('fw',) else 'will '+V.base, comp, cues_a[0]] if x)) + '.']
        # also inversion error
        a2, r2 = qp(tn,Sr,V) if tn in ('ps','pc','pas','pp','fw') else ('Can',V.base)
        wrongs.append(cap(' '.join(x for x in [pre, 'if', a2.lower(), rs, r2, comp, cues_a[0]] if x)) + '.')
        w = rng.pick(wrongs)
        if w in full: return None
        return line(f"Correct the mistake: {w}", full[:24])
    # wh
    wh = {'ps': 'How often', 'pc': 'Why', 'pas': 'When', 'pp': 'How many times', 'fw': 'When', 'can': 'Where'}[tn]
    if tn == 'pp': 
        if V.dur: wh = 'How long'
    a, r = qp(tn,Sd,V) if tn != 'can' else ('Can', V.base)
    dq = cap(' '.join(x for x in [wh, a.lower(), Sd.mid, r, comp] if x)) + '?'
    gans = rep_group(tn if tn != 'can' else 'can', Sr, V, False)
    pre = f"{sp_name} {verb}"
    opener = f'{sp_name} {verb}, "{dq[:-1]}?"'
    if level == 'easy':
        return line(f"{opener} {pre} {wh.lower()} {rs} ___ ({V.base}) {comp}.", gans)
    if level == 'medium':
        if rng.pick([0,1]): return line(f"{opener} {pre} ___ {rs} ___ ({V.base}) {comp}.", [wh.lower()], gans)
        return line(f"{opener} {pre} {wh.lower()} ___ ___ ({V.base}) {comp}.", [rs], gans) if False else line(f"{opener} {pre} {wh.lower()} {rs} ___ ({V.base}) {comp}.", gans)
    full = [cap(' '.join(x for x in [pre, wh.lower(), rs, g, comp] if x)) + '.' for g in gans if not g.startswith("'")]
    k = rng.pick(['report','fix','fix'])
    if k == 'report': return line(f"Report it: {opener}", full)
    a2, r2 = qp(tn,Sr,V) if tn != 'can' else ('Can',V.base)
    inv = cap(' '.join(x for x in [pre, wh.lower(), a2.lower(), rs, r2, comp] if x)) + '.'
    if inv in full: return None
    return line(f"Correct the mistake: {inv}", full)

# --------- commands ---------
def gen_command(level, rng):
    V = rng.pick(VERBS); comp = rng.pick(V.comps)
    sp_name, sp_pr = rng.pick(SPEAKERS)
    neg = rng.pick([False,False,True])
    polite = rng.pick([False,True])
    dont = "don't " if neg else ''
    cmd = ('Please ' + dont + V.base + ' ' + comp) if polite else cap(dont + V.base + ' ' + comp)
    verb = 'asked me' if polite else rng.pick(['told me','told me','told me'])
    ver_inf = f"{'not ' if neg else ''}to {V.base}"
    pre = f"{sp_name} {verb}"
    opener = f'{sp_name} said to me, "{cmd}."'
    if polite and rng.pick([0,1]): opener = f'{sp_name} said, "{cmd}."'
    if level == 'easy':
        return line(f"{opener} {pre} ___ ({V.base}) {comp}.", ['not to '+V.base] if neg else ['to '+V.base])
    if level == 'medium':
        k = rng.pick(['pat','verb','pat'])
        if k == 'pat': return line(f"{opener} {pre} {'not ' if neg else ''}___ ({V.base}) {comp}.", ['to '+V.base]) if neg else line(f"{opener} {pre} ___ ({V.base}) {comp}.", ['to '+V.base])
        vb = 'asked' if polite else 'told'
        return line(f"{opener} {sp_name} ___ me {ver_inf} {comp}.", ['asked'] if polite else ['told'])
    full = cap(f"{pre} {ver_inf} {comp}") + '.'
    k = rng.pick(['report','report','fix','fix'])
    if k == 'report': return line(f"Report it: {opener}", [full, cap(f"{sp_name} {'asked' if polite else 'told'} me {ver_inf} {comp}") + '.'] if True else [full])
    if neg:
        wr = rng.pick([cap(f"{pre} not {V.base} {comp}") + '.', cap(f"{pre} don't {V.base} {comp}") + '.', cap(f"{pre} that I don't {V.base} {comp}") + '.', cap(f"{sp_name} said me not to {V.base} {comp}") + '.', cap(f"{pre} not {V.ing} {comp}") + '.'])
    else:
        wr = rng.pick([cap(f"{pre} {V.base} {comp}") + '.', cap(f"{pre} that I {V.base} {comp}") + '.', cap(f"{pre} to {V.ing} {comp}") + '.', cap(f"{sp_name} said me to {V.base} {comp}") + '.'])
    if wr == full: return None
    alts = [full] + [cap(f"{sp_name} {x} me {ver_inf} {comp}") + '.' for x in ('asked','told')]
    return line(f"Correct the mistake: {wr}", alts)

# --------- reporting verbs ---------
RV = [  # (reporting verb past, pattern fn(V,comp)->(direct, reported tail), how)
 ('promised', lambda V,c: (f"I'll {V.base} {c}", f"to {V.base} {c}", f"to {V.base}"), 'I'),
 ('offered', lambda V,c: (f"Shall I {V.base} {c}?", f"to {V.base} {c}", f"to {V.base}"), 'I'),
 ('refused', lambda V,c: (f"I won't {V.base} {c}", f"to {V.base} {c}", f"to {V.base}"), 'I'),
 ('agreed', lambda V,c: (f"All right, I'll {V.base} {c}", f"to {V.base} {c}", f"to {V.base}"), 'I'),
 ('threatened', lambda V,c: (f"I'll {V.base} {c}!", f"to {V.base} {c}", f"to {V.base}"), 'I'),
 ('admitted', lambda V,c: (f"Yes, I {V.past} {c}", f"{V.ing} {c}", V.ing), 'I'),
 ('denied', lambda V,c: (f"I didn't {V.base} {c}", f"{V.ing} {c}", V.ing), 'I'),
 ('suggested', lambda V,c: (f"Let's {V.base} {c}", f"{V.ing} {c}", V.ing), 'W'),
 ('apologised', lambda V,c: (f"I'm sorry I {V.past} {c}", f"for {V.ing} {c}", f"for {V.ing}"), 'I'),
 ('insisted', lambda V,c: (f"I will {V.base} {c}!", f"on {V.ing} {c}", f"on {V.ing}"), 'I'),
 ('advised', lambda V,c: (f"You should {V.base} {c}", f"me to {V.base} {c}", f"me to {V.base}"), 'Y'),
 ('warned', lambda V,c: (f"Don't {V.base} {c}!", f"me not to {V.base} {c}", f"me not to {V.base}"), 'Y'),
 ('reminded', lambda V,c: (f"Don't forget to {V.base} {c}", f"me to {V.base} {c}", f"me to {V.base}"), 'Y'),
 ('invited', lambda V,c: (f"Would you like to {V.base} {c}?", f"me to {V.base} {c}", f"me to {V.base}"), 'Y'),
 ('begged', lambda V,c: (f"Please, please {V.base} {c}", f"me to {V.base} {c}", f"me to {V.base}"), 'Y'),
 ('ordered', lambda V,c: (f"{cap(V.base)} {c} at once", f"me to {V.base} {c} at once", f"me to {V.base}"), 'Y'),
 ('accused', lambda V,c: (f"You {V.past} {c}!", f"me of {V.ing} {c}", f"me of {V.ing}"), 'Y'),
 ('congratulated', lambda V,c: (f"Well done on {V.ing} {c}", f"me on {V.ing} {c}", f"me on {V.ing}"), 'Y'),
 ('thanked', lambda V,c: (f"Thank you for {V.ing} {c}", f"me for {V.ing} {c}", f"me for {V.ing}"), 'Y'),
]
def gen_rverb(level, rng):
    V = rng.pick(VERBS); comp = rng.pick(V.comps)
    sp_name, sp_pr = rng.pick(SPEAKERS)
    rv, fn, who = rng.pick(RV)
    direct, tail, tailshort = fn(V, comp)
    dq = direct if direct.endswith('?') else direct
    endp = '' if dq[-1] in '!?' else '.'
    opener = f'{sp_name} said, "{dq}{endp}"'
    if level == 'easy':
        return line(f"{opener} {sp_name} ___ ({rv[:-2] if not rv.endswith('ised') else rv[:-3]+'ise'}) {tail}.".replace('(promis)','(promise)') if False else f"{opener} {sp_name} ___ {tail}.", [rv] if rv != 'apologised' else ['apologised','apologized'])
    if level == 'medium':
        k = rng.pick(['pat','verb'])
        if k == 'pat': return line(f"{opener} {sp_name} {rv} ___ ({V.base}) {comp}.", [tailshort.replace(' '+comp,'')] if False else [tailshort])
        return line(f"{opener} {sp_name} ___ {tail}.", [rv] if rv != 'apologised' else ['apologised','apologized'])
    full = cap(f"{sp_name} {rv} {tail}") + '.'
    alts = [full]
    if rv == 'apologised': alts.append(cap(f"{sp_name} apologized {tail}") + '.')
    if rv in ('admitted','denied','suggested'): alts.append(cap(f"{sp_name} {rv} {tail}") + '.')
    k = rng.pick(['report','report','fix'])
    if k == 'report': return line(f"Report it, using \"{rv}\": {opener}", alts)
    # fix: wrong pattern
    wrongs = {
     'to': cap(f"{sp_name} {rv} {V.ing} {comp}") + '.',
     'ing': cap(f"{sp_name} {rv} to {V.base} {comp}") + '.',
    }
    pat = 'to' if tail.startswith('to ') or tail.startswith('me to') or tail.startswith('me not') else ('ing' if tail.startswith(V.ing) else None)
    if not pat: return None
    if pat == 'to' and tail.startswith('me'): return None
    w = wrongs[pat]
    if w in alts: return None
    return line(f"Correct the mistake: {w}", alts)

def gen_all_reported(level, rng):
    r = rng.r.random()
    if r < .45: return gen_statement(level, rng)
    if r < .7: return gen_question(level, rng)
    return gen_command(level, rng)

def gen_reported_jobs(C):
    return {
     'reported-statements': lambda: gen_topic(lambda lv,rng: gen_statement(lv,rng), C, 51),
     'reported-questions': lambda: gen_topic(lambda lv,rng: gen_question(lv,rng), C, 52),
     'reported-commands': lambda: gen_topic(lambda lv,rng: gen_command(lv,rng), C, 53),
     'reporting-verbs': lambda: gen_topic(lambda lv,rng: gen_rverb(lv,rng), C, 54),
     'reported-speech-all': lambda: gen_topic(lambda lv,rng: gen_all_reported(lv,rng), C, 55),
    }
