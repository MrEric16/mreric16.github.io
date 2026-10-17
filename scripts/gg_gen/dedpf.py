from lib import *
from passive import gen_topic
def cap1(s): return s[0].upper() + s[1:]
# (S, pn, Pn, pos)
SG = [("Tom","he","He","his"),("Anna","she","She","her"),("My brother","he","He","his"),("My sister","she","She","her"),("My friend Ali","he","He","his"),("My cousin Dilya","she","She","her")]
PL = [("The students","they","They","their"),("My parents","they","They","their"),("The boys","they","They","their"),("The girls","they","They","their")]
NOW = {
'must':[("{X} is wearing a white coat and a stethoscope.","a doctor"),("{X} has won the national competition three times.","a very good player"),("{X} has been running for two hours.","very tired"),
 ("{X} speaks five languages.","clever"),("{X} lives in a huge house and drives an expensive car.","rich"),("{X} is wearing a uniform and a badge.","a police officer"),
 ("{X} has been working all night.","exhausted"),("{X} always gets top marks.","a good student"),("{X} has not eaten since morning.","hungry"),("{X} is shivering and wearing two coats.","cold"),
 ("{X} has just won the lottery.","very happy"),("{X} teaches at the university.","very intelligent"),("{X} has a new baby and no sleep.","tired"),("{X} is carrying a huge suitcase and a passport.","going on holiday"),
 ("{X} has lived in London for ten years.","good at English"),("{X} has just run a marathon.","tired out"),("{X} has three jobs.","very busy"),("{X} is holding a tennis racket.","a tennis player"),
 ("{X} is always smiling.","happy"),("{X} has been waiting for hours.","bored")],
'cant':[("{X} is only six years old.","a university student"),("{X} is in Spain this week.","at school today"),("{X} hates sport.","a professional footballer"),("{X} never eats meat.","eating a steak"),
 ("{X} is sitting next to me.","in the next room"),("{X} has no money at all.","rich"),("{X} is afraid of water.","swimming in the lake"),("{X} cannot drive.","the driver of that bus"),
 ("{X} is on a plane to Paris.","at home now"),("{X} failed every exam.","the best student"),("{X} always goes to bed at nine.","at the disco now"),("{X} is terrible at maths.","a maths teacher"),
 ("{X} has just had lunch.","hungry"),("{X} is deaf.","listening to the radio"),("{X} does not speak any English.","the English teacher"),("{X} is in hospital.","at the party"),
 ("{X} left an hour ago.","still here"),("{X} is fifteen.","old enough to vote"),("{X} is asleep upstairs.","in the garden")],
'might':[("I do not know where {X} is.","in the library"),("{X} has not answered the phone.","in the shower"),("I cannot see {pos} car.","at work"),("I am not sure what {X} does.","a teacher"),
 ("{X} is not at home.","at the shops"),("I have not met {X}.","a student"),("{X} is looking worried.","in trouble"),("{X} did not come to school.","ill"),("{X} does not look well.","getting a cold"),
 ("{X} is late.","stuck in traffic"),("{X} is quiet today.","tired"),("{X} has a big bag.","going away"),("Nobody knows where {X} lives.","in the old town"),("{X} is not on the list.","invited"),
 ("{X} is wearing a suit.","going to an interview"),("{X} has a map in {pos} hand.","lost"),("{X} never talks about {pos} job.","a secret agent"),("{X} is not answering the door.","asleep")],
}
PAST = {
'must':[("{X} looks very happy.","passed the exam","passed the exam"),("{X} has a tan.","spent a week on the beach","spent a week on the beach"),("{X} is covered in mud.","fell into a puddle","fallen into a puddle"),
 ("{X} has a bad cough.","caught a cold","caught a cold"),("{X} knows all the answers.","studied hard","studied hard"),("{X} is out of breath.","ran all the way here","run all the way here"),
 ("{X} is very sleepy.","stayed up late","stayed up late"),("{X} is holding a trophy.","won the match","won the match"),("{X} is very upset.","failed the test","failed the test"),
 ("{X} smells of smoke.","was near a fire","been near a fire"),("{X} is crying.","heard bad news","heard bad news"),("{X} is limping.","hurt a leg","hurt a leg"),
 ("{X} has sunburn.","stayed in the sun too long","stayed in the sun too long"),("{X} is very pale.","saw a ghost","seen a ghost"),("{X} is carrying shopping bags.","went to the shops","been to the shops"),
 ("{X} speaks fluent French.","lived in Paris","lived in Paris")],
'cant':[("{X} was with me all evening.","broke the window","broken the window"),("{X} does not speak Chinese.","wrote this letter in Chinese","written this letter in Chinese"),
 ("{X} was in class all morning.","saw the film","seen the film"),("{X} is afraid of heights.","climbed that mountain","climbed that mountain"),("{X} was ill in bed.","won the race","won the race"),
 ("{X} was abroad last week.","came to the party","come to the party"),("{X} never drinks coffee.","drank all the coffee","drunk all the coffee"),("{X} does not know how to swim.","swam across the river","swum across the river"),
 ("{X} had no money.","bought that car","bought that car"),("{X} hates football.","watched the match","watched the match"),("{X} cannot drive.","drove the bus","driven the bus"),
 ("{X} is allergic to nuts.","ate the cake","eaten the cake"),("{X} does not have a key.","opened the door","opened the door"),("{X} has never been to Paris.","took that photo in Paris","taken that photo in Paris"),
 ("{X} was only two in 2010.","started school in 2010","started school in 2010")],
'might':[("I do not know where {X} is.","missed the bus","missed the bus"),("{X} has not called me back.","forgot","forgotten"),("{X} did not come to school.","caught a cold","caught a cold"),
 ("{X} is not in the office.","went home","gone home"),("{X} is very quiet.","fell asleep","fallen asleep"),("Nobody saw {X} today.","left early","left early"),("{X} is late.","got lost","got lost"),
 ("{X} is not answering the phone.","left the phone at home","left the phone at home"),("I have not seen {X} since Monday.","moved to another city","moved to another city"),("{X} looks angry.","had an argument","had an argument"),
 ("{X} is not at the party.","stayed at home","stayed at home"),("{X} has not done the homework.","lost the book","lost the book")],
}
ANSD = {'must':['must'],'cant':["can't","cannot","couldn't"],'might':['might','may','could']}
DEG = {'must':'(certain)','cant':'(certain it is not true)','might':'(not sure)'}
def mid(S): return S[0].lower()+S[1:] if S.split()[0] in ('My','Our','The') else S
def _ev(t, X, pos): return cap1(t.format(X=X, pos=pos))
def gen_deduction(level, rng):
    S, pn, Pn, pos = rng.pick(SG)
    kind = rng.pick(['must','must','cant','cant','might','might'])
    past = rng.pick([0,1])
    fr = rng.pick([1,2])
    if not past:
        t, pred = rng.pick(NOW[kind])
        mid_ = f"be {pred}"
        mk = lambda mod: (f"{_ev(t,S,pos)} {Pn} {mod} be {pred}." if fr == 1 else f"{S} {mod} be {pred}. {_ev(t,pn,pos)}")
        two = lambda: (f"{_ev(t,S,pos)} {Pn} ___ ___ {pred}." if fr == 1 else f"{S} ___ ___ {pred}. {_ev(t,pn,pos)}")
        fixrest = f"be {pred}"; 
        rew = {'must':f"I am sure {mid(S)} is {pred}.", 'cant':f"I am sure {mid(S)} is not {pred}.", 'might':f"Perhaps {mid(S)} is {pred}."}[kind]
        gdf = lambda m: f"{S} {m} be {pred}."
        wrong = {'must':[f"{S} must to be {pred}.",f"{S} musts be {pred}.",f"{S} must is {pred}."],'cant':[f"{S} can't to be {pred}.",f"{S} can't is {pred}.",f"{S} don't can be {pred}."],'might':[f"{S} might to be {pred}.",f"{S} might is {pred}.",f"{S} mights be {pred}."]}[kind]
        ctx = _ev(t, S, pos)
    else:
        t, pas, pp = rng.pick(PAST[kind])
        mk = lambda mod: (f"{_ev(t,S,pos)} {Pn} {mod} have {pp}." if fr == 1 else f"{S} {mod} have {pp}. {_ev(t,pn,pos)}")
        two = lambda: (f"{_ev(t,S,pos)} {Pn} ___ ___ {pp}." if fr == 1 else f"{S} ___ ___ {pp}. {_ev(t,pn,pos)}")
        rew = {'must':f"I am sure {mid(S)} {pas}.", 'cant':f"I am sure it is impossible that {mid(S)} {pas}.", 'might':f"Perhaps {mid(S)} {pas}."}[kind]
        gdf = lambda m: f"{S} {m} have {pp}."
        wrong = {'must':[f"{S} must of {pp}.",f"{S} must had {pp}.",f"{S} must to have {pp}."],'cant':[f"{S} can't of {pp}.",f"{S} can't had {pp}.",f"{S} can't to have {pp}."],'might':[f"{S} might of {pp}.",f"{S} might had {pp}.",f"{S} mights have {pp}."]}[kind]
        ctx = _ev(t, S, pos)
    blank = (lambda: (f"{_ev(t,S,pos)} {Pn} ___ {'be '+pred if not past else 'have '+pp}." if fr == 1 else f"{S} ___ {'be '+pred if not past else 'have '+pp}. {_ev(t,pn,pos)}"))
    if level == 'easy': return line(blank() + ' ' + DEG[kind], ANSD[kind])
    if level == 'medium':
        if rng.pick([0,1]): return line(two() + ' ' + DEG[kind], ANSD[kind], ['have' if past else 'be'])
        return line(blank() + ' ' + DEG[kind], ANSD[kind])
    k = rng.pick(['rewrite','fix'])
    if k == 'rewrite':
        nm = {'must':'must','cant':"can't",'might':'might'}[kind]
        ex = {'must':[gdf('must')],'cant':[gdf("can't"),gdf('cannot')],'might':[gdf('might'),gdf('may'),gdf('could')]}[kind]
        lbl = 'Rewrite with "' + nm + (' have' if past else '') + '": '
        return line(lbl + (ctx + ' ' if True else '') + rew, [ctx + ' ' + g for g in ex])
    ex = {'must':[gdf('must')],'cant':[gdf("can't"),gdf('cannot')],'might':[gdf('might'),gdf('may'),gdf('could')]}[kind]
    return line('Correct the mistake: ' + ctx + ' ' + rng.pick(wrong), [ctx + ' ' + g for g in ex])

