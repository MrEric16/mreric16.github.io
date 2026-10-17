from lib import *
PAIRS_RAW = """
I|study hard|I|pass the exam
you|miss the bus|you|be late for school
she|practise every day|she|play better
we|leave early|we|catch the train
he|eat too much|he|feel sick
they|win the match|they|celebrate
I|have time|I|visit my grandmother
you|work hard|you|get good marks
she|save money|she|buy a new laptop
we|take a taxi|we|arrive on time
he|forget his keys|he|stay outside
they|miss the train|they|call a taxi
I|see Aziz|I|give him the book
you|press this button|the machine@sg|start
it|rain|we|stay at home
the weather@sg|be nice|we|go to the park
you|add sugar|the tea@sg|taste sweeter
I|feel tired|I|go to bed early
she|be late|the teacher@sg|get angry
we|not hurry|we|miss the film
he|not study|he|fail the test
they|not practise|they|lose
you|not water the plants|the plants@pl|die
I|not sleep well|I|feel awful
the baby@sg|cry|her mother@sg|pick her up
you|drop that glass|it|break
you|touch the fire|you|get burnt
the shop@sg|be open|I|buy some bread
my friend@sg|call|I|answer the phone
I|win the lottery|I|travel the world
he|know the answer|he|tell us
she|have a car|she|drive to work
we|live near the sea|we|swim every day
they|have more time|they|learn Spanish
you|ask nicely|she|help you
I|find your keys|I|give them to you
the students@pl|do their homework|the teacher@sg|be happy
my brother@sg|clean his room|my mum@sg|give him some pocket money
you|eat healthy food|you|stay fit
we|buy tickets early|we|get good seats
he|run every morning|he|lose weight
she|read a lot|she|learn new words
I|practise speaking|I|improve my English
you|speak slowly|they|understand you
the train@sg|be late|we|miss the connection
I|have the money|I|buy that jacket
you|use a dictionary|you|find the word
she|drink coffee late|she|not sleep
we|take the motorway|we|get there faster
he|wear a coat|he|not catch a cold
I|know his number|I|call him
they|invite us|we|go to the party
you|turn on the heating|the room@sg|get warm
the teacher@sg|explain it again|I|understand
the weather@sg|be bad|the match@sg|be cancelled
you|mix red and blue|you|get purple
water@sg|reach 100 degrees|it|boil
you|cut an apple|it|turn brown
you|leave milk in the sun|it|go sour
I|miss breakfast|I|feel hungry by ten
they|come early|we|have time for coffee
he|get a pay rise|he|buy a car
she|pass her exams|her parents@pl|be proud
I|speak to the manager|he|listen to me
we|book a hotel|we|not sleep in the car
you|call me|I|come immediately
she|get the job|she|move to Dubai
my sister@sg|lend me her phone|I|text you
I|see a spider|I|scream
he|find a wallet|he|take it to the police
they|play well|they|score a goal
the lights@pl|go out|I|light a candle
I|not understand a word|I|look it up
the bus@sg|not come|we|walk
we|have homework|we|stay in
you|mix oil and water|they|not blend
I|have a headache|I|take a pill
she|go to the market|she|buy fresh fruit
you|forget your password|you|lose access
he|drive too fast|he|have an accident
we|recycle paper|we|save trees
they|plant more trees|the air@sg|be cleaner
I|get home early|I|cook dinner
you|touch hot water|it|hurt
she|miss the bus|she|walk to school
we|stay up late|we|feel tired the next day
he|not eat breakfast|he|feel dizzy
I|go to the bazaar|I|buy some apricots
they|win the lottery|they|buy a big house
you|study every evening|you|know the grammar
she|take the medicine|she|feel better
I|come first|my dad@sg|be proud of me
you|wake up early|you|have time for breakfast
my parents@pl|visit us|my mum@sg|cook plov
the road@sg|be icy|the drivers@pl|go slowly
the tickets@pl|be cheap|I|buy two
we|have a day off|we|go hiking
he|ask me|I|help him
you|put salt on ice|it|melt faster
I|have enough money|I|go abroad
the exam@sg|be easy|everyone@sg|pass
"""
EXTRA_FORMS = {
 'study':('studies','studied','studied','studying'), 'pass':('passes','passed','passed','passing'), 'miss':('misses','missed','missed','missing'),
 'practise':('practises','practised','practised','practising'), 'play':('plays','played','played','playing'), 'leave':('leaves','left','left','leaving'),
 'catch':('catches','caught','caught','catching'), 'eat':('eats','ate','eaten','eating'), 'feel':('feels','felt','felt','feeling'),
 'win':('wins','won','won','winning'), 'celebrate':('celebrates','celebrated','celebrated','celebrating'), 'have':('has','had','had','having'),
 'visit':('visits','visited','visited','visiting'), 'work':('works','worked','worked','working'), 'get':('gets','got','got','getting'),
 'save':('saves','saved','saved','saving'), 'buy':('buys','bought','bought','buying'), 'take':('takes','took','taken','taking'),
 'arrive':('arrives','arrived','arrived','arriving'), 'forget':('forgets','forgot','forgotten','forgetting'), 'stay':('stays','stayed','stayed','staying'),
 'call':('calls','called','called','calling'), 'see':('sees','saw','seen','seeing'), 'give':('gives','gave','given','giving'), 'press':('presses','pressed','pressed','pressing'),
 'start':('starts','started','started','starting'), 'rain':('rains','rained','rained','raining'), 'go':('goes','went','gone','going'), 'be':('is','was','been','being'),
 'add':('adds','added','added','adding'), 'taste':('tastes','tasted','tasted','tasting'), 'hurry':('hurries','hurried','hurried','hurrying'),
 'fail':('fails','failed','failed','failing'), 'lose':('loses','lost','lost','losing'), 'water':('waters','watered','watered','watering'), 'die':('dies','died','died','dying'),
 'sleep':('sleeps','slept','slept','sleeping'), 'cry':('cries','cried','cried','crying'), 'pick':('picks','picked','picked','picking'), 'drop':('drops','dropped','dropped','dropping'),
 'break':('breaks','broke','broken','breaking'), 'touch':('touches','touched','touched','touching'), 'know':('knows','knew','known','knowing'), 'tell':('tells','told','told','telling'),
 'drive':('drives','drove','driven','driving'), 'live':('lives','lived','lived','living'), 'swim':('swims','swam','swum','swimming'), 'learn':('learns','learned','learned','learning'),
 'ask':('asks','asked','asked','asking'), 'help':('helps','helped','helped','helping'), 'find':('finds','found','found','finding'), 'do':('does','did','done','doing'),
 'clean':('cleans','cleaned','cleaned','cleaning'), 'run':('runs','ran','run','running'), 'read':('reads','read','read','reading'), 'improve':('improves','improved','improved','improving'),
 'speak':('speaks','spoke','spoken','speaking'), 'understand':('understands','understood','understood','understanding'), 'use':('uses','used','used','using'),
 'drink':('drinks','drank','drunk','drinking'), 'wear':('wears','wore','worn','wearing'), 'catch':('catches','caught','caught','catching'), 'invite':('invites','invited','invited','inviting'),
 'turn':('turns','turned','turned','turning'), 'explain':('explains','explained','explained','explaining'), 'mix':('mixes','mixed','mixed','mixing'), 'reach':('reaches','reached','reached','reaching'),
 'cut':('cuts','cut','cut','cutting'), 'leave':('leaves','left','left','leaving'), 'come':('comes','came','come','coming'), 'book':('books','booked','booked','booking'),
 'lend':('lends','lent','lent','lending'), 'text':('texts','texted','texted','texting'), 'scream':('screams','screamed','screamed','screaming'), 'take':('takes','took','taken','taking'),
 'score':('scores','scored','scored','scoring'), 'light':('lights','lit','lit','lighting'), 'walk':('walks','walked','walked','walking'), 'recycle':('recycles','recycled','recycled','recycling'),
 'plant':('plants','planted','planted','planting'), 'cook':('cooks','cooked','cooked','cooking'), 'hurt':('hurts','hurt','hurt','hurting'), 'wake':('wakes','woke','woken','waking'),
 'put':('puts','put','put','putting'), 'melt':('melts','melted','melted','melting'), 'boil':('boils','boiled','boiled','boiling'), 'reload':('reloads','reloaded','reloaded','reloading'),
 'blend':('blends','blended','blended','blending'), 'look':('looks','looked','looked','looking'), 'take':('takes','took','taken','taking'), 'stay':('stays','stayed','stayed','staying'),
 'move':('moves','moved','moved','moving'), 'lose':('loses','lost','lost','losing'), 'buy':('buys','bought','bought','buying'), 'listen':('listens','listened','listened','listening'),
 'answer':('answers','answered','answered','answering'), 'celebrate':('celebrates','celebrated','celebrated','celebrating'),
}
FORMS_C = dict(FORMS); FORMS_C.update(EXTRA_FORMS)
class Cl:
    pass
