from lib import *
from passive import gen_topic
from linkers import CONTRAST
import re as _re
NAMES = [("Tom","he","him","his"),("Aziz","he","him","his"),("Jasur","he","him","his"),("Karim","he","him","his"),("Anna","she","her","her"),("Malika","she","her","her"),("Dilnoza","she","her","her"),("Sara","she","her","her"),
         ("My brother","he","him","his"),("My sister","she","her","her"),("Our teacher","she","her","her"),("My dad","he","him","his")]
N2 = ["two","three","four","five","six","ten"]
def fix(s): return _re.sub(r'\s+', ' ', s).replace(' ,', ',').replace(' .', '.').replace(' ?', '?').strip()
def lc(n): return n[0].lower() + n[1:] if n.split()[0] in ('My','Our') else n
def cap(s): return s[0].upper() + s[1:]
TOO = [("soup","hot","eat"),("bag","heavy","carry"),("exam","difficult","pass"),("box","big","lift"),("book","difficult","understand"),("writing","small","read"),("car","expensive","buy"),
 ("problem","hard","solve"),("task","long","finish"),("question","hard","answer"),("test","easy","fail"),("tea","hot","drink"),("coat","small","wear"),("song","fast","sing"),("film","scary","watch")]
TOO_P = [("I","me"),("he","him"),("she","her"),("we","us"),("they","them")]
CMP = [("tall","taller"),("old","older"),("fast","faster"),("strong","stronger"),("young","younger"),("cheap","cheaper"),("heavy","heavier"),("big","bigger"),("busy","busier"),("early","earlier"),("clever","cleverer"),("quiet","quieter")]
UNL = [("study hard","fail the exam"),("hurry up","miss the bus"),("wear a coat","get cold"),("leave now","be late"),("water the plant","lose it"),("eat breakfast","feel hungry"),("practise every day","not improve"),("go to bed early","feel tired tomorrow"),("take an umbrella","get wet"),("revise the words","forget them"),("start now","not finish on time"),("save some money","not afford the trip")]
PASS = [("cancelled","cancelled","match"),("built","built","bridge"),("painted","painted","wall"),("stole","stolen","car"),("broke","broken","window"),("wrote","written","letter"),("sent","sent","parcel"),
 ("cleaned","cleaned","room"),("repaired","repaired","road"),("opened","opened","shop"),("closed","closed","school"),("destroyed","destroyed","house"),("invited","invited","guest"),("won","won","prize"),("found","found","wallet")]
REP = ["finish the report","call the doctor","visit the museum","bring the book","fix the bike","clean the kitchen","write the email","buy some bread","help with the project","send the photos"]
WISH = [("have a bigger flat","had a bigger flat"),("live near the sea","lived near the sea"),("speak Chinese","spoke Chinese"),("know the answer","knew the answer"),("play the guitar","played the guitar"),("have a car","had a car"),("have more time","had more time"),("live in London","lived in London"),("know her number","knew her number")]
DED = ["at home","in the library","very tired","in the kitchen","at work","asleep","very happy","ill","on the bus","angry"]
ADV = ["see a doctor","study harder","take a taxi","wait a little","buy a new phone","get more sleep","call the police","drink more water"]
def structures(rng):
    return ['has','used','usedq','too','notas','unless','passive','reported','wish','must','cant','despite','advised']
