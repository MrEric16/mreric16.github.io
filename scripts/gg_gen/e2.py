from lib import *
from passive import gen_topic
from e1 import SX, _cp, _q, PASTCUE, POS
NAMES = [Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('Karim','sg','he',True),Subj('Dilnoza','sg','she',True)]
PRON = {'i':'I','you':'you','he':'he','she':'she','we':'we','they':'they'}
def _pr(S): return PRON[S.pron]
def _sm(S): return S.text if S.proper or S.text == 'I' else S.mid

# ============ 1. purpose and result ============
# (base, past, rest, goal)
PURP = [("study","studied","hard","pass the exam"),("get up","got up","early","catch the bus"),("go","went","to the shop","buy some bread"),("save","saved","money","buy a new phone"),
        ("turn on","turned on","the light","see better"),("call","called","the school","ask about the homework"),("use","used","a dictionary","check the spelling"),
        ("write","wrote","notes","remember the lesson"),("take","took","a map","find the way"),("walk","walked","to school","keep fit"),("open","opened","the window","get some fresh air"),
        ("go","went","to the library","borrow a book"),("practise","practised","every day","win the competition"),("sit","sat","at the front","hear the lesson"),
        ("run","ran","to the station","catch the train"),("learn","learned","English","get a better job"),("use","used","a calculator","save time"),("stay","stayed","at home","finish the project")]
AVOID = [("leave","left","early","miss the bus"),("speak","spoke","quietly","wake the baby"),("write","wrote","it down","forget it"),("take","took","an umbrella","get wet"),
         ("set","set","an alarm","be late"),("wear","wore","a coat","catch a cold"),("check","checked","the map","get lost"),("lock","locked","the door","lose anything"),
         ("walk","walked","slowly","slip on the ice"),("study","studied","every night","fail the exam"),("hurry","hurried","to the bank","be late"),("keep","kept","quiet","disturb the others")]
RES = [("cold","day","we stayed at home"),("difficult","test","nobody finished it"),("heavy","bag","I couldn't lift it"),("long","film","we fell asleep"),("loud","song","we couldn't talk"),
       ("hot","soup","nobody could eat it"),("interesting","book","everyone read it twice"),("good","teacher","everybody liked her"),("expensive","phone","nobody bought it"),
       ("big","meal","we couldn't finish it"),("beautiful","view","we took fifty photos"),("small","room","we couldn't move"),("bad","storm","the flights were cancelled"),
       ("busy","day","I forgot my lunch"),("boring","lesson","the students yawned"),("tall","man","he hit his head"),("funny","joke","we laughed for ages"),("strong","wind","the tree fell down")]
