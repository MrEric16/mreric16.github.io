from lib import *
from passive import gen_topic
# (A clause, A noun/-ing form, B clause, optional question template with {L})
CONTRAST = [
 ("it was raining","the rain","we played football","Did you play football {L}?"),
 ("it was raining","the rain","we didn't stay at home","Did you stay at home {L}?"),
 ("Tom was tired","being tired","he finished his homework","Did Tom finish his homework {L}?"),
 ("Anna was ill","her illness","she went to school","Did Anna go to school {L}?"),
 ("the test was difficult","the difficulty of the test","Karim got a high mark",None),
 ("the flat was expensive","the high price","they bought it","Did they buy the flat {L}?"),
 ("Malika studied hard","studying hard","she failed the exam",None),
 ("we left early","leaving early","we missed the train","Did you miss the train {L}?"),
 ("Jasur didn't have a ticket","not having a ticket","he got into the stadium",None),
 ("the film was long","the length of the film","we enjoyed it","Did you enjoy the film {L}?"),
 ("the weather was cold","the cold weather","the children swam in the sea",None),
 ("Dilya was afraid of flying","her fear of flying","she took the plane","Did Dilya take the plane {L}?"),
 ("they were poor","their poverty","they were happy",None),
 ("Aziz was very busy","being very busy","he helped us","Did Aziz help you {L}?"),
 ("the road was icy","the icy road","he drove fast",None),
 ("Sara had a headache","having a headache","she played the piano","Did Sara play the piano {L}?"),
 ("we had little money","our lack of money","we had a great holiday",None),
 ("it was very late","the late hour","they kept talking",None),
 ("the food was cheap","the low price","it was delicious",None),
 ("Ali didn't speak Chinese","not speaking Chinese","he got the job in Beijing",None),
 ("the traffic was heavy","the heavy traffic","we arrived on time","Did you arrive on time {L}?"),
 ("Anna was nervous","being nervous","she gave a brilliant speech","Did Anna give a good speech {L}?"),
 ("the room was small","the small size of the room","it felt comfortable",None),
 ("Karim didn't study","not studying","he passed the test",None),
]
CAUSE = [
 ("it was raining","the rain","we stayed at home","Did you stay at home {L}?"),
 ("Tom was ill","his illness","he missed the lesson","Did Tom miss the lesson {L}?"),
 ("the test was difficult","the difficulty of the test","many students failed",None),
 ("the flat was expensive","the high price","they didn't buy it","Did they buy the flat {L}?"),
 ("Malika studied hard","her hard work","she passed the exam",None),
 ("we missed the bus","missing the bus","we were late",None),
 ("the film was boring","the boring film","we left early","Did you leave early {L}?"),
 ("the road was icy","the icy road","the drivers went slowly",None),
 ("Anna was tired","her tiredness","she went to bed early","Did Anna go to bed early {L}?"),
 ("the traffic was heavy","the heavy traffic","Karim was late for work","Was Karim late for work {L}?"),
 ("the shop was closed","the closed shop","we bought bread at the bazaar",None),
 ("the weather was hot","the hot weather","everyone swam in the river",None),
 ("Jasur didn't have a key","not having a key","he couldn't open the door",None),
 ("the power failed","the power cut","the lesson stopped",None),
 ("Dilya was afraid of dogs","her fear of dogs","she crossed the street","Did Dilya cross the street {L}?"),
 ("the food was delicious","the delicious food","we ate everything",None),
 ("the exam was easy","the easy exam","everybody finished early",None),
 ("it was snowing","the snow","school was closed","Was school closed {L}?"),
]
def capf(s): return s[0].upper() + s[1:]
def cform(kind, A, N, B, form):
    if kind == 'contrast':
        return {'alth': (f"Although {A}, {B}.", f"{capf(B)} although {A}."), 'desp': (f"Despite {N}, {B}.", f"{capf(B)} despite {N}."), 'insp': (f"In spite of {N}, {B}.", f"{capf(B)} in spite of {N}."),
                'how': (f"{capf(A)}. However, {B}.", None), 'but': (f"{capf(A)}, but {B}.", None)}[form]
    return {'bec': (f"Because {A}, {B}.", f"{capf(B)} because {A}."), 'becof': (f"Because of {N}, {B}.", f"{capf(B)} because of {N}."), 'so': (f"{capf(A)}, so {B}.", None),
            'ther': (f"{capf(A)}. Therefore, {B}.", None), 'asr': (f"{capf(A)}. As a result, {B}.", None)}[form]
LINK = {'alth': ['although','though','even though'], 'desp': ['despite','in spite of'], 'insp': ['in spite of','despite'], 'how': ['however'], 'but': ['but'],
        'bec': ['because'], 'becof': ['because of'], 'so': ['so'], 'ther': ['therefore'], 'asr': ['as a result']}
