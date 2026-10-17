from lib import *
from passive import gen_topic
SUBJD = [Subj('I','i','i'),Subj('You','you','you'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),
 Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('My brother','sg','he'),Subj('Our teacher','sg','she'),Subj('My parents','pl','they'),Subj('The students','pl','they')]
def _be(S): return 'am' if S.kind == 'i' else ('is' if S.kind == 'sg' else 'are')
def _bep(S): return 'was' if S.kind in ('i','sg') else 'were'
# adjective + preposition: (adj, [preps], objects)
ADJ = [("afraid",["of"],["spiders","the dark","flying","dogs","heights"]),("good",["at"],["maths","chess","drawing","languages","cooking"]),
 ("interested",["in"],["history","music","science","politics","art"]),("proud",["of"],["his work","her team","the result","their school"]),
 ("keen",["on"],["football","sport","travelling","reading"]),("responsible",["for"],["the project","the keys","this class"]),
 ("famous",["for"],["its food","its mountains","its old buildings"]),("angry",["with","at"],["the driver","the waiter","his brother"]),
 ("worried",["about"],["the exam","the weather","the results","money"]),("tired",["of"],["waiting","the noise","this weather"]),
 ("similar",["to"],["mine","this one","her sister's"]),("different",["from","to"],["the others","mine"]),
 ("married",["to"],["a doctor","a teacher","an engineer"]),("surprised",["at","by"],["the news","the price","the result"]),
 ("excited",["about"],["the trip","the party","the holiday"]),("bad",["at"],["sport","dancing","spelling","maths"]),
 ("fond",["of"],["chocolate","music","animals"]),("jealous",["of"],["his friends","her success"]),("full",["of"],["water","people","books"]),
 ("capable",["of"],["winning","doing it","more"]),("scared",["of"],["snakes","exams","the doctor"]),("crazy",["about"],["football","pizza","films"]),
 ("polite",["to"],["everyone","the guests"]),("rude",["to"],["the waiter","her teacher"]),("kind",["to"],["animals","children"]),("late",["for"],["school","work","the lesson"]),
 ("ready",["for"],["the test","the trip","dinner"]),("sorry",["for"],["the delay","his mistake"]),("satisfied",["with"],["the service","their work","the room"]),
 ("disappointed",["with","by"],["the film","the result"]),("pleased",["with"],["the gift","the news"]),("serious",["about"],["the course","his studies"]),
 ("typical",["of"],["him","this city"]),("aware",["of"],["the problem","the risk"]),("nervous",["about"],["the interview","the exam"]),
 ("sure",["about","of"],["the answer","that"]),("allergic",["to"],["nuts","cats","dust"]),("fed up",["with"],["the noise","homework"]),("bored",["with"],["the film","this game"])]
# verb + preposition: (base, s, past, pp?, [preps], objects)
VERB = [("depend","depends","depended",["on"],["the weather","the price","the teacher"]),("listen","listens","listened",["to"],["music","the radio","the teacher"]),
 ("wait","waits","waited",["for"],["the bus","a friend","the results"]),("believe","believes","believed",["in"],["ghosts","hard work","himself"]),
 ("belong","belongs","belonged",["to"],["my uncle","the school","a club"]),("worry","worries","worried",["about"],["money","the exam","her health"]),
 ("complain","complains","complained",["about"],["the food","the noise","the service"]),("succeed","succeeds","succeeded",["in"],["the exam","business","finding a job"]),
 ("insist","insists","insisted",["on"],["paying","going","a refund"]),("rely","relies","relied",["on"],["his friends","the internet","her parents"]),
 ("agree","agrees","agreed",["with"],["his boss","the teacher","me"]),("laugh","laughs","laughed",["at"],["the joke","the clown","his mistakes"]),
 ("pay","pays","paid",["for"],["the tickets","dinner","the repairs"]),("think","thinks","thought",["about","of"],["the problem","the future","the trip"]),
 ("dream","dreams","dreamed",["of","about"],["a new car","becoming a pilot","a holiday"]),("suffer","suffers","suffered",["from"],["headaches","stress","the heat"]),
 ("concentrate","concentrates","concentrated",["on"],["the lesson","her work","the road"]),("participate","participates","participated",["in"],["the contest","the project","the discussion"]),
 ("apologise","apologises","apologised",["for"],["being late","the mistake"]),("apply","applies","applied",["for"],["a job","a visa","the course"]),
 ("look","looks","looked",["at"],["the picture","the board","the map"]),("search","searches","searched",["for"],["his keys","a flat","information"]),
 ("talk","talks","talked",["about"],["the film","football","the exam"]),("speak","speaks","spoke",["to"],["the manager","her mum"]),("arrive","arrives","arrived",["at","in"],["the station","the airport"]),
  ("hear","hears","heard",["about","of"],["the news","the accident"]),("care","cares","cared",["about"],["his friends","the environment"]),
  ("focus","focuses","focused",["on"],["the details","her studies"]),("object","objects","objected",["to"],["the plan","the decision"])]
