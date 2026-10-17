from lib import *
from passive import gen_topic
SUBJ_W = [Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('Jasur','sg','he',True),Subj('Dilnoza','sg','she',True),
 Subj('My brother','sg','he'),Subj('My sister','sg','she'),Subj('Our teacher','sg','she'),Subj('My dad','sg','he'),Subj('My mum','sg','she'),Subj('Mr Karimov','sg','he',True)]
THINGS = ["The film","The road","The hotel","The test","The room","The journey","This city","The food","The idea","The lesson"]
# person adjectives: (root, adj)
PADJ = [("success","successful"),("care","careful"),("hope","hopeful"),("help","helpful"),("thought","thoughtful"),("health","healthy"),("wealth","wealthy"),("fame","famous"),
 ("courage","courageous"),("patience","patient"),("honesty","honest"),("creation","creative"),("energy","energetic"),("ambition","ambitious"),("generosity","generous"),
 ("friend","friendly"),("danger","dangerous"),("music","musical"),("fashion","fashionable"),("anger","angry"),("luck","lucky"),("sleep","sleepy"),("hunger","hungry"),("nerve","nervous"),("envy","envious")]
# thing adjectives
TADJ = [("use","useful"),("danger","dangerous"),("comfort","comfortable"),("beauty","beautiful"),("pain","painful"),("peace","peaceful"),("fashion","fashionable"),("fame","famous"),
 ("cloud","cloudy"),("rain","rainy"),("wind","windy"),("sun","sunny"),("snow","snowy"),("noise","noisy"),("history","historical"),("nation","national"),("culture","cultural"),
 ("harm","harmful"),("profit","profitable"),("value","valuable"),("surprise","surprising"),("amaze","amazing"),("excite","exciting"),("bore","boring"),("tire","tiring")]
# negative: (root adj, negative)
NEGA = [("happy","unhappy"),("possible","impossible"),("honest","dishonest"),("patient","impatient"),("legal","illegal"),("regular","irregular"),("polite","impolite"),("kind","unkind"),
 ("usual","unusual"),("fair","unfair"),("correct","incorrect"),("responsible","irresponsible"),("comfortable","uncomfortable"),("popular","unpopular"),("organised","disorganised"),
 ("lucky","unlucky"),("friendly","unfriendly"),("healthy","unhealthy"),("logical","illogical"),("mature","immature"),("perfect","imperfect"),("probable","improbable"),("visible","invisible"),
 ("expensive","inexpensive"),("necessary","unnecessary"),("known","unknown"),("able","unable"),("clear","unclear"),("safe","unsafe"),("tidy","untidy")]
NEGA_PERSON = {"happy","honest","patient","polite","kind","fair","responsible","comfortable","organised","lucky","friendly","healthy","mature","perfect","able","tidy","popular"}
# adverbs: (root, adverb)
ADV = [("care","carefully"),("quick","quickly"),("slow","slowly"),("patience","patiently"),("luck","luckily"),("success","successfully"),("easy","easily"),("happy","happily"),
 ("angry","angrily"),("nerve","nervously"),("clear","clearly"),("beauty","beautifully"),("fluent","fluently"),("brave","bravely"),("calm","calmly"),("noise","noisily"),("polite","politely"),("safe","safely"),("gentle","gently"),("honest","honestly")]
MV = [("sing","sings","sang"),("drive","drives","drove"),("speak","speaks","spoke"),("work","works","worked"),("write","writes","wrote"),("walk","walks","walked"),
 ("play","plays","played"),("explain","explains","explained"),("answer","answers","answered"),("dance","dances","danced"),("cook","cooks","cooked"),("paint","paints","painted")]
# verb -> noun
VN = [("decide","decision"),("argue","argument"),("invent","invention"),("discover","discovery"),("explain","explanation"),("suggest","suggestion"),("improve","improvement"),
 ("develop","development"),("educate","education"),("arrive","arrival"),("organise","organisation"),("introduce","introduction"),("announce","announcement"),("destroy","destruction"),
 ("produce","production"),("protect","protection"),("replace","replacement"),("create","creation"),("collect","collection"),("translate","translation"),("solve","solution"),("choose","choice"),
 ("agree","agreement"),("decorate","decoration"),("compete","competition"),("complain","complaint"),("describe","description"),("apply","application"),("inform","information"),("prepare","preparation")]
NADJ = ["important","surprising","difficult","clear","sudden","a good one","wrong","interesting","useful"]
# person nouns
PN = [("teach","teacher"),("act","actor"),("visit","visitor"),("employ","employee"),("art","artist"),("science","scientist"),("music","musician"),("politics","politician"),
 ("assist","assistant"),("direct","director"),("invent","inventor"),("sing","singer"),("photograph","photographer"),("journal","journalist"),("engine","engineer"),("library","librarian"),("tour","tourist"),("compete","competitor"),("report","reporter"),("manage","manager")]
