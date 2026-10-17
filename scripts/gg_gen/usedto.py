from lib import *
from passive import gen_topic
SG = [Subj('I','i','i'),Subj('You','you','you'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('My brother','sg','he'),Subj('My sister','sg','she'),Subj('My parents','pl','they'),Subj('The students','pl','they')]
STATES = [("have","a small flat"),("have","long hair"),("be","very shy"),("be","good at swimming"),("live","in a village"),("like","spicy food"),("have","a dog"),("be","afraid of the dark"),("have","a bike"),("know","everybody in the street"),("be","keen on football"),("own","an old car")]
ACTS = [("play","football after school"),("walk","to school with friends"),("visit","the grandparents every summer"),("go","swimming on Sundays"),("read","comics every night"),("eat","ice cream after dinner"),("ride","a bike to school"),("watch","cartoons on Saturday mornings"),("sing","in the school choir"),("draw","pictures all day"),("collect","stamps"),("catch","the bus to school")]
def cue(S):
    if S.pron == 'i': return "when I was a child"
    if S.pron == 'you': return "when you were a child"
    if S.pron in ('he','she'): return f"when {S.pron} was a child"
    return "when " + ("we" if S.pron == 'we' else "they") + " were children"
def agr(S, verb):
    return verb
def forms(S, v, rest, mood, mode):
    c = cue(S)
    if mode == 'used':
        if mood == 'aff': return f"{S.text} used to {v} {rest} {c}."
        if mood == 'neg': return f"{S.text} didn't use to {v} {rest} {c}."
        return f"Did {S.mid} use to {v} {rest} {c}?"
    return None
def bev(S): return 'was' if S.kind in ('i','sg') else 'were'
def gen_used(level, rng):
    S = rng.pick(SG); mood = rng.pick(['aff','aff','neg','q'])
    fam = rng.pick(['used','used','would','beused','getused'])
    if fam == 'used' or (fam == 'would' and False):
        st = rng.pick([0,1])
        v, rest = rng.pick(STATES if st else ACTS)
        if v == 'be' and S.pron == 'i': pass
        # 'be' states: "used to be", ok for all
        good = forms(S, v, rest, mood, 'used')
        hint = f"({v})"
        if mood == 'aff': q = f"{S.text} ___ {rest} {cue(S)}. ({v})"
        elif mood == 'neg': q = f"{S.text} ___ {rest} {cue(S)}. ({v})"
        else: q = f"___ {S.mid} {rest} {cue(S)}? ({v})"
        ansmap = {'aff':f"used to {v}", 'neg':f"didn't use to {v}", 'q':f"Did"}
        if level == 'easy':
            # blank 'used to' only
            if mood == 'q': return line(f"Did {S.mid} ___ {v} {rest} {cue(S)}?", ['use to'])
            if mood == 'neg': return line(f"{S.text} didn't ___ {v} {rest} {cue(S)}.", ['use to'])
            return line(f"{S.text} ___ {v} {rest} {cue(S)}.", ['used to'])
        if level == 'medium':
            if mood == 'aff': return line(f"{S.text} ___ {rest} {cue(S)}. (use to {v})", [f"used to {v}"])
            if mood == 'neg': return line(f"{S.text} ___ {rest} {cue(S)}. (not use to {v})", [f"didn't use to {v}", f"did not use to {v}", f"never used to {v}"] if False else [f"didn't use to {v}", f"did not use to {v}"])
            return line(f"___ {S.mid} ___ {rest} {cue(S)}? (use to {v})", ['Did'], [f"use to {v}"])
        k = rng.pick(['fix','fix','fix','neg','q','would'])
        if k == 'fix':
            if mood == 'neg': bad = f"{S.text} didn't used to {v} {rest} {cue(S)}."
            elif mood == 'q': bad = f"Did {S.mid} used to {v} {rest} {cue(S)}?"
            else: bad = f"{S.text} use to {v} {rest} {cue(S)}."
            gd = [good]
            if mood == 'neg': gd = [good, good.replace("didn't use to", "did not use to")]
            return line('Correct the mistake: ' + bad, gd)
        if k == 'neg':
            if mood != 'aff': return None
            return line('Make a negative sentence: ' + good, [forms(S, v, rest, 'neg', 'used'), forms(S, v, rest, 'neg', 'used').replace("didn't use to", "did not use to")])
        if k == 'q':
            if mood != 'aff': return None
            return line('Make a question: ' + good, [forms(S, v, rest, 'q', 'used')])
        if st or mood != 'aff': return None
        return line('Rewrite with would: ' + good, [good.replace(' used to ', ' would ')])
    if fam == 'would':
        v, rest = rng.pick(ACTS)
        if mood != 'aff': return None
        good = f"{S.text} would {v} {rest} {cue(S)}."; q = f"{S.text} ___ {v} {rest} {cue(S)}."
        if level == 'hard': return None
        return line(q + ' (would / used to)', ['would', 'used to'])
    # be/get used to + -ing
    v, rest = rng.pick([("get up","early"),("walk","to work"),("work","at night"),("live","alone"),("drive","on the left"),("eat","spicy food"),("speak","English every day"),("sleep","in a tent"),("study","for hours"),("cook","for a big family")])
    g = {'get up':'getting up','walk':'walking','work':'working','live':'living','drive':'driving','eat':'eating','speak':'speaking','sleep':'sleeping','study':'studying','cook':'cooking'}[v]
    kind = fam
    b = 'am' if S.kind == 'i' else ('is' if S.kind == 'sg' else 'are')
    if kind == 'beused':
        if mood == 'aff': good = f"{S.text} {b} used to {g} {rest}."; blank = f"{S.text} {b} used to ___ ({v}) {rest}."
        elif mood == 'neg': good = (f"{S.text} {b}n't used to {g} {rest}." if S.kind != 'i' else f"{S.text} am not used to {g} {rest}."); blank = good.replace(g, f"___ ({v})")
        else: good = f"{cap(b)} {S.mid} used to {g} {rest}?"; blank = good.replace(g, f"___ ({v})")
    else:
        if mood == 'aff': good = f"{S.text} will get used to {g} {rest}."; blank = good.replace(g, f"___ ({v})")
        elif mood == 'neg': good = f"{S.text} won't get used to {g} {rest}."; blank = good.replace(g, f"___ ({v})")
        else: good = f"Will {S.mid} get used to {g} {rest}?"; blank = good.replace(g, f"___ ({v})")
    if level != 'hard': return line(blank, [g])
    wrong = good.replace(g, v)
    return line('Correct the mistake: ' + wrong, [good])
def gen_used_jobs(C):
    return {'used-to-would-and-be-used-to': lambda: gen_topic(gen_used, C, 100)}
