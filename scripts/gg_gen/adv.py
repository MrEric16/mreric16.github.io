from lib import *
from passive import gen_topic
def _cp(s): return s[0].upper() + s[1:]
FREQ = [("always","100%"),("usually","90%"),("often","70%"),("sometimes","40%"),("rarely","10%"),("never","0%")]
SUBJF = [Subj('I','i','i'),Subj('You','you','you'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),
 Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('My brother','sg','he'),Subj('Our teacher','sg','she'),Subj('My parents','pl','they')]
BEA = [("late","is","am","are"),("tired","is","am","are"),("busy","is","am","are"),("at home","is","am","are"),("on time","is","am","are"),("hungry","is","am","are"),("polite","is","am","are"),("nervous","is","am","are")]
def _be(S): return 'am' if S.kind == 'i' else ('is' if S.kind == 'sg' else 'are')

def gen_freq(level, rng):
    adv, pc = rng.pick(FREQ); S = rng.pick(SUBJF)
    k = rng.pick({'easy':['pc','pc','be','lex','lex'],'medium':['lex','be','modal','neg','q','pc','fix'],'hard':['neg','q','fix','fix','modal','be','lex']}[level])
    if k == 'pc':
        V, comp = vcomp(rng)
        if adv == 'never': adv, pc = 'always', '100%'
        v = V.s if S.sg else V.base
        h = ' (always / usually / often / sometimes / rarely / never)' if level != 'easy' else ''
        return line(f"{S.text} ___ {v} {comp}. ({pc} of the time)" + h, [adv])
    if k == 'lex':
        V, comp = vcomp(rng); v = V.s if S.sg else V.base
        base = f"{S.text} {v} {comp}."
        if level == 'easy': return line(f"{S.text} ___ {v} {comp}. ({adv})" if False else f"Put '{adv}' in the sentence: {base}", [f"{S.text} {adv} {v} {comp}."])
        return line(f"Put '{adv}' in the sentence: {base}", [f"{S.text} {adv} {v} {comp}."])
    if k == 'be':
        w, _, _, _ = rng.pick(BEA); b = _be(S)
        return line(f"Put '{adv}' in the sentence: {S.text} {b} {w}.", [f"{S.text} {b} {adv} {w}."])
    if k == 'modal':
        V, comp = vcomp(rng)
        m = rng.pick(['can','will','should','must'])
        if adv == 'never' and m == 'must': m = 'can'
        return line(f"Put '{adv}' in the sentence: {S.text} {m} {V.base} {comp}.", [f"{S.text} {m} {adv} {V.base} {comp}."])
    if k == 'neg':
        if adv in ('never','rarely'): return None
        V, comp = vcomp(rng); d = 'doesn' if S.sg else 'don'
        if level == 'easy': return None
        return line(f"Make a negative sentence with '{adv}': {S.text} {V.s if S.sg else V.base} {comp}.", [f"{S.text} {d}'t {adv} {V.base} {comp}."])
    if k == 'q':
        V, comp = vcomp(rng)
        if S.text == 'I': return None
        d = 'Does' if S.sg else 'Do'; sm = S.mid
        if adv == 'never': adv, pc = 'ever', ''
        if adv == 'ever':
            return line(f"Make a question with 'ever': {S.text} {V.s if S.sg else V.base} {comp}.", [f"{d} {sm} ever {V.base} {comp}?"])
        if level == 'easy': return None
        return line(f"Make a question with '{adv}': {S.text} {V.s if S.sg else V.base} {comp}.", [f"{d} {sm} {adv} {V.base} {comp}?"])
    # fix
    if level == 'easy': return None
    kk = rng.pick(['a','b','c'])
    if kk == 'a':
        V, comp = vcomp(rng); v = V.s if S.sg else V.base
        return line(f"Correct the mistake: {S.text} {v} {comp} {adv}.", [f"{S.text} {adv} {v} {comp}."])
    if kk == 'b':
        w, _, _, _ = rng.pick(BEA); b = _be(S)
        return line(f"Correct the mistake: {S.text} {adv} {b} {w}.", [f"{S.text} {b} {adv} {w}."])
    V, comp = vcomp(rng); v = V.s if S.sg else V.base
    d = 'Does' if S.sg else 'Do'
    if S.text == 'I': return None
    return line(f"Correct the mistake: {d} {S.mid} {V.base} {adv} {comp}?" if False else f"Correct the mistake: {S.text} don't {adv} {V.base} {comp}.".replace("don't", "doesn't" if S.sg else "don't") if False else f"Correct the mistake: {S.text} {adv} {'doesn' if S.sg else 'don'}'t {V.base} {comp}.", [f"{S.text} {'doesn' if S.sg else 'don'}'t {adv} {V.base} {comp}.", f"{S.text} never {V.s if S.sg else V.base} {comp}."]) if adv in ('often','usually','sometimes','always') else None