def _a(w): return 'an' if w[0] in 'aeiou' else 'a'
def gen_pr(level, rng):
    S = rng.pick(SX); sub = S.text; p = _pr(S)
    k = rng.pick({'easy':['to','to','sothat','sosuch','sosuch','neg','why'],
                  'medium':['to','sothat','sosuch2','sosuch2','neg','why','q'],
                  'hard':['jto','jsothat','jneg','jso','jsuch','cm1','cm2','cm3','tq']}[level])
    H = {'to': {'easy':' (to / for)','medium':' (to / for / so that / so)','hard':''}[level],
         'st': {'easy':' (so that / to)','medium':' (so that / to / in order / for)','hard':''}[level],
         'ss': {'easy':' (so / such)','medium':'','hard':''}[level],
         'ng': {'easy':' (to / in order not to)','medium':' (to / not to / in order not to / so that)','hard':''}[level]}
    if k in ('to', 'sothat', 'why', 'q', 'jto', 'jsothat', 'cm1', 'tq'):
        b, pa, rest, goal = rng.pick(PURP)
        if k == 'to':
            return line(f"{sub} {pa} {rest} ___ {goal}." + H['to'], ['to', 'in order to', 'so as to'])
        if k == 'sothat':
            return line(f"{sub} {pa} {rest} ___ {p} could {goal}." + H['st'], ['so that'])
        if k == 'why':
            return line(f"Why did {_q(S)} {b} {rest}? ___ {goal}." + H['to'], ['to', 'in order to', 'so as to'])
        if k == 'q':
            return line(f"Did {_q(S)} {b} {rest} ___ {goal}?" + H['to'], ['to', 'in order to', 'so as to'])
        if k == 'jto':
            return line(f"Join with 'to': {sub} {pa} {rest}. {_cp(p)} wanted to {goal}.", [f"{sub} {pa} {rest} to {goal}.", f"{sub} {pa} {rest} in order to {goal}.", f"{sub} {pa} {rest} so as to {goal}."])
        if k == 'jsothat':
            return line(f"Join with 'so that': {sub} {pa} {rest}. {_cp(p)} wanted to {goal}.", [f"{sub} {pa} {rest} so that {p} could {goal}."])
        if k == 'cm1':
            return line(f"Correct the mistake: {sub} {pa} {rest} for {goal.replace(goal.split()[0], goal.split()[0] + 'ing', 1) if not goal.split()[0].endswith('e') else goal.replace(goal.split()[0], goal.split()[0][:-1] + 'ing', 1)}.",
                        [f"{sub} {pa} {rest} to {goal}.", f"{sub} {pa} {rest} in order to {goal}.", f"{sub} {pa} {rest} so as to {goal}."])
        if k == 'tq':
            return line(f"Make a question: {sub} {pa} {rest} to {goal}.", [f"Did {_q(S)} {b} {rest} to {goal}?"])
    if k in ('neg', 'jneg', 'cm2'):
        b, pa, rest, av = rng.pick(AVOID)
        if k == 'neg':
            return line(f"{sub} {pa} {rest} ___ {av}." + H['ng'], ['in order not to', 'so as not to'])
        if k == 'jneg':
            return line(f"Join with 'in order not to': {sub} {pa} {rest}. {_cp(p)} didn't want to {av}.", [f"{sub} {pa} {rest} in order not to {av}.", f"{sub} {pa} {rest} so as not to {av}."])
        return line(f"Correct the mistake: {sub} {pa} {rest} to not {av}.", [f"{sub} {pa} {rest} in order not to {av}.", f"{sub} {pa} {rest} so as not to {av}.", f"{sub} {pa} {rest} not to {av}."])
    adj, noun, res = rng.pick(RES)
    if k == 'sosuch':
        if rng.pick([0, 1]):
            return line(f"The {noun} was ___ {adj} that {res}." + H['ss'], ['so'])
        return line(f"It was ___ {_a(adj)} {adj} {noun} that {res}." + H['ss'], ['such'])
    if k == 'sosuch2':
        if rng.pick([0, 1]):
            return line(f"The {noun} was ___ {adj} ___ {res}.", ['so'], ['that'])
        return line(f"It was ___ {_a(adj)} {adj} {noun} ___ {res}.", ['such'], ['that'])
    if k == 'jso':
        return line(f"Join with 'so ... that': The {noun} was very {adj}. {_cp(res)}.", [f"The {noun} was so {adj} that {res}."])
    if k == 'jsuch':
        return line(f"Join with 'such ... that': The {noun} was very {adj}. {_cp(res)}.", [f"It was such {_a(adj)} {adj} {noun} that {res}."])
    if k == 'cm3':
        if rng.pick([0, 1]):
            return line(f"Correct the mistake: It was so {_a(adj)} {adj} {noun} that {res}.", [f"It was such {_a(adj)} {adj} {noun} that {res}."])
        return line(f"Correct the mistake: The {noun} was such {adj} that {res}.", [f"The {noun} was so {adj} that {res}."])
    return None

