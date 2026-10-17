from lib import *
from passive import gen_topic

# base, comparative(s), superlative(s)
PA = [("tall",["taller"],["tallest"]),("short",["shorter"],["shortest"]),("young",["younger"],["youngest"]),("old",["older"],["oldest"]),("strong",["stronger"],["strongest"]),
      ("fast",["faster"],["fastest"]),("slow",["slower"],["slowest"]),("funny",["funnier"],["funniest"]),("clever",["cleverer","more clever"],["cleverest","most clever"]),
      ("friendly",["friendlier","more friendly"],["friendliest","most friendly"]),("lazy",["lazier"],["laziest"]),("busy",["busier"],["busiest"]),("happy",["happier"],["happiest"]),
      ("fit",["fitter"],["fittest"]),("quiet",["quieter","more quiet"],["quietest","most quiet"]),("shy",["shyer","more shy"],["shyest","most shy"]),("careful",["more careful"],["most careful"]),
      ("intelligent",["more intelligent"],["most intelligent"]),("polite",["politer","more polite"],["politest","most polite"]),("patient",["more patient"],["most patient"]),
      ("confident",["more confident"],["most confident"]),("creative",["more creative"],["most creative"]),("generous",["more generous"],["most generous"]),("serious",["more serious"],["most serious"]),
      ("hard-working",["more hard-working"],["most hard-working"]),("energetic",["more energetic"],["most energetic"]),("popular",["more popular"],["most popular"]),("talkative",["more talkative"],["most talkative"])]
TH_KIND = {
 'veh':(["car","bike","scooter","motorbike"],[("fast",["faster"],["fastest"]),("slow",["slower"],["slowest"]),("old",["older"],["oldest"]),("new",["newer"],["newest"]),("big",["bigger"],["biggest"]),("small",["smaller"],["smallest"]),
        ("cheap",["cheaper"],["cheapest"]),("expensive",["more expensive"],["most expensive"]),("comfortable",["more comfortable"],["most comfortable"]),("modern",["more modern"],["most modern"]),("popular",["more popular"],["most popular"])]),
 'dev':(["phone","laptop","camera","watch","tablet"],[("new",["newer"],["newest"]),("old",["older"],["oldest"]),("small",["smaller"],["smallest"]),("big",["bigger"],["biggest"]),("cheap",["cheaper"],["cheapest"]),("expensive",["more expensive"],["most expensive"]),
        ("light",["lighter"],["lightest"]),("heavy",["heavier"],["heaviest"]),("modern",["more modern"],["most modern"]),("useful",["more useful"],["most useful"]),("popular",["more popular"],["most popular"])]),
 'clo':(["coat","bag","shirt","jacket","dress"],[("new",["newer"],["newest"]),("old",["older"],["oldest"]),("cheap",["cheaper"],["cheapest"]),("expensive",["more expensive"],["most expensive"]),("light",["lighter"],["lightest"]),("heavy",["heavier"],["heaviest"]),
        ("comfortable",["more comfortable"],["most comfortable"]),("big",["bigger"],["biggest"]),("small",["smaller"],["smallest"]),("beautiful",["more beautiful"],["most beautiful"]),("popular",["more popular"],["most popular"])]),
}
COLORS = ["red","blue","green","black","white","grey","yellow","brown"]
MODS = ["much","a lot","far","a bit","slightly"]
OPP_P = {"tall":"short","short":"tall","young":"old","old":"young","strong":"weak","fast":"slow","slow":"fast"}
OPP_T = {"expensive":"cheap","cheap":"expensive","heavy":"light","light":"heavy","big":"small","small":"big","new":"old","old":"new","fast":"slow","slow":"fast"}
def comp_of(adj):
    for k in list(TH_KIND.values()):
        for a in k[1]:
            if a[0]==adj: return a[1]
    for a in PA:
        if a[0]==adj: return a[1]
    if adj=="weak": return ["weaker"]
    return None
def sup_of(adj):
    for k in list(TH_KIND.values()):
        for a in k[1]:
            if a[0]==adj: return a[2]
    for a in PA:
        if a[0]==adj: return a[2]
    if adj=="weak": return ["weakest"]
NAMES = ["Tom","Anna","Aziz","Malika","Jasur","Dilnoza","Karim","Sara","Sardor","Dilya","Ali"]
IRR = [("good","better","best","student"),("bad","worse","worst","player")]
def pair(rng):
    a,b = rng.sample(NAMES,2) if hasattr(rng,'sample') else (rng.pick(NAMES), rng.pick([n for n in NAMES]))
    return a,b
def two_names(rng):
    a = rng.pick(NAMES); b = rng.pick([n for n in NAMES if n != a]); return a,b
def thing_ctx(rng):
    kind = rng.pick(list(TH_KIND)); nouns, adjs = TH_KIND[kind]
    n = rng.pick(nouns); adj = rng.pick(adjs)
    c1 = rng.pick(COLORS); c2 = rng.pick([c for c in COLORS if c != c1])
    return n, adj, c1, c2