# noun + prep fixed templates: (aff, neg, q, answer preps)
NOUNP = [
 ("There is a good reason ___ this delay.","There isn't a good reason ___ this delay.","Is there a good reason ___ this delay?",["for"]),
 ("Tom has a lot of respect ___ his teachers.","Tom doesn't have much respect ___ his teachers.","Does Tom have respect ___ his teachers?",["for"]),
 ("The cause ___ the fire was a cigarette.","The cause ___ the fire wasn't a cigarette.","Was a cigarette the cause ___ the fire?",["of"]),
 ("There has been an increase ___ prices.","There hasn't been an increase ___ prices.","Has there been an increase ___ prices?",["in"]),
 ("We need a solution ___ this problem.","We don't need a solution ___ this problem.","Do we need a solution ___ this problem?",["to"]),
 ("Anna has a lot of interest ___ art.","Anna doesn't have much interest ___ art.","Does Anna have an interest ___ art?",["in"]),
 ("There is a big difference ___ the two cities.","There isn't a big difference ___ the two cities.","Is there a big difference ___ the two cities?",["between"]),
 ("He has no experience ___ teaching.","He doesn't have much experience ___ teaching.","Does he have any experience ___ teaching?",["of","in"]),
 ("Their attitude ___ work is positive.","Their attitude ___ work isn't positive.","Is their attitude ___ work positive?",["to","towards"]),
 ("I have no idea ___ the answer.","I don't have any idea ___ the answer.","Do you have any idea ___ the answer?",["about","of"]),
 ("She wrote a letter ___ the manager.","She didn't write a letter ___ the manager.","Did she write a letter ___ the manager?",["to"]),
 ("There is no need ___ a visa.","There isn't any need ___ a visa.","Is there a need ___ a visa?",["for"]),
 ("My advice ___ you is to study hard.","My advice ___ you isn't to study less.","Is my advice ___ you clear?",["to","for"]),
 ("The demand ___ new phones is high.","The demand ___ new phones isn't high.","Is the demand ___ new phones high?",["for"]),
 ("He is on holiday ___ two weeks.","He isn't on holiday ___ two weeks.","Is he on holiday ___ two weeks?",["for"]),
 ("There is a problem ___ my phone.","There isn't a problem ___ my phone.","Is there a problem ___ my phone?",["with"]),
 ("What is the matter ___ you?","Nothing is the matter ___ you.","Is something the matter ___ you?",["with"]),
 ("Her knowledge ___ history is excellent.","Her knowledge ___ history isn't excellent.","Is her knowledge ___ history excellent?",["of","about"]),
 ("The key ___ success is hard work.","The key ___ success isn't luck.","Is hard work the key ___ success?",["to"]),
 ("I read an article ___ climate change.","I didn't read an article ___ climate change.","Did you read an article ___ climate change?",["about","on"]),
 ("There was a lot of damage ___ the building.","There wasn't any damage ___ the building.","Was there any damage ___ the building?",["to"]),
 ("He gave me a reply ___ my email.","He didn't give me a reply ___ my email.","Did he give you a reply ___ your email?",["to"]),
]
CONF = ["at","in","on","of","for","to","with","about","from","by"]
def _pick_wrong(rng, ok):
    c = [p for p in CONF if p not in ok and not (p in ('at','by') and 'at' in ok) ]
    return rng.pick(c)
