from lib import *
from passive import gen_topic

def A(np):  # indefinite article for 'the x' style noun
    return ('an ' if np[0] in 'aeiou' else 'a ') + np
PERSONS = [("man","men"),("woman","women"),("boy","boys"),("girl","girls"),("student","students"),("neighbour","neighbours"),("driver","drivers"),("singer","singers"),
 ("player","players"),("customer","customers"),("tourist","tourists"),("child","children"),("artist","artists"),("lady","ladies"),("passenger","passengers"),("visitor","visitors"),
 ("writer","writers"),("runner","runners"),("cousin","cousins"),("guest","guests"),("clerk","clerks"),("reporter","reporters"),("dancer","dancers"),("swimmer","swimmers")]
# person subject-gap clause uses VERBS (non-achievement + comps)
P_TAIL = [("my cousin","my cousins"),("a friend of mine","friends of mine"),("very kind","very kind"),("from Spain","from Spain"),("in my class","in my class"),("waiting outside","waiting outside"),
 ("very famous","very famous"),("on the phone","on the phone"),("angry","angry"),("a good cook","good cooks"),("my uncle's friend","my uncle's friends"),("really funny","really funny"),
 ("new here","new here"),("in the garden","in the garden"),("very polite","very polite"),("late today","late today")]
# things: (sg noun, pl noun, [(3sg predicate, plural predicate)])
THINGS_S = [
 ("bus","buses",[("goes to the airport","go to the airport"),("leaves at six","leave at six"),("stops near the park","stop near the park")]),
 ("phone","phones",[("rings all day","ring all day"),("costs a lot of money","cost a lot of money"),("has a big screen","have big screens")]),
 ("book","books",[("tells a funny story","tell funny stories"),("has a blue cover","have blue covers"),("explains the rules","explain the rules")]),
 ("shop","shops",[("sells fresh bread","sell fresh bread"),("opens at eight","open at eight"),("stays open late","stay open late")]),
 ("train","trains",[("arrives at noon","arrive at noon"),("goes to the coast","go to the coast"),("leaves from platform two","leave from platform two")]),
 ("road","roads",[("leads to the river","lead to the river"),("goes through the forest","go through the forest"),("crosses the bridge","cross the bridge")]),
 ("machine","machines",[("makes strong coffee","make strong coffee"),("works very well","work very well"),("washes the clothes","wash the clothes")]),
 ("dog","dogs",[("barks all night","bark all night"),("lives next door","live next door"),("follows me home","follow me home")]),
 ("film","films",[("starts at nine","start at nine"),("lasts three hours","last three hours"),("makes me laugh","make me laugh")]),
 ("restaurant","restaurants",[("serves good food","serve good food"),("closes at midnight","close at midnight"),("stands on the corner","stand on the corner")]),
 ("teacher's desk","teachers' desks",[("stands by the window","stand by the window")]),
 ("lamp","lamps",[("lights the room","light the room"),("hangs over the table","hang over the tables")]),
 ("key","keys",[("opens the back door","open the back door"),("hangs on the wall","hang on the wall")]),
 ("website","websites",[("gives free advice","give free advice"),("helps students","help students")]),
 ("plane","planes",[("flies to Dubai","fly to Dubai"),("lands at noon","land at noon")]),
 ("flat","flats",[("has two balconies","have two balconies"),("faces the park","face the park")]),
 ("ticket","tickets",[("gets you into the museum","get you into the museum"),("costs five pounds","cost five pounds")]),
 ("river","rivers",[("runs through the town","run through the town"),("flows into the lake","flow into the lake")]),
]
T_TAIL = [("on the table","on the table"),("very expensive","very expensive"),("mine","mine"),("broken","broken"),("brand new","brand new"),("too old","too old"),("in the car","in the car"),("not here","not here"),
 ("really useful","really useful"),("on sale","on sale"),("famous","famous"),("in good condition","in good condition"),("a bargain","bargains")]
