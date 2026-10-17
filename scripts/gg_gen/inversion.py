from lib import *
from passive import gen_topic
import re as _re

def _cp(s): return s[0].upper() + s[1:]
# (subj, past, pp, rest, until-clause) -> realised only after
UNT = [
 ("Tom","realised","realised","his mistake","he checked the answers"),
 ("Anna","understood","understood","the rule","her teacher drew a diagram"),
 ("Aziz","noticed","noticed","the missing page","he got home"),
 ("Malika","felt","felt","hungry","she smelled the soup"),
 ("the students","knew","known","the results","the teacher read them out"),
 ("Jasur","saw","seen","the sign","he was past the gate"),
 ("my brother","learned","learned","the truth","he spoke to his boss"),
 ("Dilnoza","found","found","her keys","she emptied her bag"),
 ("we","heard","heard","the news","we turned on the radio"),
 ("I","remembered","remembered","her name","she smiled at me"),
 ("the children","woke","woken","up","the sun came through the window"),
 ("Mr Karimov","saw","seen","the damage","the rain stopped"),
 ("my parents","knew","known","about the party","a friend told them"),
 ("the team","left","left","the stadium","the final whistle blew"),
 ("Sara","called","called","her mum","she arrived at the hotel"),
 ("they","started","started","dinner","the guests arrived"),
]
UNT_NEG = {  # base forms for "didn't" version
 "realised":"realise","understood":"understand","noticed":"notice","felt":"feel","knew":"know","saw":"see",
 "learned":"learn","found":"find","heard":"hear","remembered":"remember","woke":"wake","left":"leave","called":"call","started":"start"}
