from lib import *
from passive import gen_topic
# (imperative, positive condition, negative condition, positive result, negative result) - all 2nd person
P = [
 ("Hurry up","you hurry","you don't hurry","you'll catch the bus","you'll miss the bus"),
 ("Study hard","you study hard","you don't study hard","you'll pass the exam","you'll fail the exam"),
 ("Wear a coat","you wear a coat","you don't wear a coat","you'll stay warm","you'll catch a cold"),
 ("Save money","you save money","you don't save money","you'll buy a car","you won't buy a car"),
 ("Go to bed early","you go to bed early","you don't go to bed early","you'll feel fresh tomorrow","you'll be tired tomorrow"),
 ("Practise every day","you practise every day","you don't practise every day","you'll improve","you won't improve"),
 ("Ask for help","you ask for help","you don't ask for help","you'll understand the lesson","you won't understand the lesson"),
 ("Leave now","you leave now","you don't leave now","you'll arrive on time","you'll be late"),
 ("Drink more water","you drink more water","you don't drink more water","you'll feel better","you'll get a headache"),
 ("Revise the vocabulary","you revise the vocabulary","you don't revise the vocabulary","you'll do well in the test","you'll do badly in the test"),
 ("Be careful","you are careful","you aren't careful","you'll be fine","you'll have an accident"),
 ("Book a table","you book a table","you don't book a table","you'll get a seat","you won't get a seat"),
 ("Take notes","you take notes","you don't take notes","you'll remember everything","you'll forget the details"),
 ("Call me","you call me","you don't call me","I'll pick you up","I won't pick you up"),
 ("Charge your phone","you charge your phone","you don't charge your phone","you'll be able to call me","you won't be able to call me"),
 ("Keep calm","you keep calm","you don't keep calm","you'll think clearly","you'll make mistakes"),
 ("Listen carefully","you listen carefully","you don't listen carefully","you'll understand","you'll get confused"),
 ("Eat breakfast","you eat breakfast","you don't eat breakfast","you'll have more energy","you'll feel weak by ten"),
 ("Back up your files","you back up your files","you don't back up your files","you'll keep your work","you'll lose your work"),
 ("Turn off the oven","you turn off the oven","you don't turn off the oven","you'll save electricity","you'll waste electricity"),
 ("Lock the door","you lock the door","you don't lock the door","you'll feel safe","you'll worry all night"),
 ("Wear sunscreen","you wear sunscreen","you don't wear sunscreen","you'll avoid sunburn","you'll get sunburnt"),
 ("Wake up early","you wake up early","you don't wake up early","you'll see the sunrise","you'll miss the sunrise"),
 ("Warm up first","you warm up first","you don't warm up first","you'll avoid injury","you'll hurt yourself"),
 ("Phone the doctor","you phone the doctor","you don't phone the doctor","you'll get an appointment","you won't get an appointment"),
 ("Learn ten words a day","you learn ten words a day","you don't learn ten words a day","your vocabulary will grow","your vocabulary won't grow"),
 ("Press save","you press save","you don't press save","you'll keep the document","you'll lose the document"),
 ("Read the instructions","you read the instructions","you don't read the instructions","you'll know what to do","you'll get stuck"),
 ("Be polite","you are polite","you aren't polite","people will help you","people won't help you"),
 ("Work as a team","you work as a team","you don't work as a team","you'll finish on time","you won't finish on time"),
]
# precautions: (imperative, event positive, event negative-ish)
INCASE = [
 ("Take an umbrella","it rains"),("Take a jacket","it gets cold"),("Bring some water","you get thirsty"),("Write down the address","you forget it"),("Take some cash","the card machine is broken"),
 ("Leave early","there is a lot of traffic"),("Save the file","the computer crashes"),("Take a map","you get lost"),("Bring a snack","you get hungry"),("Keep the receipt","you need to return the shirt"),
 ("Buy some bread","the shop is closed tomorrow"),("Charge the laptop","the power cuts out"),("Take a book","the journey is boring"),("Check the time","the bus is early"),("Call him","he forgets the meeting"),
]
def cap1(s): return s[0].upper() + s[1:]
def q_of(res):
    if res.startswith("you'll "): return "Will you " + res[7:]
    if res.startswith("I'll "): return "Will I " + res[5:]
    if res.startswith("you won't "): return "Will you " + res[10:]
    if res.startswith("I won't "): return "Will I " + res[8:]
    return None
def forms(row):
    imp, cp, cn, rp, rn = row
    return {
     'if': (f"If {cp}, {rp}.", f"{cap1(rp)} if {cp}."),
     'unless': (f"Unless {cp}, {rn}." if rn.find("n't") < 0 and True else None, None),
    }