# object-gap: noun, plural, [(base, past, pp, s)]
OBJS = [
 ("book","books",[("buy","bought","bought","buys"),("read","read","read","reads"),("write","wrote","written","writes"),("borrow","borrowed","borrowed","borrows"),("lose","lost","lost","loses"),("find","found","found","finds")]),
 ("film","films",[("watch","watched","watched","watches"),("see","saw","seen","sees"),("like","liked","liked","likes"),("choose","chose","chosen","chooses")]),
 ("cake","cakes",[("bake","baked","baked","bakes"),("make","made","made","makes"),("eat","ate","eaten","eats"),("buy","bought","bought","buys")]),
 ("picture","pictures",[("paint","painted","painted","paints"),("draw","drew","drawn","draws"),("take","took","taken","takes"),("see","saw","seen","sees")]),
 ("phone","phones",[("buy","bought","bought","buys"),("lose","lost","lost","loses"),("find","found","found","finds"),("break","broke","broken","breaks"),("use","used","used","uses")]),
 ("song","songs",[("sing","sang","sung","sings"),("write","wrote","written","writes"),("hear","heard","heard","hears"),("like","liked","liked","likes")]),
 ("bag","bags",[("buy","bought","bought","buys"),("carry","carried","carried","carries"),("lose","lost","lost","loses"),("find","found","found","finds")]),
 ("car","cars",[("buy","bought","bought","buys"),("drive","drove","driven","drives"),("sell","sold","sold","sells"),("repair","repaired","repaired","repairs"),("wash","washed","washed","washes")]),
 ("meal","meals",[("cook","cooked","cooked","cooks"),("eat","ate","eaten","eats"),("prepare","prepared","prepared","prepares"),("order","ordered","ordered","orders")]),
 ("letter","letters",[("write","wrote","written","writes"),("send","sent","sent","sends"),("read","read","read","reads"),("receive","received","received","receives")]),
 ("dress","dresses",[("wear","wore","worn","wears"),("buy","bought","bought","buys"),("make","made","made","makes"),("choose","chose","chosen","chooses")]),
 ("story","stories",[("tell","told","told","tells"),("write","wrote","written","writes"),("read","read","read","reads"),("hear","heard","heard","hears")]),
 ("game","games",[("play","played","played","plays"),("win","won","won","wins"),("like","liked","liked","likes"),("watch","watched","watched","watches")]),
 ("window","windows",[("break","broke","broken","breaks"),("clean","cleaned","cleaned","cleans"),("open","opened","opened","opens"),("paint","painted","painted","paints")]),
 ("photo","photos",[("take","took","taken","takes"),("show","showed","shown","shows"),("send","sent","sent","sends"),("like","liked","liked","likes")]),
 ("jacket","jackets",[("wear","wore","worn","wears"),("buy","bought","bought","buys"),("lose","lost","lost","loses"),("borrow","borrowed","borrowed","borrows")]),
 ("table","tables",[("make","made","made","makes"),("buy","bought","bought","buys"),("paint","painted","painted","paints"),("carry","carried","carried","carries")]),
 ("idea","ideas",[("have","had","had","has"),("like","liked","liked","likes"),("suggest","suggested","suggested","suggests")]),
]
O_TAIL = [("on the table","on the table"),("very expensive","very expensive"),("mine","mine"),("broken","broken"),("brand new","brand new"),("too old","too old"),("in the car","in the car"),("not here","not here"),
 ("really good","really good"),("a bargain","bargains"),("in the kitchen","in the kitchen"),("on sale","on sale")]