# ============ 2. wh-questions ============
WHSTAT = [("{N} goes to the gym THREE TIMES A WEEK.", "Ask about the words in capitals", ["How often does {N} go to the gym?"], "How often"),
          ("{N} lives in Samarkand BECAUSE {POSU} JOB IS THERE.", "Ask about the words in capitals", ["Why does {N} live in Samarkand?"], "Why"),
          ("{N} travels to school BY BUS.", "Ask about the words in capitals", ["How does {N} travel to school?"], "How"),
          ("{N} is FIFTEEN years old.", "Ask about the words in capitals", ["How old is {N}?"], "How old"),
          ("{N} has TWO brothers.", "Ask about the words in capitals", ["How many brothers does {N} have?"], "How many"),
          ("{N} spent TWENTY POUNDS on the book.", "Ask about the words in capitals", ["How much did {N} spend on the book?"], "How much"),
          ("{N} waited for the bus FOR AN HOUR.", "Ask about the words in capitals", ["How long did {N} wait for the bus?"], "How long"),
          ("{N} lives TWO KILOMETRES from the school.", "Ask about the words in capitals", ["How far does {N} live from the school?"], "How far"),
          ("{N} likes THE BLUE ONE.", "Ask about the words in capitals", ["Which one does {N} like?"], "Which"),
          ("{N}'s favourite subject is HISTORY.", "Ask about the words in capitals", ["What is {N}'s favourite subject?"], "What"),
          ("{N} is from UZBEKISTAN.", "Ask about the words in capitals", ["Where is {N} from?"], "Where"),
          ("{N} was born IN 2010.", "Ask about the words in capitals", ["When was {N} born?"], "When"),
          ("{N} is VERY TALL.", "Ask about the words in capitals", ["How tall is {N}?"], "How tall"),
          ("{N} is talking TO THE TEACHER.", "Ask about the words in capitals", ["Who is {N} talking to?", "Who is {N} talking with?"], "Who"),
          ("{N} cooks plov FOR {POSU} FAMILY.", "Ask about the words in capitals", ["Who does {N} cook plov for?"], "Who"),
          ("{N} didn't come to school BECAUSE {PU} WAS ILL.", "Ask about the words in capitals", ["Why didn't {N} come to school?"], "Why"),
          ("{N} didn't answer the phone BECAUSE {PU} WAS BUSY.", "Ask about the words in capitals", ["Why didn't {N} answer the phone?"], "Why"),
          ("{N} was late BECAUSE THE BUS BROKE DOWN.", "Ask about the words in capitals", ["Why was {N} late?"], "Why"),
          ("{N} has been in Tashkent FOR THREE YEARS.", "Ask about the words in capitals", ["How long has {N} been in Tashkent?"], "How long"),
          ("{N} usually gets up AT SIX O'CLOCK.", "Ask about the words in capitals", ["What time does {N} usually get up?", "When does {N} usually get up?"], "What time"),
          ("{N} is going to meet HER COUSIN.".replace('HER COUSIN', 'A FRIEND'), "Ask about the words in capitals", ["Who is {N} going to meet?"], "Who"),
          ("{N} will arrive ON FRIDAY.", "Ask about the words in capitals", ["When will {N} arrive?"], "When"),
          ("{N} is reading A DETECTIVE NOVEL.", "Ask about the words in capitals", ["What is {N} reading?"], "What"),
          ("{N} is crying BECAUSE {PU} LOST {POSU} PHONE.", "Ask about the words in capitals", ["Why is {N} crying?"], "Why")]
PLACE_TO = {'school', 'work', 'the shop', 'the station', 'the airport', 'the market', 'the cinema', 'the park', 'the museum', 'the hospital', 'the bank'}
PLACE_AT = {'the hospital', 'the party', 'the door', 'the wedding', 'home', 'school', 'work', 'the bank', 'the station'}
PEOPLE = ('friend', 'manager', 'teacher', 'doctor', 'neighbour', 'relatives', 'dentist', 'new people', 'president', 'headteacher', 'children', 'class')
def _kind(comp):
    if comp.startswith('in '): return 'place'
    if comp.startswith('near ') or comp.startswith('along '): return 'place'
    if comp.startswith('at ') and comp[3:] in PLACE_AT: return 'place'
    if comp.startswith('to ') and comp[3:] in PLACE_TO: return 'place'
    if comp.split(' ')[0] in ('to', 'for', 'on', 'with', 'about', 'up', 'down', 'off', 'out', 'at', 'of', 'into'): return None
    if comp in ('home early', 'home late', 'back early', 'badly', 'late', 'ill', 'tired', 'nervous', 'hello', 'goodbye', 'nothing', 'hard', 'every day'): return None
    if any(w in comp for w in PEOPLE): return 'person'
    return 'obj'
