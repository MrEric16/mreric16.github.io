from lib import *
from passive import gen_topic
import re as _re
NOUNS = [("brother","brothers"),("sister","sisters"),("cousin","cousins"),("neighbour","neighbours"),("friend","friends"),("teacher","teachers"),
 ("uncle","uncles"),("aunt","aunts"),("student","students"),("classmate","classmates"),("colleague","colleagues"),("player","players")]
NUMS = ["three","four","five","six","seven","eight","ten","twelve"]
def _cp(s): return s[0].upper() + s[1:]

def gen_det(level, rng):
    sg, pl = rng.pick(NOUNS); V, comp = vcomp(rng)
    k = rng.pick(['both','all','neither','none','either','each','every','whole','allwhole','tq','tn','tneg','tnone','fix','fix'])
    n = rng.pick(NUMS)
    H = {'easy':{'both':' (both / all)','all':' (both / all)','neither':' (neither / none)','none':' (neither / none)'},
         'medium':' (both / all / neither / none / either)', 'hard':''}
    def hint(k):
        if level == 'easy': return H['easy'].get(k, '')
        return H['medium'] if level == 'medium' else ''
    if k == 'both':
        return line(f"I have two {pl}. ___ of them {V.base} {comp}." + hint(k), ['Both'] if False else ['both'])
    if k == 'all':
        return line(f"I have {n} {pl}. ___ of them {V.base} {comp}." + hint(k), ['all'])
    if k == 'neither':
        return line(f"My two {pl} don't {V.base} {comp}. ___ of them {V.s} {comp}." + hint(k), ['neither'])
    if k == 'none':
        return line(f"My {n} {pl} don't {V.base} {comp}. ___ of them {V.base} {comp}." + hint(k), ['none'])
    if k == 'either':
        if level == 'easy': h = ' (either / neither)'
        elif level == 'medium': h = ' (both / either / neither / each / every)'
        else: h = ''
        return line(f"I don't know ___ of my two {pl}." + h, ['either'])
    if k == 'each':
        h = {'easy':' (each / every)','medium':' (each / every / all / both)','hard':''}[level]
        if rng.pick([0,1]):
            return line(f"There are {n} {pl}. ___ of them {V.s} {comp}." + h, ['Each'.lower()])
        return line(f"There are {n} {pl} and ___ {sg} {V.s} {comp}." + h, ['each','every'])
    if k == 'every':
        h = {'easy':' (every / all)','medium':' (every / all / each of / both)','hard':''}[level]
        return line(f"___ {sg} in the room {V.s} {comp}." + h, ['every','each'])
    if k == 'whole':
        h = ' (all / whole)' if level != 'hard' else ''
        thing = rng.pick(['day','week','morning','class','book','cake','film','city','story','team'])
        return line(f"I spent the ___ {thing} thinking about it." + h, ['whole'])
    if k == 'allwhole':
        h = ' (all / whole)' if level != 'hard' else ''
        thing = rng.pick(['day','week','morning','night','year','summer'])
        return line(f"I spent ___ {thing} thinking about it." + h, ['all'])
    # transforms
    if k == 'tq':
        pre = rng.pick(['Both','All'])
        o = 'both' if pre == 'Both' else 'all'
        return line(f"Make a question: {pre} of the {pl} {V.base} {comp}.", [f"Do {o} of the {pl} {V.base} {comp}?"])
    if k == 'tn':
        if level == 'easy': return None
        return line(f"Make a negative sentence with 'Neither': Both of the {pl} {V.base} {comp}.", [f"Neither of the {pl} {V.s} {comp}.", f"Neither of the {pl} {V.base} {comp}."])
    if k == 'tneg':
        if level == 'easy': return None
        return line(f"Make a negative sentence with 'No': Every {sg} {V.s} {comp}.", [f"No {sg} {V.s} {comp}."])
    if k == 'tnone':
        if level == 'easy': return None
        return line(f"Make a negative sentence with 'None': All of the {pl} {V.base} {comp}.", [f"None of the {pl} {V.base} {comp}.", f"None of the {pl} {V.s} {comp}."])
    # fix
    if level != 'hard': return None
    fx = rng.pick(['b1','b2','b3','b4','b5'])
    if fx == 'b1':
        return line(f"Correct the mistake: Both of my {sg} {V.base} {comp}.", [f"Both of my {pl} {V.base} {comp}."])
    if fx == 'b2':
        return line(f"Correct the mistake: Every of my {pl} {V.s} {comp}.", [f"Every one of my {pl} {V.s} {comp}.", f"Each of my {pl} {V.s} {comp}."])
    if fx == 'b3':
        return line(f"Correct the mistake: Neither of my {pl} don't {V.base} {comp}.", [f"Neither of my {pl} {V.s} {comp}.", f"Neither of my {pl} {V.base} {comp}."])
    if fx == 'b4':
        return line(f"Correct the mistake: Each {pl} {V.base} {comp}.", [f"Each {sg} {V.s} {comp}.", f"Each of the {pl} {V.s} {comp}.", f"Each of my {pl} {V.s} {comp}."])
    return line(f"Correct the mistake: All of my {sg} {V.base} {comp}.", [f"All of my {pl} {V.base} {comp}."])

def gen_dets_jobs(C):
    return {'determiners': lambda: gen_topic(gen_det, C, 130)}