# person object-gap: person noun, [(base, past, pp, s)]
POBJ = [("woman","women"),("man","men"),("girl","girls"),("boy","boys"),("teacher","teachers"),("doctor","doctors"),("student","students"),("singer","singers"),("player","players"),("neighbour","neighbours"),("driver","drivers")]
P_OBJ_V = [("meet","met","met","meets"),("see","saw","seen","sees"),("know","knew","known","knows"),("invite","invited","invited","invites"),("help","helped","helped","helps"),("ask","asked","asked","asks"),("call","called","called","calls"),("thank","thanked","thanked","thanks"),("visit","visited","visited","visits"),("like","liked","liked","likes"),("meet","met","met","meets")]
CSUBJ = [("I","I",'i'),("we","we",'pl'),("they","they",'pl'),("Tom","he",'sg'),("Anna","she",'sg'),("my mother","she",'sg'),("my brother","he",'sg'),("my friend","he",'sg'),("my sister","she",'sg'),("the teacher","she",'sg'),("my parents","they",'pl'),("our neighbours","they",'pl')]
# whose: (possessed noun sg, pl, [(sg pred, pl pred)])
WHOSE = [("bike","bikes",[("was stolen","were stolen"),("is red","are red"),("broke yesterday","broke yesterday")]),
 ("car","cars",[("was damaged","were damaged"),("is outside","are outside"),("broke down","broke down")]),
 ("phone","phones",[("rang in the lesson","rang in the lesson"),("is on the table","are on the table"),("was lost","were lost")]),
 ("dog","dogs",[("barked all night","barked all night"),("ran away","ran away"),("is very friendly","are very friendly")]),
 ("brother","brothers",[("plays for Barcelona","play for Barcelona"),("is a pilot","are pilots"),("lives in Tokyo","live in Tokyo")]),
 ("sister","sisters",[("is a doctor","are doctors"),("works in Paris","work in Paris"),("won the prize","won the prize")]),
 ("house","houses",[("is on the corner","are on the corner"),("was sold last week","were sold last week"),("has a red roof","have red roofs")]),
 ("mother","mothers",[("teaches maths","teach maths"),("is a nurse","are nurses"),("speaks four languages","speak four languages")]),
 ("English","English",[("is excellent","is excellent")]),
 ("bag","bags",[("was left on the bus","were left on the bus"),("is open","are open")]),
 ("son","sons",[("goes to my school","go to my school"),("is only three","are only three")]),
 ("laptop","laptops",[("stopped working","stopped working"),("is on the desk","are on the desks")]),
 ("passport","passports",[("was lost","were lost"),("is out of date","are out of date")]),
]
WH_PEOPLE = [("girl","girls"),("man","men"),("woman","women"),("boy","boys"),("student","students"),("teacher","teachers"),("neighbour","neighbours"),("tourist","tourists")]
W_TAIL = [("crying","crying"),("my friend","my friends"),("very upset","very upset"),("from Spain","from Spain"),("in my class","in my class"),("waiting outside","waiting outside"),("here today","here today"),("really kind","really kind")]
WHERE = [("town","we grew up"),("restaurant","we had dinner"),("hotel","they stayed"),("school","my father studied"),("village","my grandfather was born"),("park","we play football"),("shop","I bought these shoes"),("cafe","we met"),
 ("house","I lived as a child"),("city","she works"),("beach","we spent the summer"),("hospital","my sister works"),("street","they live"),("library","I do my homework"),("gym","Tom trains"),("stadium","they play"),("market","my mother buys vegetables"),("airport","we said goodbye"),("island","they spent their holiday"),("office","my dad works")]
WHEN = [("day","we first met"),("year","I started school"),("moment","she saw him"),("summer","we went to Spain"),("morning","the exam began"),("night","the storm hit the town"),("week","we moved house"),("time","they arrived"),("day","I lost my phone"),("year","my sister was born"),("month","we got the keys"),("evening","the power went off")]
PLACE_TAIL = ['very old','closed today','far from here','near the park','very crowded','quite famous','closed for repairs','almost empty','closed in winter','on the corner','too expensive','really big']
W_FRAME = ["This is {np}","That was {np}","I remember {np}","I love {np}","I can't forget {np}"]
WHY = [("reason","he left early"),("reason","she was late"),("reason","they moved to London"),("reason","I called you"),("reason","Tom stopped playing football"),("reason","the shop closed"),("reason","we cancelled the trip"),("reason","Anna changed her job")]
BE = {'sg': ('is',"isn't",'Is'), 'pl': ('are',"aren't",'Are')}
def build_sentence(np_phrase, rp, clause, be_form, comp, mode):
    """np_phrase: 'the woman'; mode aff/neg/q"""
    if mode == 'aff': return f"{cap(np_phrase)} {rp} {clause} {be_form[0]} {comp}."
    if mode == 'neg': return f"{cap(np_phrase)} {rp} {clause} {be_form[1]} {comp}."
    return f"{be_form[2]} {np_phrase} {rp} {clause} {comp}?"