def mood3(rng): return rng.pick(['aff','aff','neg','q'])
def cmp_sentence(A, B, adj_text, mood, mod=None):
    m = (mod + ' ') if mod else ''
    if mood == 'aff': return f"{A} is {m}{adj_text} than {B}."
    if mood == 'neg': return f"{A} isn't {m}{adj_text} than {B}."
    return f"Is {A[0].lower()+A[1:] if A.split()[0] in ('This','That','The') else A} {m}{adj_text} than {B}?"
def comp_ctx(rng):
    if rng.pick([0,1,1]):
        a,b = two_names(rng); adj = rng.pick(PA); return a, b, adj, 'P'
    n, adj, c1, c2 = thing_ctx(rng)
    if rng.pick([0,1]): return f"The {c1} {n}", f"the {c2} {n}", adj, 'T'
    return f"This {n}", f"that {n}", adj, 'T'
def mod_ok(rng, mood, level):
    return rng.pick(MODS) if (level != 'easy' and mood != 'q' and rng.pick([0,1,0])) else None
def gen_comp(level, rng):
    k = rng.pick(['reg','reg','reg','irr']) if level != 'easy' else 'reg'
    mood = mood3(rng)
    if k == 'irr':
        a,b = two_names(rng); g,c,s,n = rng.pick(IRR)
        if mood == 'aff': q = f"{a} is a ___ ({g}) {n} than {b}."
        elif mood == 'neg': q = f"{a} isn't a ___ ({g}) {n} than {b}."
        else: q = f"Is {a} a ___ ({g}) {n} than {b}?"
        if level != 'hard': return line(q, [c])
        wrong = {'better':'gooder','worse':'badder'}[c]
        return line('Correct the mistake: ' + q.replace(f"___ ({g})", wrong), [q.replace(f"___ ({g})", c)])
    A,B,adj,kind = comp_ctx(rng)
    base, comps, sups = adj
    mod = mod_ok(rng, mood, level)
    q = cmp_sentence(A, B, f"___ ({base})", mood, mod)
    good = cmp_sentence(A, B, comps[0], mood, mod)
    if level != 'hard': return line(q, comps)
    kk = rng.pick(['fix','fix','fix','neg','q','opp','facts'])
    if kk == 'fix':
        wrong = base if all(c.startswith('more ') for c in comps) else 'more ' + comps[0]
        bad = cmp_sentence(A, B, wrong, mood, mod)
        if bad == good or wrong in comps: return None
        return line('Correct the mistake: ' + bad, [cmp_sentence(A,B,c,mood,mod) for c in comps])
    if kk == 'neg':
        if mood != 'aff': return None
        return line('Make a negative sentence: ' + good, [cmp_sentence(A,B,c,'neg') for c in comps])
    if kk == 'q':
        if mood != 'aff': return None
        return line('Make a question: ' + good, [cmp_sentence(A,B,c,'q') for c in comps])
    if kk == 'opp':
        opp = (OPP_P if kind == 'P' else OPP_T).get(base)
        if not opp or mood != 'aff' or mod: return None
        oc = comp_of(opp)
        B2 = B[0].upper()+B[1:] if B.split()[0] in ('the','that') else B
        return line(f"{good} {B2} is ___ ({opp}) than {A[0].lower()+A[1:] if A.split()[0] in ('The','This') else A}.", oc)
    # facts
    if kind == 'P' and base in ('tall','old'):
        x = rng.pick([150,160,170,175,180,185]); y = x - rng.pick([5,10,15])
        if base == 'tall': f = f"{A} is {x} cm tall. {B[0].upper()+B[1:]} is {y} cm tall."
        else: x = rng.pick([14,15,16,17,18,19]); y = x - rng.pick([1,2,3]); f = f"{A} is {x}. {B[0].upper()+B[1:]} is {y}."
        return line(f"Write a sentence with a comparative ({base}): {f}", [f"{A} is {comps[0]} than {B}.", f"{B} is {comp_of(OPP_P[base])[0]} than {A}."])
    return None
def sup_frame(rng):
    return rng.pick([("student","in the class"),("student","in our group"),("player","in the team"),("person","in the family")])
