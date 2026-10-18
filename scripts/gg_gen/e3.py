from lib import *
from passive import gen_topic
from e1 import SX, _cp, _q, POS, _v
from e2 import _sm, _pr, _ing_first
def _be(S, past=False):
    if past: return 'was' if S.kind in ('i', 'sg') else 'were'
    return be_pres(S)
def _bn(S, past=False):   # negative be
    b = _be(S, past)
    return "am not" if b == 'am' else b + "n't"

# ============ 1. participle adjectives ============
# verb, -ed, -ing, noun phrase, plural?
PA = [("bore","bored","boring","lesson",0),("interest","interested","interesting","book",0),("excite","excited","exciting","match",0),("tire","tired","tiring","journey",0),
      ("surprise","surprised","surprising","news",0),("confuse","confused","confusing","instructions",1),("annoy","annoyed","annoying","noise",0),
      ("disappoint","disappointed","disappointing","result",0),("frighten","frightened","frightening","film",0),("amaze","amazed","amazing","view",0),
      ("embarrass","embarrassed","embarrassing","mistake",0),("relax","relaxed","relaxing","holiday",0),("shock","shocked","shocking","story",0),
      ("depress","depressed","depressing","weather",0),("worry","worried","worrying","news",0),("fascinate","fascinated","fascinating","documentary",0),
      ("exhaust","exhausted","exhausting","hike",0),("terrify","terrified","terrifying","dream",0),("irritate","irritated","irritating","noise",0),
      ("satisfy","satisfied","satisfying","result",0),("inspire","inspired","inspiring","speech",0),("thrill","thrilled","thrilling","ride",0),
      ("disgust","disgusted","disgusting","smell",0),("amuse","amused","amusing","joke",0),("encourage","encouraged","encouraging","feedback",0)]
def gen_pa(level, rng):
    v, ed, ing, noun, pl = rng.pick(PA); S = rng.pick(SX); past = rng.pick([True, False])
    bn = _be(S, past) if False else None
    bt = ('were' if past else 'are') if pl else ('was' if past else 'is')       # be for the thing
    btn = bt + "n't" if bt not in ('am',) else "am not"
    bs = _be(S, past); bsn = _bn(S, past)
    sub = S.text; th = f"The {noun}"
    k = rng.pick({'easy':['ed','ed','ing','ing','ned','ning','sq'],'medium':['ed2','ing2','ned','ning','sq','tq','choose'],
                  'hard':['cm_th','cm_th','cm_pe','cm_pe','neg_t','q_t','cm_th','cm_pe']}[level])
    H = f" ({v})"
    if k == 'ed':
        return line(f"{th} {bt} {ing}. {sub} {bs} ___{H}.", [ed])
    if k == 'ing':
        return line(f"{sub} {bs} {ed}. {th} {bt} ___{H}.", [ing])
    if k == 'ned':
        return line(f"{th} {btn} {ing}. {sub} {bsn} ___{H}.", [ed])
    if k == 'ning':
        return line(f"{sub} {bsn} {ed}. {th} {btn} ___{H}.", [ing])
    if k == 'sq':
        if rng.pick([0, 1]): return line(f"{_cp(bt)} the {noun} ___{H}? Yes, it {bt}.", [ing])
        return line(f"{_cp(bs)} {_q(S)} ___{H}? Yes, {_pr(S) if S.pron != 'you' else 'I'} {bs}.".replace(' I am.', ' I am.'), [ed]) if S.pron != 'i' else None
    if k == 'ed2':
        return line(f"{sub} {bs} ___ ({v}) because the {noun} {bt} ___ ({v}).", [ed], [ing])
    if k == 'ing2':
        return line(f"{th} {bt} so ___ ({v}) that {_sm(S) if not S.proper else S.text} {bs} ___ ({v}).", [ing], [ed])
    if k == 'tq':
        return line(f"{_cp(bs)} {_q(S)} ___ ({v}) because the {noun} {bt} ___ ({v})?", [ed], [ing])
    if k == 'choose':
        if rng.pick([0, 1]): return line(f"{th} {bt} ___. ({ed} / {ing})", [ing]) if rng.pick([0, 1]) else line(f"{th} {bt} ___. ({ing} / {ed})", [ing])
        return line(f"{sub} {bs} ___. ({ed} / {ing})", [ed]) if rng.pick([0, 1]) else line(f"{sub} {bs} very ___ after the {noun}. ({ing} / {ed})", [ed])
    if k == 'cm_th':
        return line(f"Correct the mistake: {th} {bt} {ed}.", [f"{th} {bt} {ing}."])
    if k == 'cm_pe':
        sp = {'i':'I','you':'You','he':'He','she':'She','we':'We','they':'They'}
        return line(f"Correct the mistake (it is how {_pr(S) if S.pron not in ('i',) else 'I'} feel{'s' if S.kind == 'sg' else ''}): {sub} {bs} very {ing}.", [f"{sub} {bs} very {ed}."])
    if k == 'neg_t':
        return line(f"Make a negative sentence: {th} {bt} {ing}.", [f"{th} {btn} {ing}.", f"{th} {bt} not {ing}."])
    if k == 'q_t':
        return line(f"Make a question: {th} {bt} {ing}.", [f"{_cp(bt)} the {noun} {ing}?"])
    return None