def _stat(rng):
    N = rng.pick(NAMES + [Subj('My brother','sg','he'),Subj('Our teacher','sg','she'),Subj('My parents','pl','they')])
    V = rng.pick(VERBS); comp = rng.pick(V.comps); kind = _kind(comp)
    if not kind: return None
    return N, V, comp, kind
def gen_wh(level, rng):
    k = rng.pick({'easy':['fill','fill','fill','fillh'],'medium':['cap','cap','cap','hand','hand'],'hard':['cm','cm','cm','hand','hand','cap']}[level])
    if k == 'hand':
        N = rng.pick(NAMES); row = rng.pick(WHSTAT); stmt, ins, qs, wh = row
        P = N.pron; q_ = {'he':'his','she':'her'}[N.pron]
        def f(t): return t.replace('{N}', N.text).replace('{PU}', P.upper()).replace('{POSU}', q_.upper()).replace('{P}', P).replace('{POS}', q_).replace('{POS2}', q_)
        return line(f"{ins}: {f(stmt)}", [f(x) for x in qs])
    r = _stat(rng)
    if not r: return None
    N, V, comp, kind = r; cue = rng.pick(PASTCUE); sub = N.text; nm = _q(N)
    if kind == 'person': kind = 'obj'; wo = 'Who'
    else: wo = 'What'
    asked = rng.pick(['subj', 'obj', 'time']) if kind == 'obj' else rng.pick(['subj', 'place', 'time'])
    if asked == 'subj': wh, q = 'Who', f"Who {V.past} {comp} {cue}?"
    elif asked == 'obj': wh, q = wo, f"{wo} did {nm} {V.base} {cue}?"
    elif asked == 'place': wh, q = 'Where', f"Where did {nm} {V.base} {cue}?"
    else: wh, q = 'When', f"When did {nm} {V.base} {comp}?"
    if k == 'cap':
        if asked == 'subj': st = f"{sub.upper()} {V.past} {comp} {cue}."
        elif asked == 'obj': st = f"{sub} {V.past} {comp.upper()} {cue}."
        elif asked == 'place': st = f"{sub} {V.past} {comp.upper()} {cue}."
        else: st = f"{sub} {V.past} {comp} {cue.upper()}."
        return line(f"Ask about the words in capitals: {st}", [q])
    if k == 'fill' or k == 'fillh':
        h = ' (who / what / where / when)' if level == 'easy' else ''
        if asked == 'subj': return line(f"___ {V.past} {comp} {cue}? {sub}." + h, ['who'])
        if asked == 'obj': return line(f"___ did {nm} {V.base} {cue}? {_cp(comp)}." + h, [wo.lower()])
        if asked == 'place': return line(f"___ did {nm} {V.base} {cue}? {_cp(comp)}." + h, ['where'])
        return line(f"___ did {nm} {V.base} {comp}? {_cp(cue)}." + h, ['when'])
    # cm: wrong question forms
    if asked == 'subj':
        return line(f"Correct the mistake: Who did {V.base} {comp} {cue}?", [q])
    if asked == 'obj':
        return line(f"Correct the mistake: {wo} {nm} did {V.base} {cue}?", [q])
    if asked == 'place':
        return line(f"Correct the mistake: Where {nm} {V.past} {cue}?", [q])
    return line(f"Correct the mistake: When {nm} did {V.base} {comp}?", [q])

# ============ 3. verbs that change meaning ============
STOP_Q = [("smoke","smoking"),("eat sweets","eating sweets"),("play computer games","playing computer games"),("drink coffee","drinking coffee"),("talk in class","talking in class"),
          ("cry","crying"),("shout","shouting"),("laugh","laughing"),("text in lessons","texting in lessons"),("eat meat","eating meat")]
STOP_P = [("buy some bread","buying some bread"),("ask for directions","asking for directions"),("check the map","checking the map"),("take a photo","taking a photo"),
          ("have a rest","having a rest"),("talk to a friend","talking to a friend"),("get some water","getting some water"),("look at the view","looking at the view"),
          ("buy a ticket","buying a ticket"),("fill the tank","filling the tank")]
