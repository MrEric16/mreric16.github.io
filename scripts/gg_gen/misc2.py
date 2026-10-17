from lib import *
from passive import gen_topic
SGp = [Subj('I','i','i'),Subj('You','you','you'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('Karim','sg','he',True),Subj('Dilya','sg','she',True),Subj('My brother','sg','he'),Subj('My sister','sg','she'),Subj('My parents','pl','they')]
POSS = {'i':'my','you':'your','he':'his','she':'her','we':'our','they':'their'}
def mood3(rng): return rng.pick(['aff','aff','neg','q'])
# ================= causative =================
CAUS = [("car","repaired"),("hair","cut"),("teeth","checked"),("flat","painted"),("windows","cleaned"),("suit","cleaned"),("laptop","fixed"),("eyes","tested"),("photo","taken"),("documents","translated"),("house","built"),("parcel","delivered"),("bike","serviced"),("nails","done"),("dress","made"),("garden","designed"),("blood pressure","checked"),("carpet","cleaned"),("phone","repaired"),("bag","delivered")]
CAUS_AG = {"car":"a mechanic","hair":"a hairdresser","teeth":"a dentist","flat":"a decorator","windows":"a cleaner","suit":"a dry cleaner","laptop":"a technician","eyes":"an optician","photo":"a photographer","documents":"a translator","house":"a builder","parcel":"a courier","bike":"a mechanic","nails":"a beautician","dress":"a tailor","garden":"a designer","blood pressure":"a nurse","carpet":"a cleaner","phone":"a technician","bag":"a courier"}
CAUS_BASE = {"repaired":"repair","cut":"cut","checked":"check","painted":"paint","cleaned":"clean","fixed":"fix","tested":"test","taken":"take","translated":"translate","built":"build","delivered":"deliver","serviced":"service","done":"do","made":"make","designed":"design"}
TENSES = [('ps','every month'),('ps','twice a year'),('past','last week'),('past','yesterday'),('past','two days ago'),('will','next week'),('will','tomorrow'),('pc','at the moment'),('pp','this week'),('pp','already')]
def caus_sent(S, obj, pp, tense, cue, mood, hv='have'):
    ps = f"{POSS[S.pron]} {obj}" if obj not in ('photo',) else f"{POSS[S.pron]} photo"
    sg = S.kind == 'sg'
    v = hv
    if tense == 'ps':
        if mood == 'aff': return f"{S.text} {'has' if sg and hv=='have' else ('gets' if sg else v)} {ps} {pp} {cue}.".replace(' get ', ' get ') if hv=='have' or True else ''
    return None
def hform(S, tense, mood, hv):
    sg = S.kind == 'sg'
    if hv == 'have': h3, hp, hpp, hing = 'has', 'had', 'had', 'having'
    else: h3, hp, hpp, hing = 'gets', 'got', 'got', 'getting'
    base = hv
    if tense == 'ps':
        if mood == 'aff': return (h3 if sg else base), None
        return ("doesn't" if sg else "don't"), base
    if tense == 'past':
        if mood == 'aff': return hp, None
        return "didn't", base
    if tense == 'will':
        if mood == 'aff': return 'will', base
        return "won't", base
    if tense == 'pc':
        b = 'am' if S.kind == 'i' else ('is' if sg else 'are')
        return (b if mood == 'aff' else (b + 'n\'t' if S.kind != 'i' else 'am not')), hing
    h = 'has' if sg else 'have'
    return (h if mood == 'aff' else h + "n't"), hpp
def caus_full(S, obj, pp, tense, cue, mood, hv):
    ps = f"{POSS[S.pron]} {obj}"
    a, b = hform(S, tense, mood, hv)
    if mood == 'q':
        if tense == 'ps': return f"{'Does' if S.kind=='sg' else 'Do'} {S.mid} {hv} {ps} {pp} {cue}?"
        if tense == 'past': return f"Did {S.mid} {hv} {ps} {pp} {cue}?"
        if tense == 'will': return f"Will {S.mid} {hv} {ps} {pp} {cue}?"
        if tense == 'pc': return f"{'Am' if S.kind=='i' else ('Is' if S.kind=='sg' else 'Are')} {S.mid} having {ps} {pp} {cue}?" if hv=='have' else f"{'Am' if S.kind=='i' else ('Is' if S.kind=='sg' else 'Are')} {S.mid} getting {ps} {pp} {cue}?"
        hh = 'Has' if S.kind == 'sg' else 'Have'
        return f"{hh} {S.mid} {'had' if hv=='have' else 'got'} {ps} {pp} {cue}?"
    mid = f"{a} {b}" if b else a
    return f"{S.text} {mid} {ps} {pp} {cue}."
def gen_caus(level, rng):
    S = rng.pick(SGp); obj, pp = rng.pick(CAUS); tense, cue = rng.pick(TENSES); mood = mood3(rng); hv = rng.pick(['have','have','get'])
    if tense == 'pp' and cue == 'already' and mood != 'aff': cue = 'yet' if mood == 'neg' else 'yet'
    if tense == 'pp' and cue == 'already' and mood == 'q': cue = 'yet'
    if mood == 'neg' and tense == 'pp' and cue == 'already': cue = 'yet'
    good = caus_full(S, obj, pp, tense, cue, mood, hv)
    ps = f"{POSS[S.pron]} {obj}"
    if level == 'easy':
        # blank the pp
        return line(good.replace(f" {pp} ", f" ___ ({CAUS_BASE[pp]}) ", 1), [pp])
    if level == 'medium':
        # blank the causative verb phrase
        a, b = hform(S, tense, mood, hv)
        if mood == 'q': return line(good.replace(f" {pp} ", f" ___ ({CAUS_BASE[pp]}) ", 1), [pp])
        if tense in ('ps','past','will'):
            if mood == 'aff' and tense in ('ps','past'):
                return line(f"{S.text} ___ ({hv}) {ps} ___ ({CAUS_BASE[pp]}) {cue}.", [a], [pp])
            if mood == 'neg': return line(f"{S.text} ___ ({hv}) {ps} ___ ({CAUS_BASE[pp]}) {cue}.", [f"{a} {b}", f"{a.replace('n’t','n’t')} {b}".replace("doesn't","does not").replace("don't","do not").replace("didn't","did not").replace("won't","will not")], [pp])
        return line(good.replace(f" {pp} ", f" ___ ({CAUS_BASE[pp]}) ", 1), [pp])
    k = rng.pick(['fix','fix','rewrite','rewrite','neg','q'])
    if k == 'fix':
        # active instead of causative
        bad = good.replace(f" {pp} ", f" {CAUS_BASE[pp]} ", 1)
        if bad == good: return None
        if tense in ('past','pp') and mood != 'q': bad = good.replace(f" {pp} ", f" {CAUS_BASE[pp]}ing ", 1) if False else bad
        return line('Correct the mistake: ' + bad, [good])
    if k == 'rewrite':
        if tense not in ('ps','past') or mood != 'aff' or hv != 'have': return None
        agent = CAUS_AG[obj]
        pos = POSS[S.pron]
        if tense == 'past':
            vp = {'repaired':'repaired','cut':'cut','checked':'checked','painted':'painted','cleaned':'cleaned','fixed':'fixed','tested':'tested','taken':'took','translated':'translated','built':'built','delivered':'delivered','serviced':'serviced','done':'did','made':'made','designed':'designed'}[pp]
            act = f"{cap(agent)} {vp} {pos} {obj} {cue}."
        else:
            v3 = {'repaired':'repairs','cut':'cuts','checked':'checks','painted':'paints','cleaned':'cleans','fixed':'fixes','tested':'tests','taken':'takes','translated':'translates','built':'builds','delivered':'delivers','serviced':'services','done':'does','made':'makes','designed':'designs'}[pp]
            act = f"{cap(agent)} {v3} {pos} {obj} {cue}."
        return line(f"Rewrite with 'have' ({S.text} did not do it): {act}", [good, good.replace(' has ', ' gets ').replace(' had ', ' got ').replace(' have ', ' get ')])
    if mood != 'aff': return None
    if k == 'neg': return line('Make a negative sentence: ' + good, [caus_full(S, obj, pp, tense, cue, 'neg', hv)])
    return line('Make a question: ' + good, [caus_full(S, obj, pp, tense, cue, 'q', hv)])
# ================= wish =================
W_PRES = [("have","a bigger flat"),("live","in a bigger city"),("know","the answer"),("speak","Chinese"),("have","more free time"),("own","a faster laptop"),("play","the guitar"),("have","a car"),("live","near the sea"),("have","a garden"),("know","more people here"),("earn","more money")]
W_PRES_NEG = [("have to","work on Sundays"),("have to","get up early"),("have to","wear a uniform"),("have to","do the dishes"),("have to","share a room")]
W_BE = [("taller",""),("here",""),("at home",""),("a doctor",""),("richer",""),("on holiday",""),("better at maths","")]
W_PAST = [("go","to the party","gone"),("study","harder","studied"),("take","the bus","taken"),("buy","that jacket","bought"),("phone","her","phoned"),("listen","to my advice","listened"),("learn","French","learned"),("say","sorry","said"),("book","a ticket","booked"),("bring","an umbrella","brought"),("wake up","earlier","woken up"),("save","more money","saved")]
W_PAST_TIME = ["last night","yesterday","last week","last year","on Saturday"]
W_WOULD = [("stop","making noise"),("turn","the music down"),("listen","to me"),("clean","the kitchen"),("arrive","on time"),("close","the door"),("help","me"),("answer","my messages"),("tidy","the room"),("tell","the truth")]
def wsent(S, rest_clause, mood, wh='wish'):
    sg = S.kind == 'sg'
    w = 'wishes' if (sg and wh == 'wish') else 'wish'
    if mood == 'aff': return f"{S.text} {w} {rest_clause}."
    if mood == 'neg': return f"{S.text} {'doesn' + chr(39) + 't' if sg else 'don' + chr(39) + 't'} wish {rest_clause}."
    return f"{'Does' if sg else 'Do'} {S.mid} wish {rest_clause}?"
def pron_subj(S): return {'i':'I','you':'you','he':'he','she':'she','we':'we','they':'they'}[S.pron]
def gen_wish(level, rng):
    S = rng.pick(SGp); mood = rng.pick(['aff','aff','aff','neg','q']); pr = pron_subj(S)
    sg = S.kind == 'sg'
    fam = rng.pick(['pres','pres','past','past','would','if','be'])
    if fam == 'pres':
        v, rest = rng.pick(W_PRES)
        past = {'have':'had','live':'lived','know':'knew','speak':'spoke','own':'owned','play':'played','earn':'earned'}[v]
        # present regret
        fact = f"{S.text} {'doesn' + chr(39) + 't' if sg else 'don' + chr(39) + 't'} {v} {rest}."
        if level == 'easy':
            return line(f"{S.text} {'doesn' + chr(39) + 't' if sg else 'don' + chr(39) + 't'} {v} {rest}. {S.text} {'wishes' if sg else 'wish'} {pr} ___ ({v}) {rest}.", [past]) if S.pron != 'you' or True else None
        if level == 'medium' and mood == 'q':
            return line(f"{'Does' if sg else 'Do'} {S.mid} wish {pr} ___ ({v}) {rest}?", [past])
        good = f"{S.text} {'wishes' if sg else 'wish'} {pr} {past} {rest}."
        if level == 'medium': return line(f"{fact} {S.text} {'wishes' if sg else 'wish'} {pr} ___ ({v}) {rest}.", [past])
        k = rng.pick(['fix','fix','rewrite'])
        if k == 'fix': return line('Correct the mistake: ' + f"{S.text} {'wishes' if sg else 'wish'} {pr} {v if v != 'have' else 'have'}{'s' if False else ''} {rest}.", [good])
        return line('Rewrite with wish: ' + fact, [good])
    if fam == 'be':
        w, _ = rng.pick(W_BE)
        fact = f"{S.text} {'isn' + chr(39) + 't' if S.kind == 'sg' else ('am not' if S.kind == 'i' else 'aren' + chr(39) + 't')} {w}."
        if pr == 'I': good = [f"{S.text} wish I were {w}.", f"{S.text} wish I was {w}."]
        else: good = [f"{S.text} {'wishes' if sg else 'wish'} {pr} were {w}.", f"{S.text} {'wishes' if sg else 'wish'} {pr} was {w}."]
        base = f"{S.text} {'wishes' if sg else 'wish'} {pr} ___ {w}."
        if level == 'easy': return line(f"{fact} {base} (be)", ['were','was'])
        if level == 'medium': return line(f"{fact} {base} (be)", ['were','was'])
        return line('Rewrite with wish: ' + fact, good)
    if fam == 'past':
        v, rest, pp = rng.pick(W_PAST); t = rng.pick(W_PAST_TIME)
        didnt = f"{S.text} didn't {v} {rest} {t}."
        good = f"{S.text} {'wishes' if sg else 'wish'} {pr} had {pp} {rest}."
        if level == 'easy': return line(f"{didnt} {S.text} {'wishes' if sg else 'wish'} {pr} ___ ({v}) {rest}.", [f"had {pp}"])
        if level == 'medium':
            if mood == 'q': return line(f"{'Does' if sg else 'Do'} {S.mid} wish {pr} ___ ({v}) {rest} {t}?", [f"had {pp}"])
            return line(f"{didnt} {S.text} {'wishes' if sg else 'wish'} {pr} ___ ({v}) {rest}.", [f"had {pp}"])
        k = rng.pick(['fix','fix','rewrite','ifonly'])
        if k == 'fix': return line('Correct the mistake: ' + f"{S.text} {'wishes' if sg else 'wish'} {pr} {pp if pp != 'woken up' else 'woken up'} {rest}.", [good]) if False else line('Correct the mistake: ' + f"{S.text} {'wishes' if sg else 'wish'} {pr} {pp} {rest}.", [good])
        if k == 'ifonly': return line('Rewrite with If only: ' + good, [f"If only {pr} had {pp} {rest}."])
        return line('Rewrite with wish: ' + didnt, [good])
    if fam == 'would':
        v, rest = rng.pick(W_WOULD); other = rng.pick([o for o in ["my brother","my neighbour","the boy next door","my sister","our teacher","the students"] if o not in S.text.lower()])
        ob = other
        wo = 'would'
        pl = other in ("the students",)
        fact = f"{cap(other)} {'don' + chr(39) + 't' if pl else 'doesn' + chr(39) + 't'} {v} {rest}. It is annoying."
        good = f"{S.text} {'wishes' if sg else 'wish'} {other} would {v} {rest}."
        if level == 'easy': return line(f"{fact} {S.text} {'wishes' if sg else 'wish'} {other} ___ {v} {rest}. (would / will)", ['would'])
        if level == 'medium': return line(f"{S.text} {'wishes' if sg else 'wish'} {other} ___ {v} {rest}. (would / will / is)", ['would'])
        k = rng.pick(['fix','ifonly'])
        if k == 'fix': return line('Correct the mistake: ' + f"{S.text} {'wishes' if sg else 'wish'} {other} will {v} {rest}.", [good])
        return line('Rewrite with If only: ' + good, [f"If only {other} would {v} {rest}."])
    # if only
    v, rest = rng.pick(W_PRES); past = {'have':'had','live':'lived','know':'knew','speak':'spoke','own':'owned','play':'played','earn':'earned'}[v]
    fact = f"{S.text} {'doesn' + chr(39) + 't' if sg else 'don' + chr(39) + 't'} {v} {rest}."
    good = f"If only {pr} {past} {rest}."
    if level != 'hard': return line(f"{fact} If only {pr} ___ ({v}) {rest}.", [past])
    return line('Rewrite with If only: ' + fact, [good])
# ================= phrasal verbs =================
SEP = [("turn","turned","off","the light","it","stop a machine or light"),("turn","turned","on","the TV","it","start a machine"),("turn","turned","down","the music","it","make quieter"),("turn","turned","up","the radio","it","make louder"),
       ("put","put","on","his coat","it","wear"),("take","took","off","his shoes","them","remove clothes"),("pick","picked","up","the phone","it","lift"),("put","put","off","the meeting","it","postpone"),("call","called","off","the match","it","cancel"),
       ("fill","filled","in","the form","it","complete"),("look","looked","up","the word","it","search in a dictionary"),("throw","threw","away","the rubbish","it","put in the bin"),("give","gave","up","smoking","it","stop"),("set","set","up","a company","it","start"),
       ("try","tried","on","the jacket","it","test the size"),("write","wrote","down","the number","it","record on paper"),("hand","handed","in","the homework","it","give to the teacher"),("work","worked","out","the answer","it","calculate"),("switch","switched","off","the heating","it","stop a machine"),("pick","picked","up","the children","them","collect"),
       ("take","took","back","the book","it","return"),("bring","brought","up","the children","them","raise"),("show","showed","off","the new car","it","display proudly"),("cut","cut","down","the tree","it","fell"),("knock","knocked","down","the old wall","it","demolish")]
INSEP = [("look","looked","after","the children","them","take care of"),("look","looked","for","the keys","them","search for"),("get","got","on","the bus","it","board"),("get","got","off","the train","it","leave a vehicle"),("run","ran","into","an old friend","him","meet by chance"),("come","came","across","an old photo","it","find by chance"),
         ("deal","dealt","with","the problem","it","handle"),("get","got","over","the flu","it","recover from"),("look","looked","into","the problem","it","investigate"),("go","went","through","the documents","them","examine carefully"),("depend","depended","on","the weather","it","be determined by")]
IRRBASE = {}
def pv_sent(S, v, vp, part, obj, mood, order='std'):
    if mood == 'aff': return f"{S.text} {vp} {part} {obj}."
    if mood == 'neg': return f"{S.text} didn't {v} {part} {obj}."
    return f"Did {S.mid} {v} {part} {obj}?"
def pv_sent_pron(S, v, vp, part, pron, mood, sep):
    if sep:
        if mood == 'aff': return f"{S.text} {vp} {pron} {part}."
        if mood == 'neg': return f"{S.text} didn't {v} {pron} {part}."
        return f"Did {S.mid} {v} {pron} {part}?"
    if mood == 'aff': return f"{S.text} {vp} {part} {pron}."
    if mood == 'neg': return f"{S.text} didn't {v} {part} {pron}."
    return f"Did {S.mid} {v} {part} {pron}?"
SB = [Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('Karim','sg','he',True),Subj('Dilya','sg','she',True),Subj('My brother','sg','he'),Subj('My sister','sg','she'),Subj('My parents','pl','they'),Subj('The students','pl','they'),Subj('I','i','i'),Subj('We','pl','we'),Subj('They','pl','they')]
def gen_pv(level, rng):
    S = rng.pick(SB); mood = mood3(rng); sep = rng.pick([True, True, False])
    v, vp, part, obj, pron, gloss = rng.pick(SEP if sep else INSEP)
    if obj in ('his coat','his shoes','his') : pass
    if obj.startswith('his '):
        obj = POSS[S.pron] + obj[3:] if S.pron in POSS else obj
    # tom's coat etc: use possessive of subject
    full = pv_sent(S, v, vp, part, obj, mood)
    blank = full.replace(f" {part} ", " ___ ", 1)
    if level == 'easy': return line(blank + f" ({gloss})", [part])
    if level == 'medium':
        if rng.pick([0,1]):
            if mood == 'aff': return line(f"{S.text} ___ {obj}. ({v} {part})", [f"{vp} {part}"])
            if mood == 'neg': return line(f"{S.text} ___ {obj}. ({v} {part}, negative)", [f"didn't {v} {part}", f"did not {v} {part}"])
            return line(f"___ {S.mid} ___ {obj}? ({v} {part})", ['Did'], [f"{v} {part}"])
        return line(blank + f" ({gloss})", [part])
    k = rng.pick(['pron','pron','fix','fix','move'])
    if k == 'pron':
        if obj in ('smoking',): return None
        ans = [pv_sent_pron(S, v, vp, part, pron, mood, sep)]
        return line('Replace the object with a pronoun: ' + full, ans)
    if k == 'fix':
        if sep and obj != 'smoking':
            bad = pv_sent_pron(S, v, vp, part, pron, mood, False)
            if mood == 'aff': bad = f"{S.text} {vp} {part} {pron}."
            return line('Correct the mistake: ' + bad, [pv_sent_pron(S, v, vp, part, pron, mood, True)])
        else:
            bad = pv_sent_pron(S, v, vp, part, pron, mood, True)
            return line('Correct the mistake: ' + bad, [pv_sent_pron(S, v, vp, part, pron, mood, False)])
    if not sep or obj == 'smoking': return None
    # move particle
    alt = (f"{S.text} {vp} {obj} {part}." if mood == 'aff' else (f"{S.text} didn't {v} {obj} {part}." if mood == 'neg' else f"Did {S.mid} {v} {obj} {part}?"))
    return line('Put the particle in another position: ' + full, [alt])
def gen_misc2_jobs(C):
    return {'causative-have-something-done': lambda: gen_topic(gen_caus, C, 101),
            'wish-and-if-only': lambda: gen_topic(gen_wish, C, 102),
            'phrasal-verbs-separable-and-inseparable': lambda: gen_topic(gen_pv, C, 103)}