# ============ 2. commonly confused words ============
CW = """
its/it's|The dog wagged ___ tail.=its/it's;___ a lovely day today.=it's/its;The company changed ___ name.=its/it's;I think ___ going to rain.=it's/its;The cat hurt ___ paw.=its/it's;___ been a long week.=it's/its;Is ___ raining outside?=it's/its;The school is proud of ___ students.=its/it's
their/there/they're|___ going to the cinema tonight.=they're/their/there;The students left ___ bags in the hall.=their/there/they're;Put the books over ___.=there/their/they're;___ are twenty students in the class.=There/Their/They're;I think ___ late.=they're/their/there;Our neighbours sold ___ car.=their/there/they're;Don't go ___ without a coat.=there/their/they're;Are ___ any questions?=there/their/they're
your/you're|___ late for the lesson.=You're/Your;Is this ___ pen?=your/you're;I think ___ right.=you're/your;Don't forget ___ homework.=your/you're;___ going to love it.=You're/Your;What's ___ name?=your/you're;Are ___ ready?=you/your
whose/who's|___ bag is this?=Whose/Who's;___ coming to the party?=Who's/Whose;The girl ___ phone rang left the room.=whose/who's;___ been using my pen?=Who's/Whose;I don't know ___ book it is.=whose/who's;Do you know ___ at the door?=who's/whose
affect/effect|The weather can ___ your mood.=affect/effect;The new law had a big ___ on prices.=effect/affect;Smoking will ___ your health.=affect/effect;What ___ did the medicine have?=effect/affect;Noise can ___ your concentration.=affect/effect;The ___ of the storm was terrible.=effect/affect
lose/loose|Don't ___ your keys.=lose/loose;My tooth is ___.=loose/lose;I always ___ my umbrella.=lose/loose;These trousers are too ___.=loose/lose;We might ___ the match.=lose/loose;The screw is ___.=loose/lose
then/than|She is taller ___ her brother.=than/then;We had dinner, and ___ we watched a film.=then/than;I like tea more ___ coffee.=than/then;First we ate, and ___ we left.=then/than;It is easier ___ I thought.=than/then;He is not older ___ me.=than/then
to/too/two|I have ___ brothers.=two/to/too;It is ___ cold to swim.=too/to/two;We went ___ the park.=to/too/two;She is ___ young to drive.=too/to/two;He bought ___ tickets.=two/to/too;Would you like some tea ___?=too/to/two
accept/except|Everyone came ___ Tom.=except/accept;Please ___ my apology.=accept/except;The shop opens every day ___ Sunday.=except/accept;Will she ___ the job?=accept/except;I ___ your offer.=accept/except;All the students passed ___ one.=except/accept
advice/advise|Can you give me some ___?=advice/advise;I ___ you to wait.=advise/advice;That was good ___.=advice/advise;Doctors ___ people to sleep well.=advise/advice;Thank you for your ___.=advice/advise;What do you ___ me to do?=advise/advice
practice/practise|I need to ___ my English.=practise/practice;Football ___ is on Friday.=practice/practise;You should ___ every day.=practise/practice;Piano ___ takes time.=practice/practise
weather/whether|The ___ is lovely today.=weather/whether;I don't know ___ she is at home.=whether/weather;Ask him ___ he wants tea.=whether/weather;What is the ___ like?=weather/whether
quiet/quite|Please be ___.=quiet/quite;It is ___ cold today.=quite/quiet;The library is very ___.=quiet/quite;I am ___ tired.=quite/quiet;It was ___ a good film.=quite/quiet
say/tell|He ___ hello to everyone.=said/told;She ___ me a story.=told/said;Don't ___ a lie.=tell/say;What did you ___?=say/tell;He ___ goodbye and left.=said/told;Can you ___ me the time?=tell/say;Please ___ the truth.=tell/say
lend/borrow|Can I ___ your pen?=borrow/lend;Could you ___ me some money?=lend/borrow;She ___ a book from the library.=borrowed/lent;He ___ me his bike.=lent/borrowed;Did you ___ him your notes?=lend/borrow
bring/take|___ your book to school tomorrow.=Bring/Take;Please ___ this parcel to the post office.=take/bring;Can you ___ me a glass of water?=bring/take;I ___ the dog for a walk every day.=take/bring;Don't ___ your phone to the exam.=bring/take
look/see/watch|I like to ___ football on TV.=watch/look/see;___ at that bird!=Look/See/Watch;Can you ___ the board?=see/look/watch;We ___ a film last night.=watched/looked/saw;She ___ at the picture for ages.=looked/saw/watched;Did you ___ Tom at the party?=see/look/watch
hear/listen|I ___ to music every day.=listen/hear;Can you ___ that noise?=hear/listen;Please ___ to the teacher.=listen/hear;I can't ___ you.=hear/listen;Don't ___ to him.=listen/hear
rise/raise|The sun ___ in the east.=rises/raises;Please ___ your hand.=raise/rise;Prices ___ every year.=rise/raise;They ___ the flag every morning.=raise/rise
fun/funny|The party was great ___.=fun/funny;He told a ___ joke.=funny/fun;The film was really ___.=funny/fun;We had a lot of ___.=fun/funny;Was it ___ at the beach?=fun/funny
sensible/sensitive|It is ___ to take an umbrella.=sensible/sensitive;She is very ___ to noise.=sensitive/sensible;That is a ___ idea.=sensible/sensitive;He is a ___ boy who cries easily.=sensitive/sensible
beside/besides|She sat ___ me.=beside/besides;___ English, he speaks French.=Besides/Beside;The park is ___ the school.=beside/besides;___ the homework, I have to clean my room.=Besides/Beside
alone/lonely|He likes to be ___ sometimes.=alone/lonely;She felt ___ in the new city.=lonely/alone;Don't leave me ___.=alone/lonely;He is very ___ without friends.=lonely/alone
economic/economical|The ___ situation is difficult.=economic/economical;This car is very ___.=economical/economic;It is an ___ problem.=economic/economical;A small car is more ___.=economical/economic
historic/historical|It was a ___ victory.=historic/historical;He reads ___ novels.=historical/historic;This is a ___ moment for our school.=historic/historical;She studies ___ facts.=historical/historic
among/between|The ball is ___ the two chairs.=between/among;She was ___ the crowd.=among/between;Choose ___ tea and coffee.=between/among;He was happy ___ his friends.=among/between
dessert/desert|We had ice cream for ___.=dessert/desert;The ___ is hot and dry.=desert/dessert;Don't ___ your friends.=desert/dessert
where/wear/were|___ are my shoes?=Where/Wear/Were;They ___ late.=were/where/wear;I ___ a coat in winter.=wear/where/were;We ___ at home yesterday.=were/wear/where;___ do you live?=Where/Were/Wear
whole/hole|I ate the ___ cake.=whole/hole;There is a ___ in my sock.=hole/whole;They worked the ___ day.=whole/hole
knew/new|I ___ the answer.=knew/new;She bought a ___ phone.=new/knew;He ___ the way.=knew/new
write/right|You are ___.=right/write;Please ___ your name.=write/right;Turn ___ at the corner.=right/write
buy/by|I want to ___ a ticket.=buy/by;The book was written ___ a teacher.=by/buy;Where can I ___ bread?=buy/by
hear/here|Come ___!=here/hear;I can ___ music.=hear/here;Is she ___ today?=here/hear
no/know|I ___ the answer.=know/no;There is ___ milk.=no/know;Do you ___ him?=know/no
piece/peace|A ___ of cake, please.=piece/peace;We want ___ in the world.=peace/piece;He gave me a ___ of advice.=piece/peace
"""
CWG = []
for _l in CW.strip().split('\n'):
    _g, _body = _l.split('|', 1)
    for _it in _body.split(';'):
        _s, _c = _it.split('=')
        _opts = _c.split('/')
        CWG.append((_g, _s, _opts[0], _opts[1:]))
