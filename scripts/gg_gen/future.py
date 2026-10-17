from tense import *

# hand-written context banks. (text with ___ , answers)
SPONT = [  # decision made at the moment of speaking -> will
 ("'I'm thirsty.' 'I ___ (get) you some water.'", ['will get',"'ll get"]),
 ("'The phone is ringing.' 'I ___ (answer) it.'", ['will answer',"'ll answer"]),
 ("'I can't carry all these bags.' 'Don't worry. I ___ (help) you.'", ['will help',"'ll help"]),
 ("'I've left my wallet at home.' 'Don't worry. I ___ (lend) you some money.'", ['will lend',"'ll lend"]),
 ("'It's very hot in here.' 'I ___ (open) the window.'", ['will open',"'ll open"]),
 ("'We haven't got any milk.' 'OK, I ___ (buy) some on my way home.'", ['will buy',"'ll buy"]),
 ("'Someone is knocking at the door.' 'I ___ (see) who it is.'", ['will see',"'ll see"]),
 ("'I can't find my pen.' 'I ___ (look) for it with you.'", ['will look',"'ll look"]),
 ("'This box is very heavy.' 'I ___ (carry) it for you.'", ['will carry',"'ll carry"]),
 ("'I don't know the answer.' 'I ___ (ask) the teacher.'", ['will ask',"'ll ask"]),
 ("'I'm cold.' 'I ___ (close) the window.'", ['will close',"'ll close"]),
 ("'The bus has just left.' 'OK, we ___ (take) a taxi.'", ['will take',"'ll take"]),
 ("'There's no sugar.' 'I ___ (go) to the shop.'", ['will go',"'ll go"]),
 ("'I'm hungry.' 'I ___ (make) you a sandwich.'", ['will make',"'ll make"]),
 ("'My bag is broken.' 'I ___ (fix) it for you.'", ['will fix',"'ll fix"]),
 ("'I have forgotten Anna's number.' 'I ___ (call) her for you.'", ['will call',"'ll call"]),
 ("'It's raining.' 'Wait here. I ___ (get) an umbrella.'", ['will get',"'ll get"]),
 ("'The room is dirty.' 'I ___ (clean) it now.'", ['will clean',"'ll clean"]),
 ("'I don't understand this word.' 'I ___ (explain) it.'", ['will explain',"'ll explain"]),
 ("'I'm tired.' 'I ___ (drive) then.'", ['will drive',"'ll drive"]),
 ("'We need some bread.' 'OK. I ___ (bake) some.'", ['will bake',"'ll bake"]),
 ("'My phone is dead.' 'You can use mine. I ___ (give) it to you.'", ['will give',"'ll give"]),
 ("'The photocopier isn't working.' 'I ___ (call) the technician.'", ['will call',"'ll call"]),
 ("'I'm lost.' 'Don't worry. I ___ (show) you the way.'", ['will show',"'ll show"]),
 ("'That's the doorbell.' 'I ___ (open) the door.'", ['will open',"'ll open"]),
 ("'I'd like to see the menu.' 'Of course. I ___ (bring) it now.'", ['will bring',"'ll bring"]),
 ("'It's Mum's birthday tomorrow!' 'Oh no! I ___ (buy) her a present now.'", ['will buy',"'ll buy"]),
 ("'I can't reach the top shelf.' 'I ___ (get) it for you.'", ['will get',"'ll get"]),
 ("'The film starts soon.' 'OK, I ___ (turn) off my phone.'", ['will turn',"'ll turn"]),
 ("'I'm too busy to cook.' 'I ___ (cook) dinner tonight.'", ['will cook',"'ll cook"]),
 ("'There is a spider in the bath!' 'I ___ (get) rid of it.'", ['will get',"'ll get"]),
 ("'The printer is empty.' 'I ___ (find) some paper.'", ['will find',"'ll find"]),
 ("'Which one do you want?' 'Hmm, I ___ (have) the blue one.'", ['will have',"'ll have"]),
 ("'Shall we go by bus or by train?' 'I think we ___ (go) by train.'", ['will go',"'ll go"]),
 ("'I'm worried about the test.' 'I ___ (help) you study.'", ['will help',"'ll help"]),
 ("'The kitchen is a mess.' 'I ___ (wash) the dishes.'", ['will wash',"'ll wash"]),
 ("'It's too noisy here.' 'I ___ (ask) them to be quiet.'", ['will ask',"'ll ask"]),
 ("'I need a lift to the airport.' 'I ___ (take) you.'", ['will take',"'ll take"]),
 ("'I haven't got a pen.' 'Here, I ___ (lend) you mine.'", ['will lend',"'ll lend"]),
 ("'There's nothing to eat.' 'I ___ (order) a pizza.'", ['will order',"'ll order"]),
 ("'I can't open this jar.' 'Give it to me. I ___ (try).'", ['will try',"'ll try"]),
 ("'My computer has crashed.' 'I ___ (restart) it for you.'", ['will restart',"'ll restart"]),
 ("'Someone left the lights on.' 'I ___ (turn) them off.'", ['will turn',"'ll turn"]),
 ("'The baby is crying.' 'I ___ (pick) him up.'", ['will pick',"'ll pick"]),
 ("'I can't hear the teacher.' 'I ___ (ask) her to speak louder.'", ['will ask',"'ll ask"]),
 ("'I have no change.' 'Don't worry. I ___ (pay).'", ['will pay',"'ll pay"]),
 ("'My car won't start.' 'I ___ (push) it.'", ['will push',"'ll push"]),
 ("'I'm bored.' 'I ___ (put) some music on.'", ['will put',"'ll put"]),
 ("'It's getting dark.' 'I ___ (switch) on the light.'", ['will switch',"'ll switch"]),
 ("'I'm late for the lesson.' 'I ___ (tell) the teacher you're coming.'", ['will tell',"'ll tell"]),
 ("'My feet hurt.' 'Sit down. I ___ (bring) you a chair.'", ['will bring',"'ll bring"]),
 ("'We're out of tea.' 'I ___ (make) some coffee instead.'", ['will make',"'ll make"]),
 ("'I'm thinking about a present for Dad.' 'I know! I ___ (buy) him a book.'", ['will buy',"'ll buy"]),
]
EVID = [  # evidence now -> going to
 ("Look at those black clouds! It ___ (rain).", ['is going to rain']),
 ("Watch out! That boy ___ (fall) off his bike.", ['is going to fall']),
 ("Look! The baby is so sleepy. She ___ (fall) asleep.", ['is going to fall']),
 ("The sky is red this evening. It ___ (be) a beautiful day tomorrow.", ['is going to be']),
 ("Be careful! You ___ (spill) your coffee.", ['are going to spill']),
 ("Look at the score. Our team ___ (win).", ['is going to win']),
 ("He is driving too fast. He ___ (have) an accident.", ['is going to have']),
 ("There is no petrol in the car. We ___ (stop).", ['are going to stop']),
 ("Look at his face. He ___ (cry).", ['is going to cry']),
 ("The glass is on the edge of the table. It ___ (fall).", ['is going to fall']),
 ("I feel terrible. I think I ___ (be) sick.", ['am going to be']),
 ("The traffic is terrible. We ___ (be) late.", ['are going to be']),
 ("Look at that crack in the ice! It ___ (break).", ['is going to break']),
 ("Her eyes are red. She ___ (cry).", ['is going to cry']),
 ("The teacher looks angry. He ___ (shout).", ['is going to shout']),
 ("The runner is far ahead of the others. She ___ (win).", ['is going to win']),
 ("There are no tickets left. We ___ (not / get) in.", ["aren't going to get", "are not going to get"]),
 ("It is 8.55 and the lesson starts at 9. We ___ (be) late.", ['are going to be']),
 ("The wind is getting stronger. There ___ (be) a storm.", ['is going to be']),
 ("Look! The cat is climbing the curtain. It ___ (fall).", ['is going to fall']),
 ("The pot is boiling over. The water ___ (spill) on the floor.", ['is going to spill']),
 ("Listen! The orchestra is tuning up. The concert ___ (start).", ['is going to start']),
 ("My tooth hurts a lot. I ___ (go) to the dentist.", ['am going to go']),
 ("She has bought flour and eggs. She ___ (bake) a cake.", ['is going to bake']),
 ("Look at the sky. It ___ (snow).", ['is going to snow']),
 ("The boy is standing on the wall and he can't balance. He ___ (fall).", ['is going to fall']),
 ("The clouds are disappearing. It ___ (be) sunny.", ['is going to be']),
 ("The car in front is braking. We ___ (stop) too.", ['are going to stop']),
 ("He hasn't studied at all. He ___ (fail) the exam.", ['is going to fail']),
 ("They've dug a big hole in the road. They ___ (build) a new pipe.", ['are going to build']),
 ("Her suitcase is on the bed. She ___ (travel).", ['is going to travel']),
 ("Look at his muscles! He ___ (lift) that weight easily.", ['is going to lift']),
 ("There's a long queue. We ___ (wait) for ages.", ['are going to wait']),
 ("Be careful with that knife! You ___ (cut) yourself.", ['are going to cut']),
 ("The petrol light is on. The car ___ (stop) soon.", ['is going to stop']),
 ("She's holding a pencil and an empty page. She ___ (draw) something.", ['is going to draw']),
 ("The goalkeeper is out of position. The striker ___ (score).", ['is going to score']),
 ("The coffee is too hot. You ___ (burn) your tongue.", ['are going to burn']),
 ("The film has just started. It ___ (be) very long.", ['is going to be']),
 ("Dark clouds are coming. We ___ (get) wet.", ['are going to get']),
]
OFFER = [  # promises / offers / refusals -> will
 ("I promise I ___ (not / tell) anyone your secret.", ["won't tell","will not tell"]),
 ("I ___ (not / lend) you any more money!", ["won't lend","will not lend"]),
 ("The car ___ (not / start). It's very old.", ["won't start","will not start"]),
 ("I promise I ___ (call) you as soon as I arrive.", ["will call","'ll call"]),
 ("Don't worry. I ___ (be) on time.", ["will be","'ll be"]),
 ("I promise I ___ (never / lie) to you again.", ["will never lie","'ll never lie"]),
 ("He ___ (not / listen) to anybody. He is so stubborn.", ["won't listen","will not listen"]),
 ("I ___ (not / forget) your birthday this year, I promise.", ["won't forget","will not forget"]),
 ("Shall I help you? Yes, please. I think I ___ (need) it.", ["will need","'ll need"]),
 ("I promise I ___ (do) the dishes tonight.", ["will do","'ll do"]),
]
PLAN_END = ['next week','next month','next year','tomorrow','this weekend','next summer','after school','on Saturday','in July','at the weekend']
PLAN_LEAD = [("I've decided:", 'I'), ("I've already made up my mind:", 'I'), ("We've decided:", 'we'), ("We've already bought the tickets:", 'we'), ("My plan is clear:", 'I'), ("I've got a plan:", 'I')]

