from lib import *
from passive import gen_topic
NAMES = ["Tom","Anna","Aziz","Malika","Jasur","Dilnoza","Karim","Sara","Sardor","Dilya","Ali"]
THINGS = ["an umbrella","an apple","an egg","an orange","an old car","a new phone","a big house","a cheap bag","an expensive watch","a useful app","an interesting book","a red coat","an old bike","a small camera","a yellow umbrella","a blue pen","an ugly shirt","a clean towel","an empty bottle","a heavy suitcase","an easy exam","a long letter","a hot coffee","an orange scarf","a unique idea","an honest answer","a university course","an hour-long film"]
PLAIN = ["umbrella","apple","egg","orange","car","phone","house","bag","watch","app","book","coat","bike","camera","pen","shirt","bottle","towel","letter","scarf"]
JOBS = ["teacher","manager","doctor","pilot","nurse","dentist","lawyer","driver","chef","engineer","electrician","accountant","architect","actor","artist","singer","scientist","journalist","baker","photographer","designer","programmer","mechanic","builder","interpreter"]
PRED = ["a present","a gift","a surprise","a good one"]
V_TH = [("has","have"),("needs","need"),("wants","want"),("finds","find"),("loses","lose"),("sees","see"),("buys","buy"),("takes","take")]
V_TH_LIFE = [("has","have"),("needs","need"),("wants","want")]
# (verb3, base, rest with {A}, answer, bad)
TAB = [
 ("plays","play","{A} guitar after school","the","a"),("plays","play","{A} piano every evening","the","a"),("plays","play","{A} violin in the school orchestra","the","a"),
 ("watches","watch","{A} news at nine","the","a"),("listens","listen","to {A} radio in the morning","the","a"),("looks","look","at {A} moon every night","the","a"),
 ("plays","play","{A} football at weekends","x","the"),("plays","play","{A} chess with his friends","x","the"),("plays","play","{A} tennis on Saturdays","x","the"),("plays","play","{A} basketball after school","x","the"),
 ("has","have","{A} breakfast at seven","x","the"),("has","have","{A} dinner at home","x","the"),("has","have","{A} lunch at one","x","the"),
 ("goes","go","to {A} school every day","x","the"),("goes","go","to {A} bed at eleven","x","the"),("goes","go","to {A} work by metro","x","the"),("goes","go","to {A} church on Sundays","x","the"),
 ("travels","travel","by {A} train","x","the"),("travels","travel","by {A} bus","x","the"),("travels","travel","by {A} plane","x","the"),
 ("speaks","speak","{A} English at work","x","the"),("studies","study","{A} history on Mondays","x","the"),("studies","study","{A} biology at school","x","the"),("stays","stay","at {A} home on Sundays","x","the"),
]
XA = ['x','no article','nothing','zero','none']
def art_of(phrase): return phrase.split(' ',1)[0]
def rest_of(phrase): return phrase.split(' ',1)[1]
def cap1(s): return s[0].upper()+s[1:]
def mood3(rng): return rng.pick(['aff','aff','neg','q'])
def sent(name, v3, vb, rest, mood):
    if mood == 'aff': return f"{name} {v3} {rest}."
    if mood == 'neg': return f"{name} {'doesn' + chr(39) + 't'} {vb} {rest}."
    return f"Does {name} {vb} {rest}?"
def be_sent(name, pred, mood):
    if mood == 'aff': return f"{name} is {pred}."
    if mood == 'neg': return f"{name} isn't {pred}."
    return f"Is {name} {pred}?"
def clean(s): return s.replace('  ',' ')
def case_a(rng, mood):
    name = rng.pick(NAMES)
    if rng.pick([0,1,0]):
        job = rng.pick(JOBS); art = 'an' if job[0] in 'aeiou' else 'a'
        return be_sent(name, f"{{A}} {job}", mood), art, f"{art} {job}"
    th = rng.pick(THINGS); v3, vb = rng.pick(V_TH)
    return sent(name, v3, vb, "{A} " + rest_of(th), mood), art_of(th), th
