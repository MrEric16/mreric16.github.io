from lib import *
from passive import gen_topic
SGq = [Subj('I','i','i'),Subj('You','you','you'),Subj('He','sg','he'),Subj('She','sg','she'),Subj('We','pl','we'),Subj('They','pl','they'),Subj('Tom','sg','he',True),Subj('Anna','sg','she',True),Subj('Aziz','sg','he',True),Subj('Malika','sg','she',True),Subj('Karim','sg','he',True),Subj('Dilya','sg','she',True),Subj('My brother','sg','he'),Subj('My sister','sg','she'),Subj('My parents','pl','they'),Subj('The students','pl','they')]
def mood2(rng): return rng.pick(['aff','neg'])
def _lab(S): return S.text[0].lower() + S.text[1:] if S.text.split()[0] in ('He','She','We','They','You','The','My','Our','This','That','These','Those','Her','His','Their') else S.text
def pr_sub(S): return {'i':'I','you':'you','he':'he','she':'she','we':'we','they':'they'}[S.pron]
NOTDO = ('be',)
# ====== question tags ======
ADJ = ["tired","hungry","late","ready","busy","happy","nervous","bored","angry","at home","in the garden","from Uzbekistan"]
def tag_for(S, kind, neg, extra=None):
    """tag text for subject S, auxiliary kind, statement polarity neg"""
    p = pr_sub(S)
    if kind == 'bepres':
        a = {'I':'am','you':'are','he':'is','she':'is','we':'are','they':'are'}[p]
        if not neg:
            return ("aren't I" if p == 'I' else f"{a}n't {p}"), ([] if p != 'I' else ["am I not"])
        return f"{a} {p}", []
    if kind == 'bepast':
        a = 'was' if p in ('I','he','she') else 'were'
        return (f"{a}n't {p}" if not neg else f"{a} {p}"), []
    if kind == 'dopres':
        a = 'does' if p in ('he','she') else 'do'
        return (f"{a}n't {p}" if not neg else f"{a} {p}"), []
    if kind == 'dopast':
        return (f"didn't {p}" if not neg else f"did {p}"), []
    if kind == 'perf':
        a = 'has' if p in ('he','she') else 'have'
        return (f"{a}n't {p}" if not neg else f"{a} {p}"), []
    if kind == 'can':
        return (f"can't {p}" if not neg else f"can {p}"), []
    if kind == 'will':
        return (f"won't {p}" if not neg else f"will {p}"), []
    if kind == 'should':
        return (f"shouldn't {p}" if not neg else f"should {p}"), []
def tag_stmt(S, kind, neg, V, comp, adj):
    sg = S.kind == 'sg'; p = pr_sub(S); t = S.text
    if kind == 'bepres':
        b = 'am' if p == 'I' else ('is' if sg else 'are')
        return f"{t} {b}{'n' + chr(39) + 't' if neg and p != 'I' else (' not' if neg else '')} {adj}"
    if kind == 'bepast':
        b = 'was' if (p == 'I' or sg) else 'were'
        return f"{t} {b}{'n' + chr(39) + 't' if neg else ''} {adj}"
    if kind == 'dopres':
        if neg: return f"{t} {'doesn' + chr(39) + 't' if sg else 'don' + chr(39) + 't'} {V.base} {comp}"
        return f"{t} {V.s if sg else V.base} {comp}"
    if kind == 'dopast':
        return f"{t} {'didn' + chr(39) + 't ' + V.base if neg else V.past} {comp}"
    if kind == 'perf':
        h = 'has' if sg else 'have'
        return f"{t} {h}{'n' + chr(39) + 't' if neg else ''} {V.pp} {comp}"
    if kind == 'can':
        return f"{t} {'can' + chr(39) + 't' if neg else 'can'} {V.base} {comp}"
    if kind == 'will':
        return f"{t} {'won' + chr(39) + 't' if neg else 'will'} {V.base} {comp}"
    return f"{t} {'shouldn' + chr(39) + 't' if neg else 'should'} {V.base} {comp}"
