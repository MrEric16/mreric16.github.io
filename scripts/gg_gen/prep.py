from lib import *
from passive import gen_topic
NAMES = ["Tom","Anna","Aziz","Malika","Jasur","Dilnoza","Karim","Sara","Sardor","Dilya","Ali"]
# ---- time ----
ACT = [("gets up","get up"),("has lunch","have lunch"),("goes to bed","go to bed"),("starts work","start work"),("does homework","do homework"),("plays football","play football"),("studies English","study English"),("visits the grandparents","visit the grandparents"),("goes shopping","go shopping"),("has a meeting","have a meeting"),("calls a friend","call a friend"),("goes for a walk","go for a walk")]
ACT_PAST = [("started school","start school"),("moved house","move house"),("got a new job","get a new job"),("learned to swim","learn to swim"),("bought a bike","buy a bike"),("visited Dubai","visit Dubai"),("finished university","finish university"),("won a prize","win a prize")]
AT = ["6 o'clock","7.30","half past eight","noon","midnight","night","the weekend","Christmas","lunchtime","breakfast time","a quarter to nine","10.15"]
ON = ["Monday","Tuesday morning","Friday evening","Saturday","Sundays","her birthday","New Year's Day","the 5th of May","15 March","Wednesday afternoon","Thursday","the first of June"]
IN = ["January","March","the morning","the afternoon","the evening","summer","winter","spring","October","the holidays","the summer holidays","autumn"]
INY = ["2012","2015","2018","2019","1999","2020"]
XT = ["every day","next week","last Friday","tomorrow","this evening","every Monday","next month","last year","yesterday morning","this morning"]
def cap1(s): return s[0].upper()+s[1:]
def mood3(rng): return rng.pick(['aff','aff','neg','q'])
def tsent(name, act, tp, mood, past=False):
    v3, vb = act
    if past:
        # act = (past form, base)
        if mood == 'aff': return f"{name} {v3} {tp}."
        if mood == 'neg': return f"{name} didn't {vb} {tp}."
        return f"Did {name} {vb} {tp}?"
    if mood == 'aff': return f"{name} {v3} {tp}."
    if mood == 'neg': return f"{name} doesn't {vb} {tp}."
    return f"Does {name} {vb} {tp}?"
def gen_time(level, rng):
    mood = mood3(rng); name = rng.pick(NAMES)
    k = rng.pick(['at','at','on','on','in','in','iny','x'] if level != 'easy' else ['at','on','in','at','on','in','iny'])
    if k == 'iny': act = rng.pick(ACT_PAST); past = True; prep = 'in'; ph = rng.pick(INY)
    else:
        act = rng.pick(ACT); past = False
        if k == 'at': prep, ph = 'at', rng.pick(AT)
        elif k == 'on': prep, ph = 'on', rng.pick(ON)
        elif k == 'in': prep, ph = 'in', rng.pick(IN)
        else: prep, ph = 'x', rng.pick(XT)
    if k == 'x' and level == 'easy': return None
    full = (prep + ' ' + ph) if prep != 'x' else ph
    good = tsent(name, act, full, mood, past)
    blank = tsent(name, act, ('___ ' + ph) if prep != 'x' else ph.replace(ph, '___ ' + ph), mood, past)
    if k == 'x': blank = tsent(name, act, '___ ' + ph, mood, past)
    ans = XA if prep == 'x' else [prep]
    if level == 'easy': return line(blank + ' (at / on / in)', ans)
    if level == 'medium': return line(blank + ' (at / on / in / x)', ans) + '' if False else line(blank + ' (at / on / in / x = no preposition)', ans)
    kk = rng.pick(['fix','fix','fix','neg','q'])
    if kk == 'fix':
        wrongs = [p for p in ('at','on','in') if p != prep]
        w = rng.pick(wrongs)
        bad = tsent(name, act, (w + ' ' + ph) if prep != 'x' else (w + ' ' + ph), mood, past)
        return line('Correct the mistake: ' + bad, [good])
    if mood != 'aff': return None
    if kk == 'neg': return line('Make a negative sentence: ' + good, [tsent(name, act, full, 'neg', past)])
    return line('Make a question: ' + good, [tsent(name, act, full, 'q', past)])
XA = ['x','no preposition','nothing','none','zero']
# ---- place ----
PLACE_PRED = [("waiting ___ the bus stop","at"),("standing ___ the door","at"),("standing ___ the corner of the street","at"),("sleeping ___ bed","in"),("working ___ the garden","in"),("having dinner ___ home","at"),("talking ___ the phone","on"),("looking ___ the mirror","in"),
 ("hanging ___ the wall","on"),("lying ___ the floor","on"),("swimming ___ the sea","in"),("lying ___ the beach","on"),("sitting ___ the back of the bus","at"),("travelling ___ the bus","on"),("sitting ___ the car","in"),("living ___ the fourth floor","on"),
 ("waiting ___ the traffic lights","at"),("working ___ a computer","on"),("standing ___ the queue","in"),("watching a film ___ TV","on"),("playing ___ the garden","in"),("swimming ___ the pool","in"),("relaxing ___ the sofa","on"),("waiting ___ the entrance","at"),
 ("sleeping ___ the sofa","on"),("singing ___ the shower","in"),("writing ___ the board","on"),("standing ___ the window","at"),("sitting ___ the kitchen","in"),("studying ___ home","at"),("working ___ the third floor","on"),("sitting ___ the front row","in"),("sitting ___ the train","on"),("waiting ___ the gate","at"),("cooking ___ the kitchen","in")]
