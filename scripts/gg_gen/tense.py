from lib import *

def negs(a):
    if a == 'will': return ["won't","will not"]
    if a == 'am': return ["am not","'m not"]
    return [a + "n't", a + " not"]
# ---------- cue pools ----------
PS_END = ['every day','every morning','every week','on Mondays','at the weekend','twice a week','in the evening','every summer','on Fridays','every year']
PS_PRE = ['usually','often','always','sometimes']
PC_END = ['now','at the moment','right now']
PC_END_FREE = PC_END + ['these days','this week']
PAS_E = ['yesterday','last night','last week','two days ago','last Monday','last month','on Sunday','last weekend','last summer','three days ago']
PAS_D = ['in 2015','ten years ago','five years ago','last year','in 2010','two years ago','in 2018','a long time ago']
PAC_LEAD = ["At eight o'clock last night,","At nine o'clock yesterday morning,","At midnight,","This time yesterday,","At six o'clock yesterday evening,","At half past seven this morning,","At noon yesterday,","At ten o'clock last night,"]
PAC_END = ['when the phone rang','when the headteacher came in','when it started to rain','when the lights went out','when I arrived','when I called','when the bell rang','when the storm began']
PP_AFF = ['already','three times','this week','twice','so far','recently','many times']
PP_NEG = ['yet','this week','so far','recently']
PP_Q = ['yet','this week','so far','recently']
PP_DUR = ['for two years','since 2019','for a long time','since last summer','for five years','since January']
PPC_END = ['for two hours','since nine o\'clock','all morning','all day','lately','for a long time','since breakfast','for ten minutes','for three hours','since lunch']
PAP_END = ['when the guests arrived','when I got home','when the film started','when the bell rang','before the headteacher came','before the match began','by the time we arrived','before the storm started','when the manager called','before the bus left']
F_END = ['tomorrow','next week','next month','next year','tonight','in two days','on Friday','this weekend','next summer','on Saturday']
PAPN_END = ['for two hours','all morning','since nine o\'clock','for a long time','for three hours','all day','for ten minutes','since breakfast','for hours','for an hour']
PAPN_CL = ['when the guests arrived','when I got home','when the bell rang','when the headteacher came in','when I called','when the storm began','when the film started','when the manager arrived']
FP_END = ['by Friday','by next year','by the end of the week','by six o\'clock','by this time tomorrow','by next summer','by the end of the month','by 2030','by the end of this year','by midnight']
FP_LEAD = ['By Friday,','By next year,','By the end of the week,','By six o\'clock,','By this time tomorrow,','By next summer,','By the end of the month,','By 2030,','By the time you arrive,','By the time the lesson starts,']
FPN_LEAD = ['By next June,','By Friday,','By the end of this year,','By 2030,','By six o\'clock,','By next summer,','By the end of the month,','By the time you arrive,','By this time next year,','By the end of the lesson,']
FPN_OK = set('play watch read write study work live cook clean walk run drive swim talk listen sing dance paint draw build wait teach practise learn travel wash repair prepare design discuss sweep bake download organise perform'.split())
FPN_NEAR = ['By six o\'clock,','By this time tomorrow,','By the end of the lesson,','By the time you arrive,','By midnight,','By lunchtime,']
FPN_FAR = ['By next June,','By 2030,','By the end of this year,','By next summer,','By this time next year,','By 2035,']
FPN_END = ['for two years','for ten years','for five hours','for three months','for a long time','for six weeks','for two hours','for twenty years','for eight hours','for a whole year']
FPC_END = ['tomorrow at six','on Saturday','next Friday','tonight','this weekend','next week','on Monday morning','at the weekend']