def _fill(s, w): return s.replace('___', w)
def gen_cw(level, rng):
    g, s, ok, wr = rng.pick(CWG)
    opts = [ok] + wr
    if level == 'easy':
        rng.shuffle(opts)
        return line(f"{s} ({' / '.join(o.lower() if not s.startswith('___') else o for o in opts)})", [ok])
    if level == 'medium':
        same = [x for x in CWG if x[0] == g and x[1] != s]
        if not same: return None
        g2, s2, ok2, wr2 = rng.pick(same)
        if rng.pick([0, 1]):
            allopts = sorted(set([o for x in CWG if x[0] == g for o in [x[2]] + x[3]]))
            rng.shuffle(allopts)
            return line(f"1) {s} 2) {s2} ({' / '.join(a.lower() for a in allopts)})", [ok], [ok2])
        return line(f"{s} {s2}", [ok], [ok2])
    w = rng.pick(wr)
    return line(f"Correct the mistake: {_fill(s, w)}", [_fill(s, ok)])

# ============ 3. would rather, had better, it's time, prefer ============
def gen_wr(level, rng):
    S = rng.pick(SX); V = rng.pick(VERBS); comp = rng.pick(V.comps); V2 = rng.pick([x for x in VERBS if x.base != V.base]); comp2 = rng.pick(V2.comps)
    sub = S.text; sm = _sm(S); pf = 'prefers' if S.kind == 'sg' else 'prefer'
    S2 = rng.pick([x for x in SX if x.text != S.text and x.pron != S.pron])
    k = rng.pick({'easy':['wr','wr','wrn','wrq','hb','hbn','time','timeq','pref','wp','wpn'],
                  'medium':['wr','wrn','wrq','hb','hbn','time','timeq','pref','wp','wpq','wrp','wrpn'],
                  'hard':['cm_wr','cm_hb','cm_time','cm_pref','rew_hb','rew_wr','rew_time','neg_hb','neg_wr','q_wr','cm_wp']}[level])
    if k == 'wr': return line(f"{sub} would rather ___ ({V.base}) {comp}.", [V.base])
    if k == 'wrn': return line(f"{sub} would rather not ___ ({V.base}) {comp}.", [V.base])
    if k == 'wrq': return line(f"Would {_q(S)} rather ___ ({V.base}) {comp}?", [V.base])
    if k == 'hb': return line(f"{sub} had better ___ ({V.base}) {comp}.", [V.base])
    if k == 'hbn': return line(f"{sub} had better not ___ ({V.base}) {comp}.", [V.base])
    if k == 'time': return line(f"It's time {sm} ___ ({V.base}) {comp}.", [V.past])
    if k == 'timeq': return line(f"Isn't it time {sm} ___ ({V.base}) {comp}?", [V.past])
    if k == 'pref': return line(f"{sub} {pf} ___ ({V.base}) {comp} to ___ ({V2.base}) {comp2}.", [_ing_first(V.base)], [_ing_first(V2.base)])
    if k == 'wp': return line(f"{sub} would prefer ___ ({V.base}) {comp}.", [f"to {V.base}"])
    if k == 'wpn': return line(f"{sub} would prefer not ___ ({V.base}) {comp}.", [f"to {V.base}"])
    if k == 'wpq': return line(f"Would {_q(S)} prefer ___ ({V.base}) {comp}?", [f"to {V.base}"])
    if k == 'wrp': return line(f"{sub} would rather {_sm(S2)} ___ ({V.base}) {comp}.", [V.past])
    if k == 'wrpn': return line(f"{sub} would rather {_sm(S2)} ___ (not / {V.base}) {comp}.", [f"didn't {V.base}", f"did not {V.base}"])
    if k == 'cm_wr': return line(f"Correct the mistake: {sub} would rather to {V.base} {comp}.", [f"{sub} would rather {V.base} {comp}."])
    if k == 'cm_hb': return line(f"Correct the mistake: {sub} had better to {V.base} {comp}.", [f"{sub} had better {V.base} {comp}."])
    if k == 'cm_time': return line(f"Correct the mistake: It's time {sm} {V.base} {comp}.", [f"It's time {sm} {V.past} {comp}.", f"It is time {sm} {V.past} {comp}."])
    if k == 'cm_pref':
        i1, i2 = _ing_first(V.base), _ing_first(V2.base)
        return line(f"Correct the mistake: {sub} {pf} {V.base} {comp} to {V2.base} {comp2}.", [f"{sub} {pf} {i1} {comp} to {i2} {comp2}."])
    if k == 'cm_wp': return line(f"Correct the mistake: {sub} would prefer {_ing_first(V.base)} {comp}.", [f"{sub} would prefer to {V.base} {comp}."])
    if k == 'rew_hb': return line(f"Rewrite with 'had better': {sub} should {V.base} {comp}.", [f"{sub} had better {V.base} {comp}."])
    if k == 'rew_wr': return line(f"Rewrite with 'would rather': {sub} {pf} to {V.base} {comp}.", [f"{sub} would rather {V.base} {comp}."])
    if k == 'rew_time': return line(f"Rewrite with 'It's time': {sub} should {V.base} {comp} now.", [f"It's time {sm} {V.past} {comp}.", f"It is time {sm} {V.past} {comp}."])
    if k == 'neg_hb': return line(f"Make a negative sentence: {sub} had better {V.base} {comp}.", [f"{sub} had better not {V.base} {comp}."])
    if k == 'neg_wr': return line(f"Make a negative sentence: {sub} would rather {V.base} {comp}.", [f"{sub} would rather not {V.base} {comp}."])
    if k == 'q_wr': return line(f"Make a question: {sub} would rather {V.base} {comp}.", [f"Would {_q(S)} rather {V.base} {comp}?"])
    return None

