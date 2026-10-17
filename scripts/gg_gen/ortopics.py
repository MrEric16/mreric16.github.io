from tense import *

def fc(t, S, V, pol, rng):
    c = dict(lead='', kind='none', pre='', end='')
    if t == 'ps':
        if pol == 'aff' and rng.pick([0,1]): c['pre'] = rng.pick(['usually','often','always','sometimes'])
        else: c['end'] = rng.pick(['every day','every morning','every week','on Mondays','at the weekend','twice a week','every summer','on Fridays'])
    elif t == 'pc':
        if rng.pick([0,0,1]): c['lead'], c['kind'] = 'Look!', 'sentence'
        else: c['end'] = rng.pick(['now','at the moment','right now'])
    elif t == 'pas':
        c['end'] = rng.pick(PAS_D if V.dur else (PAS_E + PAS_D[:3]))
    elif t == 'pac':
        if rng.pick([0,1]): c['lead'], c['kind'] = rng.pick(PAC_LEAD), 'clause'
        else: c['end'] = rng.pick(PAC_END)
    elif t == 'pp':
        pool = {'aff': ['already','three times','this week','so far','twice'], 'neg': ['yet','so far','this week'], 'q': ['yet','so far','this week']}[pol]
        c['end'] = rng.pick(pool)
    elif t == 'ppc':
        c['end'] = rng.pick(['for two hours',"since nine o'clock",'all morning','all day','lately','for three hours','since breakfast'])
    return c

def Pn(S): return {'i':'I'}.get(S.pron, S.pron.capitalize()) if S.kind != 'i' else 'I'
def pl(S): return 'I' if S.kind == 'i' else S.pron

# ----- pair specific contrast items -----
EVENTS = [("the phone ___ (ring)",'rang'),("the lights ___ (go) out",'went'),("the bell ___ (ring)",'rang'),("it ___ (start) to rain",'started'),
          ("the teacher ___ (come) in",'came'),("somebody ___ (knock) on the door",'knocked'),("the alarm ___ (go) off",'went'),("the power ___ (fail)",'failed')]
def contrast_ps_pc(S,rng):
    V1,V2 = rng.pick(VERBS), rng.pick(VERBS); c1,c2 = rng.pick(V1.comps), rng.pick(V2.comps)
    h = rng.pick(['usually','often','always']); e = rng.pick(['right now','at the moment','today'])
    k = rng.pick(['a','a','b'])
    if k == 'a':
        return line(f"{S.text} {h} ___ ({V1.base}) {c1}, but {e} {pl(S)} ___ ({V2.base}) {c2}.", grp('ps',S,V1), grp('pc',S,V2))
    return line(f"{S.text} ___ ({V1.base}) {c1} {rng.pick(['every day','every week','on Mondays'])}, but at the moment {pl(S)} ___ (not / {V1.base}) {c1}.", grp('ps',S,V1), grp('pc',S,V1,True))
def contrast_pas_pac(S,rng):
    V1,V2 = rng.pick(VERBS), rng.pick(VERBS); c1,c2 = rng.pick(V1.comps), rng.pick(V2.comps)
    ev, evans = rng.pick(EVENTS)
    k = rng.pick(['a','b','c','d','e'])
    if k == 'a': return line(f"{S.text} ___ ({V1.base}) {c1} when {ev}.", grp('pac',S,V1), [evans])
    if k == 'b': return line(f"While {S.mid} ___ ({V1.base}) {c1}, {ev}.", grp('pac',S,V1), [evans])
    if k == 'c': return line(f"When {ev}, {S.mid} ___ ({V1.base}) {c1}.", [evans], grp('pac',S,V1))
    if k == 'd':
        S2 = rng.pick([x for x in SUBJ if x.text != S.text])
        if not valid('pac',V2): return None
        return line(f"While {S.mid} ___ ({V1.base}) {c1}, {S2.mid} ___ ({V2.base}) {c2}.", grp('pac',S,V1), grp('pac',S2,V2))
    cue = rng.pick(PAS_D if V1.dur or V2.dur else PAS_E)
    return line(f"{S.text} ___ ({V1.base}) {c1} and then ___ ({V2.base}) {c2} {cue}.", grp('pas',S,V1), grp('pas',S,V2))