EXC = [
 ("I am late","aren't I",["am I not"],"I am not late","am I"),
 ("Let's go home","shall we",[],None,None),
 ("Open the window","will you",["won't you","can you","could you"],"Don't open the window","will you"),
 ("Close the door","will you",["won't you","can you","could you"],"Don't close the door","will you"),
 ("Be quiet","will you",["won't you"],"Don't be noisy","will you"),
 ("Nobody called","did they",[],None,None),
 ("Nobody is here","are they",[],None,None),
 ("Somebody is waiting for you","aren't they",["isn't he","isn't she"],None,None),
 ("Everybody enjoyed the party","didn't they",[],None,None),
 ("Everybody is ready","aren't they",[],None,None),
 ("There is a problem","isn't there",[],"There isn't a problem","is there"),
 ("There are some apples","aren't there",[],"There aren't any apples","are there"),
 ("This is your bag","isn't it",[],"This isn't your bag","is it"),
 ("That is your bike","isn't it",[],"That isn't your bike","is it"),
 ("Nothing happened","did it",[],None,None),
 ("Let's start now","shall we",[],None,None),
]
def gen_tag(level, rng):
    if rng.pick([0,0,0,1]) and level != 'easy':
        t = rng.pick(EXC)
        st, tg, alts, nst, ntg = t
        if rng.pick([0,1]) and nst:
            st, tg, alts = nst, ntg, []
        punct = '!' if False else ''
        base = f"{st}, ___?"
        if level == 'medium': return line(base, [tg] + alts)
        k = rng.pick(['fix','fix'])
        wrong = {"aren't I":"amn't I","shall we":"will we","will you":"don't you","did they":"didn't they","are they":"aren't they","aren't they":"are they","didn't they":"did they","isn't there":"isn't it","aren't there":"aren't they","is there":"isn't there","are there":"aren't there","isn't it":"is it","is it":"isn't it","did it":"didn't it","am I":"aren't I"}.get(tg)
        if not wrong: return None
        return line('Correct the mistake: ' + f"{st}, {wrong}?", [f"{st}, {tg}?"] + [f"{st}, {a}?" for a in alts])
    S = rng.pick(SGq); neg = rng.pick([False, False, True]); kind = rng.pick(['bepres','bepast','dopres','dopast','perf','can','will','should'])
    if level == 'easy' and kind in ('perf','should'): kind = 'dopres'
    V = rng.pick([v for v in VERBS if not v.ach]); comp = rng.pick(V.comps); adj = rng.pick(ADJ)
    if kind == 'perf' and not hasattr(V, 'pp'): return None
    st = tag_stmt(S, kind, neg, V, comp, adj)
    tg, alts = tag_for(S, kind, neg)
    full = f"{st}, {tg}?"
    if level != 'hard': return line(f"{st}, ___?", [tg] + alts)
    k = rng.pick(['fix','fix','fix','fix2'])
    if k == 'fix':
        # same polarity tag
        samepol, _ = tag_for(S, kind, not neg)
        return line('Correct the mistake: ' + f"{st}, {samepol}?", [full] + [f"{st}, {a}?" for a in alts])
    # wrong auxiliary
    other = {'bepres':'dopres','bepast':'dopast','dopres':'bepres','dopast':'bepast','perf':'dopres','can':'will','will':'can','should':'can'}[kind]
    wt, _ = tag_for(S, other, neg if False else neg)
    if wt == tg: return None
    return line('Correct the mistake: ' + f"{st}, {wt}?", [full] + [f"{st}, {a}?" for a in alts])
