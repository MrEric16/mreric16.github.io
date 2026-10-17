from lib import *
from passive import gen_topic
SUBJC = [Subj('I','i','i'),Subj('You','you','you'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),
 Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('My brother','sg','he'),Subj('Our teacher','sg','she'),Subj('My parents','pl','they'),Subj('The students','pl','they')]
F = {'make':('makes','made'),'do':('does','did'),'take':('takes','took'),'get':('gets','got'),'have':('has','had')}
# (phrase, [accepted verbs])
C = [
 ("a mistake",['make']),("an effort",['make']),("progress",['make']),("a decision",['make']),("a suggestion",['make']),("money",['make']),
 ("a phone call",['make']),("a mess",['make']),("friends",['make']),("a noise",['make']),("an appointment",['make']),("a complaint",['make']),
 ("a plan",['make']),("an excuse",['make']),("a difference",['make']),("an offer",['make']),("a speech",['make']),("a promise",['make']),("a living",['make']),
 ("the dishes",['do']),("the shopping",['do']),("the laundry",['do']),("the ironing",['do']),("housework",['do']),("homework",['do']),("research",['do']),
 ("exercise",['do']),("business",['do']),("damage",['do']),("a favour",['do']),("a course",['do','take']),("harm",['do']),("an experiment",['do']),("your best",['do']),
 ("a photo",['take']),("a break",['take','have']),("a risk",['take']),("a chance",['take']),("a shower",['take','have']),("an exam",['take']),("notes",['take']),
 ("medicine",['take']),("a taxi",['take']),("a look",['take','have']),("responsibility",['take']),("a bath",['take','have']),("a seat",['take','have']),("advice",['take']),("care of the baby",['take']),
 ("a job",['get']),("a ticket",['get']),("a promotion",['get']),("a message",['get']),("a letter",['get']),("a present",['get']),("a degree",['get']),("a cold",['get','have']),
 ("breakfast",['have']),("lunch",['have']),("dinner",['have']),("a party",['have']),("fun",['have']),("a rest",['have','take']),("a headache",['have']),("a chat",['have']),
 ("an argument",['have']),("a good time",['have']),("a cup of tea",['have']),("a meeting",['have']),("a go",['have']),("a holiday",['have','take']),("a dream",['have']),("a lesson",['have','take']),
]
ADJC = [("angry",'get'),("tired",'get'),("lost",'get'),("ready",'get'),("wet",'get'),("married",'get'),("better",'get'),("worse",'get'),("hungry",'get'),("dressed",'get'),("old",'get'),("home",'get'),("nervous",'get'),("bored",'get')]
def gen_col(level, rng):
    k = rng.pick(['n','n','n','n','adj','fix'])
    S = rng.pick(SUBJC)
    if k == 'adj':
        a, v = rng.pick(ADJC)
        if a == 'home': t = 'got'
        t = rng.pick(['aff','neg','q'])
        if t == 'aff': s, ans = f"{S.text} ___ {a} very quickly.", ['got']
        elif t == 'neg': s, ans = f"{S.text} didn't ___ {a}.", ['get']
        else:
            if S.text == 'I': return None
            s, ans = f"Did {S.mid} ___ {a}?", ['get']
        if a in ('married','dressed','ready'): s = s.replace(' very quickly','')
        h = '' if level == 'hard' else (' (get / become / go)' if level == 'easy' else ' (make / do / take / get / have)')
        return line(s + h, ans)
    ph, ok = rng.pick(C)
    if k == 'fix':
        if level != 'hard': return None
        wrong = rng.pick([v for v in F if v not in ok])
        t = rng.pick(['past','neg'])
        if t == 'past':
            s = f"{S.text} {F[wrong][1]} {ph}."
            return line(f"Correct the mistake: {s}", [f"{S.text} {F[v][1]} {ph}." for v in ok])
        return line(f"Correct the mistake: {S.text} didn't {wrong} {ph}.", [f"{S.text} didn't {v} {ph}." for v in ok])
    t = rng.pick(['pres','past','neg','q','qp'])
    if t == 'pres':
        s = f"{S.text} ___ {ph} every week."; ans = [F[v][0] if S.sg else v for v in ok]
        if S.kind == 'i' or S.kind == 'you' or S.kind == 'pl': ans = list(ok)
    elif t == 'past': s = f"{S.text} ___ {ph} last week."; ans = [F[v][1] for v in ok]
    elif t == 'neg': s = f"{S.text} {'doesn' if S.sg else 'don'}'t ___ {ph}."; ans = list(ok)
    elif t == 'q':
        s = f"{'Does' if S.sg else 'Do'} {S.mid} ___ {ph}?"; ans = list(ok)
        if S.text == 'I': return None
    else:
        if S.text == 'I': return None
        s = f"Did {S.mid} ___ {ph}?"; ans = list(ok)
    if level == 'easy':
        pool = [v for v in F if v not in ok]; rng.shuffle(pool); opts = [ok[0]] + pool[:2]; rng.shuffle(opts)
        h = ' (' + ' / '.join(opts) + ')'
    elif level == 'medium': h = ' (make / do / take / get / have)'
    else: h = ''
    return line(s + h, ans)
def gen_col_jobs(C):
    return {'collocations-make-do-take-get-have': lambda: gen_topic(gen_col, C, 141)}