def gen_link(level, rng):
    kind = rng.pick(['contrast','cause'])
    A, N, B, Q = rng.pick(CONTRAST if kind == 'contrast' else CAUSE)
    forms = ['alth','desp','insp','how','but'] if kind == 'contrast' else ['bec','becof','so','ther','asr']
    f = rng.pick(forms)
    first, second = cform(kind, A, N, B, f)
    import re as _re
    clause_form = f in ('alth','bec')
    block2 = clause_form and _re.match(r'(he|she|they|it) ', B) and A[:1].isupper()
    sent = second if (second and not block2 and rng.pick([0,1])) else first
    l = LINK[f]
    if kind == 'contrast':
        hint2 = ' (although / despite)'; hint5 = ' (although / despite / in spite of / however / but)'
    else:
        hint2 = ' (because / because of)'; hint5 = ' (because / because of / so / therefore / as a result)'
    target = l[0]
    answers = list(l)
    # q forms
    if Q and rng.pick([0,0,1]):
        fq = rng.pick(['alth','desp'] if kind == 'contrast' else ['bec','becof'])
        if kind == 'contrast':
            L = {'alth': f"although {A}", 'desp': f"despite {N}"}[fq]
        else:
            L = {'bec': f"because {A}", 'becof': f"because of {N}"}[fq]
        PR = {'Tom':'he','Aziz':'he','Jasur':'he','Karim':'he','Ali':'he','Anna':'she','Malika':'she','Dilya':'she','Sara':'she'}
        mm = _re.match(r'(\w+) (.*)', A)
        if mm and mm.group(1) in PR and fq in ('alth','bec'): L = L.replace(mm.group(1) + ' ', PR[mm.group(1)] + ' ', 1)
        qfull = Q.format(L=L)
        w = LINK[fq][0]
        if level == 'easy':
            return line(Q.format(L=f"___ {L[len(w)+1:]}") + (hint2), LINK[fq])
        if level == 'medium':
            return line(Q.format(L=f"___ {L[len(w)+1:]}") + hint5, LINK[fq])
        other = {'alth':'despite','desp':'although','bec':'because of','becof':'because'}[fq]
        # wrong: swap form types
        wrong = Q.format(L=(f"despite {A}" if fq == 'alth' else (f"although {N}" if fq == 'desp' else (f"because of {A}" if fq == 'bec' else f"because {N}"))))
        qa = [qfull] + ([qfull.replace('despite', 'in spite of')] if fq == 'desp' else [])
        return line('Correct the mistake: ' + wrong, qa)
    blank_sent = None
    # find the linker inside sentence to blank
    low = sent
    for lk in sorted(l, key=len, reverse=True):
        pass
    word = target
    idx = sent.find(word) if sent.find(word) >= 0 else sent.find(word.capitalize())
    if idx < 0: return None
    cap_it = (idx == 0)
    shown = sent[:idx] + '___' + sent[idx+len(word):]
    if level == 'easy':
        if f in ('how','but','so','ther','asr'):
            hint = hint5
        else: hint = hint2
        return line(shown + hint, [a.capitalize() if cap_it else a for a in answers] if False else answers)
    if level == 'medium':
        return line(shown + hint5, answers)
    k = rng.pick(['fix','fix','rewrite','rewrite','rewrite'])
    if k == 'fix':
        if f in ('alth',): bad = sent.replace('Although', 'Despite', 1).replace(' although ', ' despite ', 1)
        elif f in ('desp','insp'): bad = sent.replace('Despite', 'Although').replace('despite', 'although').replace('In spite of', 'Although').replace('in spite of', 'although')
        elif f == 'bec': bad = sent.replace('Because ', 'Because of ', 1).replace(' because ', ' because of ', 1)
        elif f == 'becof': bad = sent.replace('Because of', 'Because', 1).replace(' because of ', ' because ', 1)
        else: return None
        if bad == sent: return None
        alts = [sent]
        if f == 'desp': alts.append(sent.replace('Despite', 'In spite of').replace(' despite ', ' in spite of '))
        if f == 'insp': alts.append(sent.replace('In spite of', 'Despite').replace(' in spite of ', ' despite '))
        return line('Correct the mistake: ' + bad, alts)
    # rewrite from another form
    others = [x for x in forms if x != f]
    g = rng.pick(others)
    s_from, s_from2 = cform(kind, A, N, B, f)
    s_to, s_to2 = cform(kind, A, N, B, g)
    word_to = LINK[g][0]
    blk = g in ('alth','bec') and _re.match(r'(he|she|they|it) ', B) and A[:1].isupper()
    tgt = [x for x in (s_to, (None if blk else s_to2)) if x]
    src = s_from
    name = {'alth':'although','desp':'despite','insp':'in spite of','how':'however','but':'but','bec':'because','becof':'because of','so':'so','ther':'therefore','asr':'as a result'}[g]
    # acceptable: alternatives for 'although' (though / even though) are not accepted by design for rewrite
    return line(f"Rewrite with '{name}': " + src, tgt)
def gen_link_jobs(C):
    return {'linkers': lambda: gen_topic(gen_link, C, 120)}