def cues(t, S, V, pol, rng, free=True):
    """return dict(lead, kind, pre, end). kind: none|sentence|clause"""
    c = dict(lead='', kind='none', pre='', end='')
    if t == 'ps':
        if pol == 'aff' and rng.pick([0,1]): c['pre'] = rng.pick(PS_PRE)
        else: c['end'] = rng.pick(PS_END)
    elif t == 'pc':
        if rng.pick([0,0,1]): c['lead'], c['kind'] = 'Look!', 'sentence'
        else: c['end'] = rng.pick(PC_END_FREE if free else PC_END)
    elif t == 'pas':
        c['end'] = rng.pick(PAS_D if V.dur else (PAS_E + PAS_D[:3]))
    elif t == 'pac':
        if rng.pick([0,1]): c['lead'], c['kind'] = rng.pick(PAC_LEAD), 'clause'
        else: c['end'] = rng.pick(PAC_END)
    elif t == 'pp':
        pool = {'aff': PP_AFF, 'neg': PP_NEG, 'q': PP_Q}[pol]
        if V.dur and rng.pick([0,1]): pool = PP_DUR if pol != 'q' else PP_Q
        c['end'] = rng.pick(pool)
        if V.ach and c['end'] in PP_DUR: c['end'] = 'so far'
    elif t == 'ppc':
        c['end'] = rng.pick(PPC_END)
    elif t == 'pap':
        c['end'] = rng.pick(PAP_END)
    elif t in ('fw','fg'):
        if t == 'fw' and pol != 'q' and rng.pick([0,0,1]): c['lead'], c['kind'] = rng.pick(['I think','Perhaps','I expect','I am sure']), 'clause'; c['lead'] += ','  if c['lead']=='Perhaps' else ''
        c['end'] = rng.pick(F_END)
    elif t == 'fpc':
        c['end'] = rng.pick(FPC_END)
    elif t == 'papn':
        c['end'] = rng.pick(PAPN_END) + ' ' + rng.pick(PAPN_CL) if rng.pick([0,1]) else rng.pick(PAPN_CL) + ', ' + 'x'
        if c['end'].endswith(', x'):
            c['lead'], c['kind'] = 'When ' + c['end'][5:-3] + ',', 'clause'; c['end'] = rng.pick(PAPN_END)
    elif t == 'fp':
        if rng.pick([0,1]): c['lead'], c['kind'] = rng.pick(FP_LEAD), 'clause'
        else: c['end'] = rng.pick(FP_END)
    elif t == 'fpn':
        far = (V.dur or V.base in ('live','study','work','teach','learn','practise','play','travel','paint','sing')) and rng.pick([0,1])
        c['kind'] = 'clause'
        if far: c['lead'], c['end'] = rng.pick(FPN_FAR), rng.pick(['for two years','for ten years','for six months','for three years','for a whole year','for five years'])
        else: c['lead'], c['end'] = rng.pick(FPN_NEAR), rng.pick(['for two hours','for three hours','for an hour','for four hours'])
    return c

def subj_text(S, kind): return S.text if kind in ('none','sentence') else S.mid

def aff(t, S, V, comp, c, group=None):
    g = group if group is not None else full_group(t,S,V,False)
    core = ' '.join(x for x in [subj_text(S,c['kind']), c['pre'], g, comp, c['end']] if x) + '.'
    s = (c['lead'] + ' ' + core) if c['lead'] else core
    return cap(s)

def neg(t, S, V, comp, c, group=None):
    g = group if group is not None else full_group(t,S,V,True)
    c2 = dict(c, pre='')
    return aff(t,S,V,comp,c2,g)

def ques(t, S, V, comp, c, aux=None, rest=None):
    a, r = qp(t,S,V)
    a = aux if aux is not None else a
    r = rest if rest is not None else r
    if c['kind'] == 'clause' and a != '___': a = a.lower()
    words = [a, S.mid, r, comp, c['end']]
    core = ' '.join(x for x in words if x) + '?'
    s = (c['lead'] + ' ' + core) if c['lead'] else core
    return cap(s) if not s.startswith('___') else s

def aux_list(t,S,V): return [qp(t,S,V)[0]]

def valid(t, V):
    if t in ('ppc','fpn','papn') and V.ach: return False
    if t in ('fpn','papn') and V.base not in FPN_OK: return False
    return True

