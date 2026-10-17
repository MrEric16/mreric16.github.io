from lib import *
from passive import gen_topic
from comp import NAMES, TH_KIND, COLORS, OPP_P, OPP_T, comp_of, PA, two_names, thing_ctx

# too table: (subject type, adj, infinitive phrase, opposite adj for enough)
TOO_P = [("tired","go out","energetic"),("young","drive a car","old"),("short","reach the shelf","tall"),("weak","lift the box","strong"),("nervous","speak in public","calm"),("busy","come to the party","free"),
         ("shy","talk to strangers","confident"),("sleepy","do homework","awake"),("slow","catch the bus","fast"),("scared","watch the film","brave"),("lazy","clean the room","active")]
ENO_P = [("tall","reach the shelf"),("old","drive a car"),("strong","lift the box"),("fast","catch the bus"),("brave","watch a horror film"),("clever","solve the puzzle"),("fit","run a marathon"),("rich","buy a flat"),("confident","speak in public"),("patient","wait for an hour"),("old","vote"),("calm","stay in the room")]
TOO_T = [("hot","drink"),("heavy","carry"),("expensive","buy"),("difficult","understand"),("cold","swim in"),("small","sit in"),("noisy","sleep in"),("far","walk to"),("dark","read in"),("crowded","enjoy")]
ENO_T = [("warm","swim in"),("big","sit in"),("quiet","sleep in"),("light","carry"),("cheap","buy"),("easy","understand"),("bright","read in"),("comfortable","sleep in")]
OBJ_T = {"hot":["the soup","the tea","the coffee"],"heavy":["the bag","the box","the suitcase"],"expensive":["the jacket","the laptop","the watch"],"difficult":["the text","the lesson","the rule"],"cold":["the sea","the river","the lake"],"small":["the car","the chair","the room"],"noisy":["the room","the hotel","the flat"],
         "far":["the school","the station","the shop"],"dark":["the room","the hall","the garden"],"crowded":["the bus","the market","the beach"],
         "warm":["the sea","the river","the lake"],"big":["the car","the chair","the room"],"quiet":["the room","the hotel","the flat"],"light":["the bag","the box","the suitcase"],"cheap":["the jacket","the laptop","the watch"],"easy":["the text","the lesson","the rule"],"bright":["the room","the hall","the kitchen"],"comfortable":["the bed","the sofa","the hotel"]}
# fix grammar: "too cold to swim in" etc. need subj and infinitive; build "<Obj> is too hot to drink."
TOO_TH = {"hot":"drink","heavy":"carry","expensive":"buy","difficult":"understand","cold":"swim in","small":"sit in","noisy":"sleep in","far":"walk to","dark":"read in","crowded":"enjoy"}
OPP_TE = {"hot":"cool","heavy":"light","expensive":"cheap","difficult":"easy","cold":"warm","small":"big","noisy":"quiet","far":"near","dark":"bright","crowded":"quiet"}
def p_aux(neg): return "isn't" if neg else "is"
def sent(subj, adj, tail, mood, word, nm=None):
    # word: 'too' -> "S is too ADJ tail"; 'enough' -> "S is ADJ enough tail"
    core = f"too {adj}" if word == 'too' else f"{adj} enough"
    if mood == 'aff': return f"{subj} is {core} {tail}."
    if mood == 'neg': return f"{subj} isn't {core} {tail}."
    s = subj[0].lower()+subj[1:] if subj.split()[0] in ('The','This') else subj
    return f"Is {s} {core} {tail}?"
def too_case(rng):
    if rng.pick([0,1]):
        a = rng.pick(NAMES); adj, inf, opp = rng.pick(TOO_P)
        return a, adj, 'to ' + inf, opp, 'P', None
    adj = rng.pick(list(TOO_TH)); o = rng.pick(OBJ_T[adj])
    inf = TOO_TH[adj]
    sub = o[0].upper()+o[1:]
    return sub, adj, 'to ' + inf, OPP_TE[adj], 'T', None