REM_T = [("lock the door","locking the door"),("post the letter","posting the letter"),("call the dentist","calling the dentist"),("buy some milk","buying some milk"),
         ("turn off the light","turning off the light"),("send the email","sending the email"),("bring the book","bringing the book"),("pay the bill","paying the bill"),("feed the cat","feeding the cat")]
REM_M = [("meet the president","meeting the president"),("visit the museum","visiting the museum"),("see the sea for the first time","seeing the sea for the first time"),
         ("ride a horse","riding a horse"),("win the prize","winning the prize"),("swim in the river","swimming in the river"),("sing on stage","singing on stage"),
         ("fly to London","flying to London"),("hold a snake","holding a snake")]
TRY_E = [("lift the box","lifting the box"),("open the window","opening the window"),("speak Spanish","speaking Spanish"),("reach the shelf","reaching the shelf"),("fix the bike","fixing the bike"),
         ("learn the poem","learning the poem"),("push the door","pushing the door")]
TRY_X = [("use a different key","using a different key"),("turn it off and on","turning it off and on"),("add some salt","adding some salt"),("ask the teacher","asking the teacher"),
         ("press the red button","pressing the red button"),("clean the screen","cleaning the screen"),("sit somewhere else","sitting somewhere else")]
REG_T = [("tell you that the flight is late","telling"),("inform you that the shop is closed","informing"),("say that the lesson is cancelled","saying")]
REG_P = [("buy that phone","buying that phone"),("tell a lie","telling a lie"),("lose my temper","losing my temper"),("say that","saying that"),("leave school early","leaving school early"),
         ("shout at her","shouting at her"),("eat so much","eating so much")]
MEAN = {'stop_q':'(sense: quit a habit)','stop_p':'(sense: pause in order to do something)','rem_t':'(sense: not forget a task)','rem_m':'(sense: recall a memory)',
        'try_e':'(sense: make an effort)','try_x':'(sense: test something as an experiment)','reg_p':'(sense: be sorry about the past)'}