def plan_item(rng, neg_=False):
    V = rng.pick([v for v in VERBS if not v.ach]); comp = rng.pick(V.comps); end = rng.pick(PLAN_END)
    lead, subj = rng.pick(PLAN_LEAD)
    S = [s for s in SUBJ if s.text == ('We' if subj.lower() == 'we' else 'I')][0]
    S1 = SUBJ[0] if S.text == 'I' else SUBJ[4]
    if neg_:
        return line(f"{lead} {subj} ___ (not / {V.base}) {comp} {end}.", grp('fg',S1,V,True)), V
    return line(f"{lead} {subj} ___ ({V.base}) {comp} {end}.", grp('fg',S1,V)), V

def gen_wg(level, rng):
    r = rng.r.random()
    if level == 'easy':
        if r < .4: q,a = rng.pick(SPONT); return line(q,a)
        if r < .65: q,a = rng.pick(EVID); return line(q,a)
        l,_ = plan_item(rng); return l
    if level == 'medium':
        if r < .25: q,a = rng.pick(SPONT); return line(q,a)
        if r < .45: q,a = rng.pick(EVID); return line(q,a)
        if r < .55: q,a = rng.pick(OFFER); return line(q,a)
        if r < .8: l,_ = plan_item(rng); return l
        l,_ = plan_item(rng, True); return l
    # hard
    if r < .3:
        a = rng.pick(['spont','plan','evid'])
        if a == 'spont':
            q,ans = rng.pick(SPONT)
            return line('Correct the mistake: ' + q.replace('___ (','are going to... (') if False else q, ans)
        if a == 'plan':
            l,V = plan_item(rng); return l
        q,ans = rng.pick(EVID); return line(q,ans)
    if r < .55:
        # two-blank dialogue: plan then spontaneous
        V1 = rng.pick(VERBS); c1 = rng.pick(V1.comps)
        q,ans = rng.pick(SPONT)
        return line(q, ans)
    if r < .8:
        # question forms
        V = rng.pick(VERBS); comp = rng.pick(V.comps); end = rng.pick(PLAN_END)
        kind = rng.pick(['gt','w'])
        if kind == 'gt':
            S = rng.pick([s for s in SUBJ if s.kind != 'i'])
            a,rr = qp('fg',S,V); return line(f"I know {S.mid} has decided already. ___ {S.mid} ___ ({V.base}) {comp} {end}?", [a],[rr])
        S = rng.pick([s for s in SUBJ if s.kind != 'i'])
        return line(f"Look at the sign! {S.text} ___ (not / {V.base}) {comp}. It's not allowed.", grp('fg',S,V,True)) if False else None
    S = SUBJ[0]
    V = rng.pick(VERBS); comp = rng.pick(V.comps)
    return line(f"'Oh, I've just realised I haven't got any money.' 'Don't worry, I ___ (pay) for {rng.pick(['lunch','the tickets','the taxi','you'])}.'", ['will pay',"'ll pay"])