def pclause(rng, plural):
    V = rng.pick([v for v in VERBS if not v.ach]); c = rng.pick(V.comps)
    t = rng.pick(['pres','pres','past','past','neg','negp'])
    if t == 'pres': return (V.base if plural else V.s) + ' ' + c, 'pres', V, c
    if t == 'past': return V.past + ' ' + c, 'past', V, c
    if t == 'neg': return (("don't " if plural else "doesn't ") + V.base) + ' ' + c, 'neg', V, c
    return f"didn't {V.base} {c}", 'negp', V, c
def oclause(rng, vs):
    base, past, pp, s = rng.pick(vs); subj, pron, k = rng.pick(CSUBJ)
    t = rng.pick(['past','past','perf','pres','negp','negperf'])
    if t == 'past': return f"{subj} {past}", subj, pron, 'past'
    if t == 'perf': return f"{subj} {'has' if k=='sg' else 'have'} {pp}", subj, pron, 'perf'
    if t == 'pres': return f"{subj} {s if k=='sg' else base}", subj, pron, 'pres'
    if t == 'negp': return f"{subj} didn't {base}", subj, pron, 'neg'
    hn = "hasn't" if k == 'sg' else "haven't"
    return f"{subj} {hn} {pp}", subj, pron, 'neg'
OBJPRON = {'I':'me','we':'us','they':'them','he':'him','she':'her'}

def rel_item(rng):
    """returns dict describing one defining relative-clause situation"""
    kind = rng.pick(['p_subj','p_subj','t_subj','t_subj','t_obj','t_obj','p_obj','whose','where','when','why'])
    plural = rng.pick([False, False, True]) if kind in ('p_subj','t_subj','t_obj','p_obj','whose') else False
    d = dict(kind=kind, plural=plural)
    be = BE['pl' if plural else 'sg']; d['be'] = be
    if kind == 'p_subj':
        n, np_ = rng.pick(PERSONS); np = 'the ' + (np_ if plural else n)
        clause, tense, V, c = pclause(rng, plural)
        comp = rng.pick(P_TAIL)[1 if plural else 0]
        d.update(np=np, nps=A(n) if not plural else np_, rp_ok=['who','that'], rp_bad='which', clause=clause, comp=comp, subj_pron=('They' if plural else rng.pick(['He','She'])), s2=clause, obj=False, person=True)
    elif kind == 't_subj':
        n, pl, preds = rng.pick(THINGS_S); pr = rng.pick(preds)
        np = 'the ' + (pl if plural else n); clause = pr[1 if plural else 0]
        comp = rng.pick(T_TAIL)[1 if plural else 0]
        d.update(np=np, nps=(pl if plural else A(n)), rp_ok=['which','that'], rp_bad='who', clause=clause, comp=comp, subj_pron=('They' if plural else 'It'), s2=clause, obj=False, person=False)
    elif kind == 't_obj':
        n, pl, vs = rng.pick(OBJS); cl, subj, pron, tn = oclause(rng, vs)
        np = 'the ' + (pl if plural else n); comp = rng.pick(O_TAIL)[1 if plural else 0]
        d.update(np=np, nps=(pl if plural else A(n)), rp_ok=['which','that'], rp_bad='who', clause=cl, comp=comp, s2=cl + (' them' if plural else ' it'), obj=True, person=False, omit=True)
    elif kind == 'p_obj':
        n, pl = rng.pick(POBJ); base, past, pp, s = rng.pick(P_OBJ_V); subj, pron, k = rng.pick(CSUBJ)
        t = rng.pick(['past','past','perf','negp'])
        if t == 'past': cl = f"{subj} {past}"
        elif t == 'perf': cl = f"{subj} {'has' if k=='sg' else 'have'} {pp}"
        else: cl = f"{subj} didn't {base}"
        np = 'the ' + (pl if plural else n); comp = rng.pick(P_TAIL)[1 if plural else 0]
        d.update(np=np, nps=(pl if plural else A(n)), rp_ok=['who','that','whom'], rp_bad='which', clause=cl, comp=comp, s2=cl + (' them' if plural else (' him' if n in ('man','boy') else ' her' if n in ('woman','girl') else ' him')), obj=True, person=True, omit=True)
        d['p_obj_pron'] = True
    elif kind == 'whose':
        pn, ppl = rng.pick(WH_PEOPLE); poss, possp, preds = rng.pick(WHOSE); pr = rng.pick(preds)
        np = 'the ' + (ppl if plural else pn)
        # possessed noun number follows pred form chosen independently (use singular possessed noun)
        clause = f"{poss} {pr[0]}"
        comp = rng.pick(W_TAIL)[1 if plural else 0]
        d.update(np=np, nps=(ppl if plural else A(pn)), rp_ok=['whose'], rp_bad='who', clause=clause, comp=comp, s2=f"{'Their' if plural else rng.pick(['His','Her'])} {poss} {pr[0]}", obj=False, person=True, whose=True)
    elif kind == 'where':
        pl_, cl = rng.pick(WHERE); np = 'the ' + pl_
        d.update(np=np, nps=A(pl_), rp_ok=['where'], rp_bad='which', clause=cl, comp=rng.pick(PLACE_TAIL), s2=cl + ' there', obj=False, person=False, place=True, be=BE['sg'])
    elif kind == 'when':
        w, cl = rng.pick(WHEN); np = 'the ' + w
        d.update(np=np, nps=A(w), rp_ok=['when','that'], rp_bad='where', clause=cl, comp=rng.pick(['unforgettable','a Monday','very cold','the best one','hard to forget','a long time ago']), s2=cl + ' then', obj=False, person=False, time=True, be=BE['sg'])
    else:
        w, cl = rng.pick(WHY); np = 'the reason'
        d.update(np=np, nps='a reason', rp_ok=['why','that'], rp_bad='where', clause=cl, comp=rng.pick(['clear','a secret','simple','not important','obvious','strange']), s2=cl, obj=False, person=False, why=True, be=BE['sg'])
    if kind in ('where','when','why'): d['plural'] = False
    return d

