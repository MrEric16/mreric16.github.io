from lib import *
from passive import gen_topic
def _cp(s): return s[0].upper() + s[1:]
def _lc(P): return P[0].lower() + P[1:] if P.split()[0] in ('My','Our','The','You') else P
REFL = {'i':'myself','you':'yourself','he':'himself','she':'herself','we':'ourselves','they':'themselves'}
# (base, past, rest after reflexive)
RV = [("cut","cut","while cooking dinner"),("hurt","hurt","playing football"),("burn","burned","on the oven"),("teach","taught","to play the guitar"),
 ("blame","blamed","for the mistake"),("introduce","introduced","to the new class"),("enjoy","enjoyed","at the party"),("help","helped","to some cake"),
 ("prepare","prepared","for the exam"),("behave","behaved","at the wedding"),("express","expressed","clearly"),("defend","defended","in court"),
 ("tell","told","to stay calm"),("push","pushed","too hard"),("ask","asked","a difficult question"),("lock","locked","out of the flat"),("see","saw","on the screen"),
 ("look at","looked at","in the mirror"),("hit","hit","with the door"),("surprise","surprised","with the result")]
PAIRS = [("Tom and Anna","they"),("Aziz and Malika","they"),("My brother and I","we"),("The twins","they"),("Jasur and Dilnoza","they"),("My parents","they"),("You and your sister","you"),("Our neighbours","they")]
RECIP = [("love","loved"),("help","helped"),("call","called"),("know","knew"),("write to","wrote to"),("respect","respected"),("trust","trusted"),("see","saw"),
 ("talk to","talked to"),("look at","looked at"),("understand","understood"),("hug","hugged"),("phone","phoned"),("support","supported")]
