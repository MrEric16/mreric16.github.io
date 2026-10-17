from lib import *
from passive import gen_topic
from tense import negs

def cap1(s): return s[0].upper() + s[1:]
SM = [Subj('I','i','i'),Subj('You','you','you'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),
      Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj("My brother","sg","he"),Subj('My sister','sg','she'),Subj('The students','pl','they'),Subj('My parents','pl','they')]
def be_ans(S): 
    b = be_pres(S); return [b + ' able to'] + (["'m able to"] if S.kind == 'i' else (["'s able to"] if S.kind == 'sg' else ["'re able to"]))
def bep_ans(S): return [be_past(S) + ' able to', 'managed to']

# ================= ABILITY =================
PAST_T = ['As a child,','Ten years ago,','At the age of ten,','When I was little,' ,'In 2010,']
FUT_T = ['Next year,','By next summer,','In a few weeks,','After the course,','By the end of the year,']
SPEC_T = ['Yesterday','Last week','Last night','On Monday']
SINCE = ['January','2019','last summer','childhood','the accident']
def ability_forms(S, rng):
    V = rng.pick([v for v in VERBS if not v.ach]); comp = rng.pick(V.comps)
    Va = rng.pick([v for v in VERBS if v.ach]); ca = rng.pick(Va.comps)
    mode = rng.pick(['now','now','past','fut','spec','perf'])
    d = dict(mode=mode, S=S)
    if mode == 'now':
        d.update(vp=f"{V.base} {comp}", lead='', tail=' now', aff='can', neg=["can't","cannot"], aux='Can')
    elif mode == 'past':
        d.update(vp=f"{V.base} {comp}", lead=rng.pick(PAST_T)+' ', tail='', aff='could', neg=["couldn't","could not"], aux='Could')
    elif mode == 'fut':
        d.update(vp=f"{V.base} {comp}", lead=rng.pick(FUT_T)+' ', tail='', aff='will be able to', neg=["won't be able to","will not be able to"], aux='Will')
    elif mode == 'spec':
        d.update(vp=f"{Va.base} {ca}", lead=rng.pick(SPEC_T)+' ', tail=', after three attempts', aff=bep_ans(S), neg=[be_past(S)+"n't able to", be_past(S)+" not able to", "couldn't","could not"], aux=None)
    else:
        d.update(vp=f"{V.base} {comp}", lead='', tail=' since '+rng.pick(SINCE), aff=[have_pres(S)+' been able to'], neg=[have_pres(S)+"n't been able to", have_pres(S)+' not been able to'], aux=None)
    return d
def a_sent(d, form):  # form: 'aff'|'neg'|'plain' -> sentence text using display modal
    S = d['S']; m = d['mode']; lead = d['lead']; subj = (S.mid if lead else S.text)
    if form == 'aff':
        mod = {'now':'can','past':'could','fut':'will be able to','spec':f"{be_past(S)} able to",'perf':f"{have_pres(S)} been able to"}[m]
    else:
        mod = {'now':"can't",'past':"couldn't",'fut':"won't be able to",'spec':f"{be_past(S)}n't able to",'perf':f"{have_pres(S)}n't been able to"}[m]
    return f"{lead}{subj} {mod} {d['vp']}{d['tail']}."
def a_blank(d, form, hint='', cue=True):
    S = d['S']; lead = d['lead']; subj = (S.mid if lead else S.text)
    m = d['mode']; neg = '(not' in hint
    extra = ''
    if cue and m in ('now','past','fut'):
        be = {'now':'is','past':'was','fut':'will be'}[m]
        extra = f" It {be} {'impossible' if neg else 'easy'} for {S.objp}."
    return f"{lead}{subj} ___{hint} {d['vp']}{d['tail']}.{extra}"