def rel_forms(d, rp):
    """the three main-clause moods for a given relative pronoun ('' = omitted)"""
    r = (rp + ' ') if rp else ''
    np = d['np']; be = d['be']; cl = d['clause']; comp = d['comp']
    aff = f"{cap(np)} {r}{cl} {be[0]} {comp}."
    neg = f"{cap(np)} {r}{cl} {be[1]} {comp}."
    q = f"{be[2]} {np} {r}{cl} {comp}?"
    return {'aff': aff, 'neg': neg, 'q': q}
def blank_forms(d, mood):
    f = rel_forms(d, '___'); return f[mood]
def all_ok_sentences(d, mood):
    out = []
    for rp in d['rp_ok']: out.append(rel_forms(d, rp)[mood])
    if d.get('omit') or (d['kind'] in ('when','why')): out.append(rel_forms(d, '')[mood].replace('  ', ' '))
    return out

def gen_rel_def(level, rng):
    d = rel_item(rng); mood = rng.pick(['aff','aff','neg','q'])
    # easy: single blank; the relative pronoun only
    if level == 'easy':
        mood = rng.pick(['aff','aff','neg','q'])
        ans = d['rp_ok']
        return line(blank_forms(d, mood), ans)
    if level == 'medium':
        k = rng.pick(['blank2','blank','choose'])
        f = rel_forms(d, '___')
        if k == 'blank2':
            # also blank the be-verb in the main clause
            be = d['be']
            if mood == 'aff':
                txt = f"{cap(d['np'])} ___ {d['clause']} ___ {d['comp']}."; return line(txt, d['rp_ok'], [be[0]])
            if mood == 'neg':
                txt = f"{cap(d['np'])} ___ {d['clause']} ___ {d['comp']}."; return line(txt, d['rp_ok'], [be[1], be[0] + ' not'])
            txt = f"___ {d['np']} ___ {d['clause']} {d['comp']}?"; return line(txt, [be[2]], d['rp_ok'])
        if k == 'choose':
            alts = ' / '.join(rng.r.sample(['who','which','whose','where','when'], 4) if False else ([d['rp_ok'][0], d['rp_bad']] if rng.pick([0,1]) else [d['rp_bad'], d['rp_ok'][0]]))
            return line(f"{f[mood]} ({alts})", d['rp_ok'])
        return line(f[mood], d['rp_ok'])
    # hard
    k = rng.pick(['join','join','fix','fix','omit'])
    if k == 'join' or (k == 'omit' and not d.get('omit')):
        frame = rng.pick(W_FRAME) if d['kind'] in ('where','when','why') else None
        # sentence 1 / sentence 2 for the join
        if d['kind'] in ('where','when','why'):
            np_ = d['np']
            if d['kind'] == 'why': s1 = f"{cap(np_)} {d['be'][0]} {d['comp']}."; s1_join = f"{cap(np_)} ___ {d['clause']} {d['be'][0]} {d['comp']}."
            s2 = f"{cap(d['s2'])}."
            if d['kind'] == 'where':
                s1 = f"{rng.pick(['This is','That was','I remember','We visited'])} {np_}."
            elif d['kind'] == 'when':
                s1 = f"{rng.pick(['This is','That was','I remember','Do you remember'])} {np_}."
            else:
                s1 = f"{cap(np_)} {d['be'][0]} {d['comp']}. "
            if d['kind'] == 'why':
                s1 = f"{cap(np_)} {d['be'][0]} {d['comp']}."
                return line(f"Join with 'why': {s1} {s2}", [f"{cap(np_)} why {d['clause']} {d['be'][0]} {d['comp']}.", f"{cap(np_)} that {d['clause']} {d['be'][0]} {d['comp']}.", f"{cap(np_)} {d['clause']} {d['be'][0]} {d['comp']}."])
            lead = s1[:-1]
            rp = d['rp_ok'][0]
            outs = [f"{lead} {rp} {d['clause']}."]
            if d['kind'] == 'where': outs.append(f"{lead} in which {d['clause']}.")
            if d['kind'] == 'when': outs += [f"{lead} that {d['clause']}.", f"{lead} {d['clause']}."]
            return line(f"Join with '{rp}': {s1} {s2}", outs)
        # persons / things: first sentence is main clause with np_indef, second gives the clause
        np_ind = d['nps']
        frames = ["I know {np}", "We met {np}", "Tom saw {np}", "I saw {np}"] if d['kind'] != 'p_subj' or True else []
        fr = rng.pick(["I know {np}", "We met {np}", "Anna called {np}", "They invited {np}", "I saw {np}"] if d['person'] else ["I like {np}", "I saw {np}", "Look at {np}", "We talked about {np}", "I remember {np}"])
        s1 = fr.format(np=np_ind if not d['plural'] else d['nps']) + '.'
        # make np indefinite plural bare: 'women' etc
        if d.get('whose'):
            s2 = d['s2'] + '.'; first = d['rp_ok'][0]
            ans = [f"{s1[:-1]} whose {d['clause'].split(' ',1)[0]} {d['clause'].split(' ',1)[1]}."]
            return line(f"Join with 'whose': {s1} {s2}", ans)
        pron_ans = d['rp_ok']
        s2 = f"{d['subj_pron']} {d['s2']}." if not d['obj'] else f"{cap(d['s2'])}."
        if d['obj']:
            outs = [f"{s1[:-1]} {rp} {d['clause']}." for rp in d['rp_ok']] + [f"{s1[:-1]} {d['clause']}."]
        else:
            outs = [f"{s1[:-1]} {rp} {d['clause']}." for rp in d['rp_ok']]
        rpq = d['rp_ok'][0]
        return line(f"Join the sentences: {s1} {s2}", outs)
    if k == 'omit':
        # may the pronoun be left out? (object gap) -> rewrite without pronoun
        base = rel_forms(d, d['rp_ok'][1] if len(d['rp_ok']) > 1 else d['rp_ok'][0])[mood]
        return line("Leave out the relative pronoun: " + base, [rel_forms(d, '')[mood].replace('  ', ' ')])
    # fix: wrong relative pronoun
    bad = d['rp_bad']
    if d.get('whose'): bad = 'who'
    wrong = rel_forms(d, bad)[mood]
    if d['kind'] in ('where','when','why'):
        if d['kind'] == 'where': bad = rng.pick(['which','that','who'])
        elif d['kind'] == 'when': bad = rng.pick(['where','which'])
        else: bad = rng.pick(['where','which'])
        wrong = rel_forms(d, bad)[mood]
    if wrong in all_ok_sentences(d, mood): return None
    return line('Correct the mistake: ' + wrong, all_ok_sentences(d, mood))

