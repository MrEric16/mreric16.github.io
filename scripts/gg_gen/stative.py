from lib import *
from passive import gen_topic
from tense import negs
def cap1(s): return s[0].upper() + s[1:]
SP = [Subj('I','i','i'),Subj('You','you','you'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),
      Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('My brother','sg','he'),Subj('My sister','sg','she'),Subj('The students','pl','they'),Subj('My parents','pl','they')]
# person-subject state verbs: base, s, ing, objects
ST = [
("know","knows","knowing",["the answer","her phone number","the way to the station","the capital of France","my address"]),
("love","loves","loving",["chocolate","dogs","summer","this song","pizza"]),
("want","wants","wanting",["a glass of water","a new bike","some help","a holiday","a sandwich"]),
("need","needs","needing",["help","a coffee","more time","a new pen","a rest"]),
("understand","understands","understanding",["the question","this rule","the story","the instructions","the problem"]),
("believe","believes","believing",["your story","the news","his excuse","my promise"]),
("like","likes","liking",["tea","rainy days","this film","fish","jazz"]),
("hate","hates","hating",["getting up early","spiders","exams","cold weather","queues"]),
("prefer","prefers","preferring",["tea to coffee","cats to dogs","the window seat","summer to winter"]),
("own","owns","owning",["a big house","two cars","a small shop","a farm"]),
("remember","remembers","remembering",["my birthday","your name","the way home","the first day at school"]),
("recognise","recognises","recognising",["your voice","that man","this song","the street"]),
("doubt","doubts","doubting",["his story","the result","your answer"]),
("agree","agrees","agreeing",["with you","with the teacher","with my plan"]),
("seem","seems","seeming",["very happy","a bit tired","angry","nervous"]),
]
# thing-subject state verbs
TH = [
("cost","costs","costing",["ten pounds","a lot of money","too much"],[("The ticket",0),("This book",0),("These shoes",1),("The tickets",1)]),
("belong","belongs","belonging",["to the teacher","to me","to my brother"],[("This bag",0),("These keys",1),("The pen",0),("Those books",1)]),
("contain","contains","containing",["a lot of sugar","three rooms","no salt"],[("This juice",0),("The box",0),("These biscuits",1),("The flat",0)]),
("taste","tastes","tasting",["delicious","sweet","terrible"],[("The soup",0),("This cake",0),("These apples",1),("The tea",0)]),
("smell","smells","smelling",["nice","of fish","wonderful"],[("The kitchen",0),("This flower",0),("These roses",1),("The bread",0)]),
("sound","sounds","sounding",["great","strange","interesting"],[("That idea",0),("Your plan",0),("Those songs",1),("His story",0)]),
("weigh","weighs","weighing",["ten kilos","a lot","two tons"],[("The bag",0),("This box",0),("These stones",1),("The parcel",0)]),
]
CUE_NOW = ['right now','at the moment']
# dual-meaning: stative sense / dynamic sense
DS = [("have","has","two sisters"),("have","has","a new car"),("have","has","a big garden"),("have","has","brown eyes"),
      ("think","thinks","that you are right"),("think","thinks","it is a good idea"),("think","thinks","the exam is difficult"),
      ("see","sees","what you mean"),("see","sees","the point"),("look","looks","tired"),("look","looks","very happy"),("look","looks","like her mother")]
DD = [("have","having","lunch"),("have","having","a shower"),("have","having","a party"),("have","having","a great time"),("have","having","a break"),
      ("think","thinking","about the exam"),("think","thinking","about the holiday"),("see","seeing","the doctor"),("look","looking","at the photos"),("look","looking","for the keys"),
      ("look","looking","out of the window"),("taste","tasting","the soup"),("taste","tasting","the cake"),("smell","smelling","the flowers"),("weigh","weighing","the fruit"),("weigh","weighing","the parcel")]
