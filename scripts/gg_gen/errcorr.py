from lib import *
from passive import gen_topic
import depprep
SUBJE = [Subj('I','i','i'),Subj('You','you','you'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),
 Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('My brother','sg','he'),Subj('Our teacher','sg','she'),Subj('My parents','pl','they'),Subj('The students','pl','they')]
def _be(S): return 'am' if S.kind == 'i' else ('is' if S.kind == 'sg' else 'are')
ART_V = ["umbrella","engineer","apple","orange","idea","egg","exam","email","actor","artist","uncle","elephant","answer","office"]
ART_C = ["car","book","house","teacher","phone","bag","film","doctor","table","city","student","song"]
ART_T = [("hour","an"),("university","a"),("European city","a"),("honest man","an"),("one-day trip","a")]
UNC = ["water","money","time","homework","advice","information","traffic","furniture","luggage","rice","news"]
CNT = ["books","students","chairs","friends","cars","apples","tickets","mistakes","questions","pictures","rooms"]
CMPW = [("more big","bigger"),("more easy","easier"),("more fast","faster"),("more cheap","cheaper"),("more old","older"),("more hot","hotter"),("more tall","taller"),("gooder","better"),("more bad","worse"),("beautifuller","more beautiful"),("more expensive","more expensive")]
CONF = [("The dog wagged it's tail.","The dog wagged its tail.","it's","its"),("Their going to the park.","They're going to the park.","Their","They're"),
 ("Your late for the lesson.","You're late for the lesson.","Your","You're"),("She is taller then her sister.","She is taller than her sister.","then","than"),
 ("I have to many books.","I have too many books.","to many","too many"),("Please put the books over their.","Please put the books over there.","their","there"),
 ("He did good on the test.","He did well on the test.","good","well"),("I should of called you.","I should have called you.","should of","should have"),
 ("We could of won the match.","We could have won the match.","could of","could have"),("Who's bag is this?","Whose bag is this?","Who's","Whose"),
 ("The weather effects my mood.","The weather affects my mood.","effects","affects"),("I lost my keys, and I can't find it.","I lost my keys, and I can't find them.","it","them"),
 ("He suggested to go home.","He suggested going home.","to go","going"),("She enjoys to read novels.","She enjoys reading novels.","to read","reading"),
 ("I'm agree with you.","I agree with you.","I'm agree","I agree"),("We discussed about the plan.","We discussed the plan.","discussed about","discussed")]
