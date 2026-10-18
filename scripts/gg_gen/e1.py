from lib import *
from verbs import Verb
from passive import gen_topic
def _cp(s): return s[0].upper() + s[1:]
POS = {'i':'my','you':'your','he':'his','she':'her','we':'our','they':'their'}
SX = [Subj('I','i','i'),Subj('You','you','you'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),
      Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),
      Subj('My brother','sg','he'),Subj('My sister','sg','she'),Subj('Our teacher','sg','she'),Subj('My parents','pl','they'),Subj('The students','pl','they')]
def _q(S): return S.text if S.proper or S.text == 'I' else S.mid   # subject inside a question
def _v(S, V): return V.s if S.kind == 'sg' else V.base
def _dont(S): return "doesn't" if S.kind == 'sg' else "don't"
def _did(S): return 'did'

# ============ 1. irregular verbs ============
_IR = """go|goes|went|gone|going|to school;to the market;to the cinema;home early;to the park
see|sees|saw|seen|seeing|a film;the manager;a big bird;the doctor
break|breaks|broke|broken|breaking|a window;a plate;a glass;a phone
begin|begins|began|begun|beginning|a new book;the lesson;a new course
catch|catches|caught|caught|catching|the bus;a cold;a fish;the ball
choose|chooses|chose|chosen|choosing|a book;a gift;a new phone
come|comes|came|come|coming|home late;to the party;back early
cut|cuts|cut|cut|cutting|the cake;a piece of paper;the grass
do|does|did|done|doing|the homework;the shopping;the washing-up
fall|falls|fell|fallen|falling|off a bike;down the stairs;into the river
feel|feels|felt|felt|feeling|ill;tired;nervous
find|finds|found|found|finding|a wallet;a key;a coin;a cheap flat
fly|flies|flew|flown|flying|to Dubai;to London;to Istanbul
forget|forgets|forgot|forgotten|forgetting|the password;an umbrella;the answer
hear|hears|heard|heard|hearing|a noise;the news;a strange sound
hide|hides|hid|hidden|hiding|the keys;a present;a secret
hold|holds|held|held|holding|a meeting;a baby;the door
keep|keeps|kept|kept|keeping|a diary;a secret;a pet rabbit
know|knows|knew|known|knowing|the answer;the way;the phone number
leave|leaves|left|left|leaving|home early;the office;a note
lose|loses|lost|lost|losing|a key;the match;a phone;a bag
pay|pays|paid|paid|paying|the bill;for the tickets;in cash
put|puts|put|put|putting|the book on the desk;the keys in the bag
say|says|said|said|saying|hello;goodbye;nothing
sit|sits|sat|sat|sitting|on the sofa;at the back;next to the window
sleep|sleeps|slept|slept|sleeping|late;badly;in a tent
spend|spends|spent|spent|spending|a lot of money;the weekend at home;two hours on it
stand|stands|stood|stood|standing|at the door;in a queue;near the window
steal|steals|stole|stolen|stealing|a bike;a wallet
tell|tells|told|told|telling|a story;a lie;the truth;a joke
think|thinks|thought|thought|thinking|about it;about the answer
throw|throws|threw|thrown|throwing|a ball;a stone;an old shoe
understand|understands|understood|understood|understanding|the question;the rules;the lesson
wake|wakes|woke|woken|waking|up early;up late
wear|wears|wore|worn|wearing|a suit;a red coat;glasses;a uniform
win|wins|won|won|winning|the match;a prize;the race;a medal
grow|grows|grew|grown|growing|vegetables;tomatoes;flowers
lend|lends|lent|lent|lending|a pen;a bike;some notes
ring|rings|rang|rung|ringing|the bell;the dentist;a friend"""
IRR = []
for _l in _IR.split('\n'):
    p = _l.split('|'); IRR.append(Verb(p[0], p[1], p[2], p[3], p[4], p[5].split(';'), ''))
_have = {v.base for v in IRR}
for _v0 in VERBS:
    if not _v0.past.endswith('ed') and _v0.base not in _have and _v0.base not in ('read',): IRR.append(_v0); _have.add(_v0.base)