# ---------- single-tense error generators ----------
def wrong(t, S, V, comp, c, pol, rng):
    """return a wrong version of the correct sentence for `pol` (aff/neg/q) or None"""
    cor = {'aff': aff, 'neg': neg, 'q': ques}[pol](t,S,V,comp,c)
    cands = []
    def sub(group_wrong, p=None):
        p = p or pol
        if p == 'aff': return aff(t,S,V,comp,c,group_wrong)
        if p == 'neg': return neg(t,S,V,comp,c,group_wrong)
    if t == 'ps':
        if pol == 'aff':
            cands.append(sub(V.base if S.sg else V.s))
            if S.sg: cands.append(sub(f"is {V.ing}") if False else sub(V.base))
        if pol == 'neg':
            if S.sg: cands += [sub(f"doesn't {V.s}"), sub(f"don't {V.base}")]
            else: cands += [sub(f"don't {V.s}"), sub(f"doesn't {V.base}")]
        if pol == 'q':
            if S.sg: cands += [ques(t,S,V,comp,c,'Does',V.s), ques(t,S,V,comp,c,'Do',V.base)]
            else: cands += [ques(t,S,V,comp,c,'Do',V.s), ques(t,S,V,comp,c,'Does',V.base)]
    elif t in ('pc','fpc'):
        b = be_pres(S); other = 'are' if b != 'are' else 'is'
        if pol == 'aff': cands += [sub(V.ing), sub(f"{other} {V.ing}"), sub(f"{b} {V.base}")]
        if pol == 'neg': cands += [sub(f"not {V.ing}"), sub(f"{other}n't {V.ing}"), sub(f"{b}n't {V.base}")]
        if pol == 'q': cands += [ques(t,S,V,comp,c,other.capitalize(),V.ing), ques(t,S,V,comp,c,b.capitalize(),V.base)]
    elif t == 'pas':
        if pol == 'aff':
            if V.past != V.base + 'ed' and V.past != V.base + 'd' and not V.past.endswith('ied'): cands += [sub(V.base + 'ed' if not V.base.endswith('e') else V.base + 'd')]
            cands.append(sub(V.s if S.sg else V.base))
        if pol == 'neg': cands += [sub(f"didn't {V.past}"), sub(f"don't {V.base}" if not S.sg else f"doesn't {V.base}")]
        if pol == 'q': cands += [ques(t,S,V,comp,c,'Did',V.past), ques(t,S,V,comp,c,'Do' if not S.sg else 'Does',V.base)]
    elif t == 'pac':
        b = be_past(S); other = 'were' if b == 'was' else 'was'
        if pol == 'aff': cands += [sub(f"{other} {V.ing}"), sub(f"{b} {V.base}"), sub(V.ing)]
        if pol == 'neg': cands += [sub(f"{other}n't {V.ing}"), sub(f"didn't {V.ing}")]
        if pol == 'q': cands += [ques(t,S,V,comp,c,other.capitalize(),V.ing), ques(t,S,V,comp,c,'Did',V.ing)]
    elif t == 'pp':
        h = have_pres(S); other = 'have' if h == 'has' else 'has'
        if pol == 'aff':
            cands += [sub(f"{h} {V.base}"), sub(f"{other} {V.pp}")]
            if V.past != V.pp: cands.append(sub(f"{h} {V.past}"))
        if pol == 'neg':
            cands += [sub(f"{h}n't {V.base}"), sub(f"{other}n't {V.pp}")]
            if V.past != V.pp: cands.append(sub(f"{h}n't {V.past}"))
        if pol == 'q':
            cands += [ques(t,S,V,comp,c,other.capitalize(),V.pp), ques(t,S,V,comp,c,h.capitalize(),V.base)]
            if V.past != V.pp: cands.append(ques(t,S,V,comp,c,h.capitalize(),V.past))
    elif t == 'ppc':
        h = have_pres(S); other = 'have' if h == 'has' else 'has'
        if pol == 'aff': cands += [sub(f"{h} {V.ing}"), sub(f"{other} been {V.ing}"), sub(f"{h} been {V.base}")]
        if pol == 'neg': cands += [sub(f"{h}n't {V.ing}"), sub(f"{other}n't been {V.ing}")]
        if pol == 'q': cands += [ques(t,S,V,comp,c,other.capitalize(),f"been {V.ing}"), ques(t,S,V,comp,c,h.capitalize(),V.ing)]
    elif t == 'pap':
        if pol == 'aff':
            cands += [sub(f"had {V.base}"), sub(f"has {V.pp}")]
            if V.past != V.pp: cands.append(sub(f"had {V.past}"))
        if pol == 'neg':
            cands += [sub(f"hadn't {V.base}"), sub(f"didn't had {V.pp}")]
        if pol == 'q':
            cands += [ques(t,S,V,comp,c,'Has',V.pp), ques(t,S,V,comp,c,'Had',V.base)]
    elif t == 'papn':
        if pol == 'aff': cands += [sub(f"had {V.ing}"), sub(f"{be_past(S)} {V.ing}"), sub(f"has been {V.ing}"), sub(f"had been {V.base}")]
        if pol == 'neg': cands += [sub(f"hadn't {V.ing}"), sub(f"hadn't been {V.base}"), sub(f"hasn't been {V.ing}")]
        if pol == 'q': cands += [ques(t,S,V,comp,c,'Had',V.ing), ques(t,S,V,comp,c,'Has',f"been {V.ing}"), ques(t,S,V,comp,c,'Had',f"been {V.base}")]
    elif t == 'fp':
        if pol == 'aff': cands += [sub(f"will {V.pp}"), sub(f"will have {V.base}"), sub(f"have {V.pp}")] + ([sub(f"will {V.base}")] if True else []) + ([sub(f"will have {V.past}")] if V.past != V.pp else [])
        if pol == 'neg': cands += [sub(f"won't {V.pp}"), sub(f"won't have {V.base}"), sub(f"haven't {V.pp}")] + ([sub(f"won't have {V.past}")] if V.past != V.pp else [])
        if pol == 'q': cands += [ques(t,S,V,comp,c,'Will',V.pp), ques(t,S,V,comp,c,'Will',f"have {V.base}"), ques(t,S,V,comp,c,'Have',V.pp) if True else None] + ([ques(t,S,V,comp,c,'Will',f"have {V.past}")] if V.past != V.pp else [])
    elif t == 'fpn':
        if pol == 'aff': cands += [sub(f"will have {V.ing}"), sub(f"will been {V.ing}"), sub(f"will have been {V.base}"), sub(f"will be {V.ing}")]
        if pol == 'neg': cands += [sub(f"won't have {V.ing}"), sub(f"won't been {V.ing}"), sub(f"won't have been {V.base}")]
        if pol == 'q': cands += [ques(t,S,V,comp,c,'Will',f"have {V.ing}"), ques(t,S,V,comp,c,'Will',f"been {V.ing}"), ques(t,S,V,comp,c,'Will',f"have been {V.base}")]
    elif t == 'fw':
        if pol == 'aff': cands += [sub(f"will {V.s}") if S.sg else sub(f"will {V.ing}"), sub(f"will to {V.base}"), sub(f"wills {V.base}")]
        if pol == 'neg': cands += [sub(f"won't {V.s}") if S.sg else sub(f"won't {V.ing}"), sub(f"don't {V.base}") if not S.sg else sub(f"doesn't {V.base}")]
        if pol == 'q': cands += [ques(t,S,V,comp,c,'Will',V.s) if S.sg else ques(t,S,V,comp,c,'Will',V.ing), ques(t,S,V,comp,c,'Do' if not S.sg else 'Does',V.base)]
    elif t == 'fg':
        b = be_pres(S); other = 'are' if b != 'are' else 'is'
        if pol == 'aff': cands += [sub(f"{b} going {V.base}"), sub(f"going to {V.base}"), sub(f"{other} going to {V.base}")]
        if pol == 'neg': cands += [sub(f"{b}n't going {V.base}"), sub(f"{other}n't going to {V.base}")]
        if pol == 'q': cands += [ques(t,S,V,comp,c,b.capitalize(),f"going {V.base}"), ques(t,S,V,comp,c,other.capitalize(),f"going to {V.base}")]
    cands = [x for x in cands if x and x != cor]
    return (rng.pick(cands), cor) if cands else None