def parse_subj(tok):
    if tok.endswith('@sg'): return Subj(tok[:-3],'sg','he',True)
    if tok.endswith('@pl'): return Subj(tok[:-3],'pl','they',True)
    k = {'I':'i','you':'you','he':'sg','she':'sg','it':'sg','we':'pl','they':'pl'}[tok]
    return Subj(tok if tok == 'I' else tok, k, {'I':'i','you':'you','he':'he','she':'she','it':'he','we':'we','they':'they'}[tok], True)
PAIRS = []
for ln in PAIRS_RAW.strip().split('\n'):
    a,b,c,d = ln.split('|'); PAIRS.append((parse_subj(a),b,parse_subj(c),d))

def split_vp(vp):
    w = vp.split(' ')
    neg = False
    if w[0] == 'not': neg = True; w = w[1:]
    return neg, w[0], ' '.join(w[1:])
def forms_of(v):
    return FORMS_C[v]
def be_f(kind, form):
    if form == 'pres': return 'am' if kind == 'i' else ('is' if kind == 'sg' else 'are')
    if form == 'past': return 'were'
    return None
def conj(vp, S, form, flip=False):
    """returns (list of accepted answers, full display string) for the verb phrase in tense form.
    form: pres, will, past (subj), pastperf, would, wouldhave"""
    neg, v, rest = split_vp(vp)
    if flip: neg = not neg
    s3, past, pp, ing = forms_of(v)
    tail = (' ' + rest) if rest else ''
    k = S.kind
    ans = []
    if form == 'pres':
        if v == 'be':
            b = be_f(k,'pres'); ans = ([("'m not" if b=='am' else f"{b}n't"), f"{b} not"] if neg else [b])
            full = f"{b} not" if neg else b
        else:
            h = 'do' if k != 'sg' else 'does'
            if neg: ans = [f"{h}n't {v}", f"{h} not {v}"]; full = f"{h} not {v}"
            else: ans = [s3 if k == 'sg' else v]; full = ans[0]
    elif form == 'will':
        if neg: ans = [f"won't {v}", f"will not {v}"]; full = f"will not {v}"
        else: ans = [f"will {v}", f"'ll {v}"]; full = f"will {v}"
    elif form == 'past':
        if v == 'be':
            ans = ([f"weren't", "were not", "wasn't", "was not"] if neg else ['were','was']) if k in ('i','sg') else ([f"weren't","were not"] if neg else ['were'])
            full = 'were not' if neg else 'were'
        else:
            if neg: ans = [f"didn't {v}", f"did not {v}"]; full = f"did not {v}"
            else: ans = [past]; full = past
    elif form == 'pastperf':
        if neg: ans = [f"hadn't {pp}", f"had not {pp}"]; full = f"had not {pp}"
        else: ans = [f"had {pp}", f"'d {pp}"]; full = f"had {pp}"
    elif form == 'would':
        if neg: ans = [f"wouldn't {v}", f"would not {v}"]; full = f"would not {v}"
        else: ans = [f"would {v}", f"'d {v}"]; full = f"would {v}"
    elif form == 'wouldhave':
        if neg: ans = [f"wouldn't have {pp}", f"would not have {pp}"]; full = f"would not have {pp}"
        else: ans = [f"would have {pp}", f"'d have {pp}"]; full = f"would have {pp}"
    return ans, full + tail, tail

