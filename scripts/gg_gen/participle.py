from lib import *
from passive import gen_topic

def _cp(s): return s[0].upper() + s[1:]
PEOPLE = [("Tom","he","his"),("Aziz","he","his"),("Jasur","he","his"),("Karim","he","his"),("Mr Karimov","he","his"),
          ("Anna","she","her"),("Malika","she","her"),("Dilnoza","she","her"),("Sara","she","her"),("Mrs Ivanova","she","her"),
          ("my brother","he","his"),("my sister","she","her"),("our teacher","she","her"),("my dad","he","his"),("my mum","she","her")]
# (ing, was-doing) while-clauses
WHILE = [("walking home","was walking home"),("waiting for the bus","was waiting for the bus"),("reading a book","was reading a book"),
 ("crossing the road","was crossing the road"),("cooking dinner","was cooking dinner"),("talking on the phone","was talking on the phone"),
 ("watching TV","was watching TV"),("sitting in the park","was sitting in the park"),("running for the train","was running for the train"),
 ("shopping in town","was shopping in town"),("looking for {p} keys","was looking for {p} keys"),("working in the garden","was working in the garden"),
 ("listening to music","was listening to music"),("studying in the library","was studying in the library"),("drinking coffee","was drinking coffee")]
WMAIN = ["saw an old friend","dropped {p} phone","met the director","heard a strange noise","found some money","fell over","had a great idea","got a text message",
 "lost {p} umbrella","noticed a beautiful bird","met a famous singer","slipped on the ice"]
# (pp phrase for having, had-done clause)
AFTER = [("finished {p} homework","had finished {p} homework"),("eaten breakfast","had eaten breakfast"),("read the instructions","had read the instructions"),
 ("locked the door","had locked the door"),("done {p} shopping","had done {p} shopping"),("cleaned the kitchen","had cleaned the kitchen"),
 ("seen the film twice","had seen the film twice"),("taken the exam","had taken the exam"),("written the email","had written the email"),
 ("packed {p} bags","had packed {p} bags"),("said goodbye","had said goodbye"),("learned the words","had learned the words"),("found the address","had found the address")]
AMAIN = ["went to bed","called a taxi","left the house","watched TV","relaxed for an hour","went for a walk","sent the message","phoned a friend",
 "took a long rest","started the next exercise"]
# (-ing negative, negative clause)
NEG = [("knowing the answer","didn't know the answer"),("having any money","didn't have any money"),("wanting to be late","didn't want to be late"),
 ("understanding the question","didn't understand the question"),("feeling well","didn't feel well"),("having a ticket","didn't have a ticket"),
 ("knowing the way","didn't know the way"),("speaking Chinese","didn't speak Chinese"),("having a pen","didn't have a pen"),
 ("seeing the sign","didn't see the sign"),("wanting to argue","didn't want to argue"),("hearing the bell","didn't hear the bell")]
NMAIN = ["stayed silent","asked for help","stayed at home","took a taxi","asked a stranger","walked home","missed the start","said nothing","looked at the map","waited outside"]
# thing, be, pp phrases, mains
THINGS = [("The house","was","is","built in 1900",["is very old","is now a museum","needs a new roof"]),
 ("The house","was","is","painted yellow",["looks very bright","is easy to see"]),
 ("The film","was","is","made in 1995",["is still very popular","is on TV tonight"]),
 ("The book","was","is","written by my teacher",["is very funny","is hard to find"]),
 ("The bridge","was","is","damaged in the storm",["is closed today","needs repair"]),
 ("The cake","was","is","baked by my mum",["tastes delicious","is almost gone"]),
 ("The letters","were","are","sent last week",["haven't arrived yet","are on my desk"]),
 ("The windows","were","are","broken by the wind",["need to be replaced","are covered with tape"]),
 ("The students","were","are","chosen for the team",["are very proud","start training today"]),
 ("The cars","were","are","made in Uzbekistan",["are cheap to run","are sold all over Asia"]),
 ("The pictures","were","are","taken in Samarkand",["are beautiful","are on my phone"]),
 ("The shop","was","is","opened last month",["is already busy","sells fresh bread"]),
 ("The song","was","is","sung by a local band",["is on the radio","is very catchy"]),
 ("The teacher","was","is","given the best award",["is very happy","makes a speech"]),
 ("The room","was","is","cleaned this morning",["looks perfect","smells fresh"]),
 ("The tower","was","is","completed in 1980",["is the tallest in town","is a famous landmark"])]