ALT = {"care":["careless"],"hope":["hopeless"],"help":["helpless"],"thought":["thoughtless"],"use":["useless"],"harm":["harmless"],"pain":["painless"],"fame":[],"energy":[]}
def _be(S): return 'is'
def gen_wf(level, rng):
    k = rng.pick(['padj','tadj','nega','adv','vn','pn','two','fix'])
    if level == 'hard' and k not in ('fix',) and rng.pick([0,0,1]): k = 'two'
    if level == 'easy' and k in ('two','fix'): k = rng.pick(['padj','tadj','nega','adv','vn','pn'])
    S = rng.pick(SUBJ_W)
    def one(k):
        t = rng.pick(['aff','neg','q'])
        if k == 'padj':
            r, a = rng.pick(PADJ); pos = 'adjective'
            a = [a] + ALT.get(r, [])
            s = {'aff':f"{S.text} is very ___ ({r.upper()}).",'neg':f"{S.text} isn't ___ ({r.upper()}).",'q':f"Is {S.mid} ___ ({r.upper()})?"}[t]
            return s, a, 'adjective'
        if k == 'tadj':
            r, a = rng.pick(TADJ); T = rng.pick(THINGS)
            a0 = a; a = [a] + ALT.get(r, [])
            if r in ('cloud','rain','wind','sun','snow'): T = rng.pick(["The weather","The weekend","The morning","This city","Yesterday"])
            elif r in ('fame','history','nation','culture'): T = rng.pick(["This city","The hotel","The film","The building","The museum"])
            elif r in ('noise',): T = rng.pick(["The room","The hotel","This city","The classroom"])
            a_ = a0
            if a0 in ('surprising','amazing','exciting','boring','tiring') and T in ('The weather','The road'): T = 'The film'
            s = {'aff':f"{T} was ___ ({r.upper()}).",'neg':f"{T} wasn't ___ ({r.upper()}).",'q':f"Was {T[0].lower()+T[1:]} ___ ({r.upper()})?"}[t]
            return s, a, 'adjective'
        if k == 'nega':
            r, a = rng.pick(NEGA)
            subj = S.text if r in NEGA_PERSON else rng.pick(THINGS)
            if r in ('known','visible','possible','probable','necessary','clear','safe','legal','usual','correct','regular','logical','expensive','perfect') and r in NEGA_PERSON: subj = rng.pick(THINGS)
            s = {'aff':f"{subj} is ___ ({r.upper()}) [opposite].",'neg':f"{subj} isn't ___ ({r.upper()}) [opposite].",'q':f"Is {subj[0].lower()+subj[1:] if subj.split()[0] in ('The','This') or subj.split()[0] in ('My','Our') else subj} ___ ({r.upper()}) [opposite]?"}[t]
            return s, [a], 'adjective'
        if k == 'adv':
            r, a = rng.pick(ADV); v = rng.pick(MV)
            s = {'aff':f"{S.text} {v[1]} ___ ({r.upper()}).",'neg':f"{S.text} doesn't {v[0]} ___ ({r.upper()}).",'q':f"Does {S.mid} {v[0]} ___ ({r.upper()})?"}[t]
            return s, [a], 'adverb'
        if k == 'vn':
            r, a = rng.pick(VN); adj = rng.pick(NADJ)
            s = {'aff':f"The ___ ({r.upper()}) was {adj}.",'neg':f"The ___ ({r.upper()}) wasn't {adj}.",'q':f"Was the ___ ({r.upper()}) {adj}?"}[t]
            if adj == 'a good one': s = s.replace(' a good one', ' very important')
            return s, [a], 'noun'
        r, a = rng.pick(PN)
        s = {'aff':f"{S.text} is a ___ ({r.upper()}).",'neg':f"{S.text} isn't a ___ ({r.upper()}).",'q':f"Is {S.mid} a ___ ({r.upper()})?"}[t]
        if a[0] in 'aeiou': s = s.replace(' a ___', ' an ___')
        return s, [a], 'noun'
    if k == 'fix':
        if level != 'hard': return None
        kk = rng.pick(['padj','tadj','nega','adv','vn','pn'])
        s, a, pos = one(kk)
        r = s[s.index('(')+1:s.index(')')].lower()
        a = a[0]
        wrong = rng.pick({'adjective':[r + 'ly', r + 'ness', r + 'ment'], 'adverb':[r, r + 'ful', r + 'ness'], 'noun':[r + 'ly', r + 'ful', r]}[pos])
        if wrong == a or wrong == r and pos == 'adjective': return None
        full = _re_sub(s, r, a)
        if '[opposite]' in s: bad = bad if False else None
        bad = _re_sub(s, r, wrong)
        return line(f"Correct the mistake: {bad}", [full] + ([_re_sub(s, r, x) for x in ALT.get(r, [])] if pos == 'adjective' else []))
    if k == 'two':
        k1, k2 = rng.pick([('padj','adv'),('tadj','vn'),('pn','padj'),('nega','vn'),('vn','tadj')])
        s1, a1, p1 = one(k1); s2, a2, p2 = one(k2)
        s1 = s1.replace('?', '.') if False else s1
        if s1.endswith('?') or s2.endswith('?'): return None
        return line(f"{s1} {s2}", a1, a2)
    s, a, pos = one(k)
    if level == 'easy' and '[opposite]' not in s: s = s + f" [{pos}]"
    return line(s, a)
def _re_sub(s, r, a):
    import re
    return re.sub(r"___ \(" + r.upper() + r"\)", a, s)
def gen_wf_jobs(C):
    return {'word-formation': lambda: gen_topic(gen_wf, C, 142)}