def gen_sup(level, rng):
    mood = mood3(rng)
    if rng.pick([0,1,1]) and level != 'easy' or (level == 'easy' and rng.pick([0,1])):
        a = rng.pick(NAMES); n, ctx = sup_frame(rng)
        if rng.pick([0,0,1]) and level != 'easy':
            g,c,s,nn = rng.pick(IRR)
            pre = {'aff':f"{a} is the ___ ({g}) {nn} in the class.",'neg':f"{a} isn't the ___ ({g}) {nn} in the class.",'q':f"Is {a} the ___ ({g}) {nn} in the class?"}[mood]
            if level != 'hard': return line(pre, [s])
            wrong = {'best':'goodest','worst':'baddest'}[s]
            return line('Correct the mistake: ' + pre.replace(f"___ ({g})", wrong), [pre.replace(f"___ ({g})", s)])
        base, comps, sups = rng.pick(PA)
        def mk(x):
            if mood == 'aff': return f"{a} is the {x} {n} {ctx}."
            if mood == 'neg': return f"{a} isn't the {x} {n} {ctx}."
            return f"Is {a} the {x} {n} {ctx}?"
        q = mk(f"___ ({base})")
        if level != 'hard': return line(q, sups)
    else:
        kind = rng.pick(list(TH_KIND)); nouns, adjs = TH_KIND[kind]
        nn = rng.pick(nouns); base, comps, sups = rng.pick(adjs)
        lead = rng.pick(['This', 'That'])
        ctx = rng.pick(["in the showroom","in the whole showroom"]) if kind == 'veh' else rng.pick(["in the shop","in the shop window","in the whole shop"])
        def mk(x):
            if mood == 'aff': return f"{lead} {nn} is the {x} {ctx}."
            if mood == 'neg': return f"{lead} {nn} isn't the {x} {ctx}."
            return f"Is {lead.lower()} {nn} the {x} {ctx}?"
        q = mk(f"___ ({base})")
        if level != 'hard': return line(q, sups)
        a = lead + ' ' + nn
    kk = rng.pick(['fix','fix','fix','neg','q','facts'])
    good = mk(sups[0])
    if kk == 'fix':
        wrong = base if all(x.startswith('most ') for x in sups) else 'most ' + sups[0]
        if wrong in sups: return None
        bad = mk(wrong)
        if bad == good: return None
        return line('Correct the mistake: ' + bad, [mk(s) for s in sups])
    if kk == 'neg':
        if mood != 'aff': return None
        return line('Make a negative sentence: ' + good, [mk_m(mk, s, 'neg', good) for s in sups])
    if kk == 'q':
        if mood != 'aff': return None
        return line('Make a question: ' + good, [mk_m(mk, s, 'q', good) for s in sups])
    return None
def mk_m(mk, s, mood, good):
    # rebuild from the affirmative sentence
    if mood == 'neg': return good.replace(' is the ', " isn't the ").replace(sups_of_good(good), s) if False else good.replace(' is the ', " isn't the ", 1)
    parts = good.rstrip('.').split(' is the ', 1)
    subj = parts[0]; subj = subj[0].lower()+subj[1:] if subj.split()[0] in ('This','That') else subj
    return f"Is {subj} the {parts[1]}?"
def shop_of(kind): return 'showroom' if kind == 'veh' else 'shop'
def gen_comp_or_sup(level, rng):
    mood = mood3(rng); which = rng.pick(['c','s'])
    if rng.pick([0,1]):
        a,b = two_names(rng); base, comps, sups = rng.pick(PA); n, ctx = sup_frame(rng)
        if which == 'c': q = {'aff':f"{a} is ___ ({base}) than {b}.",'neg':f"{a} isn't ___ ({base}) than {b}.",'q':f"Is {a} ___ ({base}) than {b}?"}[mood]; ans = comps
        else: q = {'aff':f"{a} is the ___ ({base}) {n} {ctx}.",'neg':f"{a} isn't the ___ ({base}) {n} {ctx}.",'q':f"Is {a} the ___ ({base}) {n} {ctx}?"}[mood]; ans = sups
    else:
        kind = rng.pick(list(TH_KIND)); nouns, adjs = TH_KIND[kind]; nn = rng.pick(nouns); base, comps, sups = rng.pick(adjs)
        if which == 'c': q = {'aff':f"This {nn} is ___ ({base}) than that {nn}.",'neg':f"This {nn} isn't ___ ({base}) than that {nn}.",'q':f"Is this {nn} ___ ({base}) than that {nn}?"}[mood]; ans = comps
        else: sh = shop_of(kind); q = {'aff':f"This {nn} is the ___ ({base}) in the {sh}.",'neg':f"This {nn} isn't the ___ ({base}) in the {sh}.",'q':f"Is this {nn} the ___ ({base}) in the {sh}?"}[mood]; ans = sups
    if level == 'easy': return line(q, ans)
    if level == 'medium':
        # no 'than' / 'the' clue removed: blank includes the article for superlatives
        if which == 's': return line(q.replace('the ___', '___'), ['the ' + a for a in ans])
        return line(q, ans)
    # hard: choose between the two forms
    c0, s0 = comps[0], sups[0]
    if which == 'c':
        return line(q.replace(f"___ ({base})", f"___ ({base})") if False else 'Correct the mistake: ' + q.replace(f"___ ({base})", s0), [q.replace(f"___ ({base})", c) for c in comps])
    return line('Correct the mistake: ' + q.replace(f"the ___ ({base})", c0), [q.replace(f"___ ({base})", s) for s in sups])
def gen_comp_jobs(C):
    return {'comparatives': lambda: gen_topic(gen_comp, C, 91),
            'superlatives': lambda: gen_topic(gen_sup, C, 92),
            'comparatives-or-superlatives': lambda: gen_topic(gen_comp_or_sup, C, 93)}