def gen_kw(level, rng):
    st = rng.pick(['has','has','used','usedq','too','too','notas','unless','passive','passive','reported','wish','must','cant','despite','despite','advised'])
    hard_only = ('unless','passive','reported','wish','despite','advised','usedq','must','cant')
    if level == 'hard' and st not in hard_only and rng.pick([0,0,1]): return None
    n, sp, so, sposs = rng.pick(NAMES)
    if st == 'has':
        V = rng.pick([v for v in VERBS if v.dur]); c = rng.pick(V.comps); k = rng.pick(N2)
        s1 = f"{n} started {V.ing} {c} {k} years ago."; key = 'HAS'
        vs = [(f"{n} has", f"{V.pp} {c}", f"for {k} years.")]
        pre, mid, post = f"{n}", f"has {V.pp}", f"{c} for {k} years."
        vs = [(pre, mid, post)]
    elif st == 'used':
        V = rng.pick(VERBS); c = rng.pick(V.comps)
        s1 = f"{n} {V.past} {c} every day when {sp} was younger."; key = 'USED'
        vs = [(f"{n}", f"used to {V.base}", f"{c} every day when {sp} was younger.")]
    elif st == 'usedq':
        V = rng.pick(VERBS); c = rng.pick(V.comps)
        s1 = f"Did {n[0].lower() + n[1:] if n.split()[0] in ('My','Our') else n} {V.base} {c} when {sp} was a child?"; key = 'USE'
        nn = n[0].lower() + n[1:] if n.split()[0] in ('My','Our') else n
        vs = [(f"Did {nn}", f"use to {V.base}", f"{c} when {sp} was a child?")]
    elif st == 'too':
        th, adj, vb = rng.pick(TOO); a, b = rng.pick(TOO_P)
        s1 = f"The {th} is so {adj} that {a} can't {vb} it."; key = 'TOO'
        vs = [(f"The {th} is", f"too {adj} for {b}", f"to {vb}.")]
    elif st == 'notas':
        adj, comp = rng.pick(CMP)
        x, y = rng.pick([nm for nm in NAMES if nm[0] not in ('My brother','My sister','Our teacher','My dad')]), None
        y = rng.pick([nm for nm in NAMES if nm[0] != x[0] and nm[0] not in ('My brother','My sister','Our teacher','My dad')])
        s1 = f"{x[0]} is {comp} than {y[0]}."; key = 'AS'
        vs = [(f"{y[0]}", f"isn't as {adj}", f"as {x[0]}."), (f"{y[0]}", f"is not as {adj}", f"as {x[0]}.")]
    elif st == 'unless':
        a, b = rng.pick(UNL); sub = rng.pick(['you','we','they'])
        mod = rng.pick(['will','will']); 
        bb = b.replace('not ', "", 1) if b.startswith('not ') else b
        neg = b.startswith('not ')
        s1 = f"If {sub} don't {a}, {sub} {'won' + chr(39) + 't' if neg else 'will'} {bb}."; key = 'UNLESS'
        mv = "won't" if neg else "will"
        vs = [(f"{cap(sub)} {mv} {bb}", f"unless {sub}", f"{a}."), (f"Unless {sub} {a},", f"{sub} {mv}", f"{bb}.")]
    elif st == 'passive':
        pa, pp, ob = rng.pick(PASS)
        s1 = f"They {pa} the {ob}."; key = 'WAS'
        vs = [(f"The {ob}", f"was {pp}", ".")]
    elif st == 'reported':
        vp = rng.pick(REP)
        s1 = f"\"I will {vp},\" {lc(n)} said to me."; key = 'TOLD'
        vs = [(f"{n}", f"told me", f"{sp} would {vp}."), (f"{n}", f"told me that", f"{sp} would {vp}.")]
    elif st == 'wish':
        ph, wi = rng.pick(WISH)
        who = rng.pick([("I","I","I'm","wish"),(n,sp,f"{n} is","wishes")]) 
        sub, pr, be, wv = who
        dont = "don't" if sub == 'I' else "doesn't"
        s1 = f"{be} sorry {pr} {dont} {ph}."; key = 'WISH'
        if sub != 'I': s1 = f"{n} is sorry {sp} doesn't {ph}."
        vs = [(f"{sub}", f"{wv}", f"{pr} {wi}.")]
    elif st == 'must':
        d = rng.pick(DED)
        s1 = f"I'm sure {lc(n)} is {d}."; key = 'MUST'
        vs = [(f"{n}", "must be", f"{d}.")]
    elif st == 'cant':
        d = rng.pick(DED)
        s1 = f"I'm sure {lc(n)} isn't {d}."; key = "CAN'T"
        vs = [(f"{n}", "can't be", f"{d}."), (f"{n}", "cannot be", f"{d}.")]
    elif st == 'despite':
        A, N, B, Q = rng.pick(CONTRAST)
        if A[0].isupper() or _re.match(r'(he|she|they) ', B): pass
        s1 = f"Although {A}, {B}."; key = 'DESPITE'
        vs = [("Despite", N + ",", f"{B}."), ("In spite of", N + ",", f"{B}.")]
    else:
        ad = rng.pick(ADV)
        s1 = f"\"You should {ad},\" {lc(n)} said to me."; key = 'ADVISED'
        vs = [(f"{n}", "advised me", f"to {ad}.")]
    fulls = [fix(f"{p} {m} {q}") for p, m, q in vs]
    p0, m0, q0 = vs[0]
    if level == 'easy':
        gap = fix(f"{p0} ___ {q0}")
        return line(f"Complete the second sentence: {s1} = {gap} ({key})", [m0] + [v[1] for v in vs[1:]])
    return line(f"Rewrite using the word {key}: {s1}", fulls)
def gen_kw_jobs(C):
    return {'key-word-transformations': lambda: gen_topic(gen_kw, C, 143)}