def _mean_S(S): return S
def gen_vcm(level, rng):
    S = rng.pick(SX); sub = S.text; sm = _sm(S)
    kind = rng.pick(['stop_q','stop_p','rem_t','rem_m','try_e','try_x','reg_p','forget_t','forget_m'] + ['reg_t'] * 1)
    h = ' (to + verb / verb + -ing)' if level == 'easy' else ''
    if kind == 'stop_q': b, g = rng.pick(STOP_Q); verb, vb = 'stopped', 'stop'; cue = MEAN['stop_q']
    elif kind == 'stop_p': b, g = rng.pick(STOP_P); verb, vb = 'stopped', 'stop'; cue = MEAN['stop_p']
    elif kind == 'rem_t': b, g = rng.pick(REM_T); verb, vb = 'remembered', 'remember'; cue = MEAN['rem_t']
    elif kind == 'rem_m': b, g = rng.pick(REM_M); verb, vb = 'remembered', 'remember'; cue = MEAN['rem_m']
    elif kind == 'try_e': b, g = rng.pick(TRY_E); verb, vb = 'tried', 'try'; cue = MEAN['try_e']
    elif kind == 'try_x': b, g = rng.pick(TRY_X); verb, vb = 'tried', 'try'; cue = MEAN['try_x']
    elif kind == 'forget_t': b, g = rng.pick(REM_T); verb, vb = 'forgot', 'forget'; cue = '(sense: fail to do a task)'
    elif kind == 'forget_m': b, g = rng.pick(REM_M); verb, vb = 'never forgot', 'forget'; cue = '(sense: lose a memory)'
    elif kind == 'reg_p': b, g = rng.pick(REG_P); verb, vb = 'regretted', 'regret'; cue = MEAN['reg_p']
    else:
        S = rng.pick([Subj('I','i','i'), Subj('We','pl','we')]); sub = S.text
        b, g = rng.pick(REG_T); first = b.split(' ')[0]; rest = ' '.join(b.split(' ')[1:]); cue = '(sense: be sorry to give bad news)'
        if level == 'hard':
            return line(f"Correct the mistake: {sub} regret {_ing_first(first)} {rest}. {cue}", [f"{sub} regret to {first} {rest}."])
        return line(f"{sub} regret ___ ({first}) {rest}. {cue}" + h, [f"to {first}"])
    to = f"to {b}"; ing = g
    meaning_ing = kind in ('stop_q', 'rem_m', 'try_x', 'forget_m', 'reg_p')
    right = ing if meaning_ing else to
    wrong = to if meaning_ing else ing
    first = b.split(' ')[0]; rest = ' '.join(b.split(' ')[1:])
    k = rng.pick({'easy':['b','b','b','neg','q'],'medium':['b','b','neg','q','neg'],'hard':['cm','cm','cm','neg_t','q_t']}[level])
    base_hint = f"({first})"
    blank_right = [right.split(' ')[0] + (' ' + right.split(' ')[1] if right.startswith('to ') else '')] if False else None
    ans_first = (f"to {first}" if not meaning_ing else _ing_first(first))
    if verb == 'never forgot':
        vphr, vq = 'never forgot', 'forget'
    if k == 'b':
        return line(f"{sub} {verb} ___ {base_hint} {rest}".strip() + f". {cue}" + h, [ans_first])
    if k == 'neg':
        if verb == 'never forgot': return None
        return line(f"{sub} didn't {vb} ___ {base_hint} {rest}".strip() + f". {cue}" + h, [ans_first])
    if k == 'q':
        if verb == 'never forgot': return None
        return line(f"Did {_q(S)} {vb} ___ {base_hint} {rest}".strip() + f"? {cue}" + h, [ans_first])
    if k == 'cm':
        return line(f"Correct the mistake: {sub} {verb} {wrong}. {cue}", [f"{sub} {verb} {right}."])
    if k == 'neg_t':
        if verb == 'never forgot': return None
        return line(f"Make a negative sentence: {sub} {verb} {right}.", [f"{sub} didn't {vb} {right}.", f"{sub} did not {vb} {right}."])
    if k == 'q_t':
        if verb == 'never forgot': return None
        return line(f"Make a question: {sub} {verb} {right}.", [f"Did {_q(S)} {vb} {right}?"])
    return None
def _ing_first(w):
    fw = w.split(' ')[0]
    rest = ' '.join(w.split(' ')[1:])
    if fw.endswith('e') and not fw.endswith('ee'): ing = fw[:-1] + 'ing'
    elif fw in ('run','swim','sit','get','put','stop','plan','shop','win','cut','set','hit','begin','forget'): ing = fw + fw[-1] + 'ing'
    else: ing = fw + 'ing'
    return (ing + ' ' + rest).strip() if rest and False else ing

# ============ 4. verb + object + infinitive ============
TOV = [('asked','ask'),('told','tell'),('allowed','allow'),('advised','advise'),('reminded','remind'),('warned','warn'),('invited','invite'),('taught','teach'),
       ('persuaded','persuade'),('encouraged','encourage'),('forced','force'),('ordered','order'),('expected','expect')]
BARE = [('made','make'),('let','let')]
OBJS = ['me','him','her','us','them','you','Tom','Anna','my brother','the students','Malika','Aziz']
def _objs_for(S):
    bad = {'i':'me','he':'him','she':'her','we':'us','they':'them','you':'you'}.get(S.pron)
    return [o for o in OBJS if o != bad and o.lower() != S.text.lower()]
