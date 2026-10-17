from lib import *
from passive import gen_topic
def _cp(s): return s[0].upper() + s[1:]
P = {'I':('my','mine'),'you':('your','yours'),'he':('his','his'),'she':('her','hers'),'we':('our','ours'),'they':('their','theirs')}
THINGS = ["book","bag","phone","car","pen","coat","laptop","bike","watch","umbrella","notebook","dictionary","key","jacket","camera","scarf","wallet","cup","ticket","guitar"]
THINGS_PL = ["books","bags","shoes","keys","glasses","notes","pens","gloves","tickets","headphones"]
OWN = [("Tom","Tom's"),("Anna","Anna's"),("Aziz","Aziz's"),("Malika","Malika's"),("my brother","my brother's"),("my sister","my sister's"),("the teacher","the teacher's"),("our neighbour","our neighbour's"),("my dad","my dad's"),("Mr Karimov","Mr Karimov's"),("my cousin","my cousin's")]
OWNPL = [("the students","the students'"),("my parents","my parents'"),("the girls","the girls'"),("the boys","the boys'"),("our neighbours","our neighbours'"),("the teachers","the teachers'")]
IRR = [("children","children's"),("men","men's"),("women","women's"),("people","people's")]
PLACES = ["house","room","car","garden","office","flat","bedroom"]

def gen_poss(level, rng):
    k = rng.pick(['adj','adj','pron','pron','apos','apos','aposq','ofmine','whose','fix','fix'])
    pn = rng.pick(list(P)); th = rng.pick(THINGS)
    adj, pro = P[pn]
    sub = {'I':'I','you':'you','he':'he','she':'she','we':'we','they':'they'}[pn]
    if k == 'adj':
        t = rng.pick(['aff','neg','q'])
        art = 'an' if th[0] in 'aeiou' else 'a'
        if t == 'aff': s = f"This is ___ ({sub}) {th}."
        elif t == 'neg': s = f"That isn't ___ ({sub}) {th}."
        else: s = f"Is this ___ ({sub}) {th}?"
        return line(s, [adj])
    if k == 'pron':
        t = rng.pick(['aff','neg','q'])
        if t == 'aff': s = f"The {th} on the table is ___ ({sub})."
        elif t == 'neg': s = f"The {th} on the table isn't ___ ({sub})."
        else: s = f"Is the {th} on the table ___ ({sub})?"
        if level == 'hard' and t == 'aff':
            return line(f"Rewrite with a possessive pronoun: The {th} on the table is {adj} {th}.", [f"The {th} on the table is {pro}."]) if False else line(f"Replace '{adj} {th}' with a possessive pronoun: This {th} is {adj} {th}.", [f"This {th} is {pro}."])
        return line(s, [pro])
    if k == 'apos':
        if level == 'easy':
            o, op = rng.pick(OWN); return line(f"the {th} of {o} = {o}'s {th}? No: the {th} of {o} = ___ {th}.".replace(f"{o}'s {th}? No: ", "") if False else f"Complete: the {th} of {o} = ___ {th}", [op])
        o, op = rng.pick(OWN + OWNPL + IRR)
        pl = rng.pick(THINGS_PL)
        if level == 'medium':
            return line(f"Rewrite with an apostrophe: the {pl} of {o}.", [f"{op} {pl}."], ) if False else line(f"Rewrite with an apostrophe: These are the {pl} of {o}.", [f"These are {op} {pl}."])
        t = rng.pick(['neg','q'])
        if t == 'neg': return line(f"Make a negative sentence: This is {op} {pl}.".replace("This is", "These are" if pl in THINGS_PL else "This is"), [f"{'These are' if pl in THINGS_PL else 'This is'}n't {op} {pl}.".replace("Thesen't","These aren't").replace("This isn't","This isn't")]) if False else line(f"Make a question: {'These are' if pl in THINGS_PL else 'This is'} {op} {pl}.", [f"{'Are these' if pl in THINGS_PL else 'Is this'} {op} {pl}?"])
        return line(f"Make a negative sentence: {'These are' if pl in THINGS_PL else 'This is'} {op} {pl}.", [f"{'These aren' + chr(39) + 't' if pl in THINGS_PL else 'This isn' + chr(39) + 't'} {op} {pl}.", f"{'These are not' if pl in THINGS_PL else 'This is not'} {op} {pl}."])
    if k == 'aposq':
        o, op = rng.pick(OWN)
        pl = th
        t = rng.pick(['aff','neg','q'])
        if level == 'easy': return None
        # is it X's? -> short answers with possessive without noun
        return line(f"Answer with a possessive: Is this {th} {op}? (Yes) => Yes, it's ___.".replace(" => Yes, it's ___.", " Yes, it's ___."), [op]) if False else line(f"Is the {th} {op} or {rng.pick(['yours','mine'])}? It's ___ (the owner is {o}).", [op])
    if k == 'ofmine':
        pn2 = rng.pick(['I','you','he','she','we','they']); a, p = P[pn2]
        who = rng.pick(['friend','cousin','neighbour','teacher','colleague'])
        t = rng.pick(['aff','neg'])
        art = 'a'
        if level == 'easy': return line(f"He is {art} {who} of ___ ({pn2}).", [p])
        if level == 'medium': return line(f"Rewrite with 'of': He is one of {a} {who}s.", [f"He is a {who} of {p}."]) 
        return line(f"Correct the mistake: He is {art} {who} of {a}.", [f"He is a {who} of {p}."])
    if k == 'whose':
        if level == 'easy': return line(f"___ {th} is this? It's Tom's.", ['Whose'])
        o, op = rng.pick(OWN)
        return line(f"Make a question with 'Whose': This {th} is {op}.", [f"Whose {th} is this?", f"Whose is this {th}?"])
    # fix
    if level == 'easy': return None
    fx = rng.pick(['a','b','c','d','e'])
    if fx == 'a': return line(f"Correct the mistake: This {th} is {pro}'s.".replace(f"{pro}'s", f"{pro}'s") if pro not in ('his',) else f"Correct the mistake: This {th} is mine's.", [f"This {th} is {pro}." if pro != 'his' else f"This {th} is mine."]) if pro != 'his' else line(f"Correct the mistake: This {th} is mine's.", [f"This {th} is mine."])
    if fx == 'b': return line(f"Correct the mistake: That is {pro} {th}." if pro != adj else f"Correct the mistake: That is {pn.lower() if False else 'hers'} {th}.", [f"That is {adj} {th}."]) if pro != adj else line(f"Correct the mistake: That is hers {th}.", [f"That is her {th}."])
    if fx == 'c':
        o, op = rng.pick(IRR + [("the students","the students'")]); w = rng.pick(THINGS_PL)
        bad = o + "s'" if o in ('men','women','children','people') else "the student's"
        if o == 'the students': return line(f"Correct the mistake: The teacher read the student's {w}. (more than one student)", [f"The teacher read the students' {w}."])
        return line(f"Correct the mistake: These are the {o}s' {w}.".replace(f"the {o}s'", f"the {o}s'") if False else f"Correct the mistake: These are the {o[:-1] if o.endswith('n') and False else o}s {w}." if False else f"Correct the mistake: These are the {o}' {w}.", [f"These are the {op} {w}."])
    if fx == 'd': return line(f"Correct the mistake: Is this you {th}?", [f"Is this your {th}?"])
    return line(f"Correct the mistake: The {th} is their, not our.", [f"The {th} is theirs, not ours."])

def gen_poss_jobs(C):
    return {'possessives': lambda: gen_topic(gen_poss, C, 134)}