def gen_wg_topic(counts, seed):
    rng = Rng(seed); out = {}
    for level, n in counts.items():
        seen, lines, tries = set(), [], 0
        while len(lines) < n and tries < n * 200:
            tries += 1
            l = gen_wg(level, rng)
            if not l: continue
            q = l.split(' => ')[0]
            if q in seen: continue
            seen.add(q); lines.append(l)
        out[level] = lines
    return out


TT = [("The train",['leave','arrive']),("The bus",['leave','arrive']),("The flight",['leave','arrive']),("The film",['start','finish','end']),
      ("The lesson",['start','begin','finish','end']),("The match",['start','begin','finish','end']),("The concert",['start','begin','finish','end']),
      ("The exam",['start','begin','finish','end']),("The meeting",['start','begin','finish','end']),("The ceremony",['start','begin','finish','end']),
      ("The shop",['open','close']),("The museum",['open','close']),("The bank",['open','close']),("The library",['open','close']),("The party",['start','begin','end'])]
TT_FORMS = {'leave':'leaves','arrive':'arrives','start':'starts','finish':'finishes','end':'ends','begin':'begins','open':'opens','close':'closes'}
TT_TIME = ['at 8.30 tomorrow','at six o\'clock tonight','at nine on Friday','at 7.15 next Monday','at half past ten tomorrow morning','at noon on Saturday','at 5 p.m. tomorrow','at 6.45 tomorrow evening','at ten past two on Wednesday','at midnight on Sunday']
def tt_item(rng, mode=None):
    n, vs = rng.pick(TT); v = rng.pick(vs); tm = rng.pick(TT_TIME)
    mode = mode or rng.pick(['aff','aff','neg','q','wh'])
    if mode == 'aff': return line(f"{n} ___ ({v}) {tm}. (timetable)", [TT_FORMS[v]])
    if mode == 'neg': return line(f"{n} ___ (not / {v}) {tm}. It's cancelled. (timetable)", ["doesn't "+v, "does not "+v])
    if mode == 'q': return line(f"___ {n.lower()} {v} {tm}? (timetable)", ['Does'])
    return line(f"What time ___ {n.lower()} ___ ({v}) tomorrow? (timetable)", ['does'], [v])