PASTCUE = ['yesterday','last night','last week','two days ago','last Monday','a week ago','last year']
def _has(S): return 'has' if S.kind == 'sg' else 'have'
def gen_irr(level, rng):
    S = rng.pick(SX); V = rng.pick(IRR); comp = rng.pick(V.comps); cue = rng.pick(PASTCUE)
    k = rng.pick({'easy':['past','past','pp','pp','neg','q','neg_pp','q_pp'],
                  'medium':['forms','forms','pp','had','neg','q','neg_pp','q_pp','past'],
                  'hard':['cm_pp','cm_past','cm_reg','neg','q','neg_pp','q_pp','rew','cm_pp','cm_past']}[level])
    if k == 'past':
        return line(f"{S.text} ___ ({V.base}) {comp} {cue}.", [V.past])
    if k == 'pp':
        adv = rng.pick(['already','never','just','often'])
        h = ' (past participle)' if level == 'medium' else ''
        return line(f"{S.text} {_has(S)} {adv} ___ ({V.base}) {comp}." + h, [V.pp])
    if k == 'had':
        return line(f"By the time we arrived, {S.mid if not S.proper and S.text != 'I' else S.text} had already ___ ({V.base}) {comp}.", [V.pp])
    if k == 'neg':
        return line(f"{S.text} didn't ___ ({V.base}) {comp} {cue}.", [V.base])
    if k == 'q':
        return line(f"Did {_q(S)} ___ ({V.base}) {comp} {cue}?", [V.base])
    if k == 'neg_pp':
        return line(f"{S.text} {_has(S)}n't ___ ({V.base}) {comp}.", [V.pp])
    if k == 'q_pp':
        return line(f"{_cp(_has(S))} {_q(S)} ever ___ ({V.base}) {comp}?", [V.pp])
    if k == 'forms':
        if rng.pick([0, 1]):
            return line(f"{V.base} - ___ - ___ (past simple, past participle)", [V.past], [V.pp])
        return line(f"Write the past simple and the past participle of '{V.base}': ___ ___", [V.past], [V.pp])
    if k == 'cm_pp':
        if V.past == V.pp: return None
        return line(f"Correct the mistake: {S.text} {_has(S)} {V.past} {comp}.", [f"{S.text} {_has(S)} {V.pp} {comp}."])
    if k == 'cm_past':
        if V.past == V.pp: return None
        return line(f"Correct the mistake: {S.text} {V.pp} {comp} {cue}.", [f"{S.text} {V.past} {comp} {cue}."])
    if k == 'cm_reg':
        if V.base in ('put','cut','read') or V.base.endswith('e'): return None
        return line(f"Correct the mistake: {S.text} {V.base}ed {comp} {cue}.", [f"{S.text} {V.past} {comp} {cue}."])
    if k == 'rew':
        sm = S.text if S.proper or S.text == 'I' else S.mid
        return line(f"Rewrite in the past simple, starting with 'Yesterday': {S.text} {_v(S, V)} {comp}.", [f"Yesterday {sm} {V.past} {comp}.", f"Yesterday, {sm} {V.past} {comp}."])
    return None

# ============ 2. subject-verb agreement ============
# (subject, number, list of (verb-free predicates for be), list of verb phrases (base, s, rest))
SING = [("The news","good;surprising;on at six;interesting"),("The information","useful;correct;in the book;wrong"),("The advice","helpful;good;simple"),
        ("The furniture","new;old;very expensive;in the garage"),("The homework","easy;difficult;on the desk"),("The luggage","heavy;in the car;at the airport"),
        ("Mathematics","difficult;my favourite subject;interesting"),("Physics","hard;a useful subject"),("Economics","a popular subject;interesting"),
        ("The traffic","terrible;heavy today;slow"),("The weather","lovely;awful today;hot"),("The equipment","new;very expensive;in the cupboard"),
        ("Everyone","ready;happy;in the hall"),("Everybody","here;late;excited"),("Somebody","at the door;in the kitchen"),
        ("Each of the students","busy;ready"),("One of my friends","a doctor;in Dubai"),("Every student","tired;ready")]