# ====== indirect questions ======
STEMS_Q = ["Do you know","Could you tell me","Can you tell me","Would you mind telling me"]
STEMS_A = ["I wonder","I'd like to know","I don't know","Nobody knows","I can't remember"]
WH = ["where","when","why","how","what time"]
def ind_case(rng):
    S = rng.pick([s for s in SGq if s.pron != 'i']); V = rng.pick([v for v in VERBS if not v.ach]); comp = rng.pick(V.comps)
    sg = S.kind == 'sg'; p = pr_sub(S)
    t = rng.pick(['pres','past','pc','perf','can','be','bepast','yn_pres','yn_past','yn_be','who'])
    wh = rng.pick(WH)
    if t == 'pres':
        direct = f"{cap(wh)} {'does' if sg else 'do'} {S.mid} {V.base} {comp}?"; emb = f"{wh} {S.mid} {V.s if sg else V.base} {comp}"; wrongd = f"{wh} {'does' if sg else 'do'} {S.mid} {V.base} {comp}"; bl = (f"{wh} {S.mid} ___ ({V.base}) {comp}", V.s if sg else V.base)
    elif t == 'past':
        direct = f"{cap(wh)} did {S.mid} {V.base} {comp}?"; emb = f"{wh} {S.mid} {V.past} {comp}"; wrongd = f"{wh} did {S.mid} {V.base} {comp}"; bl = (f"{wh} {S.mid} ___ ({V.base}) {comp}", V.past)
    elif t == 'pc':
        b = 'is' if sg else 'are'
        direct = f"{cap(wh)} {b} {S.mid} {V.ing} {comp}?"; emb = f"{wh} {S.mid} {b} {V.ing} {comp}"; wrongd = f"{wh} {b} {S.mid} {V.ing} {comp}"; bl = (f"{wh} {S.mid} ___ ({V.ing}) {comp}" if False else f"{wh} {S.mid} ___ {V.ing} {comp}", b)
    elif t == 'perf':
        h = 'has' if sg else 'have'
        direct = f"{cap(wh)} {h} {S.mid} {V.pp} {comp}?"; emb = f"{wh} {S.mid} {h} {V.pp} {comp}"; wrongd = f"{wh} {h} {S.mid} {V.pp} {comp}"; bl = (f"{wh} {S.mid} ___ {V.pp} {comp}", h)
    elif t == 'can':
        direct = f"{cap(wh)} can {S.mid} {V.base} {comp}?"; emb = f"{wh} {S.mid} can {V.base} {comp}"; wrongd = f"{wh} can {S.mid} {V.base} {comp}"; bl = (f"{wh} {S.mid} ___ {V.base} {comp}", 'can')
    elif t == 'be':
        b = 'is' if sg else 'are'; ad = rng.pick(["late","ready","tired"]) if wh in ('why','how') else None
        if wh == 'why': ad = rng.pick(["late","angry","tired"])
        elif wh == 'when': ad = None
        w2 = 'where' if ad is None else wh
        if ad is None: direct = f"Where {b} {S.mid}?"; emb = f"where {S.mid} {b}"; wrongd = f"where {b} {S.mid}"; bl = (f"where {S.mid} ___", b)
        else: direct = f"{cap(wh)} {b} {S.mid} {ad}?"; emb = f"{wh} {S.mid} {b} {ad}"; wrongd = f"{wh} {b} {S.mid} {ad}"; bl = (f"{wh} {S.mid} ___ {ad}", b)
    elif t == 'bepast':
        b = 'was' if sg else 'were'; ad = rng.pick(["late","absent","angry"])
        direct = f"Why {b} {S.mid} {ad}?"; emb = f"why {S.mid} {b} {ad}"; wrongd = f"why {b} {S.mid} {ad}"; bl = (f"why {S.mid} ___ {ad}", b)
    elif t == 'yn_pres':
        direct = f"{'Does' if sg else 'Do'} {S.mid} {V.base} {comp}?"; emb = f"{{w}} {S.mid} {V.s if sg else V.base} {comp}"; wrongd = f"{{w}} {'does' if sg else 'do'} {S.mid} {V.base} {comp}"; bl = (f"{{w}} {S.mid} ___ ({V.base}) {comp}", V.s if sg else V.base)
    elif t == 'yn_past':
        direct = f"Did {S.mid} {V.base} {comp}?"; emb = f"{{w}} {S.mid} {V.past} {comp}"; wrongd = f"{{w}} did {S.mid} {V.base} {comp}"; bl = (f"{{w}} {S.mid} ___ ({V.base}) {comp}", V.past)
    elif t == 'yn_be':
        b = 'is' if sg else 'are'; ad = rng.pick(["at home","ready","busy","late"])
        direct = f"{cap(b)} {S.mid} {ad}?"; emb = f"{{w}} {S.mid} {b} {ad}"; wrongd = f"{{w}} {b} {S.mid} {ad}"; bl = (f"{{w}} {S.mid} ___ {ad}", b)
    else:
        sgv = V.s
        direct = f"Who {sgv} {comp}?"; emb = f"who {sgv} {comp}"; wrongd = f"who does {V.base} {comp}"; bl = (f"who ___ ({V.base}) {comp}", sgv)
    return t, direct, emb, wrongd, bl