ARR = ["{P}'ve got two tickets.","It's all arranged.","{P}'ve booked the table.","{P} have already bought the tickets.","My diary says so.","The teacher has arranged it."]
def arr_item(rng, neg_=False):
    V = rng.pick([v for v in VERBS if not v.ach]); comp = rng.pick(V.comps); end = rng.pick(FPC_END)
    S = rng.pick([SUBJ[0], SUBJ[4]]); a = rng.pick(ARR).replace('{P}', S.text)
    ans = grp('fpc',S,V,neg_) + grp('fg',S,V,neg_)
    return line(f"{a} {S.text} ___ ({'not / ' if neg_ else ''}{V.base}) {comp} {end}.", ans)
def gen_all(level, rng):
    r = rng.r.random()
    if level == 'easy':
        if r < .3: q,a = rng.pick(SPONT); return line(q,a)
        if r < .5: q,a = rng.pick(EVID); return line(q,a)
        if r < .75: return tt_item(rng,'aff')
        l,_ = plan_item(rng); return l
    if level == 'medium':
        if r < .2: q,a = rng.pick(SPONT); return line(q,a)
        if r < .35: q,a = rng.pick(EVID); return line(q,a)
        if r < .5: q,a = rng.pick(OFFER); return line(q,a)
        if r < .75: return tt_item(rng)
        if r < .9: return arr_item(rng)
        l,_ = plan_item(rng, True); return l
    if r < .25: return tt_item(rng)
    if r < .5: return arr_item(rng, rng.pick([False,True]))
    if r < .65: q,a = rng.pick(EVID); return line(q,a)
    if r < .8: q,a = rng.pick(SPONT); return line(q,a)
    l,_ = plan_item(rng, rng.pick([False,True])); return l
def gen_all_topic(counts, seed):
    rng = Rng(seed); out = {}
    for level, n in counts.items():
        seen, lines, tries = set(), [], 0
        while len(lines) < n and tries < n * 200:
            tries += 1
            l = gen_all(level, rng)
            if not l: continue
            q = l.split(' => ')[0]
            if q in seen: continue
            seen.add(q); lines.append(l)
        out[level] = lines
    return out
