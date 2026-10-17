from lib import *
from passive import gen_topic
from tense import negs

# (base, s, past, pattern)  pattern: ger | inf | obj | bare | both
GER = [("enjoy","enjoys","enjoyed"),("finish","finishes","finished"),("avoid","avoids","avoided"),("mind","minds","minded"),("suggest","suggests","suggested"),("practise","practises","practised"),("keep","keeps","kept"),
       ("imagine","imagines","imagined"),("miss","misses","missed"),("consider","considers","considered"),("deny","denies","denied"),("dislike","dislikes","disliked"),("risk","risks","risked"),("postpone","postpones","postponed"),("quit","quits","quit")]
INF = [("want","wants","wanted"),("decide","decides","decided"),("hope","hopes","hoped"),("plan","plans","planned"),("promise","promises","promised"),("refuse","refuses","refused"),("agree","agrees","agreed"),
       ("learn","learns","learned"),("manage","manages","managed"),("need","needs","needed"),("offer","offers","offered"),("expect","expects","expected"),("pretend","pretends","pretended"),("fail","fails","failed"),("afford","affords","afforded"),("choose","chooses","chose"),("arrange","arranges","arranged"),("threaten","threatens","threatened")]
OBJ = [("ask","asks","asked"),("tell","tells","told"),("advise","advises","advised"),("allow","allows","allowed"),("invite","invites","invited"),("teach","teaches","taught"),("remind","reminds","reminded"),("persuade","persuades","persuaded"),("order","orders","ordered"),("encourage","encourages","encouraged"),("warn","warns","warned"),("force","forces","forced")]
BARE = [("let","lets","let"),("make","makes","made")]
BOTH = [("like","likes","liked"),("love","loves","loved"),("hate","hates","hated"),("prefer","prefers","preferred"),("start","starts","started"),("begin","begins","began"),("continue","continues","continued")]
SG = [Subj('I','i','i'),Subj('You','you','you'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('My brother','sg','he'),Subj('My sister','sg','she'),Subj('My parents','pl','they'),Subj('The students','pl','they')]
OBJS = [Subj('me','i','i'),Subj('you','you','you'),Subj('him','sg','he'),Subj('her','sg','she'),Subj('us','pl','we'),Subj('them','pl','they'),Subj('Tom','sg','he',True),Subj('Anna','sg','she',True)]
def ovalue(o): return o.text
def tense_pick(rng): return rng.pick(['pres','pres','past'])
def aux_forms(S, tense, neg):
    if tense == 'pres':
        if neg: return ("doesn't" if S.kind == 'sg' else "don't"), ("does not" if S.kind == 'sg' else "do not")
    else:
        if neg: return "didn't", "did not"
    return None, None
def build(rng, kind=None):
    kind = kind or rng.pick(['ger','ger','inf','inf','obj','bare','both'])
    S = rng.pick(SG); tense = tense_pick(rng)
    V = rng.pick([v for v in VERBS if not v.ach]); comp = rng.pick(V.comps)
    pool = {'ger':GER,'inf':INF,'obj':OBJ,'bare':BARE,'both':BOTH}[kind]
    b, s3, ps = rng.pick(pool)
    O = rng.pick([o for o in OBJS if o.text != S.mid and o.objp != S.objp]) if kind in ('obj','bare') else None
    if kind == 'ger': form = V.ing; ans = [V.ing]
    elif kind == 'inf': form = 'to ' + V.base; ans = ['to ' + V.base]
    elif kind == 'obj': form = 'to ' + V.base; ans = ['to ' + V.base]
    elif kind == 'bare': form = V.base; ans = [V.base]
    else: form = V.ing; ans = [V.ing, 'to ' + V.base]
    return dict(kind=kind, S=S, tense=tense, V=V, comp=comp, b=b, s3=s3, ps=ps, O=O, form=form, ans=ans)
def verb_finite(d, neg=False):
    S, t = d['S'], d['tense']
    if t == 'past': return ("didn't " + d['b']) if neg else d['ps']
    if neg: return ("doesn't " if S.kind == 'sg' else "don't ") + d['b']
    return d['s3'] if S.kind == 'sg' else d['b']
def sentence_with(d, blank_text, mood='aff'):
    S, O = d['S'], d['O']; mid = O.text if O else ''
    tail = (f"{mid} " if mid else '') + f"{blank_text} {d['comp']}"
    if mood == 'q':
        aux = 'Did' if d['tense'] == 'past' else ('Does' if S.kind == 'sg' else 'Do')
        return f"{aux} {S.mid} {d['b']} {tail}?"
    return f"{S.text} {verb_finite(d, mood == 'neg')} {tail}."
def gen_ger_inf(level, rng):
    d = build(rng); mood = rng.pick(['aff','aff','neg','q'])
    hint = f"({d['V'].base})"
    if level == 'easy':
        return line(sentence_with(d, '___ ' + hint, mood).replace('___ ' + hint + ' ', '___ ' + hint + ' ', 1) if False else sentence_with(d, '___ ' + hint, mood), d['ans'])
    if level == 'medium':
        return line(sentence_with(d, '___ ' + hint, mood), d['ans'])
    k = rng.pick(['fix','fix','fix','neg','q','rewrite'])
    aff = sentence_with(d, d['form'], 'aff')
    if k == 'neg': return line('Make a negative sentence: ' + aff, [sentence_with(d, d['form'], 'neg')])
    if k == 'q': return line('Make a question: ' + aff, [sentence_with(d, d['form'], 'q')])
    if k == 'rewrite':
        if d['kind'] == 'both':
            return line('Rewrite with the other form: ' + sentence_with(d, d['ans'][0], 'aff'), [sentence_with(d, d['ans'][1], 'aff')])
        return None
    # fix
    wrong = {'ger':[('to ' + d['V'].base), d['V'].base],'inf':[d['V'].ing, d['V'].base],'obj':[d['V'].ing, d['V'].base, 'that ' + d['V'].base],'bare':['to ' + d['V'].base, d['V'].ing],'both':[d['V'].base]}[d['kind']]
    w = rng.pick(wrong)
    if d['kind'] == 'both':
        return None
    bad = sentence_with(d, w, 'aff')
    good = [aff]
    if bad == aff: return None
    return line('Correct the mistake: ' + bad, good)

# ---- meaning-changing verbs (stop / remember / forget / try / regret / go on) ----
MC = [
 # (stem sentence with ___ , ans, hint verb)
 ("He stopped ___ (smoke) because it was bad for his health.", ["smoking"]),
 ("He stopped ___ (buy) some bread on the way home.", ["to buy"]),
 ("She stopped ___ (talk) when the teacher came in.", ["talking"]),
 ("They stopped ___ (rest) because they were tired.", ["to rest"]),
 ("I remember ___ (lock) the door. I did it before I left.", ["locking"]),
 ("Remember ___ (lock) the door tonight!", ["to lock"]),
 ("Tom remembered ___ (post) the letter, so it arrived on time.", ["to post"]),
 ("Anna remembers ___ (meet) the president when she was a child.", ["meeting"]),
 ("I forgot ___ (call) my mother, so she was worried.", ["to call"]),
 ("I'll never forget ___ (see) the sea for the first time.", ["seeing"]),
 ("Don't forget ___ (bring) your passport.", ["to bring"]),
 ("She tried ___ (open) the window, but it was stuck.", ["to open"]),
 ("Try ___ (add) some salt. It might taste better.", ["adding"]),
 ("We tried ___ (call) him, but nobody answered.", ["to call"]),
 ("He tried ___ (turn) the heating off to see if the noise stopped.", ["turning"]),
 ("I regret ___ (tell) him the secret. It was a mistake.", ["telling"]),
 ("We regret ___ (inform) you that the flight is cancelled.", ["to inform"]),
 ("After the lesson he went on ___ (talk) about his holiday for an hour.", ["talking"]),
 ("After the introduction, she went on ___ (explain) the new rule.", ["to explain"]),
 ("I meant ___ (call) you, but I forgot.", ["to call"]),
 ("This new job means ___ (work) at weekends.", ["working"]),
]
MC_NEG = [
 ("He didn't stop ___ (smoke) until last year.", ["smoking"]),
 ("Did you remember ___ (lock) the door?", ["to lock"]),
 ("Do you remember ___ (meet) her last summer?", ["meeting"]),
 ("I didn't forget ___ (bring) my passport.", ["to bring"]),
 ("Did she regret ___ (leave) the job?", ["leaving"]),
 ("Why did they stop ___ (play) when it started to rain?", ["playing"]),
 ("We didn't try ___ (open) the box with a knife.", ["to open"]),
 ("Don't forget ___ (switch) off the lights.", ["to switch"]),
 ("Does he remember ___ (give) you the key?", ["giving"]),
 ("Have you tried ___ (eat) it with honey?", ["eating"]),
]
PREPS = [("good at","draw"),("interested in","learn"),("afraid of","fly"),("tired of","wait"),("keen on","swim"),("proud of","win"),("responsible for","clean"),("worried about","fail"),("fond of","cook"),("bored with","study"),
         ("famous for","sing"),("excited about","travel"),("capable of","lift"),("sorry for","be"),("surprised at","hear")]
PREP_V = [("look forward to","meet"),("insist on","pay"),("apologise for","be"),("succeed in","find"),("dream of","live"),("think of","move"),("depend on","know"),("object to","wait"),("get used to","wake up"),("talk about","change")]
PREP_OBJ = {"draw":"portraits","learn":"chess","fly":"in storms","wait":"in queues","swim":"in the sea","win":"the match","clean":"the classroom","fail":"the exam","cook":"fish","study":"grammar","sing":"folk songs","travel":"to Spain","lift":"heavy boxes","be":"late","hear":"the news",
          "meet":"your family","pay":"for dinner","find":"a flat","live":"abroad","move":"to a new city","know":"the answer","wake up":"early","change":"jobs"}
def ger_form(v):
    f = {"draw":"drawing","learn":"learning","fly":"flying","wait":"waiting","swim":"swimming","win":"winning","clean":"cleaning","fail":"failing","cook":"cooking","study":"studying","sing":"singing","travel":"travelling","lift":"lifting","be":"being","hear":"hearing","meet":"meeting","pay":"paying","find":"finding","live":"living","move":"moving","know":"knowing","wake up":"waking up","change":"changing"}
    return f[v]
ADJ_INF = [("easy","find"),("hard","understand"),("nice","meet"),("happy","help"),("glad","see"),("sorry","hear"),("difficult","explain"),("important","arrive"),("ready","start"),("sure","win"),("surprised","find"),("afraid","say"),("pleased","hear"),("lucky","have"),("likely","rain"),("impossible","forget")]
ADJ_OBJ = {"find":"the way","understand":"this rule","meet":"you","help":"them","see":"you again","hear":"that","explain":"the problem","arrive":"on time","start":"now","win":"the game","say":"anything","have":"such good friends","rain":"tomorrow","forget":"her face"}
ADJ_INF_V = {"find":"find","understand":"understand","meet":"meet","help":"help","see":"see","hear":"hear","explain":"explain","arrive":"arrive","start":"start","win":"win","say":"say","have":"have","rain":"rain","forget":"forget"}
def gen_ger_inf_x(level, rng):
    k = rng.pick(['mc','mc','mcneg','prep','prepv','adj','adj'])
    if k in ('mc','mcneg'):
        q, a = rng.pick(MC if k == 'mc' else MC_NEG)
        if level == 'easy': return line(q, a)
        if level == 'medium': return line(q, a)
        # hard: correct the mistake with the wrong form
        full = q.replace('___ (', '@@(')
        m = __import__('re').match(r'^(.*)@@\((\w+)\)(.*)$', full)
        pre, v, post = m.group(1), m.group(2), m.group(3)
        correct = a[0]
        wrongs = {'smoking':'to smoke','to buy':'buying','talking':'to talk','to rest':'resting','locking':'to lock','to lock':'locking','to post':'posting','meeting':'to meet','to call':'calling','seeing':'to see','to bring':'bringing','to open':'opening',
                  'adding':'to add','turning':'to turn','telling':'to tell','to inform':'informing','to explain':'explaining','working':'to work','leaving':'to leave','playing':'to play','to switch':'switching','giving':'to give','eating':'to eat'}
        w = wrongs.get(correct)
        if not w: return None
        stem = (pre + '@@' + post)
        bad = stem.replace('@@', w); good = stem.replace('@@', correct)
        return line('Correct the mistake: ' + bad, [good])
    if k == 'prep':
        adj, v = rng.pick(PREPS); S = rng.pick(SG); mood = rng.pick(['aff','neg','q'])
        o = PREP_OBJ[v]; g = ger_form(v); be = be_pres(S) if S.kind != 'i' else 'am'
        if mood == 'aff': base = f"{S.text} {be} {adj} {g} {o}."
        elif mood == 'neg': base = f"{S.text} {be}n't {adj} {g} {o}." if S.kind != 'i' else f"{S.text} am not {adj} {g} {o}."
        else: base = f"{cap(be)} {S.mid} {adj} {g} {o}?"
        if level in ('easy','medium'):
            if mood == 'aff': return line(f"{S.text} {be} {adj} ___ ({v}) {o}.", [g])
            if mood == 'neg': return line(f"{S.text} {be}n't {adj} ___ ({v}) {o}." if S.kind != 'i' else f"{S.text} am not {adj} ___ ({v}) {o}.", [g])
            return line(f"{cap(be)} {S.mid} {adj} ___ ({v}) {o}?", [g])
        w = f"{S.text} {be} {adj} to {v} {o}." if mood == 'aff' else (f"{S.text} {be}n't {adj} to {v} {o}." if mood == 'neg' and S.kind != 'i' else (f"{S.text} am not {adj} to {v} {o}." if mood == 'neg' else f"{cap(be)} {S.mid} {adj} to {v} {o}?"))
        return line('Correct the mistake: ' + w, [base])
    if k == 'prepv':
        vb, v = rng.pick(PREP_V); S = rng.pick(SG); o = PREP_OBJ[v]; g = ger_form(v)
        pres = rng.pick([True, False])
        if vb in ('get used to',):
            be = be_pres(S) if S.kind != 'i' else 'am'; mood = rng.pick(['aff','neg','q'])
            if mood == 'aff': base, qq = f"{S.text} {be} used to {g} {o}.", f"{S.text} {be} used to ___ ({v}) {o}."
            elif mood == 'neg': base, qq = (f"{S.text} {be}n't used to {g} {o}." if S.kind != 'i' else f"{S.text} am not used to {g} {o}."), (f"{S.text} {be}n't used to ___ ({v}) {o}." if S.kind != 'i' else f"{S.text} am not used to ___ ({v}) {o}.")
            else: base, qq = f"{cap(be)} {S.mid} used to {g} {o}?", f"{cap(be)} {S.mid} used to ___ ({v}) {o}?"
            if level != 'hard': return line(qq, [g])
            return line('Correct the mistake: ' + base.replace(g, 'to ' + v if v != 'wake up' else 'to wake up').replace('used to to','used to'), [base]) if False else line('Correct the mistake: ' + base.replace(' used to ' + g, ' used to ' + v), [base])
        mood = rng.pick(['aff','neg','q'])
        a = 'does' if S.kind == 'sg' else 'do'; vv = vb.split(' ')
        first, rest = vb.split(' ', 1)
        if mood == 'aff':
            f1 = {'look':'looks','insist':'insists','apologise':'apologises','succeed':'succeeds','dream':'dreams','think':'thinks','depend':'depends','object':'objects','talk':'talks'}[first]
            fin = f1 if S.kind == 'sg' else first
            base = f"{S.text} {fin} {rest} {g} {o}."; qq = f"{S.text} {fin} {rest} ___ ({v}) {o}."
        elif mood == 'neg':
            base = f"{S.text} {a}n't {first} {rest} {g} {o}."; qq = f"{S.text} {a}n't {first} {rest} ___ ({v}) {o}."
        else:
            base = f"{a.capitalize()} {S.mid} {first} {rest} {g} {o}?"; qq = f"{a.capitalize()} {S.mid} {first} {rest} ___ ({v}) {o}?"
        if level != 'hard': return line(qq, [g])
        return line('Correct the mistake: ' + base.replace(g, v if v != 'wake up' else 'wake up'), [base])
    # adjective + to-infinitive
    adj, v = rng.pick(ADJ_INF); o = ADJ_OBJ[v]; S = rng.pick(SG); mood = rng.pick(['aff','neg','q'])
    be = be_pres(S) if S.kind != 'i' else 'am'
    if adj in ('easy','hard','difficult','important','impossible','likely','nice'):
        it = 'It'
        if mood == 'aff': base = f"It is {adj} to {v} {o}."; qq = f"It is {adj} ___ ({v}) {o}."
        elif mood == 'neg': base = f"It isn't {adj} to {v} {o}."; qq = f"It isn't {adj} ___ ({v}) {o}."
        else: base = f"Is it {adj} to {v} {o}?"; qq = f"Is it {adj} ___ ({v}) {o}?"
    else:
        if mood == 'aff': base = f"{S.text} {be} {adj} to {v} {o}."; qq = f"{S.text} {be} {adj} ___ ({v}) {o}."
        elif mood == 'neg': base = (f"{S.text} {be}n't {adj} to {v} {o}." if S.kind != 'i' else f"{S.text} am not {adj} to {v} {o}."); qq = base.replace(f" to {v} ", f" ___ ({v}) ")
        else: base = f"{cap(be)} {S.mid} {adj} to {v} {o}?"; qq = f"{cap(be)} {S.mid} {adj} ___ ({v}) {o}?"
    if level != 'hard': return line(qq, ['to ' + v])
    w = base.replace(f" to {v} ", f" {v}ing ") if False else base.replace(f" to {v}", f" {ger_form_safe(v)}")
    return line('Correct the mistake: ' + w, [base])
def ger_form_safe(v):
    if v == 'rain': return 'raining'
    if v.endswith('e') and v != 'be': return v[:-1] + 'ing'
    if v in ('win','begin','run','swim'): return v + v[-1] + 'ing'
    return v + 'ing'
def gen_gi_all(level, rng):
    return gen_ger_inf(level, rng) if rng.pick([0,1,1]) else gen_ger_inf_x(level, rng)
def gen_gi_jobs(C):
    return {'gerunds-and-infinitives': lambda: gen_topic(gen_gi_all, C, 82)}