def gen_place(level, rng):
    mood = mood3(rng); name = rng.pick(NAMES)
    rel = rng.pick([0,1,1,2])
    if rel == 2 and level != 'easy':
        R = [("in front of",["behind"]),("behind",["in front of"]),("above",["below","under","beneath"]),("below",["above","over"]),("on",["under","below","beneath"]),("under",["on","above","over"])]
        a, bl = rng.pick(R)
        o1 = rng.pick(["ball","bag","cat","dog","box","lamp","book","bike"])
        o2 = rng.pick(["chair","sofa","table","bed","desk","shelf","door","car","wardrobe"]) if a in ("in front of","behind") else rng.pick(["chair","sofa","table","bed","desk","shelf"])
        s1 = f"The {o1} is {a} the {o2}."
        s2 = f"The {o2} is ___ the {o1}."
        if level == 'medium': return line(f"{s1} {s2} (in front of / behind / above / below / on / under)", bl)
        allp = ['in front of','behind','above','below','on','under','beneath','over']
        ok = set(bl) | ({'on','above','over','under','below','beneath'} if a not in ('in front of','behind') else set())
        wr = rng.pick(['above','below','on','under'] if a in ('in front of','behind') else ['in front of','behind'])
        return line('Correct the mistake: ' + f"{s1} The {o2} is {wr} the {o1}.", [f"{s1} The {o2} is {x} the {o1}." for x in bl])
    pred, p = rng.pick(PLACE_PRED)
    be = 'is'
    if mood == 'aff': good = f"{name} is {pred}."
    elif mood == 'neg': good = f"{name} isn't {pred}."
    else: good = f"Is {name} {pred}?"
    q = good
    fill = lambda x: good.replace('___', x)
    if level != 'hard': return line(q + ' (at / in / on)', [p])
    kk = rng.pick(['fix','fix','fix','neg','q'])
    if kk == 'fix':
        w = rng.pick([x for x in ('at','in','on') if x != p])
        return line('Correct the mistake: ' + fill(w), [fill(p)])
    if mood != 'aff': return None
    if kk == 'neg': return line('Make a negative sentence: ' + fill(p), [f"{name} isn't {pred.replace('___', p)}."])
    return line('Make a question: ' + fill(p), [f"Is {name} {pred.replace('___', p)}?"])
# ---- movement ----
MOVE = [("walk","walked","___ the tunnel",["through"],"from one end to the other"),("swim","swam","___ the river",["across"],"from one bank to the other"),("drive","drove","___ the bridge",["over","across"],"from one side to the other"),
        ("walk","walked","___ the street",["along","down"],"in the same direction as the street"),("climb","climbed","___ the stairs",["up"],"to a higher level"),("come","came","___ the stairs",["down"],"to a lower level"),
        ("walk","walked","___ the room",["into","in"],"from outside to inside"),("come","came","___ the room",["out of"],"from inside to outside"),("jump","jumped","___ the pool",["into","in"],"from outside to inside"),("jump","jumped","___ the wall",["over"],"to the other side"),
        ("get","got","___ the car",["into","in"],"from outside to inside"),("get","got","___ the taxi",["out of"],"from inside to outside"),("walk","walked","___ the tree",["around","round"],"in a circle"),("walk","walked","___ the forest",["through"],"between the trees, from one side to the other"),
        ("fly","flew","___ the mountains",["over"],"high above them"),("run","ran","___ the hill",["up"],"to the top"),("run","ran","___ the hill",["down"],"to the bottom"),("walk","walked","___ the corridor",["along","down"],"in the same direction as the corridor"),
        ("sail","sailed","___ the lake",["across"],"from one side to the other"),("go","went","___ the tower",["up"],"to the top"),("walk","walked","___ the door",["through"],"from one side to the other"),("drive","drove","___ the tunnel",["through"],"from one end to the other"),
        ("climb","climbed","___ the tree",["up"],"to the top"),("crawl","crawled","___ the table",["under"],"below it"),("jump","jumped","___ the fence",["over"],"to the other side"),("swim","swam","___ the pool",["across"],"from one side to the other")]
EQ = {'over':{'across'},'across':{'over'},'along':{'down','up'},'down':{'along'},'into':{'in'},'in':{'into'},'around':{'round'},'through':set(),'up':{'along'},'under':set(),'out of':set()}
def gen_move(level, rng):
    vb, vp, rest, ans, gloss = rng.pick(MOVE); mood = mood3(rng)
    sub = rng.pick(NAMES + ["My brother","My sister","The boy","The girl","Our teacher","Our neighbour","The children","My parents","The tourists","The little cat"])
    name = sub
    mid = sub if sub in NAMES else sub[0].lower() + sub[1:]
    if mood == 'aff': tmpl = f"{name} {vp} {rest}."
    elif mood == 'neg': tmpl = f"{name} didn't {vb} {rest}."
    else: tmpl = f"Did {mid} {vb} {rest}?"
    g = f" ({gloss})"
    if level == 'easy': return line(tmpl + g, ans)
    if level == 'medium': return line(tmpl + g + ' (to / into / out of / through / across / along / over / under / up / down / around)', ans)
    wrong_pool = ['through','across','along','up','down','into','out of','over','under','around']
    ok = set(ans)
    for a in ans: ok |= EQ.get(a, set())
    cand = [w for w in wrong_pool if w not in ok]
    w = rng.pick(cand)
    return line('Correct the mistake' + g + ': ' + tmpl.replace('___', w), [tmpl.replace('___', a) for a in ans])
def gen_prep_jobs(C):
    return {'prepositions-of-time': lambda: gen_topic(gen_time, C, 97),
            'prepositions-of-place': lambda: gen_topic(gen_place, C, 98),
            'prepositions-of-movement': lambda: gen_topic(gen_move, C, 99)}