DYC = ['Look!','Listen!','At the moment,','Right now,','Be quiet!','Hurry up!']
CONTRACTABLE = ('I','You','He','She','We','They','Tom','Anna')
def CT(S): return ("'m" if S.kind=='i' else ("'s" if S.kind=='sg' else "'re"))
BEP = {'I':'am','you':'are','we':'are','they':'are','he':'is','she':'is','it':'is'}
def sform(S, b, s): return s if S.kind == 'sg' else b
def be(S): return be_pres(S)
def aux(S): return 'Does' if S.kind == 'sg' else 'Do'
def dont(S): return "doesn't" if S.kind == 'sg' else "don't"
def pick_item(rng):
    r = rng.pick(['st','st','st','th','ds','dd','dd','ord','ord2'])
    S = rng.pick(SP)
    if r == 'st':
        b, s, ing, objs = rng.pick(ST); o = rng.pick(objs)
        return dict(r=r, S=S, b=b, s=s, ing=ing, o=o, cue=rng.pick(['', '', ' '+rng.pick(CUE_NOW)]))
    if r == 'th':
        b, s, ing, objs, subs = rng.pick(TH); sub = rng.pick(subs); o = rng.pick(objs)
        T = Subj(sub[0], 'pl' if sub[1] else 'sg', 'they' if sub[1] else 'he', objp='them' if sub[1] else 'it')
        return dict(r=r, S=T, b=b, s=s, ing=ing, o=o, cue=rng.pick(['', ' '+rng.pick(CUE_NOW)]))
    if r == 'ds':
        b, s, o = rng.pick(DS); return dict(r=r, S=S, b=b, s=s, ing=b+'ing', o=o, cue='')
    if r == 'dd':
        b, ing, o = rng.pick(DD); return dict(r=r, S=S, b=b, s=b+'s', ing=ing, o=o, cue='', lead=rng.pick(DYC))
    V = rng.pick(VERBS); c = rng.pick(V.comps)
    return dict(r=r, S=S, b=V.base, s=V.s, ing=V.ing, o=c, cue='', lead=rng.pick(DYC) if r=='ord' else '', habit=rng.pick(['every day','on Sundays','every week','twice a week','in the evening']))
def parts(it):
    """returns (kind, lead, S, base, s, ing, o, cue) and the correct affirmative / negative / question strings"""
    S = it['S']; r = it['r']; lead = it.get('lead','')
    pre = (lead + ' ') if lead else ''
    sub = (S.text if lead.endswith('!') else S.mid) if lead else S.text
    cont = r in ('dd','ord')
    if r == 'ord2':
        tail = f" {it['habit']}"
    else: tail = it['cue']
    if cont:
        ans = [f"{be(S)} {it['ing']}"]
        ans.append(f"{CT(S)} {it['ing']}")
        neg = [f"{be(S)} not {it['ing']}", f"{be(S)}n't {it['ing']}" if S.kind != 'i' else f"'m not {it['ing']}"]
        return dict(cont=True, pre=pre, sub=sub, tail=tail, ans=ans, neg=neg)
    ans = [sform(S, it['b'], it['s'])]
    neg = [f"{dont(S)} {it['b']}", f"{'does' if S.kind=='sg' else 'do'} not {it['b']}"]
    return dict(cont=False, pre=pre, sub=sub, tail=tail, ans=ans, neg=neg)
def hint(it, extra=''):
    return f"({extra}{it['b']})" if True else ''