# ============ 4. future in the past ============
REASON = ["but it was too late","but the phone rang","but it started to rain","but the shop was closed","but there was no time","but the bus was late","but nobody answered","but something went wrong"]
def gen_fip(level, rng):
    S = rng.pick(SX); V = rng.pick(VERBS); comp = rng.pick(V.comps); sub = S.text; bs = _be(S, True); rs = rng.pick(REASON)
    S2 = rng.pick([x for x in SX if x.pron != S.pron]); sm2 = _sm(S2)
    pos = {'i':'my','you':'your','he':'his','she':'her','we':'our','they':'their'}[S.pron]
    k = rng.pick({'easy':['gt','gt','gtn','gtq','wd','wdn','wdq','wd'],
                  'medium':['gt2','gt2','gtn','gtq','wd','wdn','wdq','abq'],
                  'hard':['cm_gt','cm_gt2','cm_wd','cm_ab','rew_gt','rew_ab','neg_t','q_t']}[level])
    h = {'gt':' (was / were)','wd':' (would / will)'}
    hh = lambda x: h[x] if level == 'easy' else ''
    if k == 'gt': return line(f"{sub} ___ going to {V.base} {comp}, {rs}." + hh('gt'), [bs])
    if k == 'gt2': return line(f"{sub} ___ ({V.base}) {comp}, {rs}. (going to)", [f"{bs} going to {V.base}"])
    if k == 'gtn':
        return line(f"{sub} ___ (not) going to {V.base} {comp}, but {_pr(S) if S.pron != 'i' else 'I'} changed {pos} mind.", [f"{bs}n't", f"{bs} not"])
    if k == 'gtq': return line(f"___ {_q(S)} going to {V.base} {comp} last night? (be)" if False else f"___ {_q(S)} going to {V.base} {comp} last night?" + hh('gt'), [_cp(bs)])
    if k == 'wd': return line(f"{sub} knew that {sm2} ___ {V.base} {comp}." + hh('wd'), ['would'])
    if k == 'wdn': return line(f"{sub} knew that {sm2} ___ (not) {V.base} {comp}.", ["wouldn't", 'would not'])
    if k == 'wdq': return line(f"Did {_q(S)} think that {sm2} ___ {V.base} {comp}?" + hh('wd'), ['would'])
    if k == 'abq': return line(f"{sub} {bs} just about ___ ({V.base}) {comp} when the phone rang.", [f"to {V.base}"])
    if k == 'cm_gt': return line(f"Correct the mistake: {sub} {bs} going {V.base} {comp}, {rs}.", [f"{sub} {bs} going to {V.base} {comp}, {rs}."])
    if k == 'cm_gt2': return line(f"Correct the mistake: {sub} {bs} going to {V.past} {comp}, {rs}.", [f"{sub} {bs} going to {V.base} {comp}, {rs}."])
    if k == 'cm_wd': return line(f"Correct the mistake: {sub} knew that {sm2} will {V.base} {comp}.", [f"{sub} knew that {sm2} would {V.base} {comp}."])
    if k == 'cm_ab': return line(f"Correct the mistake: {sub} {bs} about {V.base} {comp} when the phone rang.", [f"{sub} {bs} about to {V.base} {comp} when the phone rang."])
    if k == 'rew_gt': return line(f"Rewrite with 'was / were going to': {sub} planned to {V.base} {comp}, {rs}.", [f"{sub} {bs} going to {V.base} {comp}, {rs}."])
    if k == 'rew_ab': return line(f"Rewrite with 'was / were about to': {sub} {bs} ready to {V.base} {comp} when the phone rang.", [f"{sub} {bs} about to {V.base} {comp} when the phone rang."])
    if k == 'neg_t': return line(f"Make a negative sentence: {sub} {bs} going to {V.base} {comp}.", [f"{sub} {bs}n't going to {V.base} {comp}." if bs != 'was' or True else '', f"{sub} {bs} not going to {V.base} {comp}."])
    if k == 'q_t': return line(f"Make a question: {sub} {bs} going to {V.base} {comp}.", [f"{_cp(bs)} {_q(S)} going to {V.base} {comp}?"])
    return None

