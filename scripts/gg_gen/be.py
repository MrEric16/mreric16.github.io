from lib import *
ADJ = ['tired','hungry','happy','busy','late','ill','absent','nervous','ready','angry','thirsty','bored','excited','sleepy','cold','hot','worried','clever','kind','quiet','careful','lucky','proud','free']
PLACE = ['at home','at school','in the garden','in the kitchen','in the library','at the bazaar','in Samarkand','at work','in the park','at the station','in the classroom','in Dubai','at the cinema','in the gym','at the airport']
NOUN = [('a student','students'),('a teacher','teachers'),('a doctor','doctors'),('a nurse','nurses'),('an engineer','engineers'),('a football fan','football fans'),('my best friend','my best friends'),('a good cook','good cooks'),('a taxi driver','taxi drivers'),('a singer','singers')]
FROM = ['from Uzbekistan','from Dubai','from London','from Russia','from Turkey','from Kazakhstan','from Bukhara','from Samarkand']
AGES = ['twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','twenty','thirty','forty']
PRES_END = ['today','at the moment','right now','this morning']
PAST_END = ['yesterday','last night','last week','two days ago','this morning','last Monday','at six o\'clock yesterday','last weekend']

def comp_for(S, rng, past=False):
    k = rng.pick(['adj','adj','place','place','noun','from','age'] if not past else ['adj','adj','place','place','place'])
    if k == 'adj': return rng.pick(ADJ), 'adj'
    if k == 'place': return rng.pick(PLACE), 'place'
    if k == 'noun':
        for _ in range(20):
            n = rng.pick(NOUN)
            head = n[1].split()[-1].rstrip('s')
            if head not in S.text.lower() and 'friend' not in S.text.lower(): break
        return (n[1] if S.kind in ('pl','you') else n[0]), 'noun'
    if k == 'from': return rng.pick(FROM), 'from'
    return f"{rng.pick(AGES)} years old", 'age'

def be_form(S, past, neg=False):
    if not past:
        b = be_pres(S)
        if neg: return ["'m not","am not"] if b == 'am' else [f"{b}n't", f"{b} not"]
        return [b]
    b = be_past(S)
    return [f"{b}n't", f"{b} not"] if neg else [b]
def full_be(S, past, neg=False):
    for x in be_form(S,past,neg):
        if not x.startswith("'"): return x

def gen_be(past, level, rng):
    S = rng.pick(SUBJ); comp, kind = comp_for(S, rng, past)
    end = rng.pick(PAST_END if past else PRES_END) if (kind in ('adj','place') and rng.pick([0,1,1])) else ''
    if past and not end: end = rng.pick(PAST_END)  # past needs a time cue for natural sense
    if past and kind not in ('adj','place'): return None
    def sent(group): 
        return cap(' '.join(x for x in [S.text, group, comp, end] if x) + '.')
    def qsent(aux): 
        return cap(' '.join(x for x in [aux, S.mid, comp, end] if x) + '?')
    r = rng.r.random()
    if level == 'easy':
        if r < .55: return line(sent('___ (be)'), be_form(S,past))
        if r < .8: return line(sent('___ (not / be)'), be_form(S,past,True))
        return line(qsent('___'), [cap(be_form(S,past)[0])])
    if level == 'medium':
        k = rng.pick(['wh','short','short','tag','tag','two','q2'])
        if k == 'q2': return line(qsent('___'), [cap(be_form(S,past)[0])]) if False else line(sent('___ (be)'), be_form(S,past)) 
        if k == 'wh':
            if kind == 'place': w = 'Where'
            elif kind == 'age' and not past: w = 'How old'
            elif kind == 'from' and not past: w = 'Where'
            else: return None
            core = ' '.join(x for x in [w, '___', S.mid, end] if x) + '?'
            return line(core, [be_form(S,past)[0]])
        if k == 'short':
            if S.kind == 'i': return None
            qq = qsent(cap(be_form(S,past)[0])); p = pron_ans(S)
            if rng.pick([0,1]): return line(f"{qq} Yes, {p} ___.", be_form(S,past))
            return line(f"{qq} No, {p} ___.", be_form(S,past,True))
        if k == 'tag':
            if S.kind == 'i' and not past: return None
            p = S.pron if S.kind != 'i' else 'I'
            if rng.pick([0,1]): st = sent(full_be(S,past))[:-1]; return line(f"{st}, ___ {p}?", be_form(S,past,True) if not (S.kind=='i' and not past) else ["aren't"])
            st = sent(full_be(S,past,True))[:-1]; return line(f"{st}, ___ {p}?", be_form(S,past))
        if k == 'two':
            S2 = rng.pick([x for x in SUBJ if x.text != S.text]); comp2, kind2 = comp_for(S2, rng, past)
            if past and kind2 not in ('adj','place'): return None
            if rng.pick([0,1]):
                return line(cap(f"{S.text} ___ (be) {comp}, but {S2.mid} ___ (not / be) {comp2} {end}".strip())+'.', be_form(S,past), be_form(S2,past,True))
            return line(cap(f"{S.text} ___ (be) {comp} and {S2.mid} ___ (be) {comp2} {end}".strip())+'.', be_form(S,past), be_form(S2,past))
        return None
    k = rng.pick(['neg','q','fix','fix','aff'])
    if k == 'neg': return line('Make a negative sentence: ' + sent(full_be(S,past)), [sent(full_be(S,past,True))])
    if k == 'q': return line('Make a question: ' + sent(full_be(S,past)), [qsent(cap(full_be(S,past)))])
    if k == 'aff': return line('Make an affirmative sentence: ' + sent(full_be(S,past,True)), [sent(full_be(S,past))])
    wrongs = []
    b = full_be(S,past); alts = ['am','is','are'] if not past else ['was','were']
    for a in alts:
        if a != b: wrongs.append(sent(a))
    if not past: wrongs.append(sent(f"{b} {'' }").replace(f" {b} ", ' ')) if False else None
    pol = rng.pick(['aff','neg','q'])
    if pol == 'aff':
        w = rng.pick([x for x in wrongs if x]); return line('Correct the mistake: ' + w, [sent(b)])
    if pol == 'neg':
        o = rng.pick([a for a in alts if a != b]); 
        w = sent(f"{o}n't" if o != 'am' else "am not"); return line('Correct the mistake: ' + w, [sent(full_be(S,past,True))])
    o = rng.pick([a for a in alts if a != b]); w = qsent(cap(o)); return line('Correct the mistake: ' + w, [qsent(cap(b))])

def gen_be_topic(past, counts, seed):
    rng = Rng(seed); out = {}
    for level, n in counts.items():
        seen, lines, tries = set(), [], 0
        while len(lines) < n and tries < n * 100:
            tries += 1
            l = gen_be(past, level, rng)
            if not l: continue
            q = l.split(' => ')[0]
            if q in seen: continue
            seen.add(q); lines.append(l)
        out[level] = lines
    return out