# ---------------- non-defining ----------------
ND_PEOPLE = [("Anna","she"),("Tom","he"),("Aziz","he"),("Malika","she"),("my brother","he"),("my sister","she"),("my uncle","he"),("my aunt","she"),("our teacher","she"),("my grandfather","he"),("my grandmother","she"),("my neighbour","he"),("my best friend","she"),("my cousin","he")]
ND_PRED = [("lives in Dubai","live"),("plays the guitar","play"),("works in a bank","work"),("speaks four languages","speak"),("is a nurse","be"),("is very tall","be"),("studies medicine","study"),("has two dogs","have"),("loves football","love"),("teaches English","teach"),("drives a red car","drive"),("is from Spain","be"),("writes books","write"),("sings in a choir","sing"),("paints beautiful pictures","paint")]
ND_MAIN = ["is coming to the party","called me yesterday","is my favourite","will visit us next week","won a prize last year","is very busy these days","was late again","always helps me","has just moved house","never complains"]
ND_THING = [("my phone","which","was expensive","is already broken"),("my car","which","is ten years old","still works well"),("this book","which","I borrowed from the library","is really boring"),("the film","which","we watched yesterday","was too long"),
 ("my new flat","which","has a big balcony","is near the park"),("the bus","which","goes to the airport","was late"),("our holiday","which","lasted ten days","was fantastic"),("the exam","which","everybody feared","was quite easy"),("my laptop","which","I bought last month","has stopped working"),("the hotel","which","has a pool","was very noisy")]
