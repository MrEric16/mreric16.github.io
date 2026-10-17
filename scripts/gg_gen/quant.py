from lib import *
from passive import gen_topic
COUNT = [("apples","in the bag","make a pie"),("eggs","in the fridge","make an omelette"),("tomatoes","in the fridge","make a salad"),("sandwiches","on the plate","have lunch"),("chairs","in the classroom","start the lesson"),("students","in the hall","start the lesson"),("books","on the shelf","start the project"),("pencils","in the box","finish the drawing"),("cups","in the cupboard","serve the tea"),("bananas","in the basket","make a milkshake"),("bottles","in the fridge","start the party"),("tickets","in the envelope","go to the concert"),("onions","in the kitchen","cook the soup"),("candles","in the drawer","decorate the room")]
UNC = [("milk","in the fridge","make tea"),("water","in the bottle","make soup"),("sugar","in the cupboard","bake a cake"),("rice","in the cupboard","cook dinner"),("juice","in the jug","have a drink"),("bread","in the kitchen","make toast"),("money","in the wallet","buy a ticket"),("flour","in the cupboard","bake bread"),("coffee","in the jar","make a cup"),("paper","in the printer","print the test"),("butter","in the fridge","make a sandwich"),("soup","in the pot","feed everyone"),("cheese","in the fridge","make a pizza"),("oil","in the bottle","fry the eggs")]
def mood3(rng): return rng.pick(['aff','aff','neg','q'])
def item(rng, force=None):
    c = force if force is not None else rng.pick([True, False])
    n, ctx, cons = rng.pick(COUNT if c else UNC)
    return c, n, ctx, cons
def be(c): return "are" if c else "is"
def nt(c, mood):
    # There is/are frames
    return None
def there(c, mood, q, n, ctx):
    b = be(c)
    if mood == 'aff': return f"There {b} {q} {n} {ctx}."
    if mood == 'neg': return f"There {b}n't {q} {n} {ctx}."
    return f"{cap(b)} there {q} {n} {ctx}?"
def gen_some_any(level, rng):
    c, n, ctx, cons = item(rng); mood = mood3(rng)
    if rng.pick([0,0,0,1]):
        FOOD = ('apples','eggs','tomatoes','sandwiches','bananas','onions','milk','water','sugar','rice','juice','bread','coffee','butter','soup','cheese')
        c, n, ctx, cons = item(rng)
        while n not in FOOD: c, n, ctx, cons = item(rng)
        # requests and offers
        t = rng.pick([("Would you like ___ {n}?", 'some'),("Can I have ___ {n}, please?", 'some'),("Could you give me ___ {n}?", 'some'),("Do you want ___ {n}?", 'any'),("I'd like ___ {n}, please.", 'some')])
        # 'Do you want any' is acceptable alongside some
        s, a = t
        ans = ['some','any'] if a == 'any' else ['some']
        return line(s.format(n=n) + ' (some / any)', ans)
    ans = 'some' if mood == 'aff' else 'any'
    q = there(c, mood, '___', n, ctx)
    if level != 'hard': return line(q + ' (some / any)', [ans])
    k = rng.pick(['fix','fix','neg','q'])
    good = there(c, mood, ans, n, ctx)
    if k == 'fix':
        wrong = 'any' if mood == 'aff' else 'some'
        return line('Correct the mistake: ' + there(c, mood, wrong, n, ctx), [good])
    if mood != 'aff': return None
    if k == 'neg': return line('Make a negative sentence: ' + good, [there(c, 'neg', 'any', n, ctx)])
    return line('Make a question: ' + good, [there(c, 'q', 'any', n, ctx)])