def _hint(level, rng, ok):
    if level == 'hard': return ''
    pool = [p for p in CONF if p not in ok]
    rng.shuffle(pool)
    opts = [ok[0]] + pool[:2 if level == 'easy' else 4]
    rng.shuffle(opts)
    return ' (' + ' / '.join(opts) + ')'
def gen_dp(level, rng):
    k = rng.pick(['adj','adj','verb','verb','verb','noun','noun','fix','fix'])
    S = rng.pick(SUBJD)
    if k == 'adj':
        adj, ok, objs = rng.pick(ADJ); obj = rng.pick(objs); b = _be(S); h = _hint(level, rng, ok)
        t = rng.pick(['aff','neg','q','past'])
        if t == 'aff': return line(f"{S.text} {b} {adj} ___ {obj}.{h}", ok)
        if t == 'neg': return line(f"{S.text} {b}n't {adj} ___ {obj}.".replace("amn't","'m not").replace("I 'm not","I'm not") + h, ok) if S.kind != 'i' else line(f"I'm not {adj} ___ {obj}.{h}", ok)
        if t == 'q':
            if S.text == 'I': return None
            return line(f"{_cp(b)} {S.mid} {adj} ___ {obj}?{h}", ok)
        return line(f"{S.text} {_bep(S)} {adj} ___ {obj} yesterday.{h}", ok)
    if k == 'verb':
        b0, s3, pa, ok, objs = rng.pick(VERB); obj = rng.pick(objs); h = _hint(level, rng, ok)
        t = rng.pick(['aff','neg','q','past'])
        if t == 'aff': return line(f"{S.text} {s3 if S.sg else b0} ___ {obj}.{h}", ok)
        if t == 'neg': return line(f"{S.text} {'doesn' if S.sg else 'don'}'t {b0} ___ {obj}.{h}", ok)
        if t == 'q':
            if S.text == 'I': return None
            return line(f"{'Does' if S.sg else 'Do'} {S.mid} {b0} ___ {obj}?{h}", ok)
        return line(f"{S.text} {pa} ___ {obj} last week.{h}", ok)
    if k == 'noun':
        a, n, q, ok = rng.pick(NOUNP); t = rng.pick(['a','n','q'])
        s = {'a':a,'n':n,'q':q}[t]
        return line(s + _hint(level, rng, ok), ok)
    if level == 'easy': return None
    # fix
    ft = rng.pick(['adj','verb','noun'])
    if ft == 'adj':
        adj, ok, objs = rng.pick(ADJ); obj = rng.pick(objs); w = _pick_wrong(rng, ok); b = _be(S)
        if S.text == 'I': b = 'am'
        return line(f"Correct the mistake: {S.text} {b} {adj} {w} {obj}.", [f"{S.text} {b} {adj} {p} {obj}." for p in ok])
    if ft == 'verb':
        b0, s3, pa, ok, objs = rng.pick(VERB); obj = rng.pick(objs); w = _pick_wrong(rng, ok)
        return line(f"Correct the mistake: {S.text} {pa} {w} {obj} last week.", [f"{S.text} {pa} {p} {obj} last week." for p in ok])
    a, n, q, ok = rng.pick(NOUNP); w = _pick_wrong(rng, ok)
    bad = a.replace('___', w)
    return line(f"Correct the mistake: {bad}", [a.replace('___', p) for p in ok])
def _cp(s): return s[0].upper() + s[1:]
def gen_dp_jobs(C):
    return {'dependent-prepositions': lambda: gen_topic(gen_dp, C, 140)}