PLUR = [("The trousers","too long;very old;on the chair"),("My jeans","new;too small;in the wash"),("The scissors","on the table;sharp;in the drawer"),
        ("These glasses","expensive;mine;too big"),("The clothes","clean;in the wardrobe;wet"),("The police","here;at the door;very quick"),
        ("The people","friendly;in the street;happy"),("Tom and Anna","friends;in the garden;late"),("My brother and I","in the same class;ready"),
        ("A number of students","late;absent today;ill"),("A number of the books","old;new"),("Many people","afraid of flying;at the party")]
THE_NUM = [("The number of students","small;growing;high"),("The number of cars","increasing;very high;large"),("The number of visitors","low;rising")]
LEX_S = [("The news","arrive","arrives","quickly"),("The information","change","changes","every day"),("Everyone","like","likes","music"),("Everybody","want","wants","a holiday"),
         ("Each pupil","know","knows","the answer"),("Somebody","wait","waits","outside"),("The traffic","start","starts","early"),("The weather","change","changes","often"),
         ("Each student","bring","brings","a book"),("One of my friends","play","plays","the guitar"),("Every teacher","love","loves","this school")]
LEX_P = [("The police","arrive","arrive","quickly"),("The people","wait","wait","outside"),("My jeans","fit","fit","well"),("The clothes","dry","dry","fast"),
         ("A number of students","study","study","in the library"),("Tom and Anna","walk","walk","to school"),("My brother and I","play","play","chess"),
         ("Many people","travel","travel","by train"),("The scissors","cut","cut","well")]
def _sv_pred(rng):
    pool = [(s, 'sg', p) for s, p in SING + THE_NUM] + [(s, 'pl', p) for s, p in PLUR]
    s, n, p = rng.pick(pool)
    return s, n, rng.pick(p.split(';'))
def gen_sv2(level, rng):
    if rng.pick([0,0,0,0,0,1,1,1,1]): return gen_sv_lex(level, rng)
    return _sv_be(level, rng)
def _sv_be(level, rng):
    k = rng.pick({'easy':['be','be','be','neg','q'],'medium':['be','neg','q','neg'],'hard':['cm','cm','cm','neg_t','q_t']}[level])
    s, n, p = _sv_pred(rng); isv = 'is' if n == 'sg' else 'are'; wrong = 'are' if n == 'sg' else 'is'
    sl = s if s.startswith(('Tom',)) else s[0].lower() + s[1:]
    sl = sl.replace('My brother and I', 'my brother and I')
    if k == 'be':
        h = ' (be)' if level == 'easy' else ''
        return line(f"{s} ___ {p}." + h, [isv])
    if k == 'neg': return line(f"{s} ___ {p}. (not / be)", [f"{isv}n't", f"{isv} not"])
    if k == 'q': return line(f"___ {sl} {p}? (be)", [isv])
    if k == 'cm': return line(f"Correct the mistake: {s} {wrong} {p}.", [f"{s} {isv} {p}."])
    if k == 'neg_t': return line(f"Make a negative sentence: {s} {isv} {p}.", [f"{s} {isv}n't {p}.", f"{s} {isv} not {p}."])
    return line(f"Make a question: {s} {isv} {p}.", [f"{_cp(isv)} {sl} {p}?"])