WH = ["Where","Why","When"]
def build(rng):
    k = rng.pick(['sv','sv','past','art','art','mm','neg2','cmp','prep','prep','wo','wo','conf','conf'])
    S = rng.pick(SUBJE)
    if k == 'sv':
        V, comp = vcomp(rng)
        if S.kind in ('i','you','pl'): wrong_v, right_v = V.s, V.base
        else: wrong_v, right_v = V.base, V.s
        t = rng.pick(['every day','every week','on Sundays','after school'])
        return dict(right=f"{S.text} {right_v} {comp} {t}.", wrong=f"{S.text} {wrong_v} {comp} {t}.", rt=right_v, wt=wrong_v)
    if k == 'past':
        V, comp = vcomp(rng); t = rng.pick(['yesterday','last week','two days ago','last night'])
        sent = lambda v: f"{S.text} {v} {comp} {t}." if t.startswith(('yester','last')) is False else f"{S.text} {v} {comp} {t}."
        return dict(right=f"{S.text} {V.past} {comp} {t}.", wrong=f"{S.text} {V.base} {comp} {t}.", rt=V.past, wt=V.base)
    if k == 'art':
        if rng.pick([0,0,1]):
            n, a = rng.pick(ART_T); w = 'a' if a == 'an' else 'an'
            ph = rng.pick([f"{S.text} waited for {{}} {n}.", f"{S.text} saw {{}} {n}."]) if n != 'hour' else f"{S.text} waited for {{}} {n}."
        else:
            if rng.pick([0,1]): n = rng.pick(ART_V); a, w = 'an', 'a'
            else: n = rng.pick(ART_C); a, w = 'a', 'an'
            ph = rng.pick([f"{S.text} bought {{}} {n}.", f"{S.text} wants {{}} {n}.", f"{S.text} found {{}} {n} yesterday."])
        if 'wants' in ph and S.sg is False: ph = ph.replace('wants','want')
        return dict(right=ph.format(a), wrong=ph.format(w), rt=f"{a} {n}", wt=f"{w} {n}")
    if k == 'mm':
        if rng.pick([0,1]):
            n = rng.pick(UNC); fr = rng.pick([f"There isn't {{}} {n} in the bottle.", f"How {{}} {n} do you have?", f"We don't have {{}} {n}."])
            if fr.startswith('There'): fr = f"There isn't {{}} {n} left."
            r, w = ('much','many')
        else:
            n = rng.pick(CNT); fr = rng.pick([f"There aren't {{}} {n} in the room.", f"How {{}} {n} do you have?", f"We don't have {{}} {n}."]); r, w = ('many','much')
        return dict(right=fr.format(r), wrong=fr.format(w), rt=f"{r} {n}", wt=f"{w} {n}")
    if k == 'neg2':
        V, comp = vcomp(rng); d = 'doesn' if S.sg else 'don'
        o = rng.pick([('anybody','nobody'),('anything','nothing'),('anywhere','nowhere')])
        if S.text == 'I': d = 'don'
        if o[0] == 'anybody': r = f"{S.text} {d}'t know anybody here."; w = f"{S.text} {d}'t know nobody here."
        elif o[0] == 'anything': r = f"{S.text} {d}'t have anything to eat."; w = f"{S.text} {d}'t have nothing to eat."
        else: r = f"{S.text} {d}'t go anywhere at the weekend."; w = f"{S.text} {d}'t go nowhere at the weekend."
        return dict(right=r, wrong=w, rt=o[0], wt=o[1])
    if k == 'cmp':
        w, r = rng.pick([c for c in CMPW if c[0] != c[1]])
        O = rng.pick(['Anna','Tom','Malika','Aziz']); P = rng.pick([x for x in ['Anna','Tom','Malika','Aziz'] if x != O])
        adj = {'more big':'big','more easy':'easy','more fast':'fast','more cheap':'cheap','more old':'old','more hot':'hot','more tall':'tall','gooder':'good','more bad':'bad','beautifuller':'beautiful'}[w]
        if w == 'beautifuller': fr = f"{O}'s dress is {{}} than {P}'s."
        elif w in ('gooder','more bad'): fr = f"{O}'s marks are {{}} than {P}'s."
        else: fr = f"{O} is {{}} than {P}."
        return dict(right=fr.format(r), wrong=fr.format(w), rt=r, wt=w)
    if k == 'prep':
        if rng.pick([0,1]):
            adj, ok, objs = rng.pick(depprep.ADJ); obj = rng.pick(objs); w = depprep._pick_wrong(rng, ok); b = _be(S)
            return dict(right=f"{S.text} {b} {adj} {ok[0]} {obj}.", wrong=f"{S.text} {b} {adj} {w} {obj}.", rt=f"{adj} {ok[0]}", wt=f"{adj} {w}")
        b0, s3, pa, ok, objs = rng.pick(depprep.VERB); obj = rng.pick(objs); w = depprep._pick_wrong(rng, ok)
        return dict(right=f"{S.text} {pa} {ok[0]} {obj} last week.", wrong=f"{S.text} {pa} {w} {obj} last week.", rt=f"{pa} {ok[0]}", wt=f"{pa} {w}")
    if k == 'wo':
        if S.text == 'I': return None
        V, comp = vcomp(rng); wh = rng.pick(WH); b = _be(S); sm = S.mid
        return dict(right=f"{wh} {b} {sm} {V.ing} {comp}?", wrong=f"{wh} {sm} {b} {V.ing} {comp}?", rt=f"{b} {sm}", wt=f"{sm} {b}")
    w, r, wt, rt = rng.pick(CONF)
    return dict(right=r, wrong=w, rt=rt, wt=wt)
def gen_ec(level, rng):
    d = build(rng)
    if not d or d['wrong'] == d['right']: return None
    if level == 'easy':
        if d['rt'] not in d['right']: return None
        q = d['right'].replace(d['rt'], '___', 1)
        opts = [d['rt'], d['wt']]; rng.shuffle(opts)
        return line(f"{q} ({opts[0]} / {opts[1]})", [d['rt']])
    if level == 'medium':
        return line(f"Correct the mistake: {d['wrong']}", [d['right']])
    # hard: short text, one sentence wrong
    others = []
    for _ in range(6):
        o = build(rng)
        if o and o['wrong'] != o['right']: others.append(o)
        if len(others) == 2: break
    if len(others) < 2: return None
    sents = [d['wrong'], others[0]['right'], others[1]['right']]
    order = [0,1,2]; rng.shuffle(order)
    txt = ' '.join(f"({i+1}) {sents[o]}" for i, o in enumerate(order))
    return line(f"One sentence has a mistake. Write it correctly: {txt}", [d['right']])
def gen_ec_jobs(C):
    return {'error-correction': lambda: gen_topic(gen_ec, C, 144)}