def contrast_pp_ppc(S,rng):
    V1 = rng.pick([v for v in VERBS if not v.ach]); V2 = rng.pick(VERBS)
    c1,c2 = rng.pick(V1.comps), rng.pick(V2.comps)
    dur = rng.pick(['for two hours','all morning','since nine o\'clock','all day','for three hours'])
    num = rng.pick(['three times','twice','already','so far'])
    if rng.pick([0,1]):
        return line(f"{S.text} ___ ({V1.base}) {c1} {dur}. {Pn(S)} ___ ({V2.base}) {c2} {num}.", grp('ppc',S,V1), grp('pp',S,V2))
    return line(f"{S.text} ___ ({V2.base}) {c2} {num}. {Pn(S)} ___ ({V1.base}) {c1} {dur}.", grp('pp',S,V2), grp('ppc',S,V1))
def contrast_pp_pas(S,rng):
    V1,V2 = rng.pick(VERBS), rng.pick(VERBS); c1,c2 = rng.pick(V1.comps), rng.pick(V2.comps)
    pc = rng.pick(PAS_D if V1.dur else PAS_E)
    num = rng.pick(['three times this week','twice so far','already','many times'])
    k = rng.pick(['a','b','c','ever'])
    if k == 'a': return line(f"{S.text} ___ ({V1.base}) {c1} {pc}. {Pn(S)} ___ ({V2.base}) {c2} {num}.", grp('pas',S,V1), grp('pp',S,V2))
    if k == 'b': return line(f"{S.text} ___ ({V2.base}) {c2} {num}, but {pl(S)} ___ (not / {V1.base}) {c1} {pc}.", grp('pp',S,V2), grp('pas',S,V1,True))
    if k == 'c': return line(f"___ {S.mid} ever ___ ({V1.base}) {c1}? Yes, {pn_short(S)} ___ ({V1.base}) {c1} {pc}.", ['Has' if S.sg else 'Have'], [V1.pp], [V1.past]) if S.kind != 'i' else None
    return line(f"Have you ever ___ ({V1.base}) {c1}? Yes, I ___ ({V1.base}) {c1} {pc}.", [V1.pp], [V1.past])
def pn_short(S): return S.pron

SW = lambda rng: None