def enough_case(rng):
    if rng.pick([0,1]):
        a = rng.pick(NAMES); adj, inf = rng.pick(ENO_P)
        return a, adj, 'to ' + inf, None, 'P', None
    adj = rng.pick(list(ENO_TH)); o = rng.pick(OBJ_T[adj]); sub = o[0].upper()+o[1:]
    return sub, adj, 'to ' + ENO_TH[adj], None, 'T', None
ENO_TH = {"warm":"swim in","big":"sit in","quiet":"sleep in","light":"carry","cheap":"buy","easy":"understand","bright":"read in","comfortable":"sleep in"}
def mood3(rng): return rng.pick(['aff','aff','neg','q'])
def asas_sentence(A, B, adj, mood, so=False):
    as1 = 'so' if so else 'as'
    if mood == 'aff': return f"{A} is as {adj} as {B}."
    if mood == 'neg': return f"{A} isn't {as1} {adj} as {B}."
    a = A[0].lower()+A[1:] if A.split()[0] in ('The','This') else A
    return f"Is {a} as {adj} as {B}?"
def asas_case(rng):
    if rng.pick([0,1,1]):
        a,b = two_names(rng); base,comps,sups = rng.pick(PA)
        # as...as uses base: skip two-word adjectives fine
        return a, b, base, 'P'
    kind = rng.pick(list(TH_KIND)); nouns, adjs = TH_KIND[kind]; n = rng.pick(nouns); base,_,_ = rng.pick(adjs)
    if rng.pick([0,1]): return f"This {n}", f"that {n}", base, 'T'
    c1 = rng.pick(COLORS); c2 = rng.pick([c for c in COLORS if c != c1])
    return f"The {c1} {n}", f"the {c2} {n}", base, 'T'
def gen_asas(level, rng):
    mood = mood3(rng); A,B,adj,kind = asas_case(rng)
    q = asas_sentence(A, B, f"___ ({adj})", mood)
    good = asas_sentence(A, B, adj, mood)
    if level == 'easy': return line(q, [adj])
    k = rng.pick(['as','adj','fix','fix','opp','join','cmp'] if level == 'hard' else ['as','adj','adj'])
    if level == 'medium':
        if k == 'as':
            q2 = asas_sentence(A, B, adj, mood).replace(' as ', ' ___ ', 1) if mood == 'aff' else None
            if mood == 'aff': return line(good.replace(f" as {adj} as ", f" ___ {adj} as ", 1), ['as'])
            if mood == 'neg': return line(good.replace("n't as ", "n't ___ ", 1), ['as','so'])
            return line(good.replace("? ", "? ") .replace(f" as {adj} as ", f" ___ {adj} as ", 1), ['as'])
        return line(q, [adj])
    if k == 'as' or k == 'adj':
        if mood == 'aff': return line(good.replace(f" as {adj} as ", f" ___ {adj} ___ ", 1), ['as', 'as']) if False else line(good.replace(f" as {adj} as ", f" ___ {adj} as ", 1), ['as'])
        return line(q, [adj])
    if k == 'fix':
        bad = good.replace(f" as {adj} as ", f" as {adj} than ") if mood != 'neg' else good.replace(f" as {adj} as ", f" as {adj} than ")
        if mood == 'q': bad = good.replace(f" as {adj} as ", f" as {adj} than ")
        if bad == good: return None
        return line('Correct the mistake: ' + bad, [good] + ([good.replace("n't as ", "n't so ")] if mood == 'neg' else []))
    if k == 'opp':
        opp = (OPP_P if kind == 'P' else OPP_T).get(adj)
        if not opp or mood == 'q': return None
        B2 = B[0].upper()+B[1:]
        if mood == 'aff': base_s = f"{A} isn't as {opp} as {B}."; instr = f"Rewrite with the opposite adjective ({opp}): {good}"
        else: base_s = f"{A} is as {opp} as {B}."; instr = f"Rewrite with the opposite adjective ({opp}): {good}"
        # not strictly equivalent for aff->neg; keep only negative->? skip
        return None
    if k == 'join':
        if kind != 'P' or adj not in ('tall','old','young','short'): return None
        if mood != 'aff': return None
        n = rng.pick([150,160,170,180]) if adj in ('tall','short') else rng.pick([14,15,16,17])
        unit = f"{n} cm tall" if adj in ('tall','short') else f"{n}"
        return line(f"Join with 'as ... as' ({adj}): {A} is {unit}. {B[0].upper()+B[1:]} is {unit}.", [f"{A} is as {adj} as {B}."])
    if k == 'cmp':
        # comparative -> not as...as (aff only)
        if mood != 'aff': return None
        for x in PA:
            pass
        comp = comp_of(adj)
        if not comp: return None
        cap2 = lambda s: s[0].upper()+s[1:]
        return line(f"Rewrite with 'not as ... as': {A} is {comp[0]} than {B}. => ", [f"{B} isn't as {adj} as {A}."], [f"{cap2(B)} isn't as {adj} as {A}."]) if False else line(f"Rewrite with 'not as ... as': {cap2(B)} is {comp[0]} than {A}.", [f"{A} isn't as {adj} as {B}."])
    return None