SUBJP = [Subj('I','i','i'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Our teacher','sg','she')]
def gen_refl(level, rng):
    k = rng.pick(['refl','refl','refl','recip','recip','emph','alone','fix','fix'])
    if k in ('refl',):
        S = rng.pick(SUBJP); b, p, rest = rng.pick(RV); R = REFL[S.pron]
        t = rng.pick(['aff','neg','q'])
        if t == 'aff': sent = f"{S.text} {p} ___ {rest}."; ans = [R]
        elif t == 'neg': sent = f"{S.text} didn't {b} ___ {rest}."; ans = [R]
        else:
            if S.text in ('I',): return None
            sent = f"Did {S.mid} {b} ___ {rest}?"; ans = [R]
        h = ''
        if level == 'easy': h = f" ({S.pron})" if S.pron != 'I' else ' (I)'
        if level == 'medium': h = ' (myself / yourself / himself / herself / ourselves / themselves)'
        if level == 'hard': return line(f"Make a negative sentence: {S.text} {p} {R} {rest}.", [f"{S.text} didn't {b} {R} {rest}."]) if t == 'aff' else (line(f"Make a question: {S.text} {p} {R} {rest}.", [f"Did {S.mid} {b} {R} {rest}?"]) if S.text != 'I' else None)
        return line(sent + h, ans)
    if k == 'recip':
        P, pr = rng.pick(PAIRS); b, p = rng.pick(RECIP)
        t = rng.pick(['aff','neg','q'])
        if t == 'aff': sent = f"{P} {p} ___."
        elif t == 'neg': sent = f"{P} didn't {b} ___."
        else: sent = f"Did {_lc(P)} {b} ___?"
        if t == 'q' and P in ('My brother and I','You and your sister'): return None
        if level == 'hard':
            if t == 'aff': return line(f"Make a negative sentence: {P} {p} each other.", [f"{P} didn't {b} each other."])
            if t == 'neg': return line(f"Make a question: {P} {p} each other.", [f"Did {_lc(P)} {b} each other?"]) if P not in ('My brother and I','You and your sister') else None
            return None
        h = ' (each other / themselves)' if level == 'easy' else ' (each other / themselves / ourselves / yourselves / one another)'
        return line(sent + h + ' (one to the other)', ['each other','one another'])
    if k == 'emph':
        S = rng.pick(SUBJP); R = REFL[S.pron]
        pv, bv, thing = rng.pick([("made","make","the cake"),("built","build","the website"),("wrote","write","the essay"),("did","do","the homework"),("painted","paint","the poster"),("cooked","cook","the dinner"),("fixed","fix","the bike"),("designed","design","the logo"),("cleaned","clean","the whole flat")])
        if rng.pick([0,1]): sent = f"{S.text} {pv} {thing} ___."
        else: sent = f"{S.text} didn't {bv} {thing} ___."
        return line(sent + ' (without any help)', [R, f"by {R}"])
    if k == 'alone':
        S = rng.pick(SUBJP); R = REFL[S.pron]
        t = rng.pick(['aff','neg'])
        v = rng.pick([("live","lives","lived"),("travel","travels","traveled"),("study","studies","studied"),("work","works","worked"),("cook","cooks","cooked")])
        sent = f"{S.text} {v[1] if S.sg else v[0]} by ___ (alone)." if t == 'aff' else f"{S.text} {'doesn' if S.sg else 'don'}'t {v[0]} by ___ (alone)."
        if S.pron == 'i': sent = sent.replace(' by ___', ' by ___')
        return line(sent, [R])
    # fix
    if level == 'easy': return None
    S = rng.pick(SUBJP); b, p, rest = rng.pick(RV); R = REFL[S.pron]
    kk = rng.pick(['f1','f2','f3'])
    if kk == 'f1':
        bad = {'himself':'hisself','themselves':'theirselves','herself':'hersellf','myself':'meself','ourselves':'ourself'}[R]
        if R in ('herself','myself'): bad = {'herself':'herselves','myself':'myselfs'}[R]
        return line(f"Correct the mistake: {S.text} {p} {bad} {rest}.", [f"{S.text} {p} {R} {rest}."])
    if kk == 'f2':
        objp = S.objp
        return line(f"Correct the mistake: {S.text} {p} {objp} {rest}.", [f"{S.text} {p} {R} {rest}."])
    P, pr = rng.pick(PAIRS); rb, rp = rng.pick(RECIP)
    return line(f"Correct the mistake: {P} {rp} themselves.", [f"{P} {rp} each other.", f"{P} {rp} one another."])

# indefinite pronouns
ST = [('some','any','no','every'),]
KIND = [('one',['someone','somebody'],['anyone','anybody'],['no one','nobody'],['everyone','everybody']),
        ('thing',['something'],['anything'],['nothing'],['everything']),
        ('where',['somewhere'],['anywhere'],['nowhere'],['everywhere'])]
FR = {
 'one': {'some': [("I saw ___ in the garden last night.",""),("___ is knocking at the door.",""),("Would you like to speak to ___ about the problem?","")],
         'any': [("I didn't see ___ in the garden.",""),("Is there ___ in the room?",""),("Did ___ call you yesterday?",""),("We can't ask ___ about it.","")],
         'no': [("I looked everywhere but there was ___ there.",""),("The office was empty. ___ was working.",""),("I knocked three times but ___ answered the door.","")],
         'every': [("The whole class passed, so ___ was happy.",""),("___ in my family loves football, even my grandma.",""),("___ knows the answer, so the teacher is proud.","")]},
 'thing': {'some': [("I've got ___ in my eye.",""),("Would you like ___ to drink?",""),("There is ___ strange in the kitchen.","")],
           'any': [("I didn't buy ___ at the market.",""),("Is there ___ in the fridge?",""),("Did you hear ___ ?",""),("We can't find ___ interesting on TV.","")],
           'no': [("The box is empty. There is ___ in it.",""),("I looked everywhere but found ___ useful.",""),("The shop had ___ left, so we went home.","")],
           'every': [("I packed ___ I need for the trip.",""),("She lost ___ in the fire.",""),("___ in the shop is on sale.","")]},
 'where': {'some': [("I've left my phone ___ in the house.",""),("Let's go ___ quiet.","")],
           'any': [("I can't find my keys ___.",""),("Did you go ___ interesting at the weekend?",""),("Is there ___ to sit?","")],
           'no': [("I looked in every room but my keys were ___ to be found.",""),("We had ___ to stay, so we slept in the car.","")],
           'every': [("I've looked ___ for my glasses, but they're gone.",""),("There are shops ___ in this city.","")]}}
def _gen_ind_tpl(level, rng):
    S = rng.pick(SUBJP); V, comp = vcomp(rng)
    kd = rng.pick(['one','one','one','thing','thing','where'])
    typ = rng.pick(['some','any','any','no','every'])
    pa = V.past; b = V.base
    sm = S.mid
    words = {'one':KIND[0],'thing':KIND[1],'where':KIND[2]}[kd]
    ans = words[{'some':1,'any':2,'no':3,'every':4}[typ]]
    if kd == 'one':
        if typ == 'some': fr = f"{S.text} {pa} {comp} with ___ last weekend."
        elif typ == 'any':
            fr = rng.pick([f"{S.text} didn't {b} {comp} with ___ last weekend.", f"Did {sm} {b} {comp} with ___ last weekend?"]) if S.text != 'I' else f"I didn't {b} {comp} with ___ last weekend."
        elif typ == 'no': fr = f"{S.text} wanted to {b} {comp}, but ___ wanted to join {S.objp}."
        else: fr = f"{S.text} {pa} {comp}, and ___ in the class (all of the students) clapped."
    elif kd == 'thing':
        t = rng.pick(['food','gift','pen'])
        if typ == 'some': fr = f"{S.text} bought ___ for {S.objp}self at the market.".replace(f"{S.objp}self","lunch") 
        elif typ == 'any': fr = rng.pick([f"{S.text} didn't buy ___ at the market.", f"Did {sm} buy ___ at the market?"]) if S.text != 'I' else "I didn't buy ___ at the market."
        elif typ == 'no': fr = f"{S.text} had ___ to eat, so {S.pron} was very hungry." if S.pron != 'i' else "I had ___ to eat, so I was very hungry."
        else: fr = f"{S.text} {pa} {comp} and lost ___ in the fire." if False else f"{S.text} lost ___ in the fire."
    else:
        if typ == 'some': fr = f"{S.text} wants to live ___ warm."
        elif typ == 'any': fr = rng.pick([f"{S.text} didn't go ___ at the weekend.", f"Did {sm} go ___ at the weekend?"]) if S.text != 'I' else "I didn't go ___ at the weekend."
        elif typ == 'no': fr = f"{S.text} had ___ to sleep, so {S.pron if S.pron != 'i' else 'I'} slept in the car."
        else: fr = f"{S.text} looked ___ for the keys, but couldn't find them."
    h = ''
    if level == 'easy': h = ' (some- / any- / no- / every-)'
    if level == 'medium':
        W = words
        h = f" ({W[1][0]} / {W[2][0]} / {W[3][0]} / {W[4][0]})"
    return line(fr + h, ans)

def gen_indef(level, rng):
    if rng.pick([0,1,1]): return _gen_ind_tpl(level, rng)
    if rng.pick([0,0,0,1,1]):
        k = rng.pick(['kind','kind','fix','fix','tr'])
    else: k = 'kind'
    kd = rng.pick(['one','thing','where'])
    typ = rng.pick(['some','any','no','every'])
    if k == 'kind' or level == 'easy':
        fr, _ = rng.pick(FR[kd][typ])
        words = {'one':KIND[0],'thing':KIND[1],'where':KIND[2]}[kd]
        ans = words[{'some':1,'any':2,'no':3,'every':4}[typ]]
        h = ''
        if level == 'easy':
            h = ' (some- / any- / no- / every-)' if True else ''
        if level == 'medium':
            h = f" ({'someone' if kd=='one' else 'something' if kd=='thing' else 'somewhere'} / {'anyone' if kd=='one' else 'anything' if kd=='thing' else 'anywhere'} / {'no one' if kd=='one' else 'nothing' if kd=='thing' else 'nowhere'} / {'everyone' if kd=='one' else 'everything' if kd=='thing' else 'everywhere'})"
        return line(fr.replace(' ?','?') + h, ans)
    if k == 'tr':
        if kd != 'one' or level == 'easy': return None
        V, comp = vcomp(rng)
        return rng.pick([
          line(f"Make a negative sentence: Someone {V.s} {comp}.", [f"No one {V.s} {comp}.", f"Nobody {V.s} {comp}."]),
          line(f"Make a question: Someone {V.s} {comp}.", [f"Does anyone {V.base} {comp}?", f"Does anybody {V.base} {comp}?"]),
          line(f"Make a negative sentence: Everyone {V.s} {comp}.", [f"No one {V.s} {comp}.", f"Nobody {V.s} {comp}.", f"Not everyone {V.s} {comp}."])])
    # fix
    if level != 'hard': return None
    V, comp = vcomp(rng)
    return rng.pick([
      line(f"Correct the mistake: I didn't see nobody at the party.", ["I didn't see anybody at the party.", "I didn't see anyone at the party.", "I saw nobody at the party.", "I saw no one at the party."]),
      line(f"Correct the mistake: Everyone {V.base} {comp}.", [f"Everyone {V.s} {comp}."]),
      line(f"Correct the mistake: Someone {V.base} {comp}.", [f"Someone {V.s} {comp}."]),
      line(f"Correct the mistake: There isn't something in the box.", ["There isn't anything in the box.", "There is nothing in the box."]),
      line(f"Correct the mistake: Anyone doesn't {V.base} {comp}.", [f"No one {V.s} {comp}.", f"Nobody {V.s} {comp}."]),
      line(f"Correct the mistake: Did you go somewhere interesting? No, I didn't go nowhere.", ["Did you go somewhere interesting? No, I didn't go anywhere.", "Did you go somewhere interesting? No, I went nowhere."]),
      line(f"Correct the mistake: Is there nothing in the fridge?", ["Is there anything in the fridge?"]),
    ])

# this / that / these / those
TN = [("book","books"),("pen","pens"),("bag","bags"),("phone","phones"),("chair","chairs"),("picture","pictures"),("apple","apples"),("shoe","shoes"),("key","keys"),("coat","coats"),("flower","flowers"),("cup","cups"),("car","cars"),("watch","watches"),("lamp","lamps")]
ADJ = ["new","old","expensive","cheap","heavy","beautiful","clean","useful"]
def gen_this(level, rng):
    sg, pl = rng.pick(TN); a = rng.pick(ADJ)
    near = rng.pick([0,1]); one = rng.pick([0,1])
    loc = rng.pick(['in my hand','on my desk','next to me']) if near else rng.pick(['over there','on the far shelf','across the room'])
    if level == 'easy':
        h = ' (this / that / these / those)' if False else ' (this / that)' if one else ' (these / those)'
    elif level == 'medium': h = ' (this / that / these / those)'
    else: h = ''
    ans = ('this' if near else 'that') if one else ('these' if near else 'those')
    t = rng.pick(['aff','neg','q','tr','tr2'])
    if t == 'aff':
        s = f"___ {sg} {loc} is {a}." if one else f"___ {pl} {loc} are {a}."
        return line(s + h, [ans])
    if t == 'neg':
        s = f"___ {sg} {loc} isn't {a}." if one else f"___ {pl} {loc} aren't {a}."
        return line(s + h, [ans])
    if t == 'q':
        s = f"Is ___ {sg} {loc} {a}?" if one else f"Are ___ {pl} {loc} {a}?"
        return line(s + h, [ans])
    if level == 'easy': return None
    if t == 'tr':
        if one:
            return line(f"Make it plural: {_cp(ans)} {sg} {loc} is {a}.", [f"{'These' if near else 'Those'} {pl} {loc} are {a}."])
        return line(f"Make it singular: {_cp(ans)} {pl} {loc} are {a}.", [f"{'This' if near else 'That'} {sg} {loc} is {a}."])
    if one:
        return line(f"Make a question: {_cp(ans)} {sg} {loc} is {a}.", [f"Is {ans} {sg} {loc} {a}?"])
    return line(f"Make a negative sentence: {_cp(ans)} {pl} {loc} are {a}.", [f"{_cp(ans)} {pl} {loc} aren't {a}."])

def gen_pron2_jobs(C):
    return {'reflexive-pronouns-and-each-other': lambda: gen_topic(gen_refl, C, 131),
            'indefinite-pronouns': lambda: gen_topic(gen_indef, C, 132),
            'this-that-these-those': lambda: gen_topic(gen_this, C, 133)}