def gen_ability(level, rng):
    S = rng.pick(SM); d = ability_forms(S, rng); m = d['mode']
    aff = d['aff'] if isinstance(d['aff'], list) else [d['aff']]
    if level == 'easy':
        if rng.pick([0,1]): return line(a_blank(d,'', ''), aff + (["'ll be able to"] if m=='fut' else []))
        return line(a_blank(d,'',' (not)'), d['neg'])
    if level == 'medium':
        k = rng.pick(['hint','hint','q','short','hintneg'])
        if k == 'hint':
            if m == 'now': return line(a_blank(d,'',' (be able to)'), be_ans(S))
            if m in ('past','spec'): return line(a_blank(d,'',' (be able to)'), [be_past(S)+' able to'] + (['managed to'] if m=='spec' else []))
            if m == 'fut': return line(a_blank(d,'',' (be able to)'), ['will be able to',"'ll be able to"])
            return line(a_blank(d,'',' (be able to)'), aff)
        if k == 'hintneg':
            return line(a_blank(d,'',' (not / be able to)'), d['neg'] + (["isn't able to","is not able to"] if False else []))
        if k == 'q' and d['aux']:
            S2 = S; lead = d['lead']
            return line(f"{lead}___ {S.mid} {d['vp']}{d['tail']}?" if d['mode']!='fut' else f"{lead}___ {S.mid} be able to {d['vp']}?", [d['aux']])
        if k == 'short' and d['aux'] and S.kind != 'i':
            qq = f"{d['lead']}{d['aux'] if not d['lead'] else d['aux'].lower()} {S.mid} {'be able to ' if m=='fut' else ''}{d['vp']}{d['tail']}?"
            p = pron_ans(S); w = {'now':'can','past':'could','fut':'will'}[m]
            if rng.pick([0,1]): return line(f"{qq} Yes, {p} ___.", [w])
            return line(f"{qq} No, {p} ___.", {'now':["can't","cannot"],'past':["couldn't","could not"],'fut':["won't","will not"]}[m])
        return line(a_blank(d,'',''), aff + (["'ll be able to"] if m=='fut' else []))
    k = rng.pick(['fix','fix','neg','q','rewrite'])
    full = a_sent(d,'aff'); negs_ = a_sent(d,'neg')
    lead = d['lead']; subj = (S.mid if lead else S.text)
    def alt_neg():
        out = [negs_]
        for a, b in (("can't","cannot"),("couldn't","could not"),("won't","will not")): 
            if a in negs_: out.append(negs_.replace(a,b))
        return out
    if k == 'neg': return line('Make a negative sentence: ' + full, alt_neg())
    if k == 'q' and d['aux']:
        if m == 'fut': qf = f"{lead}will {S.mid} be able to {d['vp']}?"
        else: qf = f"{lead}{d['aux'].lower() if lead else d['aux']} {S.mid} {d['vp']}{d['tail']}?"
        return line('Make a question: ' + full, [qf])
    if k == 'rewrite':
        if m == 'now': return line('Rewrite with "be able to": ' + full, [f"{S.text} {be_pres(S)} able to {d['vp']} now.", f"{S.text} {be_ans(S)[1].lstrip()} {d['vp']} now." if False else f"{S.text} {be_pres(S)} able to {d['vp']} now."])
        if m == 'past': return line('Rewrite with "be able to": ' + full, [f"{lead}{S.mid} {be_past(S)} able to {d['vp']}."])
        if m == 'fut': return line('Rewrite with "can": ' + f"{S.text} will be able to {d['vp']} next year.", [f"{S.text} can {d['vp']} next year."]) if False else None
        return None
    # fix
    if m == 'now': bad = rng.pick([f"{S.text} can to {d['vp']} now.", f"{S.text} {be_pres(S)} can {d['vp']} now."] + ([f"{S.text} cans {d['vp']} now."] if S.kind=='sg' else []) + [f"{S.text} doesn't can {d['vp']} now." if S.kind=='sg' else f"{S.text} don't can {d['vp']} now."])
    elif m == 'past': bad = rng.pick([f"{lead} {S.mid} didn't could {d['vp']}.", f"{lead} {S.mid} could to {d['vp']}.", f"{lead} {S.mid} was could {d['vp']}." if S.kind in ('i','sg') else f"{lead} {S.mid} were could {d['vp']}."])
    elif m == 'fut': bad = rng.pick([f"{lead} {S.mid} will can {d['vp']}.", f"{lead} {S.mid} will able to {d['vp']}.", f"{lead} {S.mid} will be able {d['vp']}.", f"{lead} {S.mid} will be can {d['vp']}."])
    elif m == 'spec': bad = rng.pick([f"{lead}{S.mid} {be_past(S)} able {d['vp']}{d['tail']}.", f"{lead}{S.mid} {be_past(S)} able to {Verb_ing(d['vp'])}{d['tail']}." if False else f"{lead}{S.mid} didn't able to {d['vp']}{d['tail']}."])
    else: bad = f"{S.text} {have_pres(S)} could {d['vp']}{d['tail']}."
    good = {'now':[f"{S.text} can {d['vp']} now."],'past':[f"{lead}{S.mid} could {d['vp']}."],'fut':[f"{lead}{S.mid} will be able to {d['vp']}."],'spec':[f"{lead}{S.mid} {be_past(S)} able to {d['vp']}{d['tail']}.", f"{lead}{S.mid} managed to {d['vp']}{d['tail']}."],'perf':[f"{S.text} {have_pres(S)} been able to {d['vp']}{d['tail']}."]}[m]
    if m == 'now': good.append(f"{S.text} {be_pres(S)} able to {d['vp']} now.")
    if m == 'past': good.append(f"{lead}{S.mid} {be_past(S)} able to {d['vp']}.")
    if m == 'now' and ("doesn't can" in bad or "don't can" in bad):
        return line('Correct the mistake: ' + bad, [f"{S.text} can't {d['vp']} now.", f"{S.text} cannot {d['vp']} now."])
    return line('Correct the mistake: ' + bad.replace('  ',' '), good)