TYPES = {'zero': ('pres','pres'), 'first': ('pres','will'), 'second': ('past','would'), 'third': ('pastperf','wouldhave')}
HINT = {'zero': 'general truth', 'first': 'real future', 'second': 'unreal present', 'third': 'unreal past'}


def grp_text(S, vp, form, mode, flip=False):
    """mode: 'blank' -> '___ (v)' ; 'full' -> full verb group. returns (text_without_subject, answers)"""
    ans, full, tail = conj(vp, S, form, flip)
    neg, v, rest = split_vp(vp)
    tail = (' ' + rest) if rest else ''
    if mode == 'blank':
        hint = f"(not / {v})" if (neg != flip) else f"({v})"
        return f"___ {hint}{tail}", ans
    return full, ans

def build(P, typ, rng, if_mode='full', res_mode='full', flip_res=False, unless=False, result_first=False, hint=False, forms=None, flip_if=False):
    S1,v1,S2,v2 = P
    f_if, f_res = forms or TYPES[typ]
    if unless:
        n1,_,_ = split_vp(v1)
        if not n1: return None
        t_if, a_if = grp_text(S1, v1, f_if, if_mode, flip=True); conj_word = 'unless'
    else:
        t_if, a_if = grp_text(S1, v1, f_if, if_mode, flip=flip_if); conj_word = 'if'
    t_res, a_res = grp_text(S2, v2, f_res, res_mode, flip=flip_res)
    ifc = f"{conj_word} {S1.text} {t_if}"
    resc = f"{S2.text} {t_res}"
    answers = []
    if result_first:
        s = cap(resc) + ' ' + ifc + '.'
        if res_mode == 'blank': answers.append(a_res)
        if if_mode == 'blank': answers.append(a_if)
    else:
        s = cap(ifc) + ', ' + resc + '.'
        if if_mode == 'blank': answers.append(a_if)
        if res_mode == 'blank': answers.append(a_res)
    return s, answers

