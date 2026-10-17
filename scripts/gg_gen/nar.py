from lib import *
from passive import gen_topic
from ortopics import EVENTS, EVS, pl
from tense import SUBJ
LEADS = ["Yesterday,","Last Saturday,","Last week,","On Monday,","Last night,","Last Friday,","Two days ago,","Last summer,"]
def gen_nar(level, rng):
    S = rng.pick(SUBJ)
    V1, V2, V3, V4 = [rng.pick([v for v in VERBS if not v.ach]) for _ in range(4)]
    c1, c2, c3, c4 = rng.pick(V1.comps), rng.pick(V2.comps), rng.pick(V3.comps), rng.pick(V4.comps)
    ev, evans = rng.pick(EVENTS); ev2, b2, pp2 = rng.pick(EVS)
    lead = rng.pick(LEADS); p = pl(S); P = p[0].upper() + p[1:]
    s1 = f"{lead} {S.mid} ___ ({V1.base}) {c1}."
    if rng.pick([0,1]):
        s2 = f"While {p} ___ ({V2.base}) {c2}, {ev}."
        a2 = [grp('pac',S,V2), [evans]]
    else:
        s2 = f"{P} ___ ({V2.base}) {c2} when {ev}."
        a2 = [grp('pac',S,V2), [evans]]
    if level == 'easy':
        return line(f"{s1} {s2}", grp('pas',S,V1), *a2)
    s3 = f"When {p} ___ ({V3.base}) {c3}, {ev2} ___ (already / {b2})."
    if level == 'medium':
        return line(f"{s1} {s2} {s3}", grp('pas',S,V1), *a2, grp('pas',S,V3), [f"had already {pp2}"])
    s4 = f"{P} ___ (never / {V4.base}) {c4} before that day."
    return line(f"{s1} {s2} {s3} {s4}", grp('pas',S,V1), *a2, grp('pas',S,V3), [f"had already {pp2}"], [f"had never {V4.pp}"])
def gen_nar_jobs(C):
    return {'narrative-tenses': lambda: gen_topic(gen_nar, C, 114)}