# adjectives or adverbs
AA = [("careful","carefully"),("quick","quickly"),("slow","slowly"),("loud","loudly"),("quiet","quietly"),("happy","happily"),("easy","easily"),("angry","angrily"),
 ("bad","badly"),("good","well"),("polite","politely"),("clear","clearly"),("gentle","gently"),("patient","patiently"),("nervous","nervously"),("neat","neatly"),
 ("beautiful","beautifully"),("terrible","terribly"),("fluent","fluently"),("safe","safely"),("brave","bravely"),("perfect","perfectly"),("serious","seriously"),("calm","calmly")]
MV = [("sing","sings","sang"),("drive","drives","drove"),("speak","speaks","spoke"),("work","works","worked"),("write","writes","wrote"),("walk","walks","walked"),
 ("play","plays","played"),("explain","explains","explained"),("answer","answers","answered"),("dance","dances","danced"),("cook","cooks","cooked"),("paint","paints","painted"),("swim","swims","swam"),("read","reads","read")]
SAME = [("fast","fast"),("hard","hard"),("late","late"),("early","early")]
LINK = [("looks","look"),("sounds","sound"),("smells","smell"),("tastes","taste"),("feels","feel"),("seems","seem")]
LADJ = ["good","bad","wonderful","strange","terrible","delicious","great","fresh"]
NOUN = ["driver","singer","speaker","worker","writer","dancer","cook","player","student","swimmer"]
def gen_aa(level, rng):
    S = rng.pick(SUBJF); a, ad = rng.pick(AA); mv = rng.pick(MV)
    k = rng.pick({'easy':['adv','adv','adv','adj','link','same','gw'],'medium':['adv','adj','link','same','hardly','gw','fix'],'hard':['adv','link','same','hardly','fix','fix','fix','gw']}[level])
    if k == 'adv':
        t = rng.pick(['aff','neg','q'])
        if t == 'aff': s = f"{S.text} {mv[1] if S.sg else mv[0]} ___ ({a})."
        elif t == 'neg': s = f"{S.text} {'doesn' if S.sg else 'don'}'t {mv[0]} ___ ({a})."
        else:
            if S.text == 'I': return None
            s = f"{'Does' if S.sg else 'Do'} {S.mid} {mv[0]} ___ ({a})?"
        return line(s, [ad])
    if k == 'adj':
        n = rng.pick(NOUN)
        if level == 'easy': return line(f"{S.text} {_be(S) if False else ''}".strip() and f"He is a ___ ({a}) {n}." , [a])
        return line(f"She is a ___ ({a}) {n}.", [a])
    if k == 'link':
        who = rng.pick(['The soup','The music','The flowers','This idea','The cake'])
        plur = who in ('The flowers',)
        allowed = {'The soup':['look','smell','taste'],'The music':['sound'],'The flowers':['look','smell'],'This idea':['sound','seem'],'The cake':['look','smell','taste']}[who]
        lb = rng.pick(allowed); lv = dict((y,x) for x,y in LINK)[lb]; adj = rng.pick(LADJ)
        t = rng.pick(['aff','neg'])
        lvv = lb if plur else lv
        if t == 'aff': s = f"{who} {lvv} ___ ({adj})."
        else: s = f"{who} {'don' if plur else 'doesn'}'t {lb} ___ ({adj})."
        return line(s, [adj])
    if k == 'same':
        w, w2 = rng.pick(SAME)
        mv2 = rng.pick([("drive","drives"),("work","works"),("run","runs"),("study","studies"),("arrive","arrives"),("wake up","wakes up")])
        if w in ('late','early') and mv2[0] in ('drive','run'): mv2 = ("arrive","arrives")
        if w in ('fast',) and mv2[0] in ('arrive','wake up','study'): mv2 = ("drive","drives")
        if w == 'hard' and mv2[0] in ('arrive','wake up','drive','run'): mv2 = ("work","works")
        t = rng.pick(['aff','neg'])
        s = f"{S.text} {mv2[1] if S.sg else mv2[0]} ___ ({w})." if t == 'aff' else f"{S.text} {'doesn' if S.sg else 'don'}'t {mv2[0]} ___ ({w})."
        return line(s, [w2])
    if k == 'hardly':
        if level == 'easy': return None
        V, comp = vcomp(rng)
        return line(f"Make a negative sentence with 'hardly': {S.text} {V.s if S.sg else V.base} {comp} (almost never).".replace(" (almost never)", ""), [f"{S.text} hardly {V.s if S.sg else V.base} {comp}.", f"{S.text} hardly ever {V.s if S.sg else V.base} {comp}."])
    if k == 'gw':
        n = rng.pick(['singer','driver','cook','player','speaker','swimmer'])
        h = ' (good / well)' if level != 'hard' else ''
        t = rng.pick(['a','b'])
        if t == 'a': return line(f"He is a ___ {n}." + h, ['good'])
        mvv = rng.pick([("sing","sings"),("cook","cooks"),("speak","speaks"),("swim","swims"),("drive","drives")])
        return line(f"{S.text} {mvv[1] if S.sg else mvv[0]} very ___." + h, ['well'])
    if level == 'easy': return None
    kk = rng.pick(['a','b','c','d'])
    if kk == 'a': return line(f"Correct the mistake: {S.text} {mv[1] if S.sg else mv[0]} {a}.", [f"{S.text} {mv[1] if S.sg else mv[0]} {ad}."]) if a != 'good' else None
    if kk == 'b': return line(f"Correct the mistake: She is a {ad} {rng.pick(NOUN)}.", [f"She is a {a} {'-'}".split(' -')[0] + ' ' + 'X']) if False else None
    if kk == 'c':
        lv, lb = rng.pick(LINK); adj = rng.pick(['good','strange','terrible','wonderful','great','bad'])
        if lb != 'look': return None
        adv = {'good':'well','strange':'strangely','terrible':'terribly','wonderful':'wonderfully','great':'greatly','bad':'badly'}[adj]
        return line(f"Correct the mistake: The soup looks {adv}.", [f"The soup looks {adj}."]) if adj != 'good' else line("Correct the mistake: The soup looks well.", ["The soup looks good."])
    w, w2 = rng.pick(SAME)
    return line(f"Correct the mistake: {S.text} {'works' if S.sg else 'work'} {w}ly.", [f"{S.text} {'works' if S.sg else 'work'} hard."]) if w == 'hard' else None