def full_variants(P, typ, **kw):
    """all acceptable whole-sentence answers (was/were variants)"""
    S1,v1,S2,v2 = P
    s,_ = build(P, typ, None, **kw)
    out = [s]
    if TYPES[typ][0] == 'past' and split_vp(v1)[1] == 'be' and S1.kind in ('i','sg'):
        out.append(s.replace(' were ', ' was ',1) if ' were ' in s else s)
        out.append(s.replace(' were not ', ' was not ',1))
    return list(dict.fromkeys(out))

def question(P, typ, aux_blank=False):
    S1,v1,S2,v2 = P
    f_if, f_res = TYPES[typ]
    n2, w2, r2 = split_vp(v2)
    if n2: return None
    _, ifg = None, None
    t_if, a_if = grp_text(S1, v1, f_if, 'full')
    ifc = f"if {S1.text} {t_if}"
    tail = (' ' + r2) if r2 else ''
    s3, past, pp, ing = forms_of(w2)
    if typ == 'zero':
        if w2 == 'be': aux = 'Is' if S2.kind == 'sg' else ('Am' if S2.kind == 'i' else 'Are'); core = f"{S2.text}{tail}"
        else: aux = 'Does' if S2.kind == 'sg' else 'Do'; core = f"{S2.text} {w2}{tail}"
    elif typ == 'first': aux = 'Will'; core = f"{S2.text} {w2}{tail}"
    elif typ == 'second': aux = 'Would'; core = f"{S2.text} {w2}{tail}"
    else: aux = 'Would'; core = f"{S2.text} have {pp}{tail}"
    q = (('___' if aux_blank else aux) + ' ' + core + ' ' + ifc + '?')
    return q, aux