def gen_sv_lex(level, rng):
    sing = rng.pick([True, False])
    s, b, s3, rest = rng.pick(LEX_S if sing else LEX_P)
    v = s3; base = b if sing else b
    # for singular subjects the base form is LEX_S[1], third-person is [2]; for plural subjects both [1] and [2] are base forms
    k = rng.pick({'easy':['aff','aff','neg','q'],'medium':['aff','neg','q','neg'],'hard':['cm','cm','neg_t','q_t']}[level])
    do = "doesn't" if sing else "don't"; dd = 'does' if sing else 'do'
    sl = s if s.startswith('Tom') else s[0].lower() + s[1:]
    sl = sl.replace('My brother and I', 'my brother and I')
    if k == 'aff': return line(f"{s} ___ ({b}) {rest}.", [v])
    if k == 'neg': return line(f"{s} ___ (not / {b}) {rest}.", [f"{do} {b}", f"{dd} not {b}"])
    if k == 'q': return line(f"___ {sl} {b} {rest}? (do)", [dd])
    wrong = b if sing else (b + 's' if not b.endswith(('s', 'y', 'ch')) else b + 'es')
    if k == 'cm':
        if not sing and b.endswith('y'): return None
        return line(f"Correct the mistake: {s} {wrong} {rest}.", [f"{s} {v} {rest}."])
    if k == 'neg_t': return line(f"Make a negative sentence: {s} {v} {rest}.", [f"{s} {do} {b} {rest}.", f"{s} {dd} not {b} {rest}."])
    return line(f"Make a question: {s} {v} {rest}.", [f"{_cp(dd)} {sl} {b} {rest}?"])

# ============ 3. time clauses ============
def _is3(S): return S.kind == 'sg'
# (main phrase with {o} = an object, conjunction, clause subject (None = a person), clause verb (base, 3sg), rest)
TC = [("call {o}","when",None,"arrive","arrives","at the station"),("wait here","until",None,"come","comes","back"),("have lunch","before",None,"leave","leaves","the house"),
      ("phone {o}","as soon as",None,"land","lands","in Dubai"),("give {o} the book","after",None,"finish","finishes","it"),("do the washing-up","when",None,"finish","finishes","dinner"),
      ("text {o}","as soon as",None,"get","gets","home"),("stay in the library","until",("the library",1),"close","closes","at nine"),("go for a walk","after",None,"do","does","the homework"),
      ("buy some bread","before",None,"go","goes","home"),("make a cup of tea","as soon as",None,"arrive","arrives","at work"),("start the lesson","when",("the headteacher",1),"come","comes","in"),
      ("tidy the room","before",None,"come","comes","home"),("cook dinner","after",None,"get","gets","back"),("send {o} a message","when",None,"reach","reaches","the hotel"),
      ("play football","as soon as",None,"finish","finishes","the lesson"),("watch a film","after",None,"eat","eats","dinner"),("write an email","as soon as",None,"hear","hears","the news"),
      ("go to bed","when",None,"finish","finishes","the book"),("take a taxi","after",None,"leave","leaves","the party"),("ring {o}","before",None,"go","goes","to the shop"),
      ("pay the bill","as soon as",None,"get","gets","the money"),("see the doctor","when",None,"feel","feels","ill"),("wash the car","after",None,"clean","cleans","the garage"),
      ("keep working","until",("the bell",1),"ring","rings",""),("make a plan","before",None,"meet","meets","the others"),("go out","when",("the rain",1),"stop","stops",""),
      ("start the meeting","as soon as",("the manager",1),"arrive","arrives",""),("stay at home","until",("the storm",1),"end","ends",""),("leave","before",("the film",1),"start","starts",""),
      ("clap","when",("the singer",1),"come","comes","on stage"),("open the window","after",("the room",1),"get","gets","hot")]
OBJ = ['my mother','my father','the manager','the doctor','our neighbour','my cousin']
def _tc_row(rng):
    S1 = rng.pick(SX); S2 = rng.pick([s for s in SX if s.text != S1.text])
    main, conj, fx, cb, cs, crest = rng.pick(TC)
    main = main.replace('{o}', rng.pick(OBJ))
    if fx: sm2, three = fx[0], True
    else: sm2, three = (S2.mid if not S2.proper and S2.text != 'I' else S2.text), _is3(S2)
    cl = f"{sm2} {cs if three else cb} {crest}".strip()
    cl_b = f"{sm2} ___ ({cb}) {crest}".strip()
    return S1, S2, main, conj, cb, cs, three, sm2, crest, cl, cl_b