# adjective order
OP = ["lovely","beautiful","ugly","nice","horrible","strange","boring","wonderful"]
SZ = ["big","small","tiny","huge","large"]
AGE = ["old","new","modern","ancient"]
SH = ["round","square","oval","flat"]
COL = ["red","blue","green","black","white","yellow","brown","grey"]
ORG = ["Italian","Chinese","French","Turkish","Uzbek","Indian","German","Japanese"]
MAT = {"table":["wooden","metal","glass"],"bag":["leather","plastic","cotton"],"scarf":["silk","woollen","cotton"],"vase":["glass","clay","metal"],"hat":["straw","woollen","leather"],
 "bowl":["wooden","clay","plastic"],"carpet":["woollen","silk","cotton"],"jacket":["leather","cotton","woollen"],"clock":["wooden","metal","plastic"],"mirror":["glass","metal"],"box":["wooden","metal","plastic"],"lamp":["glass","metal","plastic"]}
def _a(w): return ('an ' if w[0] in 'aeiou' else 'a ') + w
def gen_order(level, rng):
    noun = rng.pick(list(MAT))
    cats = [('op',OP),('sz',SZ),('age',AGE),('sh',SH),('col',COL),('org',ORG),('mat',MAT[noun])]
    if noun in ('scarf','jacket','hat','carpet','bag') : cats = [c for c in cats if c[0] != 'sh']
    n = {'easy':2,'medium':3,'hard':4}[level]
    chosen = sorted(rng.shuffle(list(range(len(cats))))[:n])
    adjs = [rng.pick(cats[i][1]) for i in chosen]
    if len(set(adjs)) != len(adjs): return None
    correct = ' '.join(adjs)
    sh = adjs[:]
    for _ in range(10):
        rng.shuffle(sh)
        if sh != adjs: break
    if sh == adjs: return None
    art = 'an' if adjs[0][0] in 'aeiou' else 'a'
    t = rng.pick(['aff','neg','q'])
    verb = rng.pick(['bought','found','sold','liked','wanted'])
    base = {'bought':'buy','found':'find','sold':'sell','liked':'like','wanted':'want'}[verb]
    S = rng.pick([s for s in SUBJF if s.text not in ('I','You')])
    mixed = ' / '.join(sh)
    if t == 'aff': s = f"{S.text} {verb} ___ {noun}. ({mixed})"
    elif t == 'neg': s = f"{S.text} didn't {base} ___ {noun}. ({mixed})"
    else: s = f"Did {S.mid} {base} ___ {noun}? ({mixed})"
    if level == 'hard' and rng.pick([0,1]):
        bad = f"{S.text} {verb} {art} {' '.join(sh)} {noun}."
        art2 = 'an' if adjs[0][0] in 'aeiou' else 'a'
        art_bad = 'an' if sh[0][0] in 'aeiou' else 'a'
        bad = f"{S.text} {verb} {art_bad} {' '.join(sh)} {noun}."
        return line(f"Correct the mistake: {bad}", [f"{S.text} {verb} {art2} {correct} {noun}."])
    return line(s, [f"{art} {correct}"])

def gen_adv_jobs(C):
    return {'adverbs-of-frequency': lambda: gen_topic(gen_freq, C, 135),
            'adjectives-or-adverbs': lambda: gen_topic(gen_aa, C, 136),
            'adjective-order': lambda: gen_topic(gen_order, C, 137)}