def gen_ind(level, rng):
    t, direct, emb, wrongd, bl = ind_case(rng)
    yn = t.startswith('yn_')
    stemtype = rng.pick(['q','q','a','a','neg'])
    if yn: w = rng.pick(['if','if','whether'])
    stem = rng.pick(STEMS_Q) if stemtype == 'q' else rng.pick(STEMS_A)
    end = '?' if stemtype == 'q' else '.'
    if yn:
        full = f"{stem} {emb.format(w=w)}{end}"; fulls = [f"{stem} {emb.format(w='if')}{end}", f"{stem} {emb.format(w='whether')}{end}"]
        wr = f"{stem} {wrongd.format(w=w)}{end}"
        blank = f"{stem} {bl[0].format(w=w)}{end}"
    else:
        full = f"{stem} {emb}{end}"; fulls = [full]; wr = f"{stem} {wrongd}{end}"; blank = f"{stem} {bl[0]}{end}" + {'pc':' (be, present continuous)','perf':' (have, present perfect)','can':' (can)','be':' (be, present)','bepast':' (be, past)'}.get(t, '')
    if level == 'easy':
        if yn: return line(f"{stem} ___ {emb.split(' ',1)[1]}{end} (if / whether)" if False else f"{stem} ___ {emb.format(w='').strip().replace('  ',' ')}{end} (if / whether)", ['if','whether'])
        return line(blank, [bl[1]])
    if level == 'medium':
        if yn and rng.pick([0,1]): return line(f"{stem} ___ {emb.format(w='').strip()}{end} (if / whether)", ['if','whether'])
        return line(blank, [bl[1]])
    k = rng.pick(['rewrite','rewrite','fix','fix'])
    if k == 'fix':
        if wr == full: return None
        return line('Correct the mistake: ' + wr, fulls)
    return line(f"Start with '{stem}': {direct}", fulls)
# ====== so / neither / too / either ======
def sn_case(rng):
    S1 = rng.pick([s for s in SGq if s.pron != 'I' or True]); S2 = rng.pick([s for s in SGq if s.text != S1.text])
    return S1, S2
def aux_of(S, kind, neg):
    p = pr_sub(S)
    if kind == 'bepres': return {'I':'am','you':'are','he':'is','she':'is','we':'are','they':'are'}[p]
    if kind == 'bepast': return 'was' if p in ('I','he','she') else 'were'
    if kind == 'dopres': return 'does' if p in ('he','she') else 'do'
    if kind == 'dopast': return 'did'
    if kind == 'perf': return 'has' if p in ('he','she') else 'have'
    if kind == 'can': return 'can'
    if kind == 'will': return 'will'
    return 'should'