# ============ 5. countable and uncountable nouns ============
CNT = [("book","books"),("apple","apples"),("egg","eggs"),("chair","chairs"),("student","students"),("pen","pens"),("orange","oranges"),("bag","bags"),("idea","ideas"),
       ("question","questions"),("friend","friends"),("car","cars"),("window","windows"),("tomato","tomatoes"),("potato","potatoes"),("city","cities"),("country","countries"),
       ("baby","babies"),("family","families"),("knife","knives"),("leaf","leaves"),("child","children"),("man","men"),("woman","women"),("foot","feet"),("tooth","teeth"),
       ("mouse","mice"),("person","people"),("box","boxes"),("watch","watches"),("class","classes"),("dish","dishes"),("sheep","sheep"),("fish","fish"),("photo","photos"),
       ("hero","heroes"),("wolf","wolves"),("day","days"),("boy","boys"),("bus","buses"),("glass","glasses"),("story","stories"),("party","parties")]
IRR = {"child","man","woman","foot","tooth","mouse","person","knife","leaf","wolf","sheep","fish"}
UNC = ["advice","information","furniture","luggage","news","homework","equipment","rubbish","traffic","weather","knowledge","progress","money","water","milk","bread","rice","sugar","salt","music","butter","cheese","jewellery","evidence","research"]
PIECE = ["advice","information","furniture","news","equipment","evidence","jewellery"]
FOOD = ["milk","bread","rice","sugar","salt","water","butter","cheese","money","music"]
MEAS = [("bread",["loaf","slice"],["bottle","bar","sheet"]),("water",["glass","bottle"],["loaf","bar","sheet"]),("advice",["piece"],["loaf","bottle","slice"]),
        ("information",["piece"],["glass","bar","loaf"]),("furniture",["piece"],["bottle","slice","sheet"]),("news",["piece"],["glass","loaf","bar"]),
        ("chocolate",["bar","piece"],["bottle","loaf","sheet"]),("soup",["bowl","tin"],["loaf","bar","sheet"]),("milk",["carton","glass","bottle"],["loaf","bar","sheet"]),
        ("toothpaste",["tube"],["loaf","glass","bar"]),("cheese",["slice","piece"],["bottle","loaf","glass"]),("rice",["bowl","bag"],["bottle","loaf","bar"])]