def gen_cc(level, rng):
    kind = rng.pick(['if','unless','aslong','otherwise','incase','incase','prov'])
    if kind == 'incase':
        imp, ev = rng.pick(INCASE)
        sent = f"{imp} in case {ev}."
        neg_imp = {'Take':"Don't take"}.get(imp.split()[0])
        if level == 'easy': return line(f"{imp} ___ {ev}. (in case / if)", ['in case'])
        if level == 'medium': return line(f"{imp} ___ {ev}. (in case / unless / as long as / otherwise)", ['in case'])
        k = rng.pick(['fix','fix','rewrite'])
        if k == 'fix':
            bad = f"{imp} in case {ev.replace('it rains','it will rain').replace('you get','you will get').replace('it gets','it will get')}."
            if bad == sent: return None
            return line('Correct the mistake: ' + bad, [sent])
        return line(f"Rewrite with 'in case': {imp} because {ev} and you might need it.", [sent]) if False else None
    row = rng.pick(P); imp, cp, cn, rp, rn = row
    if kind == 'if':
        mood = rng.pick(['aff','neg','q'])
        if mood == 'aff': s = f"If {cp}, {rp}."
        elif mood == 'neg': s = f"If {cn}, {rn}."
        else:
            qq = q_of(rp)
            if not qq: return None
            s = f"{qq} if {cp}?"
        if level == 'easy': return line(s.replace('If', '___', 1) + ' (if / unless)', ['if'], ) if mood != 'q' else line(s.replace(' if ', ' ___ ', 1) + ' (if / unless)', ['if'])
        if level == 'medium':
            return line((s.replace('If', '___', 1) if mood != 'q' else s.replace(' if ', ' ___ ', 1)) + ' (if / unless / in case / otherwise)', ['if'])
        return None
    if kind == 'unless':
        s1 = f"Unless {cp}, {rn}."; s2 = f"{cap1(rn)} unless {cp}."
        sent = rng.pick([s1, s2])
        if level == 'easy': return line(sent.replace('Unless', '___', 1).replace(' unless ', ' ___ ', 1) + ' (if / unless)', ['unless'])
        if level == 'medium': return line(sent.replace('Unless', '___', 1).replace(' unless ', ' ___ ', 1) + ' (if / unless / as long as / in case)', ['unless'])
        k = rng.pick(['rewrite','rewrite','fix','fix'])
        if k == 'rewrite':
            src = f"If {cn}, {rn}." if rng.pick([0,1]) else f"{cap1(rn)} if {cn}."
            return line("Rewrite with 'unless': " + src, [s1, s2] if src.startswith('If') else [s1, s2])
        bad = s1.replace(f"Unless {cp}", f"Unless {cn}") if rng.pick([0,1]) else s2.replace(f"unless {cp}", f"unless {cn}")
        return line('Correct the mistake: ' + bad, [s1, s2] if bad.startswith('Unless') else [s1, s2])
    if kind in ('aslong','prov'):
        w = 'as long as' if kind == 'aslong' else rng.pick(['provided that','providing that','provided'])
        words = ['as long as'] if kind == 'aslong' else ['provided that','providing that','provided','providing','as long as']
        if kind == 'prov': words = ['provided that','providing that','provided','providing','as long as','so long as']
        else: words = ['as long as','so long as','provided that','providing that','provided','providing']
        sent = rng.pick([f"{cap1(rp)} {w} {cp}.", f"{cap1(w)} {cp}, {rp}."])
        shown = sent.replace(w, '___', 1) if not sent.startswith(cap1(w)) else sent.replace(cap1(w), '___', 1)
        if level == 'easy': return line(shown + ' (as long as / unless)', words)
        if level == 'medium': return line(shown + ' (as long as / unless / in case / otherwise)', words)
        k = rng.pick(['rewrite','fix'])
        if k == 'rewrite': return line(f"Rewrite with '{w}': If {cp}, {rp}.", [sent] if False else [f"{cap1(w)} {cp}, {rp}.", f"{cap1(rp)} {w} {cp}."])
        bad = sent.replace(cp, cp.replace("you ", "you will ", 1)) if cp.startswith('you ') and "n't" not in cp and 'are' not in cp else None
        if not bad or bad == sent: return None
        return line('Correct the mistake: ' + bad, [sent])
    # otherwise
    sent = f"{imp}. Otherwise, {rn}."
    sent2 = f"{imp}, or {rn.replace(chr(39) + 'll', ' will') if False else rn}."
    if level == 'easy': return line(f"{imp}. ___, {rn}. (otherwise / unless)", ['Otherwise'])
    if level == 'medium': return line(f"{imp}. ___, {rn}. (otherwise / unless / in case / as long as)", ['Otherwise'])
    k = rng.pick(['rewrite','rewrite','fix'])
    if k == 'rewrite': return line(f"Rewrite with 'otherwise': If {cn}, {rn}.", [sent]) if False else line(f"Rewrite with 'otherwise': {imp} or {rn}.", [sent, f"{imp}. Otherwise {rn}."])
    return line('Correct the mistake: ' + f"{imp}. Unless, {rn}.", [sent, f"{imp}. Otherwise {rn}."])
def gen_cc_jobs(C):
    return {'conditional-connectors': lambda: gen_topic(gen_cc, C, 121)}