ND_PLACES = [("Tashkent","where","I was born"),("Paris","where","we spent our honeymoon"),("London","where","my sister studies"),("Rome","where","they met"),("Samarkand","where","my grandparents live"),("Bukhara","where","we bought the carpet"),("Dubai","where","my uncle works"),("Moscow","where","he studied")]
ND_TIMES = [("Friday","when","we have no lessons"),("July","when","the weather is hottest"),("Monday","when","the shop is closed"),("Sunday","when","we visit my grandparents"),("1 September","when","school starts")]
ND_WHOSE = [("Anna","whose","brother is a pilot","Her"),("Tom","whose","mother teaches maths","His"),("Dilya","whose","father owns a shop","Her"),("Aziz","whose","sister lives in Paris","His"),("my neighbour","whose","dog barks all night","His"),("our teacher","whose","car is outside","Her"),("Malika","whose","phone was stolen","Her"),("Jasur","whose","bike is new","His")]
def nd_item(rng):
    k = rng.pick(['pers','pers','pers','thing','thing','place','time','whose','whose'])
    if k == 'pers':
        nm, pr = rng.pick(ND_PEOPLE); pred, _ = rng.pick(ND_PRED); main = rng.pick(ND_MAIN)
        return dict(head=nm, rp='who', clause=pred, main=main, alt=[], neg_main=None, kind=k, pron=('She' if pr == 'she' else 'He'))
    if k == 'thing':
        h, rp, cl, main = rng.pick(ND_THING); return dict(head=h, rp='which', clause=cl, main=main, alt=[], kind=k)
    if k == 'place':
        h, rp, cl = rng.pick(ND_PLACES); main = rng.pick(['is a wonderful city','is very expensive','is crowded in summer','is far from here','is famous for its food','has beautiful old streets'])
        return dict(head=h, rp='where', clause=cl, main=main, alt=[], kind=k)
    if k == 'time':
        h, rp, cl = rng.pick(ND_TIMES); main = rng.pick(['is my favourite day','is always busy','is perfect for a picnic','is the best time of the week','is a good day for a trip'])
        return dict(head=h, rp='when', clause=cl, main=main, alt=[], kind=k)
    h, rp, cl, ps = rng.pick(ND_WHOSE); main = rng.pick(ND_MAIN)
    return dict(head=h, rp='whose', clause=cl, main=main, alt=[], kind=k, pos=ps)
def nd_s2(clause):
    w = clause.split(' ')
    if w[0] in ('I', 'we', 'everybody', 'Everybody'):
        return cap(w[0]) + ' ' + w[1] + ' it ' + ' '.join(w[2:]) + '.'
    return 'It ' + clause + '.'
def nd_sent(d, rp=None):
    rp = rp or d['rp']
    return f"{cap(d['head'])}, {rp} {d['clause']}, {d['main']}."