def gen_much_many(level, rng):
    c, n, ctx, cons = item(rng); mood = mood3(rng); w = 'many' if c else 'much'
    k = rng.pick(['how','how','nq','aff'])
    how = f"How {w} {n} {be(c)} there {ctx}?"
    if k == 'how':
        q = f"How ___ {n} {be(c)} there {ctx}?"
        if level != 'hard': return line(q, [w])
        return line('Correct the mistake: ' + f"How {'much' if c else 'many'} {n} {be(c)} there {ctx}?", [how])
    if k == 'aff':
        q = f"There {be(c)} ___ {n} {ctx}."
        if level == 'easy': return line(q + ' (a lot of)', ['a lot of','lots of'])
        if level == 'medium': return line(q + ' (much / many / a lot of)', ['a lot of','lots of'])
        wrong = 'much' if not c else 'many'
        return line('Correct the mistake: ' + f"There {be(c)} {wrong} {n} {ctx}.", [f"There {be(c)} a lot of {n} {ctx}.", f"There {be(c)} lots of {n} {ctx}."])
    if mood == 'q':
        q = f"{cap(be(c))} there ___ {n} {ctx}?"; a = [w, 'a lot of']
        if c: pass
        return line(q + ' (much / many / a lot of)', a) if level != 'hard' else line('Correct the mistake: ' + f"{cap(be(c))} there {'much' if c else 'many'} {n} {ctx}?", [f"{cap(be(c))} there {w} {n} {ctx}?", f"{cap(be(c))} there a lot of {n} {ctx}?"])
    mm = 'neg'
    q = f"There {be(c)}n't ___ {n} {ctx}."
    if level != 'hard': return line(q + ' (much / many / a lot of)', [w, 'a lot of'])
    return line('Correct the mistake: ' + f"There {be(c)}n't {'much' if c else 'many'} {n} {ctx}.", [f"There {be(c)}n't {w} {n} {ctx}.", f"There {be(c)}n't a lot of {n} {ctx}."])
def gen_few_little(level, rng):
    c, n, ctx, cons = item(rng); pos = rng.pick([True, False]); mood3_ = rng.pick(['aff','aff','neg'])
    b = be(c)
    if pos: ans = 'a few' if c else 'a little'; main = f"There {b} {ans} {n} {ctx}, so we can {cons}."
    else: ans = 'few' if c else 'little'; main = f"There {b} {ans} {n} {ctx}, so we can't {cons}."
    blank = main.replace(f" {ans} ", " ___ ", 1)
    if level == 'easy':
        return line(blank + (' (a few / few)' if c else ' (a little / little)'), [ans])
    if level == 'medium':
        return line(blank + ' (few / a few / little / a little)', [ans])
    k = rng.pick(['fix','fix','w'])
    if k == 'fix':
        wrongs = ['a little','little'] if c else ['a few','few']
        w = wrongs[0] if pos else wrongs[1]
        bad = main.replace(f" {ans} ", f" {w} ", 1)
        return line('Correct the mistake: ' + bad, [main])
    # which word fits: not many/much
    if pos: return None
    alt = 'many' if c else 'much'
    return line(f"Rewrite with 'not {alt}': " + main, [main.replace(f" {ans} ", f"n't {alt} ", 1).replace(f"There {b}n't", f"There {b}n't").replace(f"There {b}n't {alt}", f"There {b}n't {alt}")])
def gen_enough_too(level, rng):
    c, n, ctx, cons = item(rng); mood = mood3(rng); b = be(c)
    k = rng.pick(['enough','enough','too'])
    if k == 'enough':
        w = 'enough'
        good = there(c, mood, 'enough', n, ctx)
        q = there(c, mood, '___', n, ctx)
        if level != 'hard': return line(q + (' (enough / too many)' if c else ' (enough / too much)'), ['enough'])
        bad = good.replace(f"enough {n}", f"{n} enough")
        return line('Correct the mistake: ' + bad, [good])
    tm = 'too many' if c else 'too much'
    if mood == 'aff': good = f"There {b} {tm} {n} {ctx}."; q = f"There {b} too ___ {n} {ctx}."
    elif mood == 'neg': good = f"There {b}n't {tm} {n} {ctx}."; q = f"There {b}n't too ___ {n} {ctx}."
    else: good = f"{cap(b)} there {tm} {n} {ctx}?"; q = f"{cap(b)} there too ___ {n} {ctx}?"
    w = 'many' if c else 'much'
    if level == 'easy': return line(q + ' (much / many)', [w])
    if level == 'medium': return line(good.replace(tm, '___') + (' (enough / too many)' if c else ' (enough / too much)'), [tm])
    wr = 'too much' if c else 'too many'
    return line('Correct the mistake: ' + good.replace(tm, wr), [good])
def gen_mixed(level, rng):
    k = rng.pick(['sa','mm','fl','et'])
    return {'sa':gen_some_any,'mm':gen_much_many,'fl':gen_few_little,'et':gen_enough_too}[k](level, rng)
def gen_q_jobs(C):
    return {'quantifiers': lambda: gen_topic(gen_mixed, C, 96)}