# ================= OBLIGATION =================
MUST_P = ["wear a seatbelt in the car","show your ticket at the gate","switch off your phone in the lesson","stop at a red light","keep quiet in the library","wash your hands before eating","wear a helmet on a motorbike","do your homework every day","arrive on time for the exam","carry your ID card","queue at the bus stop","register before the course","bring a pen to the test","listen to the teacher","pay the fee by Friday","turn off the lights when you leave","lock the door at night","follow the safety rules","take off your shoes in the mosque","wear a uniform at school"]
MNT_P = ["park in front of the gate","smoke in the hospital","talk during the exam","run in the corridor","touch the paintings","use your phone while driving","cross the road on a red light","feed the animals","walk on the grass","bring food into the lab","copy from a friend in the test","swim in the lake","leave the door open","be late for the exam","enter without a ticket","cheat in the exam","drive too fast near the school","play with matches","shout in the library","waste water"]
DNT_P = ["bring a gift to the party","wear a tie today","come early","pay for the tickets","bring your own pen","wait for me","do the extra exercise","learn the poem by heart","book a table","dress formally","tell the teacher","take a coat","buy a new book","stay until the end","hurry","cook","answer all the questions","get up early on Sunday","wear a uniform on Friday","phone first"]
MUST_R = ["It is the law.","It is the rule.","It is compulsory.","It is very important."]
MNT_R = ["It is forbidden.","It is dangerous.","It is against the rules.","It is not allowed."]
DNT_R = ["It isn't necessary.","It is optional.","It is not compulsory.","There is no need."]
SO = [Subj('You','you','you'),Subj('I','i','i'),Subj('We','pl','we'),Subj('They','pl','they'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('Students','pl','they'),Subj('Drivers','pl','they'),Subj('Visitors','pl','they'),Subj('Everybody','sg','he'),Subj('The children','pl','they'),Subj('Passengers','pl','they')]
def fp(ph, S):
    if S.text in ('I',): return ph.replace('your','my')
    if S.text == 'We': return ph.replace('your','our')
    if S.text == 'You': return ph
    if S.kind == 'sg': return ph.replace('your','his' if S.pron=='he' else 'her') if S.text not in ('Everybody',) else ph.replace('your','their')
    return ph.replace('your','their')
def DT_WRONG(S): return "don't" if S.kind=='sg' else "doesn't"
def CONTR(S): return "'m" if S.kind=='i' else ("'s" if S.kind=='sg' else "'re")
def hv(S): return 'has to' if S.kind == 'sg' else 'have to'
def dhv(S): return "doesn't have to" if S.kind == 'sg' else "don't have to"
def dhv_full(S): return "does not have to" if S.kind == 'sg' else "do not have to"
def gen_obligation(level, rng):
    S = rng.pick(SO); typ = rng.pick(['must','must','mnt','mnt','dnt','dnt','dnt'])
    ph = fp(rng.pick({'must':MUST_P,'mnt':MNT_P,'dnt':DNT_P}[typ]), S)
    tm = 'now' if typ == 'mnt' else rng.pick(['now','now','past','fut'])
    lead = {'now':'','past':rng.pick(['Yesterday ','Last week ','Last year ']),'fut':rng.pick(['Tomorrow ','Next week ','Next year '])}[tm]
    subj = S.text if not lead else S.mid
    pre = lead + subj
    reason = rng.pick({'must':MUST_R,'mnt':MNT_R,'dnt':DNT_R}[typ])
    if typ == 'must' and tm != 'now': reason = 'It was compulsory.' if tm == 'past' else 'It will be compulsory.'
    if typ == 'dnt' and tm != 'now': reason = 'It was not necessary.' if tm == 'past' else 'It will not be necessary.'
    mm = {'must': {'now':'must','past':'had to','fut':'will have to'}, 'mnt': {'now':"mustn't"}, 'dnt': {'now':dhv(S),'past':"didn't have to",'fut':"won't have to"}}[typ][tm]
    full = f"{pre} {mm} {ph}."
    ans = {'must': {'now':['must',hv(S)],'past':['had to'],'fut':['will have to',"'ll have to"]}, 'mnt': {'now':["mustn't","must not","can't","cannot"]}, 'dnt': {'now':[dhv(S),dhv_full(S),"needn't","need not"],'past':["didn't have to","did not have to","didn't need to","did not need to"],'fut':["won't have to","will not have to"]}}[typ][tm]
    if level == 'easy':
        return line(f"{pre} ___ {ph}. {reason}", ans)
    aux = {'now': 'Does' if S.kind=='sg' else 'Do', 'past':'Did','fut':'Will'}[tm]
    if level == 'medium':
        k = rng.pick(['hint','hint','q','short'])
        if k == 'hint':
            if typ == 'must': return line(f"{pre} ___ (have to) {ph}. {reason}", {'now':[hv(S)],'past':['had to'],'fut':['will have to',"'ll have to"]}[tm])
            if typ == 'dnt': return line(f"{pre} ___ (not / have to) {ph}. {reason}", ans[:2] if tm=='now' else ans)
            return line(f"{pre} ___ (not) {ph}. {reason}", ans)
        if typ == 'mnt': return line(f"{pre} ___ {ph}. {reason}", ans)
        sub = S.mid
        if k == 'q':
            ld = (lead.strip()+' ') if lead else ''
            return line(f"{cap1(ld) if ld else ''}___ {sub} ___ {ph}?" if True else '', [aux if not ld else aux], ['have to']) if typ == 'must' else line(f"{pre} ___ ___ {ph}. {reason}", ans[:1] if False else [dhv(S).split(' ')[0] + "n't" if False else dhv(S).replace(' have to','')], ['have to']) if False else line(f"{cap1(ld) if ld else ''}___ {sub} ___ {ph}?", [aux], ['have to'])
        ld = lead.strip()
        qq = f"{cap1(ld)} {aux.lower()} {sub} have to {ph}?" if ld else f"{aux} {sub} have to {ph}?"
        ya = {'now':('does' if S.kind=='sg' else 'do'),'past':'did','fut':'will'}[tm]
        if S.kind == 'i': return line(f"{pre} ___ {ph}. {reason}", ans)
        pn = pron_ans(S)
        ypos = typ == 'must'
        if ypos: return line(f"{qq} Yes, {pn} ___.", [ya])
        return line(f"{qq} No, {pn} ___.", negs(ya) if ya != 'will' else ["won't","will not"])
    k = rng.pick(['fix','fix','fix','rewrite','neg','q'])
    if k == 'fix':
        if typ == 'must':
            w = {'now':[f"{pre} must to {ph}.", f"{pre} don't must {ph}.", f"{pre} musts {ph}." if S.kind=='sg' else f"{pre} has to {ph}.", f"{pre} haven't to {ph}." if False else f"{pre} must have to {ph}."],
                 'past':[f"{pre} must {ph}.", f"{pre} musted {ph}.", f"{pre} had to {ph}." if False else f"{pre} did must {ph}."],
                 'fut':[f"{pre} will must {ph}.", f"{pre} will has to {ph}.", f"{pre} will have {ph}."]}[tm]
            w = [x for x in w if x != full]
            good = {'now':[f"{pre} must {ph}.", f"{pre} {hv(S)} {ph}."],'past':[f"{pre} had to {ph}."],'fut':[f"{pre} will have to {ph}.", f"{pre} 'll have to {ph}.".replace(' '+"'ll","'ll") if False else f"{pre} will have to {ph}."]}[tm]
            if tm == 'now' and S.kind == 'sg': w = [x for x in w if 'has to' not in x]
            if tm == 'now' and S.kind != 'sg': w = [x for x in w if 'musts' not in x]
            return line('Correct the mistake: ' + rng.pick(w) + ' ' + reason, [x + ' ' + reason for x in good])
        if typ == 'mnt':
            w = [f"{pre} don't have to {ph}.", f"{pre} mustn't to {ph}.", f"{pre} not must {ph}.", f"{pre} {dhv_full(S)} {ph}."]
            w = [x.replace(" don't have to"," don't have to") for x in w]
            if S.kind == 'sg': w = [x for x in w if "don't have to" not in x] + [f"{pre} doesn't have to {ph}."]
            ww = rng.pick(w)
            return line('Correct the mistake: ' + ww + ' ' + reason, [f"{pre} mustn't {ph}. {reason}", f"{pre} must not {ph}. {reason}", f"{pre} can't {ph}. {reason}"])
        w = {'now':[f"{pre} mustn't {ph}.", f"{pre} haven't to {ph}.", f"{pre} {DT_WRONG(S)} have to {ph}."],
             'past':[f"{pre} mustn't {ph}.", f"{pre} hadn't to {ph}.", f"{pre} don't have to {ph}.", f"{pre} not had to {ph}."],
             'fut':[f"{pre} mustn't {ph}.", f"{pre} won't must {ph}.", f"{pre} don't have to {ph}."]}[tm]
        good = {'now':[f"{pre} {dhv(S)} {ph}.", f"{pre} needn't {ph}.", f"{pre} need not {ph}."],'past':[f"{pre} didn't have to {ph}.", f"{pre} didn't need to {ph}.", f"{pre} did not have to {ph}."],'fut':[f"{pre} won't have to {ph}.", f"{pre} will not have to {ph}."]}[tm]
        return line('Correct the mistake: ' + rng.pick(w) + ' ' + reason, [x + ' ' + reason for x in good])
    if k == 'rewrite':
        if typ == 'must' and tm == 'now': return line('Rewrite with "have to": ' + f"{pre} must {ph}.", [f"{pre} {hv(S)} {ph}."])
        if typ == 'mnt': return line('Rewrite with "not allowed to": ' + f"{pre} mustn't {ph}.", [f"{pre} {be_pres(S)} not allowed to {ph}.", f"{pre} {be_pres(S)}n't allowed to {ph}." if S.kind != 'i' else f"{pre} am not allowed to {ph}.", f"{pre} {CONTR(S)} not allowed to {ph}."])
        if typ == 'dnt' and tm == 'now': return line('Rewrite with "needn\'t": ' + f"{pre} {dhv(S)} {ph}.", [f"{pre} needn't {ph}.", f"{pre} need not {ph}."])
        return None
    if k == 'neg' and typ == 'must':
        return line('Make a negative sentence (no obligation): ' + full, [f"{pre} {dhv(S)} {ph}.", f"{pre} {dhv_full(S)} {ph}."] if tm == 'now' else [f"{pre} didn't have to {ph}.", f"{pre} did not have to {ph}."] if tm == 'past' else [f"{pre} won't have to {ph}.", f"{pre} will not have to {ph}."])
    if k == 'q' and typ == 'must':
        ld = lead.strip()
        base = f"{aux} {S.mid} have to {ph}?"
        qa = (cap1(ld) + ' ' + aux.lower() + base[len(aux):]) if ld else base
        alts = [qa]
        if tm == 'now': alts.append(cap1(ld) + ' must ' + S.mid + ' ' + ph + '?' if False else 'Must ' + S.mid + ' ' + ph + '?')
        return line('Make a question: ' + full, alts)
    return None

# ================= ADVICE =================
PROB1 = [("I have a headache.","take an aspirin"),("I can't sleep at night.","go to bed earlier"),("I'm always tired.","drink less coffee"),("My English is weak.","read more books"),
 ("I have a test tomorrow.","study tonight"),("I feel sick.","see a doctor"),("I eat too much sugar.","eat less sweets"),("My phone is broken.","buy a new one"),
 ("I lost my keys.","call a locksmith"),("I'm lonely.","join a club"),("I don't understand the lesson.","ask the teacher"),("I'm late for school.","take a taxi"),
 ("My tooth hurts.","go to the dentist"),("I'm bored.","read a good book"),("I forgot my friend's birthday.","apologise to her"),("I have a sore throat.","drink warm tea"),
 ("It's cold outside.","wear a coat"),("I need money.","find a part-time job"),("I'm nervous about the exam.","relax and breathe slowly"),("My neighbours are noisy.","talk to them politely"),
 ("I can't find my wallet.","check the bus station"),("I want to learn English faster.","watch films in English"),("I don't know what to wear.","ask your mum"),
 ("I have a lot of homework.","start now"),("I can't concentrate.","switch off your phone"),("The room is hot.","open the window"),("I'm hungry.","have a sandwich"),
 ("My bike is old.","repair it"),("I have a cold.","stay at home"),("I want a better job.","improve your skills"),("My eyes hurt.","rest them for a while"),
 ("I'm worried about my grades.","talk to your teacher"),("I missed the bus.","wait for the next one"),("I'm putting on weight.","do more exercise"),
 ("I spend too much money.","make a budget"),("I forget new words.","write them in a notebook"),("My laptop is slow.","delete old files"),("I'm stressed.","take a walk"),
 ("I never have time to read.","turn off the TV"),("I have a spot on my face.","wash it gently")]
PROB3 = [("Tom has a headache.","He","take an aspirin"),("Anna can't sleep at night.","She","go to bed earlier"),("My brother is always tired.","He","sleep more"),("My sister has a test tomorrow.","She","study tonight"),
 ("Our teacher feels sick.","She","see a doctor"),("My friend lost her keys.","She","call a locksmith"),("Tom is lonely.","He","join a club"),("Anna has a toothache.","She","go to the dentist"),
 ("My cousin is bored.","He","find a hobby"),("My dad has a cold.","He","stay in bed"),("My mum is stressed.","She","take a holiday"),("Tom is always late.","He","buy an alarm clock"),
 ("The students don't understand the lesson.","They","ask more questions"),("My parents are worried about money.","They","make a budget"),("My friends have an exam tomorrow.","They","go to bed early"),
 ("Anna's laptop is slow.","She","delete old files"),("Tom can't concentrate.","He","turn off his phone"),("My brother has a sore throat.","He","drink warm tea"),
 ("My sister is putting on weight.","She","do more exercise"),("The children are hungry.","They","have lunch")]
BADP = [("I have a headache.","drink five coffees"),("I can't sleep at night.","watch scary films before bed"),("I'm always tired.","stay up all night"),("I feel sick.","eat a lot of chocolate"),
 ("My tooth hurts.","ignore it"),("I have a cold.","go swimming in the river"),("I'm stressed.","skip meals"),("I have a test tomorrow.","play computer games all night"),
 ("My eyes hurt.","stare at the screen all day"),("I forget new words.","never review them"),("I'm hungry.","skip dinner"),("The room is hot.","close all the windows"),
 ("I'm nervous about the exam.","drink energy drinks"),("My phone is broken.","throw it away"),("I'm lonely.","stay in your room all day"),("I'm late for school.","walk very slowly")]
def adv_item(rng):
    if rng.pick([0,0,1]):
        pr, ad = rng.pick(PROB1); return pr, 'You', ad
    pr, p, ad = rng.pick(PROB3); return pr, p, ad
def gen_advice(level, rng):
    pr, P, ad = adv_item(rng); you = (P == 'You')
    Q = 'I' if you else None
    if you and rng.pick([0,0,1]) and level != 'hard':
        pr, adv = rng.pick(BADP); P = 'You'
        k = rng.pick(['sh','better'])
        if k == 'sh': return line(f"{pr} You ___ {adv}. It's a bad idea.", ["shouldn't","should not","ought not to","'d better not","had better not"])
        return line(f"{pr} You had better ___ {adv}. It's a bad idea.", ["not"])
    if level == 'easy':
        k = rng.pick(['sh','sh','ought','better','better2'])
        if k == 'sh': return line(f"{pr} {P} ___ {ad}.", ['should','ought to',"'d better",'had better'])
        if k == 'ought': return line(f"{pr} {P} ought ___ {ad}.", ['to'])
        if k == 'better': return line(f"{pr} {P} had ___ {ad}.", ['better'])
        return line(f"{pr} {P} ___ better {ad}.", ['had',"'d"])
    if level == 'medium':
        k = rng.pick(['q','q2','short','nq','ifwere'])
        subj = 'I' if you else {'He':'he','She':'she','They':'they'}[P]
        if k == 'q': return line(f"{pr} ___ {subj} {ad}?", ['Should'])
        if k == 'q2' and you: return line(f"{pr} What ___ I do? {P} ___ {ad}.", ['should'], ['should','ought to'])
        if k == 'short': 
            if you: return line(f"{pr} Should I {ad}? Yes, you ___.", ['should'])
            return line(f"{pr} Should {subj} {ad}? Yes, {subj} ___.", ['should'])
        if k == 'nq': 
            return line(f"{pr} Why ___ {subj} {ad}?", ['shouldn\'t','should not']) if False else line(f"{pr} What ___ {subj} do?", ['should'])
        if you: return line(f"{pr} If I ___ you, I would {ad}.", ['were','was'])
        return line(f"{pr} If I ___ {subj if False else 'him' if P=='He' else 'her' if P=='She' else 'them'}, I would {ad.replace('his ','my ').replace('her ','my ').replace('their ','my ')}.", ['were','was'])
    k = rng.pick(['fix','fix','rewrite','rewrite2','q','neg'])
    base = f"{pr} {P} should {ad}."
    if k == 'fix':
        w = rng.pick(['to','s','dont','ought','better','betterto'])
        s3 = 'ss'
        if w == 'to': return line('Correct the mistake: ' + f"{pr} {P} should to {ad}.", [base, f"{pr} {P} ought to {ad}."])
        if w == 's' and P in ('He','She'): return line('Correct the mistake: ' + f"{pr} {P} shoulds {ad}.", [base, f"{pr} {P} ought to {ad}."])
        if w == 'dont': return line('Correct the mistake: ' + f"{pr} {P} don't should {ad}.", None or [f"{pr} {P} shouldn't {ad}.", f"{pr} {P} should not {ad}."]) if False else line('Correct the mistake: ' + f"{pr} {P} don't should {ad}.", [f"{pr} {P} shouldn't {ad}.", f"{pr} {P} should not {ad}."]) if False else None
        if w == 'ought': return line('Correct the mistake: ' + f"{pr} {P} ought {ad}.", [f"{pr} {P} ought to {ad}.", base])
        if w == 'better': return line('Correct the mistake: ' + f"{pr} {P} better {ad}.", [f"{pr} {P} had better {ad}.", f"{pr} {P}'d better {ad}.", base])
        if w == 'betterto': return line('Correct the mistake: ' + f"{pr} {P} had better to {ad}.", [f"{pr} {P} had better {ad}.", f"{pr} {P}'d better {ad}.", base])
        return None
    if k == 'rewrite': return line('Rewrite with "should": ' + f"{pr} {P} ought to {ad}.", [base])
    if k == 'rewrite2': return line('Rewrite with "ought to": ' + base, [f"{pr} {P} ought to {ad}."])
    if k == 'q':
        subj = 'I' if you else {'He':'he','She':'she','They':'they'}[P]
        return line('Make a question: ' + f"{pr} {'I' if you else P} should {ad}.", [f"{pr} Should {subj} {ad}?"]) if not you else line('Make a question: ' + f"{pr} I should {ad}.", [f"{pr} Should I {ad}?"])
    return line('Make a negative sentence: ' + base, [f"{pr} {P} shouldn't {ad}.", f"{pr} {P} should not {ad}."])

from dedpf import gen_deduction, gen_perfect

# ================= ALL =================
_G = {'ability':gen_ability,'oblig':gen_obligation,'advice':gen_advice,'ded':gen_deduction,'perf':gen_perfect}
def gen_all_modals(level, rng):
    return _G[rng.pick(['ability','oblig','advice','ded','ded','perf','oblig','advice'])](level, rng)

def gen_modal_jobs(C):
    gens = [('modals-ability',gen_ability),('modals-obligation',gen_obligation),('modals-advice',gen_advice),('modals-possibility',gen_deduction),('modals-perfect',gen_perfect),('modals-all',gen_all_modals)]
    j = {}
    for i,(tid,fn) in enumerate(gens):
        j[tid] = (lambda fn=fn, i=i: gen_topic(fn, C, 60+i))
    return j