# ---------- item generators ----------
def wh_info(t, V):
    if t == 'ps': return 'How often'
    if t == 'pas': return 'When'
    if t == 'pp': return 'How long' if V.dur else 'How many times'
    if t == 'ppc': return 'How long'
    if t in ('fw','fg'): return 'When'
    return None

def short_pron(S): return pron_ans(S)

def gen_item(t, level, rng, free=True):
    S = rng.pick(SUBJ); V = rng.pick(VERBS)
    if not valid(t,V): return None
    comp = rng.pick(V.comps)
    r = rng.r.random()
    pol = 'aff'
    # ---------------- easy ----------------
    if level == 'easy':
        if r < .55: pol = 'aff'
        elif r < .8: pol = 'neg'
        else: pol = 'q'
        c = cues(t,S,V,pol,rng,free)
        if pol == 'aff':
            q = aff(t,S,V,comp,c,f"___ ({V.base})"); return line(q, grp(t,S,V,False))
        if pol == 'neg':
            q = neg(t,S,V,comp,c,f"___ (not / {V.base})"); return line(q, grp(t,S,V,True))
        a,_r = qp(t,S,V); q = ques(t,S,V,comp,c,'___',_r); return line(q, [a])
    # ---------------- medium ----------------
    if level == 'medium':
        k = rng.pick(['q2','q2','short','short','tag','tag','wh','two','two','negq'])
        c = cues(t,S,V,'q',rng,free)
        if k == 'q2':
            a,_r = qp(t,S,V)
            c2 = cues(t,S,V,'q',rng,free)
            q = ques(t,S,V,comp,c2,'___',f"___ ({V.base})")
            return line(q,[a],[_r])
        if k == 'short':
            if S.kind == 'i': return None
            c = cues(t,S,V,'q',rng,free)
            qq = ques(t,S,V,comp,c)
            p = short_pron(S)
            yes = rng.pick([True,False])
            if yes: return line(f"{qq} Yes, {p} ___.", [short_aux(t,S)])
            return line(f"{qq} No, {p} ___.", negs(short_aux(t,S)))
        if k == 'tag':
            p = S.pron if S.pron != 'i' else 'I'
            if S.kind == 'i': return None
            c = cues(t,S,V,'aff',rng,free); c['pre'] = ''
            if c['kind'] == 'sentence': return None
            if rng.pick([True,False]):
                st = aff(t,S,V,comp,c)[:-1]; ans = negs(short_aux(t,S))
            else:
                c = cues(t,S,V,'neg',rng,free)
                if c['kind'] == 'sentence': return None
                st = neg(t,S,V,comp,c)[:-1]; ans = [short_aux(t,S)]
            return line(f"{st}, ___ {p}?", ans)
        if k == 'wh':
            w = wh_info(t,V)
            if not w: return None
            a,_r = qp(t,S,V)
            if t == 'pp' and w == 'How many times' and V.ach: pass
            q = ' '.join([w,'___',S.mid,f"___ ({V.base})",comp]) + '?'
            return line(q,[a.lower()],[_r])
        if k == 'two':
            S2 = rng.pick([x for x in SUBJ if x.text != S.text]); V2 = rng.pick(VERBS)
            if not valid(t,V2): return None
            comp2 = rng.pick(V2.comps)
            c = cues(t,S,V,'aff',rng,free); c['pre'] = ''
            if c['kind'] == 'sentence': return None
            sub1 = f"{subj_text(S,c['kind'])} ___ ({V.base}) {comp}"
            sub2 = f"{S2.mid if c['kind']!='none' or True else S2.text} ___ ({V2.base}) {comp2}"
            body = f"{sub1} and {sub2}"
            if c['end']: body += ' ' + c['end']
            q = (c['lead'] + ' ' + body if c['lead'] else body) + '.'
            q = cap(q)
            return line(q, grp(t,S,V,False), grp(t,S2,V2,False))
        if k == 'negq':
            c = cues(t,S,V,'neg',rng,free)
            q = neg(t,S,V,comp,c,f"___ (not / {V.base})")
            q2 = ques(t,S,V,comp,cues(t,S,V,'q',rng,free))
            # contrast: negative statement + question answered with blank aux
            return line(q, grp(t,S,V,True))
    # ---------------- hard ----------------
    k = rng.pick(['neg','q','fix','fix','fix','aff'])
    if k == 'neg':
        c = cues(t,S,V,'neg',rng,free); c['pre'] = ''
        if c['end'] in ('already',): return None
        s1 = aff(t,S,V,comp,c); ans = [neg(t,S,V,comp,c)]
        return line('Make a negative sentence: ' + s1, ans)
    if k == 'q':
        c = cues(t,S,V,'q',rng,free); c['pre'] = ''
        if c['end'] in ('already',) or c['kind'] == 'sentence': return None
        s1 = aff(t,S,V,comp,c); ans = [ques(t,S,V,comp,c)]
        return line('Make a question: ' + s1, ans)
    if k == 'aff':
        c = cues(t,S,V,'neg',rng,free)
        if c['kind'] == 'sentence' or c['end'] == 'yet': return None
        s1 = neg(t,S,V,comp,c); ans = [aff(t,S,V,comp,dict(c,pre=''))]
        return line('Make an affirmative sentence: ' + s1, ans)
    if k == 'neg2q':
        c = cues(t,S,V,'neg',rng,free); c['pre'] = ''
        if c['kind'] == 'sentence': return None
        s1 = neg(t,S,V,comp,c)
        return line('Make a question: ' + s1, [ques(t,S,V,comp,c)])  # negative -> positive question? keep simple: statement is negative
    # fix
    pol = rng.pick(['aff','neg','q'])
    c = cues(t,S,V,pol,rng,free)
    if pol != 'aff': c['pre'] = ''
    if c['end'] == 'already' and pol != 'aff': return None
    w = wrong(t,S,V,comp,c,pol,rng)
    if not w: return None
    return line('Correct the mistake: ' + w[0], [w[1]])

def gen_tense_topic(tid, t, counts, seed, free=True):
    rng = Rng(seed)
    out = {}
    for level, n in counts.items():
        seen, lines = set(), []
        tries = 0
        while len(lines) < n and tries < n * 80:
            tries += 1
            try: l = gen_item(t, level, rng, free)
            except AssertionError as e:
                raise
            if not l or bad_prompt(l): continue
            q = l.split(' => ')[0]
            if q in seen: continue
            seen.add(q); lines.append(l)
        out[level] = lines
    return out