def gen_sn(level, rng):
    S1 = rng.pick(SGq); S2 = rng.pick([s for s in SGq if s.text != S1.text and not (s.pron == S1.pron)])
    neg = rng.pick([False, True]); kind = rng.pick(['bepres','bepast','dopres','dopast','perf','can','will','should'])
    V = rng.pick([v for v in VERBS if not v.ach]); comp = rng.pick(V.comps); adj = rng.pick(ADJ[:9])
    if S1.pron == 'i' and kind == 'dopres': pass
    st = tag_stmt(S1, kind, neg, V, comp, adj) + '.'
    a2 = aux_of(S2, kind, neg)
    n2 = a2 + ("n't" if not (a2 == 'am') else '') if neg else a2
    if neg and a2 == 'am': n2 = 'am not'
    if kind == 'can' and neg: n2 = "can't"
    if kind == 'will' and neg: n2 = "won't"
    if kind == 'should' and neg: n2 = "shouldn't"
    if kind == 'dopres' and neg: n2 = ("doesn't" if a2 == 'does' else "don't")
    sub2 = S2.text if S2.proper or S2.text == 'I' else S2.mid
    w = 'Neither' if neg else 'So'
    if neg and a2 == 'am': aux_alt = None
    variants = rng.pick(['sn','sn','tooeither'])
    if variants == 'sn':
        resp = f"{w} {a2} {sub2}."
        alt = [f"{w} {a2} {sub2}.", f"Nor {a2} {sub2}."] if neg else [f"{w} {a2} {sub2}."]
        if level == 'easy': return line(f"{st} ___ {a2} {sub2}. (so / neither)", ['neither','nor'] if neg else ['so'])
        if level == 'medium': return line(f"{st} {w} ___ {sub2}.", [a2])
        k = rng.pick(['fix','fix','write'])
        if k == 'fix':
            wrong = f"{'So' if neg else 'Neither'} {a2} {sub2}."
            return line('Correct the mistake: ' + f"{st} {wrong}", [f"{st} {x}" for x in alt])
        tooe = f"{sub2[0].upper()+sub2[1:] if S2.proper or True else sub2} {n2} {'either' if neg else 'too'}."
        tooe2 = f"{sub2[0].upper()+sub2[1:]} {n2}, {'either' if neg else 'too'}."
        pj = pr_sub(S2); pj = 'I' if pj == 'I' else pj.lower()
        if pj != sub2:
            alt = alt + [x.replace(f" {sub2}.", f" {pj}.") for x in alt]
        return line(f"Reply with '{'neither' if neg else 'so'}', using {_lab(S2)} as the subject: {st}", alt)
    # too / either
    resp = f"{sub2[0].upper()+sub2[1:]} {n2} {'either' if neg else 'too'}."
    resp_alt = f"{sub2[0].upper()+sub2[1:]} {n2}, {'either' if neg else 'too'}."
    if level == 'easy': return line(f"{st} {sub2[0].upper()+sub2[1:]} {n2} ___. (too / either)", ['either'] if neg else ['too'])
    if level == 'medium': return line(f"{st} {sub2[0].upper()+sub2[1:]} ___ {'either' if neg else 'too'}.", [n2, n2.replace("n't"," not") if "n't" in n2 and n2 not in ("can't","won't") else n2])
    k = rng.pick(['fix','write'])
    if k == 'fix':
        wrong = f"{sub2[0].upper()+sub2[1:]} {n2} {'too' if neg else 'either'}."
        return line('Correct the mistake: ' + f"{st} {wrong}", [f"{st} {resp}", f"{st} {resp_alt}"])
    pj = pr_sub(S2); pj = 'I' if pj == 'I' else pj.lower()
    extra = []
    if pj.lower() != sub2.lower():
        extra = [x.replace(sub2[0].upper() + sub2[1:], pj[0].upper() + pj[1:], 1) for x in (resp, resp_alt)]
    return line(f"Reply with '{'either' if neg else 'too'}', using {_lab(S2)} as the subject: {st}", [resp, resp_alt] + extra)
def gen_misc3_jobs(C):
    return {'question-tags': lambda: gen_topic(gen_tag, C, 104),
            'indirect-questions': lambda: gen_topic(gen_ind, C, 105),
            'so-neither-too-and-either': lambda: gen_topic(gen_sn, C, 106)}