def gen_te(level, rng):
    which = rng.pick(['too','enough','both'])
    mood = mood3(rng)
    if which == 'both' or (which == 'too'):
        sub, adj, tail, opp, kind, _ = too_case(rng); w = 'too'
        if which == 'both' and rng.pick([0,1]): sub, adj, tail, opp, kind, _ = (lambda c: (c[0], c[1], c[2], None, c[4], None))(enough_case(rng)); w = 'enough'
    else:
        sub, adj, tail, opp, kind, _ = enough_case(rng); w = 'enough'
    good = sent(sub, adj, tail, mood, w)
    if level == 'easy':
        if w == 'too': return line(sent(sub, adj, tail, mood, 'too').replace(f"too {adj}", f"___ {adj}", 1), ['too'])
        return line(sent(sub, adj, tail, mood, 'enough').replace(f"{adj} enough", f"{adj} ___", 1), ['enough'])
    if level == 'medium':
        if rng.pick([0,1]): return line(good.replace('too ', '___ ', 1).replace(f"{adj} enough", f"{adj} ___", 1), ['too' if w == 'too' else 'enough'])
        # choose by meaning: provide adjective hint
        if w == 'too': return line(sent(sub, f"___", tail, mood, 'too').replace(' too ___', f" too ___ ({adj})"), [adj]) if False else line(good.replace(f"too {adj}", f"too ___ ({adj})"), [adj])
        return line(good.replace(f"{adj} enough", f"___ ({adj}) enough"), [adj])
    k = rng.pick(['fix','fix','neg','q','opp'])
    if k == 'fix':
        if w == 'too': bad = good.replace(f"too {adj}", f"{adj} too"); 
        else: bad = good.replace(f"{adj} enough", f"enough {adj}")
        if bad == good: return None
        return line('Correct the mistake: ' + bad, [good])
    if k == 'neg':
        if mood != 'aff': return None
        return line('Make a negative sentence: ' + good, [sent(sub, adj, tail, 'neg', w)])
    if k == 'q':
        if mood != 'aff': return None
        return line('Make a question: ' + good, [sent(sub, adj, tail, 'q', w)])
    if k == 'opp':
        if w != 'too' or not opp or mood != 'aff': return None
        return line(f"Rewrite with 'enough' and the opposite adjective ({opp}): {good}", [sent(sub, opp, tail, 'neg', 'enough')])
    return None
def gen_asas_jobs(C):
    return {'as-as-too-and-enough': lambda: gen_topic(lambda lv, r: gen_asas(lv, r) if r.pick([0,1,1]) else gen_te(lv, r), C, 94)}