# (subj, past rest, pp rest, B clause)
HARD = [
 ("Tom","sat down","sat down","the phone rang"),
 ("the film","started","started","the lights went out"),
 ("Anna","opened the door","opened the door","the dog ran out"),
 ("we","got home","got home","it began to rain"),
 ("I","went to bed","gone to bed","somebody knocked on the door"),
 ("the teacher","left the room","left the room","the students started talking"),
 ("Jasur","finished his homework","finished his homework","his friends called"),
 ("the train","left the station","left the station","a man ran onto the platform"),
 ("Malika","closed her eyes","closed her eyes","the alarm clock rang"),
 ("they","reached the top","reached the top","the clouds covered the view"),
 ("the match","began","begun","the crowd started singing"),
 ("Aziz","sat in the car","sat in the car","the engine stopped"),
 ("she","turned off the light","turned off the light","she heard a strange noise"),
 ("the bus","arrived","arrived","the passengers rushed forward"),
 ("Dilnoza","took her seat","taken her seat","the lecture began"),
 ("I","put down the phone","put down the phone","it rang again"),
 ("the guests","sat down to eat","sat down to eat","the power went off"),
 ("he","won the race","won the race","he fell over"),
]
FNOT = [  # (subj, adj1, adj2) for "not only is S X but also Y"
 ("Tom","clever","kind"),("Anna","beautiful","talented"),("the film","long","boring"),("my teacher","strict","fair"),
 ("the hotel","cheap","clean"),("Aziz","tired","hungry"),("this exercise","difficult","confusing"),
 ("the weather","cold","windy"),("Malika","friendly","helpful"),("our flat","small","noisy"),("the soup","hot","delicious"),
 ("Jasur","late","rude"),("the road","icy","dangerous"),("the museum","free","interesting"),("my mum","funny","clever"),
]
COND = {
 'were': [
  ("If I were you, I would apologise.","Were I you, I would apologise."),
  ("If I were rich, I would buy a big house.","Were I rich, I would buy a big house."),
  ("If Tom were here, he would help us.","Were Tom here, he would help us."),
  ("If she were taller, she would play basketball.","Were she taller, she would play basketball."),
  ("If we were in London, we would visit the museum.","Were we in London, we would visit the museum."),
  ("If the weather were better, we would go to the beach.","Were the weather better, we would go to the beach."),
  ("If I were the director, I would change the rules.","Were I the director, I would change the rules."),
  ("If they were more careful, they would make fewer mistakes.","Were they more careful, they would make fewer mistakes."),
  ("If Anna were free, she would join us.","Were Anna free, she would join us."),
  ("If the exam were easier, everybody would pass.","Were the exam easier, everybody would pass."),
  ("If he were my brother, I would trust him.","Were he my brother, I would trust him."),
  ("If I were you, I wouldn't wait.","Were I you, I wouldn't wait."),
  ("If it were warmer, we would eat outside.","Were it warmer, we would eat outside."),
  ("If Malika were here, she would know the answer.","Were Malika here, she would know the answer."),
 ],
 'had': [
  ("If I had known, I would have called you.","Had I known, I would have called you."),
  ("If we had left earlier, we would have caught the train.","Had we left earlier, we would have caught the train."),
  ("If Tom had studied, he would have passed the test.","Had Tom studied, he would have passed the test."),
  ("If she had seen the sign, she would have stopped.","Had she seen the sign, she would have stopped."),
  ("If they had listened, they wouldn't have got lost.","Had they listened, they wouldn't have got lost."),
  ("If I had had more time, I would have finished the essay.","Had I had more time, I would have finished the essay."),
  ("If Anna had told me, I would have helped her.","Had Anna told me, I would have helped her."),
  ("If the bus had been on time, we wouldn't have been late.","Had the bus been on time, we wouldn't have been late."),
  ("If you had asked, I would have said yes.","Had you asked, I would have said yes."),
  ("If Aziz had worked harder, he would have won the prize.","Had Aziz worked harder, he would have won the prize."),
  ("If it hadn't rained, we would have gone to the park.","Had it not rained, we would have gone to the park."),
  ("If I hadn't missed the bus, I would have arrived on time.","Had I not missed the bus, I would have arrived on time."),
  ("If we hadn't argued, we would have stayed friends.","Had we not argued, we would have stayed friends."),
  ("If Jasur had known the answer, he would have raised his hand.","Had Jasur known the answer, he would have raised his hand."),
 ],
 'should': [
  ("If you should need help, call me.","Should you need help, call me."),
  ("If anyone should ask, tell them I'm busy.","Should anyone ask, tell them I'm busy."),
  ("If you should see Tom, give him this book.","Should you see Tom, give him this book."),
  ("If it should rain, we will stay at home.","Should it rain, we will stay at home."),
  ("If the phone should ring, please answer it.","Should the phone ring, please answer it."),
  ("If you should have any questions, ask the teacher.","Should you have any questions, ask the teacher."),
  ("If Anna should arrive early, let her in.","Should Anna arrive early, let her in."),
  ("If they should miss the train, they will take a taxi.","Should they miss the train, they will take a taxi."),
  ("If you should find my keys, please tell me.","Should you find my keys, please tell me."),
  ("If there should be a problem, we will call you.","Should there be a problem, we will call you."),
  ("If I should forget, remind me.","Should I forget, remind me."),
  ("If he should change his mind, let us know.","Should he change his mind, let us know."),
 ],
}
NEGADV = [  # (opener, subj, modal, base, rest)  normal: S modal not/never V rest
 ("Under no circumstances","you","must","open","this door"),
 ("Under no circumstances","students","may","use","phones in the exam"),
 ("Under no circumstances","you","should","tell","him the secret"),
 ("On no account","you","must","leave","the children alone"),
 ("On no account","visitors","may","touch","the paintings"),
 ("At no time","the staff","should","leave","the shop empty"),
 ("Under no circumstances","we","can","accept","late homework"),
 ("On no account","you","should","drive","without a licence"),
 ("Under no circumstances","passengers","must","stand","near the doors"),
 ("At no time","the pupils","may","enter","the lab alone"),
 ("In no way","the teacher","would","accept","a bad excuse"),
 ("Under no circumstances","Tom","will","change","his mind"),
 ("On no account","the children","may","play","near the river"),
 ("Under no circumstances","you","must","share","your password"),
 ("At no time","Anna","could","see","the thief's face"),
 ("Under no circumstances","we","will","give","up"),
]
def _modal_neg(m):
    return {'must':"mustn't",'may':"may not",'should':"shouldn't",'can':"can't",'would':"wouldn't",'will':"won't",'could':"couldn't"}[m]