def nd_neg(main):
    # negative main clause variants
    m = main
    swaps = [("is coming","isn't coming"),("called me","didn't call me"),("is my favourite","isn't my favourite"),("will visit","won't visit"),("won a prize","didn't win a prize"),("is very busy","isn't very busy"),("was late","wasn't late"),("always helps me","never helps me"),("has just moved","hasn't moved"),
             ("is a wonderful","isn't a wonderful"),("is very expensive","isn't very expensive"),("is crowded","isn't crowded"),("is far from","isn't far from"),("is famous","isn't famous"),("has beautiful","doesn't have beautiful"),("is my favourite day","isn't my favourite day"),("is always busy","is never busy"),("is perfect","isn't perfect"),("is the best","isn't the best"),("is a good day","isn't a good day")]
    for a, b in swaps:
        if m.startswith(a): return b + m[len(a):]
    return None
def gen_rel_nd(level, rng):
    d = nd_item(rng)
    s = nd_sent(d)
    if level == 'easy':
        return line(f"{cap(d['head'])}, ___ {d['clause']}, {d['main']}.", [d['rp']])
    if level == 'medium':
        k = rng.pick(['neg','q','plain','two'])
        if k == 'neg':
            nm = nd_neg(d['main'])
            if nm: return line(f"{cap(d['head'])}, ___ {d['clause']}, {nm}.", [d['rp']])
        if k == 'two' and d['kind'] in ('pers','thing'):
            # blank the relative pronoun and show which-type
            return line(f"{cap(d['head'])}, ___ {d['clause']}, {d['main']}. (who / which / where)", [d['rp']])
        return line(f"{cap(d['head'])}, ___ {d['clause']}, {d['main']}.", [d['rp']])
    k = rng.pick(['insert','insert','fix','fix','neg'])
    if k == 'insert':
        if d['kind'] == 'whose':
            return line(f"Add the extra information with 'whose': {cap(d['head'])} {d['main']}. ({cap(d['head'])}'s {d['clause'].replace('brother','brother',1)}.)", [s]) if False else line(f"Make one sentence with 'whose': {cap(d['head'])} {d['main']}. {d['pos']} {d['clause']}.", [s])
        pro = {'pers':'He','thing':'It','place':'','time':''}
        if d['kind'] == 'pers':
            return line(f"Add the extra information with 'who': {cap(d['head'])} {d['main']}. ({cap(d['clause'].split(' ')[0] if False else 'She')} {d['clause']}.)", [s]) if False else line(f"Make one sentence with 'who': {cap(d['head'])} {d['main']}. The person {d['clause']}.", [s]) if False else line(f"Add the extra information with 'who': {cap(d['head'])} {d['main']}. ({d['pron']} {d['clause']}.)", [s])
        if d['kind'] == 'thing':
            return line(f"Add the extra information with 'which': {cap(d['head'])} {d['main']}. (It {d['clause']}.)", [s]) if False else line(f"Add the extra information with 'which': {cap(d['head'])} {d['main']}. ({nd_s2(d['clause'])})", [s])
        if d['kind'] == 'place': return line(f"Add the extra information with 'where': {cap(d['head'])} {d['main']}. (Something happened there: {d['clause']}.)", [s]) if False else line(f"Make one sentence with 'where': {cap(d['head'])} {d['main']}. {cap(d['clause'])} there.", [s])
        return line(f"Make one sentence with 'when': {cap(d['head'])} {d['main']}. {cap(d['clause'])} then.", [s])
    if k == 'fix':
        wrong_rp = {'pers':'that','thing':'that','place':'which','time':'which','whose':'who'}[d['kind']]
        if d['kind'] == 'pers' and rng.pick([0,1]): wrong_rp = 'which'
        return line('Correct the mistake: ' + nd_sent(d, wrong_rp), [s])
    nm = nd_neg(d['main'])
    if nm: return line('Make the main clause negative: ' + s, [f"{cap(d['head'])}, {d['rp']} {d['clause']}, {nm}."])
    return None

def gen_rel_jobs(C):
    return {'relative-clauses-defining': lambda: gen_topic(gen_rel_def, C, 80),
            'relative-clauses-non-defining': lambda: gen_topic(gen_rel_nd, C, 81)}