def wrong_forms(typ, rng):
    """(if_form, res_form) producing an error for the type"""
    c = {'zero': [('will','pres'), ('pres','will'), ('past','pres')],
         'first': [('will','will'), ('past','will'), ('pres','would'), ('pres','pres')],
         'second': [('would','would'), ('pres','would'), ('past','will'), ('past','pres')],
         'third': [('would','wouldhave'), ('past','wouldhave'), ('pastperf','would'), ('pastperf','pastperf')]}[typ]
    return rng.pick(c)

def can_flip(P):
    return P[2].text in ('I','you','he','she','we','they') and not split_vp(P[3])[0]
def gen_cond(typ, level, rng, hint=False):
    P = rng.pick(PAIRS)
    h = f" ({HINT[typ]})" if hint else ''
    def done(s, ans, extra=''):
        return line(s[:-1] + h + s[-1] if False else s + h if not s.endswith('?') else s + h, *ans)
    r = rng.r.random()
    rf = rng.pick([False, False, True])
    if level == 'easy':
        if r < .45: x = build(P, typ, rng, res_mode='blank', result_first=rf)
        elif r < .8: x = build(P, typ, rng, if_mode='blank', result_first=rf)
        else:
            if not can_flip(P): return None
            x = build(P, typ, rng, res_mode='blank', flip_res=True, result_first=rf)
        if not x: return None
        return line(x[0] + h, *x[1])
    if level == 'medium':
        k = rng.pick(['both','both','both','unless','negres','qaux','bothrf'])
        if k == 'both': x = build(P, typ, rng, 'blank', 'blank')
        elif k == 'bothrf': x = build(P, typ, rng, 'blank', 'blank', result_first=True)
        elif k == 'unless':
            if typ == 'third': return None
            x = build(P, typ, rng, 'blank', 'blank', unless=True)
        elif k == 'negres':
            if not can_flip(P): return None
            x = build(P, typ, rng, 'blank', 'blank', flip_res=True)
        else:
            qx = question(P, typ, True)
            if not qx: return None
            return line(qx[0] + h, [qx[1]])
        if not x: return None
        return line(x[0] + h, *x[1])
    k = rng.pick(['convert','convert','fix','fix','neg','q','swap','unless'])
    if k == 'convert':
        if hint: return None
        t2 = rng.pick([t for t in TYPES if t != typ])
        if 'zero' in (typ, t2) and False: return None
        src = build(P, typ, rng)[0]
        fv = full_variants(P, t2)
        return line(f"Change to the {t2} conditional: " + src, fv)
    if k == 'fix':
        fi, fr = wrong_forms(typ, rng)
        w = build(P, typ, rng, forms=(fi, fr))[0]
        okv = full_variants(P, typ)
        if w in okv: return None
        return line('Correct the mistake: ' + w + h, okv)
    if k == 'neg':
        if not can_flip(P): return None
        src = build(P, typ, rng)[0]
        return line('Make the result negative: ' + src + h, full_variants(P, typ, flip_res=True))
    if k == 'q':
        qx = question(P, typ)
        if not qx: return None
        src = build(P, typ, rng)[0]
        return line('Make a question about the result: ' + src + h, [qx[0]])
    if k == 'swap':
        src = build(P, typ, rng)[0]
        sw = full_variants(P, typ, result_first=True)
        return line('Rewrite starting with the result: ' + src + h, sw)
    if k == 'unless':
        n1,_,_ = split_vp(P[1])
        if not n1 or typ == 'third': return None
        src = build(P, typ, rng)[0]
        return line('Rewrite with "unless": ' + src + h, full_variants(P, typ, unless=True))

def gen_cond_topic(typ, counts, seed, which=False):
    rng = Rng(seed); out = {}
    for level, n in counts.items():
        seen, lines, tries = set(), [], 0
        while len(lines) < n and tries < n * 200:
            tries += 1
            t = rng.pick(['zero','first','second','third']) if which else typ
            l = gen_cond(t, level, rng, hint=which)
            if not l: continue
            q = l.split(' => ')[0]
            if q in seen: continue
            seen.add(q); lines.append(l)
        out[level] = lines
    return out