def _case(rng):
    k = rng.pick(['nev','nev','nev','hard','notonly','notonly2','until','onlyafter','cond','cond','neg'])
    return k

def gen_inv(level, rng):
    k = _case(rng)
    if k == 'nev':
        S = rng.pick(SUBJ); V, comp = vcomp(rng)
        op = rng.pick(['Never','Rarely','Seldom'])
        opl = op.lower()
        t = rng.pick(['pp','ps','pas'])
        if t == 'pp':
            h = have_pres(S)
            normal = f"{S.text} {h} {opl} {V.pp} {comp}."
            inv = f"{op} {h} {S.mid} {V.pp} {comp}."; aux = h
            wrong = f"{op} {S.mid} {h} {V.pp} {comp}."
        elif t == 'ps':
            d = do_pres(S)
            normal = f"{S.text} {opl} {V.s if S.kind == 'sg' else V.base} {comp}."
            inv = f"{op} {d} {S.mid} {V.base} {comp}."; aux = d
            wrong = f"{op} {S.mid} {V.s if S.kind == 'sg' else V.base} {comp}."
        else:
            normal = f"{S.text} {opl} {V.past} {comp}."
            inv = f"{op} did {S.mid} {V.base} {comp}."; aux = 'did'
            wrong = f"{op} {S.mid} {V.past} {comp}."
        if level == 'easy':
            ht = {'pp':' (present perfect)','ps':' (present simple)','pas':' (past simple)'}[t]
            return line(inv.replace(f" {aux} ", " ___ ", 1) + ht, [aux])
        if level == 'medium':
            return line(f"Rewrite beginning with '{op}': {normal}", [inv])
        return line(f"Correct the mistake: {wrong}", [inv])
    if k == 'hard':
        S, past, pp, B = rng.pick(HARD)
        sc = _cp(S)
        normal = f"As soon as {S} {past}, {B}."
        if level == 'easy':
            return line(f"Hardly ___ {S} {pp} when {B}.", ['had'])
        if level == 'medium':
            op = rng.pick(['Hardly','No sooner'])
            conj = 'when' if op == 'Hardly' else 'than'
            return line(f"Rewrite beginning with '{op}': {normal}", [f"{op} had {S} {pp} {conj} {B}."])
        op = rng.pick(['Hardly','No sooner'])
        conj = 'when' if op == 'Hardly' else 'than'
        bad = rng.pick([
            f"{op} {S} had {pp} {conj} {B}.",
            f"{op} had {S} {pp} {'than' if conj == 'when' else 'when'} {B}.",
            f"{op} {S} {past} {conj} {B}."])
        return line(f"Correct the mistake: {bad}", [f"{op} had {S} {pp} {conj} {B}."])
    if k in ('notonly','notonly2'):
        if k == 'notonly':
            S, a1, a2 = rng.pick(FNOT)
            if S == 'this exercise' or S in ('the film','the hotel','the weather','the soup','the road','the museum','our flat'): pr = 'it'
            elif S in ('Tom','Aziz','Jasur'): pr = 'he'
            elif S in ('Anna','Malika','my mum','my teacher'): pr = 'she'
            else: pr = 'it'
            Sc = _cp(S)
            normal = f"{Sc} is not only {a1} but also {a2}."
            inv = [f"Not only is {S} {a1}, but {pr} is also {a2}.", f"Not only is {S} {a1} but {S} is also {a2}."]
            if level == 'easy':
                return line(f"Not only ___ {S} {a1}, but {pr} is also {a2}.", ['is'])
            if level == 'medium':
                return line(f"Rewrite beginning with 'Not only': {normal}", inv)
            bad = f"Not only {S} is {a1}, but {pr} is also {a2}."
            return line(f"Correct the mistake: {bad}", inv)
        S = rng.pick([s for s in SUBJ if s.text != 'You']); V1, c1 = vcomp(rng); V2, c2 = vcomp(rng)
        if V1.base == V2.base: return None
        d = do_pres(S)
        normal = f"{S.text} not only {V1.s if S.kind == 'sg' else V1.base} {c1} but also {V2.s if S.kind == 'sg' else V2.base} {c2}."
        p = S.pron
        inv = [f"Not only {d} {S.mid} {V1.base} {c1}, but {p} also {V2.s if S.kind == 'sg' else V2.base} {c2}.",
               f"Not only {d} {S.mid} {V1.base} {c1}, but {S.mid} also {V2.s if S.kind == 'sg' else V2.base} {c2}."]
        if level == 'easy':
            return line(f"Not only ___ {S.mid} {V1.base} {c1}, but {p} also {V2.s if S.kind == 'sg' else V2.base} {c2}.", [d])
        if level == 'medium':
            return line(f"Rewrite beginning with 'Not only': {normal}", inv)
        bad = f"Not only {S.mid} {V1.s if S.kind == 'sg' else V1.base} {c1}, but {p} also {V2.s if S.kind == 'sg' else V2.base} {c2}."
        return line(f"Correct the mistake: {bad}", inv)
    if k in ('until', 'onlyafter'):
        S, past, pp, rest, cl = rng.pick(UNT)
        base = UNT_NEG[past]
        sub_mid = S
        aux = 'did'
        if k == 'until':
            normal = f"{_cp(S)} didn't {base} {rest} until {cl}."
            inv = f"Not until {cl} did {S} {base} {rest}."
            if level == 'easy': return line(f"Not until {cl} ___ {S} {base} {rest}.", ['did'])
            if level == 'medium': return line(f"Rewrite beginning with 'Not until': {normal}", [inv])
            bad = rng.pick([f"Not until {cl} {S} {past} {rest}.", f"Not until {cl} {S} didn't {base} {rest}."])
            return line(f"Correct the mistake: {bad}", [inv])
        normal = f"{_cp(S)} {past} {rest} only after {cl}."
        inv = f"Only after {cl} did {S} {base} {rest}."
        if level == 'easy': return line(f"Only after {cl} ___ {S} {base} {rest}.", ['did'])
        if level == 'medium': return line(f"Rewrite beginning with 'Only after': {normal}", [inv])
        bad = f"Only after {cl} {S} {past} {rest}."
        return line(f"Correct the mistake: {bad}", [inv])
    if k == 'cond':
        t = rng.pick(['were','had','had','should'])
        n, inv = rng.pick(COND[t])
        op = _cp(t)
        if level == 'easy':
            blank = inv.replace(op + ' ', '___ ', 1)
            h = {'were': '(second conditional)', 'had': '(third conditional)', 'should': '(first conditional)'}[t]
            return line(f"{blank} {h}", [op])
        if level == 'medium':
            return line(f"Rewrite beginning with '{op}': {n}", [inv])
        if t == 'were': bad = _re.sub(r'^Were (\w+) ', lambda m: m.group(1) + ' were ', inv, 1)
        elif t == 'had': bad = _re.sub(r'^Had (\w+)( not)? ', lambda m: m.group(1) + (" hadn't " if m.group(2) else ' had '), inv, 1)
        else: bad = _re.sub(r'^Should (\w+) ', lambda m: m.group(1) + ' should ', inv, 1)
        bad = _cp(bad)
        return line(f"Correct the mistake: {bad}", [inv])
    # negative adverbials
    op, S, m, b, rest = rng.pick(NEGADV)
    Sc = _cp(S)
    normal = f"{Sc} {_modal_neg(m)} {b} {rest}." if m != 'will' else f"{Sc} won't {b} {rest}."
    inv = f"{op} {m} {S} {b} {rest}."
    if level == 'easy': return line(f"{op} ___ {S} {b} {rest}.", [m])
    if level == 'medium': return line(f"Rewrite beginning with '{op}': {normal}", [inv])
    bad = f"{op} {S} {m} {b} {rest}."
    return line(f"Correct the mistake: {bad}", [inv])

def gen_inv_jobs(C):
    return {'inversion': lambda: gen_topic(gen_inv, C, 123)}