def gen_or(tid, rng, level):
    ts = {'ps_pc':('ps','pc'),'pas_pac':('pas','pac'),'pp_ppc':('pp','ppc'),'pp_pas':('pp','pas')}[tid]
    contrast = {'ps_pc':contrast_ps_pc,'pas_pac':contrast_pas_pac,'pp_ppc':contrast_pp_ppc,'pp_pas':contrast_pp_pas}[tid]
    S = rng.pick(SUBJ); V = rng.pick(VERBS); comp = rng.pick(V.comps)
    t = rng.pick(ts); other = ts[1] if t == ts[0] else ts[0]
    if not valid(t,V): return None
    if level == 'easy':
        r = rng.r.random(); pol = 'aff' if r < .6 else ('neg' if r < .85 else 'q')
        c = fc(t,S,V,pol,rng)
        if pol == 'aff': return line(aff(t,S,V,comp,c,f"___ ({V.base})"), grp(t,S,V))
        if pol == 'neg': return line(neg(t,S,V,comp,c,f"___ (not / {V.base})"), grp(t,S,V,True))
        a,rr = qp(t,S,V); return line(ques(t,S,V,comp,c,'___',rr),[a])
    if level == 'medium':
        k = rng.pick(['single','single','q','contrast','contrast','contrast','short','tag','extra'])
        if k == 'single':
            pol = rng.pick(['aff','neg']); c = fc(t,S,V,pol,rng)
            if pol == 'aff': return line(aff(t,S,V,comp,c,f"___ ({V.base})"), grp(t,S,V))
            return line(neg(t,S,V,comp,c,f"___ (not / {V.base})"), grp(t,S,V,True))
        if k == 'q':
            c = fc(t,S,V,'q',rng); a,rr = qp(t,S,V)
            return line(ques(t,S,V,comp,c,'___',f"___ ({V.base})"),[a],[rr])
        if k == 'short':
            if S.kind == 'i': return None
            c = fc(t,S,V,'q',rng); qq = ques(t,S,V,comp,c); p = pron_ans(S)
            return line(f"{qq} Yes, {p} ___.", [short_aux(t,S)]) if rng.pick([0,1]) else line(f"{qq} No, {p} ___.", negs(short_aux(t,S)))
        if k == 'tag':
            if S.kind == 'i': return None
            c = fc(t,S,V,'aff',rng); c['pre'] = ''
            if c['kind'] == 'sentence': return None
            if rng.pick([0,1]): return line(aff(t,S,V,comp,c)[:-1] + f", ___ {S.pron}?", negs(short_aux(t,S)))
            c = fc(t,S,V,'neg',rng)
            if c['kind'] == 'sentence': return None
            return line(neg(t,S,V,comp,c)[:-1] + f", ___ {S.pron}?", [short_aux(t,S)])
        if k == 'extra':
            if tid == 'pp_pas':
                if rng.pick([0,1]): return line(f"When ___ {S.mid} ___ ({V.base}) {comp}?", ['did'], [V.base])
                return line(f"___ {S.mid} ever ___ ({V.base}) {comp}?", [cap(have_pres(S))], [V.pp]) if S.kind != 'i' else None
            if tid == 'pp_ppc':
                if V.ach: return None
                return line(f"How long ___ {S.mid} ___ ({V.base}) {comp}?", [have_pres(S)], [f"been {V.ing}"])
            if tid == 'ps_pc':
                return line(f"What ___ {S.mid} usually ___ ({V.base})?", [do_pres(S)], [V.base]) if False else None
            return None
        return contrast(S,rng)
    # hard
    k = rng.pick(['fix','fix','fix','contrast','contrast','contrast','neg','q','switch'])
    if k == 'fix':
        pol = rng.pick(['aff','neg','q']); c = fc(t,S,V,pol,rng)
        if pol != 'aff': c['pre'] = ''
        if not valid(other,V): return None
        f = {'aff': aff, 'neg': neg, 'q': ques}[pol]
        w, cr = f(other,S,V,comp,c), f(t,S,V,comp,c)
        if w == cr: return None
        return line('Correct the mistake: ' + w, [cr])
    if k == 'contrast': return contrast(S,rng)
    if k == 'switch':
        if tid != 'ps_pc': return None
        if rng.pick([0,1]):
            c = dict(lead='',kind='none',pre='',end=rng.pick(['every day','every week','on Mondays','at the weekend']))
            c2 = dict(lead='',kind='none',pre='',end='right now')
            return line('Rewrite with "right now": ' + aff('ps',S,V,comp,c), [aff('pc',S,V,comp,c2)])
        c = dict(lead='',kind='none',pre='',end='right now')
        e = rng.pick(['every day','every week','on Mondays','at the weekend'])
        c2 = dict(lead='',kind='none',pre='',end=e)
        return line(f'Rewrite with "{e}": ' + aff('pc',S,V,comp,c), [aff('ps',S,V,comp,c2)])
    c = fc(t,S,V,'neg' if k == 'neg' else 'q',rng); c['pre'] = ''
    if c['kind'] == 'sentence' or c['end'] in ('already',): return None
    s1 = aff(t,S,V,comp,c)
    if k == 'neg': return line('Make a negative sentence: ' + s1, [neg(t,S,V,comp,c)])
    return line('Make a question: ' + s1, [ques(t,S,V,comp,c)])

def gen_or_topic(tid, counts, seed):
    rng = Rng(seed); out = {}
    for level, n in counts.items():
        seen, lines, tries = set(), [], 0
        while len(lines) < n and tries < n * 100:
            tries += 1
            l = gen_or(tid, rng, level)
            if not l: continue
            q = l.split(' => ')[0]
            if q in seen: continue
            seen.add(q); lines.append(l)
        out[level] = lines
    return out