def gen_tc(level, rng):
    S1, S2, main, conj, cb, cs, three, sm2, crest, cl, cl_b = _tc_row(rng)
    m0, mrest = main.split(' ', 1) if ' ' in main else (main, '')
    mm = S1.text; ans = cs if three else cb
    k = rng.pick({'easy':['b','b','b','neg','q'],'medium':['b2','b2','neg','q2','cm'],'hard':['cm','cm','neg_t','q_t','join','join']}[level])
    if k == 'b':
        return line(f"{mm} will {main} {conj} {cl_b}.", [ans])
    if k == 'b2':
        return line(f"{mm} ___ ({m0}) {mrest} {conj} {cl_b}.".replace('  ', ' '), [f"will {m0}", f"'ll {m0}"], [ans])
    if k == 'neg':
        return line(f"{mm} won't {main} {conj} {cl_b}.", [ans])
    if k == 'q':
        return line(f"Will {_q(S1)} {main} {conj} {cl_b}?", [ans])
    if k == 'q2':
        return line(f"___ {_q(S1)} {m0} {mrest} {conj} {cl_b}? (will)".replace('  ', ' '), ['Will'], [ans])
    if k == 'cm':
        return line(f"Correct the mistake: {mm} will {main} {conj} {sm2} will {cb} {crest}.".replace('  ', ' ').replace(' .', '.'), [f"{mm} will {main} {conj} {cl}."])
    if k == 'neg_t':
        return line(f"Make a negative sentence: {mm} will {main} {conj} {cl}.", [f"{mm} won't {main} {conj} {cl}.", f"{mm} will not {main} {conj} {cl}."])
    if k == 'q_t':
        return line(f"Make a question: {mm} will {main} {conj} {cl}.", [f"Will {_q(S1)} {main} {conj} {cl}?"])
    s2 = f"{_cp(sm2)} will {cb} {crest}.".replace(' .', '.')
    a = f"{mm} will {main} {conj} {cl}."
    b = f"{_cp(conj)} {cl}, {_q(S1)} will {main}."
    return line(f"Join with '{conj}': {mm} will {main}. {s2}", [a, b])

# ============ 4. for, since, ago, already, yet, still, just ============
FOR = ['two years','three weeks','a long time','ten minutes','five months','six hours','a few days','about an hour','a year','ages']
SINCE = ['2019','Monday','last summer',"8 o'clock",'January','last year','yesterday morning','2015','Friday','the autumn']
AGO = ['two years ago','three weeks ago','ten minutes ago','a month ago','five days ago','an hour ago','a year ago','two hours ago']
DUR = [v for v in VERBS if v.dur]
TASKS = [("finish","finished","finished","the homework"),("clean","cleaned","cleaned","the kitchen"),("call","called","called","the dentist"),("buy","bought","bought","the tickets"),
         ("read","read","read","the email"),("send","sent","sent","the message"),("make","made","made","dinner"),("wash","washed","washed","the car"),("pay","paid","paid","the bill"),
         ("book","booked","booked","a table"),("write","wrote","written","the report"),("tidy","tidied","tidied","the room"),("water","watered","watered","the plants"),
         ("feed","fed","fed","the cat"),("lock","locked","locked","the door"),("post","posted","posted","the letter"),("learn","learned","learned","the poem"),
         ("answer","answered","answered","the question"),("mark","marked","marked","the tests"),("take","took","taken","the photos"),("fix","fixed","fixed","the bike"),
         ("charge","charged","charged","the phone"),("pack","packed","packed","the bags"),("plan","planned","planned","the trip"),("cook","cooked","cooked","the rice"),
         ("open","opened","opened","the window"),("repair","repaired","repaired","the computer"),("hear","heard","heard","the news"),("see","saw","seen","the film"),
         ("eat","ate","eaten","breakfast"),("find","found","found","the keys"),("choose","chose","chosen","a present"),("tell","told","told","the teacher"),("do","did","done","the shopping")]