def case_the(rng, mood):
    name = rng.pick(NAMES); n = rng.pick(PLAIN); art = 'an' if n[0] in 'aeiou' else 'a'; v3, vb = rng.pick(V_TH_LIFE)
    first = f"{name} has {art} {n}."
    pred = rng.pick(PRED)
    second = be_sent("{A} "+n, pred, mood).replace("{A} "+n, "{A} "+n)
    return first, second, n, art
def second_text(n, pred, mood, art_word):
    if mood == 'aff': return f"{art_word} {n} is {pred}."
    if mood == 'neg': return f"{art_word} {n} isn't {pred}."
    return f"Is {art_word if art_word.startswith('{') else art_word.lower()} {n} {pred}?"
def gen_art(level, rng):
    mood = mood3(rng)
    kind = rng.pick(['a','a','the','tab','tab','tab']) if level != 'easy' else rng.pick(['a','a','the'])
    if kind == 'a':
        tmpl, art, full = case_a(rng, mood)
        q = tmpl.replace('{A}', '___')
        good = tmpl.replace('{A}', art)
        if level != 'hard': return line(q, [art])
        k = rng.pick(['fix','fix','neg','q'])
        if k == 'fix':
            w = 'a' if art == 'an' else 'an'
            return line('Correct the mistake: ' + tmpl.replace('{A}', w), [good])
        return None
    if kind == 'the':
        name = rng.pick(NAMES); n = rng.pick(PLAIN); art = 'an' if n[0] in 'aeiou' else 'a'; pred = rng.pick(PRED)
        first = f"{name} {rng.pick(['has','bought','found'])} {art} {n}."
        sec = second_text(n, pred, mood, "{A}")
        sec_blank = sec.replace('{A}', '___') if mood != 'q' else sec.replace('{A}', '___')
        if level == 'easy':
            return line(f"{first} {sec_blank}", ['the'] if False else ['the'])
        if level == 'medium':
            first_b = first.replace(f" {art} ", " ___ ", 1)
            return line(f"{first_b} {sec_blank}", [art], ['the'])
        k = rng.pick(['fix','fix','twofix'])
        if k == 'fix':
            bad = second_text(n, pred, mood, 'A' if art == 'a' else 'An') if mood != 'q' else f"Is {art} {n} {pred}?"
            return line('Correct the mistake: ' + first + ' ' + bad, [first + ' ' + second_text(n, pred, mood, 'The')] if mood != 'q' else [f"{first} Is the {n} {pred}?"])
        bad_first = first.replace(f" {art} ", " the ", 1)
        return line('Correct the mistake: ' + bad_first + ' ' + second_text(n, pred, mood, 'The'), [first + ' ' + second_text(n, pred, mood, 'The')])
    # table
    name = rng.pick(NAMES); v3, vb, rest, ans, bad = rng.pick(TAB)
    good_rest = rest.replace('{A} ', '') if ans == 'x' else rest.replace('{A}', ans)
    bad_rest = rest.replace('{A}', bad)
    good = sent(name, v3, vb, good_rest, mood)
    if level == 'easy' or level == 'medium':
        hint = '(a / an / the / x)' if level == 'medium' else '(the / x)'
        q = sent(name, v3, vb, rest.replace('{A}', '___'), mood)
        note = ' (x = no article)' if True else ''
        a = XA if ans == 'x' else [ans]
        if level == 'easy':
            return line(q + ' (the or x; x = no article)', a)
        return line(q + ' (a / an / the / x)', a)
    k = rng.pick(['fix','fix','fix'])
    return line('Correct the mistake: ' + sent(name, v3, vb, bad_rest, mood), [good])
def gen_art_jobs(C):
    return {'articles': lambda: gen_topic(gen_art, C, 95)}