def gen_voi(level, rng):
    S = rng.pick(SX); sub = S.text; O = rng.pick(_objs_for(S)); V = rng.pick(VERBS); comp = rng.pick(V.comps)
    grp = rng.pick(['to','to','to','to','bare','bare','help','want'])
    h = {'to':' (to + verb / verb)','bare':' (to + verb / verb)'}
    hh = h['to'] if level == 'easy' else ''
    if grp == 'to': vp, vb = rng.pick(TOV); ans = [f"to {V.base}"]
    elif grp == 'bare': vp, vb = rng.pick(BARE); ans = [V.base]
    elif grp == 'help': vp, vb = 'helped', 'help'; ans = [f"to {V.base}", V.base]
    else: vp, vb = ('wants' if S.kind == 'sg' else 'want'), 'want'; ans = [f"to {V.base}"]
    k = rng.pick({'easy':['b','b','b','neg','q','negtell'],'medium':['b','neg','q','negtell','b'],'hard':['cm','cm','cm','neg_t','q_t','cm2']}[level])
    do_neg = "doesn't" if S.kind == 'sg' else "don't"
    if grp == 'want':
        if k == 'b': return line(f"{sub} {vp} {O} ___ ({V.base}) {comp}." + hh, ans)
        if k == 'neg': return line(f"{sub} {do_neg} want {O} ___ ({V.base}) {comp}." + hh, ans)
        if k == 'q': return line(f"{'Does' if S.kind == 'sg' else 'Do'} {_q(S)} want {O} ___ ({V.base}) {comp}?" + hh, ans)
        if k == 'negtell': return None
        if k == 'cm': return line(f"Correct the mistake: {sub} {vp} {O} {V.base} {comp}.", [f"{sub} {vp} {O} to {V.base} {comp}."])
        if k == 'cm2': return line(f"Correct the mistake: {sub} {vp} that {O} {V.base} {comp}.", [f"{sub} {vp} {O} to {V.base} {comp}."]) if False else None
        if k == 'neg_t': return line(f"Make a negative sentence: {sub} {vp} {O} to {V.base} {comp}.", [f"{sub} {do_neg} want {O} to {V.base} {comp}."])
        return line(f"Make a question: {sub} {vp} {O} to {V.base} {comp}.", [f"{'Does' if S.kind == 'sg' else 'Do'} {_q(S)} want {O} to {V.base} {comp}?"])
    if k == 'b': return line(f"{sub} {vp} {O} ___ ({V.base}) {comp}." + hh, ans)
    if k == 'neg': return line(f"{sub} didn't {vb} {O} ___ ({V.base}) {comp}." + hh, ans)
    if k == 'q': return line(f"Did {_q(S)} {vb} {O} ___ ({V.base}) {comp}?" + hh, ans)
    if k == 'negtell':
        if grp == 'to' and vb in ('tell', 'ask', 'advise', 'remind', 'warn', 'order', 'encourage'):
            return line(f"{sub} {vp} {O} not ___ ({V.base}) {comp}." + hh, ans)
        return None
    full = ans[0]
    if k == 'cm':
        if grp == 'to': return line(f"Correct the mistake: {sub} {vp} {O} {V.base} {comp}.", [f"{sub} {vp} {O} to {V.base} {comp}."])
        if grp == 'bare': return line(f"Correct the mistake: {sub} {vp} {O} to {V.base} {comp}.", [f"{sub} {vp} {O} {V.base} {comp}."])
        return None
    if k == 'cm2':
        if grp == 'to': return line(f"Correct the mistake: {sub} {vp} {O} {V.ing} {comp}.", [f"{sub} {vp} {O} to {V.base} {comp}."])
        return None
    if k == 'neg_t': return line(f"Make a negative sentence: {sub} {vp} {O} {full} {comp}.", [f"{sub} didn't {vb} {O} {full} {comp}."] + ([f"{sub} {vp} {O} not {full} {comp}."] if grp == 'to' and vb in ('tell','ask','advise','remind','warn','order','encourage') else []))
    if k == 'q_t': return line(f"Make a question: {sub} {vp} {O} {full} {comp}.", [f"Did {_q(S)} {vb} {O} {full} {comp}?"])
    return None

def gen_e2_jobs(C):
    return {'purpose-and-result': lambda: gen_topic(gen_pr, C, 311),
            'wh-questions': lambda: gen_topic(gen_wh, C, 312),
            'verbs-that-change-meaning': lambda: gen_topic(gen_vcm, C, 313),
            'verb-object-infinitive': lambda: gen_topic(gen_voi, C, 314)}