def gen_fs(level, rng):
    S = rng.pick(SX); h = _has(S)
    b, pa, pp, rest = rng.pick(TASKS)
    k = rng.pick({'easy':['for','since','ago','just','yet_n','yet_q','still','already'],
                  'medium':['for','since','ago','just','yet_n','yet_q','still','already','hl'],
                  'hard':['cm_since','cm_ago','cm_yet','cm_just','neg_yet','q_yet','put_just','cm_for']}[level])
    H = {'easy': {'fs':' (for / since)','ago':' (ago / for)','jy':' (already / yet)','st':' (still / yet)'},
         'medium': {'fs':' (for / since / ago)','ago':' (for / since / ago)','jy':' (already / yet / still / just)','st':' (already / yet / still / just)'},
         'hard': {'fs':'','ago':'','jy':'','st':''}}[level]
    if k in ('for', 'since', 'cm_since', 'cm_for'):
        V = rng.pick(DUR); comp = rng.pick(V.comps)
        if k == 'for': return line(f"{S.text} {h} {V.pp} {comp} ___ {rng.pick(FOR)}." + H['fs'], ['for'])
        if k == 'since': return line(f"{S.text} {h} {V.pp} {comp} ___ {rng.pick(SINCE)}." + H['fs'], ['since'])
        if k == 'cm_since':
            per = rng.pick(FOR); return line(f"Correct the mistake: {S.text} {h} {V.pp} {comp} since {per}.", [f"{S.text} {h} {V.pp} {comp} for {per}."])
        per = rng.pick(SINCE); return line(f"Correct the mistake: {S.text} {h} {V.pp} {comp} for {per}.", [f"{S.text} {h} {V.pp} {comp} since {per}."])
    if k == 'hl':
        V = rng.pick(DUR); comp = rng.pick(V.comps)
        return line(f"{S.text} {h} {V.pp} {comp} ___ {rng.pick(SINCE)}. (for / since)", ['since'])
    if k == 'ago':
        return line(f"{S.text} {pa} {rest} {rng.pick(AGO).replace(' ago', '')} ___." + H['ago'], ['ago'])
    if k == 'just':
        return line(f"{S.text} {h} ___ {pp} {rest}. (a moment ago)" + H['jy'], ['just'])
    if k == 'already':
        return line(f"{S.text} {h} ___ {pp} {rest}. (earlier than expected)" + H['jy'], ['already'])
    if k == 'yet_n':
        return line(f"{S.text} {h}n't {pp} {rest} ___." + H['jy'], ['yet'])
    if k == 'yet_q':
        return line(f"{_cp(h)} {_q(S)} {pp} {rest} ___?" + H['jy'], ['yet'])
    if k == 'still':
        return line(f"{S.text} ___ {h}n't {pp} {rest}. (it takes longer than expected)" + H['st'], ['still'])
    if k == 'cm_ago':
        per = rng.pick(AGO); return line(f"Correct the mistake: {S.text} {h} {pp} {rest} {per}.", [f"{S.text} {pa} {rest} {per}."])
    if k == 'cm_yet':
        return line(f"Correct the mistake: {S.text} {h}n't {pp} {rest} already.", [f"{S.text} {h}n't {pp} {rest} yet.", f"{S.text} {h} not {pp} {rest} yet."])
    if k == 'cm_just':
        return line(f"Correct the mistake: {S.text} {h} just {pp} {rest} yesterday.", [f"{S.text} {pa} {rest} yesterday."])
    if k == 'neg_yet':
        return line(f"Make a negative sentence with 'yet': {S.text} {h} {pp} {rest}.", [f"{S.text} {h}n't {pp} {rest} yet.", f"{S.text} {h} not {pp} {rest} yet."])
    if k == 'q_yet':
        return line(f"Make a question with 'yet': {S.text} {h} {pp} {rest}.", [f"{_cp(h)} {_q(S)} {pp} {rest} yet?"])
    if k == 'put_just':
        return line(f"Put 'just' in the sentence: {S.text} {h} {pp} {rest}.", [f"{S.text} {h} just {pp} {rest}."])
    return None

def gen_e1_jobs(C):
    return {'irregular-verbs': lambda: gen_topic(gen_irr, C, 301),
            'subject-verb-agreement': lambda: gen_topic(gen_sv2, C, 302),
            'time-clauses': lambda: gen_topic(gen_tc, C, 303),
            'for-since-ago-already-yet-still-just': lambda: gen_topic(gen_fs, C, 304)}