def gen_stative(level, rng):
    it = pick_item(rng); p = parts(it); S = it['S']; o = it['o']; b = it['b']
    if it['r'] == 'ord2': return gen_habit(level, rng, it)
    sent = lambda mid_: f"{p['pre']}{p['sub']} {mid_} {o}{p['tail']}."
    if level == 'easy':
        if rng.pick([0,0,1]): return line(sent(f"___ ({'not / ' if False else ''}{b})"), p['ans'])
        return line(sent(f"___ (not / {b})"), p['neg'] + ([f"{be(S)}n't {it['ing']}"] if False else []) if True else p['neg'])
    if level == 'medium':
        k = rng.pick(['q','q','short','neg','two'])
        if k == 'q':
            if p['cont']: 
                qn = f"{p['pre']}___ {S.mid} ___ ({b}) {o}{p['tail']}?"; 
                return line(qn, [be(S).capitalize() if not p['pre'] else be(S).capitalize()], [it['ing']]) if False else line(qn.replace('___ ' + S.mid, '___ ' + S.mid), [cap1(be(S))], [it['ing']])
            return line(f"{cap1(p['pre'].strip()) + ' ' if p['pre'] else ''}___ {S.mid} ___ ({b}) {o}{p['tail']}?", [aux(S)], [b])
        if k == 'short' and S.kind != 'i':
            pn = pron_ans(S)
            if p['cont']:
                qq = f"{p['pre']}{cap1(be(S)) if not p['pre'] else be(S)} {S.mid} {it['ing']} {o}?"
                bp = BEP[pn]
                if rng.pick([0,1]): return line(f"{qq} Yes, {pn} ___.", [bp])
                return line(f"{qq} No, {pn} ___.", ["am not","'m not"] if bp == 'am' else [bp + "n't", bp + " not"])
            qq = f"{aux(S)} {S.mid} {b} {o}{p['tail']}?"
            ya = 'does' if S.kind == 'sg' else 'do'
            if rng.pick([0,1]): return line(f"{qq} Yes, {pn} ___.", [ya])
            return line(f"{qq} No, {pn} ___.", negs(ya))
        if k == 'two' and not p['cont']:
            return line(sent(f"___ ___ ({b})"), [dont(S), ('does' if S.kind=='sg' else 'do') + ' not'] , [b]) if False else line(sent(f"___ (not / {b})"), p['neg'])
        return line(sent(f"___ (not / {b})"), p['neg']) if rng.pick([0,1]) else line(sent(f"___ ({b})"), p['ans'])
    # hard
    k = rng.pick(['fix','fix','fix','neg','q'])
    aff = sent(' '.join(p['ans'][0:1]))
    if p['cont']:
        affs = [sent(p['ans'][0])]
        if S.text in CONTRACTABLE:
            affs.append(f"{p['pre']}{p['sub']}{CT(S)} {it['ing']} {o}{p['tail']}.")
    else: affs = [aff]
    if k == 'fix':
        if p['cont']:
            wrong = sent(sform(S, it['b'], it['s']))
            return line('Correct the mistake: ' + wrong, affs)
        wrong = sent(f"{be(S)} {it['ing']}")
        return line('Correct the mistake: ' + wrong, affs)
    if k == 'neg':
        nf = [sent(n) for n in p['neg']]
        return line('Make a negative sentence: ' + affs[0], nf)
    qs = (f"{cap1(p['pre'].strip()) + ' ' if p['pre'] else ''}{('' if p['pre'] else '')}" )
    if p['cont']:
        q = f"{(p['pre'] + be(S)) if p['pre'] else cap1(be(S))} {S.mid} {it['ing']} {o}{p['tail']}?"
    else:
        q = f"{aux(S)} {S.mid} {b} {o}{p['tail']}?"
    return line('Make a question: ' + affs[0], [q])
def gen_habit(level, rng, it):
    S = it['S']; b = it['b']; o = it['o']; h = it['habit']
    full = f"{S.text} {sform(S, b, it['s'])} {o} {h}."
    if level == 'easy': return line(f"{S.text} ___ ({b}) {o} {h}.", [sform(S, b, it['s'])])
    if level == 'medium':
        k = rng.pick(['q','neg','short'])
        if k == 'neg': return line(f"{S.text} ___ (not / {b}) {o} {h}.", [f"{dont(S)} {b}", f"{'does' if S.kind=='sg' else 'do'} not {b}"])
        if k == 'q' or S.kind == 'i': return line(f"___ {S.mid} ___ ({b}) {o} {h}?", [aux(S)], [b])
        pn = pron_ans(S); ya = 'does' if S.kind == 'sg' else 'do'
        return line(f"{aux(S)} {S.mid} {b} {o} {h}? Yes, {pn} ___.", [ya])
    k = rng.pick(['fix','neg','q'])
    if k == 'fix':
        w = f"{S.text} {be(S)} {it['ing']} {o} {h}."
        return line('Correct the mistake: ' + w, [full])
    if k == 'neg': return line('Make a negative sentence: ' + full, [f"{S.text} {dont(S)} {b} {o} {h}.", f"{S.text} {'does' if S.kind=='sg' else 'do'} not {b} {o} {h}."])
    return line('Make a question: ' + full, [f"{aux(S)} {S.mid} {b} {o} {h}?"])
def gen_stative_jobs(C):
    return {'stative-verbs': lambda: gen_topic(gen_stative, C, 70)}