PERF = {
'should':[("{X} failed the exam.","studied harder"),("{X} missed the train.","left earlier"),("{X} got lost.","taken a map"),("{X} forgot {pos} keys.","checked {pos} bag"),
 ("{X} was late for the lesson.","got up earlier"),("{X} felt ill after the party.","eaten less"),("{X} had no money at the end of the month.","saved some"),("{X} lost the match.","trained more"),
 ("{X} did not understand the homework.","asked the teacher"),("{X} got sunburnt.","used some cream"),("{X} was hungry in the afternoon.","had breakfast"),("{X} broke {pos} phone.","bought a case")],
'shouldnt':[("{X} caught a cold.","gone out without a coat"),("{X} had an accident.","driven so fast"),("{X} lost a friend.","told the secret"),("{X} got a bad mark.","copied from a friend"),
 ("{X} was ill the next day.","eaten so much"),("{X} woke up late.","stayed up so late"),("{X} upset the headmaster.","been so rude"),("{X} lost all {pos} money.","gambled"),
 ("{X} burnt the dinner.","left it on the cooker"),("{X} failed the driving test.","been so nervous")],
'could':[("{X} did not take the job in London.","earned more money"),("{X} did not go to university.","studied medicine"),("{X} lost 2-1.","won the match"),("{X} did not call the police.","stopped the thief"),
 ("{X} stayed at home on Saturday.","gone to the beach"),("{X} did not enter the competition.","won a prize"),("{X} did not ask for help.","finished the work faster"),("{X} left school at sixteen.","passed the exams"),
 ("{X} did not learn the piano.","studied music"),("{X} did not tell the truth.","saved a lot of trouble")],
'neednt':[("{X} brought an umbrella, but it was sunny.","brought it"),("{X} cooked for twenty, but only ten came.","cooked so much"),("{X} hurried, but the train was late.","hurried"),
 ("{X} bought the book, but the teacher gave it away free.","bought it"),("{X} ironed the shirt, but nobody saw it.","ironed it"),("{X} got up at five, but the exam started at noon.","got up so early"),
 ("{X} took a taxi, but the bus was just as fast.","taken a taxi"),("{X} paid for the ticket, but entry was free.","paid"),("{X} cleaned the whole room, but the guests did not come.","cleaned it")],
}
ANSP = {'should':['should',"ought to"],'shouldnt':["shouldn't","should not","ought not to"],'could':['could','might'],'neednt':["needn't","need not"]}
FORM = {'should':'should','shouldnt':"shouldn't",'could':'could','neednt':"needn't"}
def gen_perfect(level, rng):
    S, pn, Pn, pos = rng.pick(SG + PL)
    kind = rng.pick(['should','shouldnt','could','neednt'])
    t, pp = rng.pick(PERF[kind]); pp = pp.format(pos=pos)
    fr = rng.pick([1,2])
    sit1 = _ev(t, S, pos); sit2 = _ev(t, pn, pos)
    def mk(mod, a=True): return f"{sit1} {Pn} {mod} have {pp}." if fr == 1 else f"{S} {mod} have {pp}. {sit2}"
    ctx = sit1
    if level == 'easy': return line(mk('___'), ANSP[kind])
    if level == 'medium':
        if rng.pick([0,1]) or kind in ('shouldnt','neednt'): 
            return line((f"{sit1} {Pn} ___ ___ {pp}." if fr == 1 else f"{S} ___ ___ {pp}. {sit2}"), ANSP[kind], ['have'])
        return line((f"{sit1} ___ {pn} have {pp}?" if fr == 1 and kind == 'should' else mk('___')), ['Should'] if (fr == 1 and kind == 'should') else ANSP[kind])
    k = rng.pick(['fix','fix','rewrite'])
    m = FORM[kind]
    gds = [f"{m} have {pp}."]
    if kind == 'should': gds.append(f"ought to have {pp}.")
    if kind == 'shouldnt': gds += [f"should not have {pp}.", f"ought not to have {pp}."]
    if kind == 'could': gds.append(f"might have {pp}.")
    if kind == 'neednt': gds.append(f"need not have {pp}.")
    if k == 'fix':
        w = rng.pick([f"{m} of {pp}.", f"{m} had {pp}.", f"{m} to have {pp}."])
        return line('Correct the mistake: ' + f"{sit1} {Pn} {w}", [f"{sit1} {Pn} {g}" for g in gds])
    if kind == 'should': return line('Rewrite with "should have": ' + f"{sit1} {Pn} ought to have {pp}.", [f"{sit1} {Pn} should have {pp}."])
    if kind == 'shouldnt': return line('Rewrite with "ought not to have": ' + f"{sit1} {Pn} shouldn't have {pp}.", [f"{sit1} {Pn} ought not to have {pp}."])
    if kind == 'could': return line('Rewrite with "might have": ' + f"{sit1} {Pn} could have {pp}.", [f"{sit1} {Pn} might have {pp}."])
    return line('Rewrite with "need not have": ' + f"{sit1} {Pn} needn't have {pp}.", [f"{sit1} {Pn} need not have {pp}."])