# person, ing-phrase, main
RELI = [("The man","standing at the door","is my uncle"),("The girl","sitting next to me","is from Spain"),("The boy","playing the guitar","is my cousin"),
 ("The woman","talking to the manager","is our new teacher"),("The students","waiting outside","are from another school"),
 ("The people","living next door","are very friendly"),("The children","playing in the park","are my neighbours' kids"),
 ("The driver","wearing a blue cap","is very polite"),("The runners","crossing the finish line","look exhausted"),
 ("The customers","queuing at the till","seem impatient"),("The girl","singing on the stage","is my sister"),("The man","selling flowers","knows everybody"),
 ("The tourists","taking photos","are standing in my way"),("The dog","barking at the gate","belongs to our neighbour"),("The boys","sitting at the back","are always late")]
RELI_WHO = {"The dog":"which","The dogs":"which"}

def gen_part(level, rng):
    k = rng.pick(['while','while','after','after','neg','neg','pp','pp','rel','rel'])
    if k in ('while','after','neg'):
        S, pr, p = rng.pick(PEOPLE)
        if k == 'while':
            ing, cl = rng.pick(WHILE); m = rng.pick(WMAIN)
            ing, cl, m = ing.replace('{p}', p), cl.replace('{p}', p), m.replace('{p}', p)
            normal = f"While {S} {cl}, {pr} {m}."
            tgt = f"{_cp(ing)}, {S} {m}."
            tail = f", {S} {m}."
            first = _cp(ing)
            hint_v = ing.split()[0][:-3]
            bad = rng.pick([f"{_cp(ing.split()[0][:-3])} {' '.join(ing.split()[1:])}, {S} {m}.", f"To {ing}, {S} {m}."]) if False else f"{_cp(cl)}, {S} {m}."
            blank_ing = ing.split()[0]; vb = {'walking':'walk','waiting':'wait','reading':'read','crossing':'cross','cooking':'cook','talking':'talk','watching':'watch','sitting':'sit','running':'run','shopping':'shop','looking':'look','working':'work','listening':'listen','studying':'study','drinking':'drink'}[blank_ing]
            rest0 = ' '.join(ing.split()[1:])
            bads = [f"{_cp(cl)}, {S} {m}.", f"{_cp(vb)} {rest0}, {S} {m}.".replace('  ',' ')]
            if level == 'easy':
                rest = ' '.join(ing.split()[1:])
                return line(f"Complete the participle clause: {normal} = ___ ({vb}) {rest}, {S} {m}.".replace('  ',' '), [_cp(blank_ing)])
            if level == 'medium':
                return line(f"Rewrite with a participle clause (start with the -ing form): {normal}", [tgt])
            return line(f"Correct the mistake: {rng.pick(bads)}", [tgt])
        if k == 'after':
            ph, cl = rng.pick(AFTER); m = rng.pick(AMAIN)
            ph, cl, m = ph.replace('{p}', p), cl.replace('{p}', p), m.replace('{p}', p)
            normal = f"After {S} {cl}, {pr} {m}."
            tgt = f"Having {ph}, {S} {m}."
            vb = ph.split()[0]
            base = {'finished':'finish','eaten':'eat','read':'read','locked':'lock','done':'do','cleaned':'clean','seen':'see','taken':'take','written':'write','packed':'pack','said':'say','learned':'learn','found':'find'}[vb]
            if level == 'easy':
                return line(f"Complete the participle clause: {normal} = ___ ({base}) {' '.join(ph.split()[1:])}, {S} {m}.".replace('  ',' '), [f"Having {vb}"])
            if level == 'medium':
                return line(f"Rewrite with a participle clause (start with 'Having'): {normal}", [tgt])
            bads = [f"Have {ph}, {S} {m}.", f"{_cp(ph)}, {S} {m}.", f"Having {base} {' '.join(ph.split()[1:])}, {S} {m}.".replace('  ',' ')]
            return line(f"Correct the mistake: {rng.pick(bads)}", [tgt])
        ing, cl = rng.pick(NEG); m = rng.pick(NMAIN)
        reason = rng.pick(['Because','As'])
        normal = f"{reason} {S} {cl}, {pr} {m}."
        tgt = f"Not {ing}, {S} {m}."
        first = ing.split()[0]
        vb = {'knowing':'know','having':'have','wanting':'want','understanding':'understand','feeling':'feel','speaking':'speak','seeing':'see','hearing':'hear'}[first]
        if level == 'easy':
            return line(f"Complete the participle clause: {normal} = ___ ({vb}) {' '.join(ing.split()[1:])}, {S} {m}.".replace('  ',' '), [f"Not {first}"])
        if level == 'medium':
            return line(f"Rewrite with a participle clause (start with 'Not'): {normal}", [tgt])
        bads = [f"{_cp(ing)} not, {S} {m}.", f"Not to {vb} {' '.join(ing.split()[1:])}, {S} {m}.", f"Don't {ing}, {S} {m}."]
        return line(f"Correct the mistake: {rng.pick(bads)}", [tgt])
    if k == 'pp':
        N, wd, bd, ph, mains = rng.pick(THINGS); m = rng.pick(mains)
        normal = f"{N}, which {wd} {ph}, {m}."
        low = N[0].lower() + N[1:]
        tgt = f"{_cp(ph)}, {low} {m}."
        pv = ph.split()[0]
        base = {'built':'build','painted':'paint','made':'make','written':'write','damaged':'damage','baked':'bake','sent':'send','broken':'break','chosen':'choose','taken':'take','opened':'open','sung':'sing','given':'give','cleaned':'clean','completed':'complete'}[pv]
        if level == 'easy':
            return line(f"Complete the participle clause: {normal} = ___ ({base}) {' '.join(ph.split()[1:])}, {low} {m}.", [_cp(pv)])
        if level == 'medium':
            return line(f"Rewrite with a participle clause (start with the past participle): {normal}", [tgt])
        ingf = (base[:-1] if base.endswith('e') and not base.endswith('ee') else base) + 'ing'
        bads = [f"{_cp(ingf)} {' '.join(ph.split()[1:])}, {low} {m}.", f"Been {ph}, {low} {m}."]
        return line(f"Correct the mistake: {rng.pick(bads)}", [tgt])
    # reduced relative with -ing
    N, ph, m = rng.pick(RELI)
    rp = 'which' if N in ('The dog',) else 'who'
    be = 'is' if N in ('The man','The girl','The boy','The woman','The driver','The dog') else 'are'
    normal = f"{N} {rp} {be} {ph} {m}."
    tgt = f"{N} {ph} {m}."
    if level == 'easy':
        return line(f"Shorten the relative clause: {N} {rp} {be} {ph} {m}. = {N} ___ {ph.split(' ',1)[1]} {m}.", [ph.split()[0]])
    if level == 'medium':
        return line(f"Shorten the relative clause: {normal}", [tgt])
    first = ph.split()[0]; base = first[:-3]
    if first in ('sitting','running','queuing') : base = first[:-4] if first != 'queuing' else 'queu'
    bad = rng.pick([f"{N} {be} {ph} {m}.", f"{N} {rp} {ph} {m}.", f"{N} {ph.replace(first, 'to ' + (first[:-3] if first not in ('sitting','running','queuing') else {'sitting':'sit','running':'run','queuing':'queue'}[first]), 1)} {m}."])
    return line(f"Correct the mistake: {bad}", [tgt])

def gen_part_jobs(C):
    return {'participle-clauses': lambda: gen_topic(gen_part, C, 124)}
