from lib import *
from passive import gen_topic
SUBJ3 = [Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('Karim','sg','he',True),Subj('Dilya','sg','she',True),Subj('My uncle','sg','he'),Subj('The manager','sg','she'),Subj('The students','pl','they'),Subj('The players','pl','they'),Subj('The company','sg','it',objp='it'),Subj('My neighbours','pl','they')]
# (active base, active past, past participle)
RV = [("say","said","said"),("believe","believed","believed"),("think","thought","thought"),("know","knew","known"),("report","reported","reported"),("expect","expected","expected"),("consider","considered","considered"),("understand","understood","understood"),("claim","claimed","claimed"),("allege","alleged","alleged")]
def be_p(S, past): 
    sg = S.kind == 'sg'
    return ('was' if sg else 'were') if past else ('is' if sg else 'are')
def case(rng):
    S = rng.pick(SUBJ3); V = rng.pick(VERBS); comp = rng.pick(V.comps); rv = rng.pick(RV)
    past_r = rng.pick([False, False, True])
    sg = S.kind == 'sg'
    t = rng.pick(['pres','pres','cont','earlier','earlier','neg'])
    alt = None
    if t == 'cont' and past_r: t = 'pres'
    if t == 'neg' and past_r: t = 'pres'
    if past_r:
        if t == 'pres': act = f"{S.mid} {V.past} {comp}"; inf = f"to {V.base} {comp}"
        elif t == 'cont': return None
        else: act = f"{S.mid} had {V.pp} {comp}"; inf = f"to have {V.pp} {comp}"
    else:
        if t == 'pres': act = f"{S.mid} {V.s if sg else V.base} {comp}"; inf = f"to {V.base} {comp}"
        elif t == 'cont': act = f"{S.mid} {be_p(S, False)} {V.ing} {comp}"; inf = f"to be {V.ing} {comp}"
        elif t == 'earlier':
            a1 = f"{S.mid} {V.past} {comp}"; a2 = f"{S.mid} {'has' if sg else 'have'} {V.pp} {comp}"
            act = a1 if rng.pick([0,1]) else a2; alt = a2 if act == a1 else a1; inf = f"to have {V.pp} {comp}"
        else: act = f"{S.mid} {'doesn' + chr(39) + 't' if sg else 'don' + chr(39) + 't'} {V.base} {comp}"; inf = f"not to {V.base} {comp}"
    return S, V, comp, rv, past_r, t, act, inf, alt
def gen_rv(level, rng):
    c = case(rng)
    if not c: return None
    S, V, comp, rv, past_r, t, act, inf, alt = c
    ab, apast, pp = rv
    mood = rng.pick(['aff','aff','neg','q'])
    if t == 'neg' and mood == 'neg': mood = 'aff'
    b = be_p(S, past_r); bn = b + 'n' + chr(39) + 't'
    # earlier alt acts accepted
    it_aff = f"It {'was' if past_r else 'is'} {pp} that {act}."
    pass_aff = f"{S.text} {b} {pp} {inf}."
    it_neg = f"It {'wasn' + chr(39) + 't' if past_r else 'isn' + chr(39) + 't'} {pp} that {act}."
    pass_neg = f"{S.text} {bn} {pp} {inf}."
    it_q = f"{'Was' if past_r else 'Is'} it {pp} that {act}?"
    pass_q = f"{cap(b)} {S.mid} {pp} {inf}?"
    act_aff = f"People {apast if past_r else ab} that {act}."
    act_neg = f"People {'didn' + chr(39) + 't ' + ab if past_r else 'don' + chr(39) + 't ' + ab} that {act}."
    act_q = f"{'Did' if past_r else 'Do'} people {ab} that {act}?"
    A = {'aff': act_aff, 'neg': act_neg, 'q': act_q}[mood]
    IT = {'aff': it_aff, 'neg': it_neg, 'q': it_q}[mood]
    PS = {'aff': pass_aff, 'neg': pass_neg, 'q': pass_q}[mood]
    if level == 'easy':
        ans = inf[:-len(comp)].rstrip()
        return line(f"{IT} {PS.replace(inf, '___ (' + V.base + ') ' + comp)}", [ans])
    if level == 'medium':
        return line('Rewrite starting with the subject: ' + A, [PS])
    k = rng.pick(['it','subj','subj','fixa','back'])
    if k == 'it': return line("Rewrite beginning with 'It': " + A, [IT])
    if k == 'subj': return line('Rewrite starting with the subject: ' + A, [PS])
    if k == 'back':
        its = [IT]
        if alt: its.append(IT.replace(act, alt))
        return line("Rewrite with 'It': " + PS, its)
    # fix common mistakes
    bad = rng.pick([PS.replace(' to ', ' ', 1) if ' to ' in PS else None, PS.replace(f"{pp} {inf}", f"{pp} that {inf}") if False else None])
    if not bad or bad == PS: 
        bad = PS.replace(f" {pp} to have {V.pp}", f" {pp} to {V.pp}") if 'to have' in PS else PS.replace(f" {pp} to {V.base}", f" {pp} {V.s}") if inf.startswith('to ' + V.base) else None
    if not bad or bad == PS: return None
    return line('Correct the mistake: ' + bad, [PS])
def gen_rv_jobs(C):
    return {'passive-reporting-verbs': lambda: gen_topic(gen_rv, C, 122)}