PLACES = ["in the fridge","in the bag","on the table","in the cupboard","in the kitchen","in the box","in the car","on the shelf"]
def _ar(w): return 'an' if w[0] in 'aeiou' else 'a'
def gen_cu(level, rng):
    sg, pl = rng.pick(CNT); un = rng.pick(UNC); pla = rng.pick(PLACES)
    k = rng.pick({'easy':['pl','plq','pln','art','some_a','any_n','any_q','muchmany','meas'],
                  'medium':['pl','plq','pln','art','some_a','any_n','any_q','muchmany','meas2','pl2','somethere'],
                  'hard':['cm_a','cm_pl','cm_much','cm_pl2','neg_t','q_t','cm_a','cm_pl2','cm_much']}[level])
    uh = ' (some / any)' if level == 'easy' else ' (some / any / a / much / many)' if level == 'medium' else ''
    if k == 'pl': return line(f"There are two ___ ({sg}) {pla}.", [pl])
    if k == 'plq': return line(f"Are there any ___ ({sg}) {pla}?", [pl])
    if k == 'pln': return line(f"There aren't any ___ ({sg}) {pla}.", [pl])
    if k == 'pl2': return line(f"one {sg}, two ___", [pl]) if rng.pick([0, 1]) else line(f"I saw three ___ ({sg}) yesterday.", [pl])
    if k == 'art':
        h = ' (a / an)' if level == 'easy' else ''
        return line(f"There is ___ {sg} {pla}." + h, [_ar(sg)])
    if k == 'some_a': return line(f"There is ___ {un} {pla}." + uh, ['some'])
    if k == 'any_n': return line(f"There isn't ___ {un} {pla}." + uh, ['any'])
    if k == 'any_q': return line(f"Is there ___ {un} {pla}?" + uh, ['any'])
    if k == 'somethere': return line(f"There are ___ {pl} {pla}." + (' (some / any)' if level == 'easy' else ' (some / any / a / much)'), ['some'])
    if k == 'muchmany':
        if rng.pick([0, 1]): return line(f"How ___ {un} is there {pla}?" + (' (much / many)' if level == 'easy' else ''), ['much'])
        return line(f"How ___ {pl} are there {pla}?" + (' (much / many)' if level == 'easy' else ''), ['many'])
    if k in ('meas', 'meas2'):
        n, ok, wr = rng.pick(MEAS); opts = ok + wr[:2] if k == 'meas' else ok + wr
        rng.shuffle(opts)
        return line(f"Would you like a ___ of {n}? ({' / '.join(opts)})", ok)
    if k == 'cm_a':
        n = rng.pick(PIECE)
        return line(f"Correct the mistake: She gave me an {n}." if n[0] in 'aeiou' else f"Correct the mistake: She gave me a {n}.", [f"She gave me a piece of {n}.", f"She gave me some {n}."])
    if k == 'cm_pl':
        n = rng.pick(PIECE)
        return line(f"Correct the mistake: We bought two {n}s.", [f"We bought two pieces of {n}."])
    if k == 'cm_much':
        if rng.pick([0, 1]): return line(f"Correct the mistake: I have too many {un}.", [f"I have too much {un}."])
        return line(f"Correct the mistake: How many {un} do you have?", [f"How much {un} do you have?"])
    if k == 'cm_pl2':
        if sg not in IRR: return None
        return line(f"Correct the mistake: There are two {sg}s {pla}.", [f"There are two {pl} {pla}."])
    if k == 'neg_t':
        if rng.pick([0, 1]): return line(f"Make a negative sentence: There is some {un} {pla}.", [f"There isn't any {un} {pla}.", f"There is no {un} {pla}.", f"There is not any {un} {pla}."])
        return line(f"Make a negative sentence: There are some {pl} {pla}.", [f"There aren't any {pl} {pla}.", f"There are no {pl} {pla}.", f"There are not any {pl} {pla}."])
    if k == 'q_t':
        if rng.pick([0, 1]): return line(f"Make a question: There is some {un} {pla}.", [f"Is there any {un} {pla}?"])
        return line(f"Make a question: There are some {pl} {pla}.", [f"Are there any {pl} {pla}?"])
    return None

def gen_e3_jobs(C):
    return {'participle-adjectives': lambda: gen_topic(gen_pa, C, 321),
            'commonly-confused-words': lambda: gen_topic(gen_cw, C, 322),
            'would-rather-had-better-its-time-prefer': lambda: gen_topic(gen_wr, C, 323),
            'future-in-the-past': lambda: gen_topic(gen_fip, C, 324),
            'countable-and-uncountable-nouns': lambda: gen_topic(gen_cu, C, 325)}
