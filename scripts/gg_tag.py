"""Turns fixed names / places / jobs in bank items into {x0} slot tokens (x = m f s c k l p j) so the
page can fill them with fresh random values from data/grammar/pools.json on every draw."""
import re
M = ['Tom', 'Jasur', 'Aziz', 'Ali', 'Karim', 'Sardor']
F = ['Anna', 'Dilya', 'Dilnoza', 'Malika', 'Sara']
SUR = ['Karimov']
CITY = ['Dubai', 'Samarkand', 'Tashkent', 'Bukhara', 'Paris', 'London', 'Rome', 'Moscow', 'Beijing']
CTRY = ['Spain', 'Uzbekistan', 'Kazakhstan', 'Russia', 'Turkey', 'Japan', 'Egypt', 'Brazil', 'China', 'Italy', 'India', 'Canada']
LANG = ['Spanish', 'French', 'Russian', 'Chinese', 'Uzbek', 'Italian', 'Korean']
PLACE = 'airport|hospital|cinema|restaurant|library|supermarket|bank|museum|station|gym|market|bakery|pharmacy|theatre|stadium|park|hotel|office|factory|shop|school|village|university|farm'
JOB = 'teacher|manager|doctor|dentist|mechanic|photographer|architect|tailor|baker|waiter|cleaner|postman|singer|artist|scientist|driver|chef|farmer|nurse|pilot|engineer|lawyer|designer'
FACT = re.compile(r'\b(capital|largest|biggest|famous|population|located|river|mountain|continent|Europe|Asia|Mona Lisa|Leonardo|Bell|Eiffel|invented|painted|wrote|discovered|Mars|Everest|Nile|ocean)\b')
TIED_PLACE = set('borrow borrowed read film movie films patient patients doctor nurse medicine plane flight ticket tickets book books buy bought sell sold cook food eat ate meal lunch dinner breakfast bread cake fish fly flew train bus taxi swim football match game exam teacher lesson student students homework money account loan animal animals cow cows crops wheat farmer milk exercise weights run race paint picture art exhibition salary menu waiter customer customers library suitcase luggage passport'.split())
TIED_JOB = set('homework lesson class classes exam test school student students patient patients teeth tooth car engine photo photos building suit bread table menu street letter parcel song painting experiment bus taxi food meal crops animals medicine hospital clinic mark marks grade grades planes plane flight tickets ticket dinner lunch breakfast kitchen cake'.split())
RX_NAME = re.compile(r"\b(Mr Karimov|Karimov|" + '|'.join(M + F + CITY + CTRY + LANG) + r")\b")
RX_PLACE = re.compile(r"\b(at|in|to|from|near|outside|inside|into|behind|opposite|across|around) the (" + PLACE + r")\b(?! (?:bus|building|door|gate|car|staff|manager|entrance|wall|bench|guard|tour|team|shop|office|station|park|market|school))")
RX_JOB = re.compile(r"\b(The|Our|My|the|our|my) (" + JOB + r")\b")

def tag(q, answers):
    """q: str, answers: list of lists of str -> (q, answers) with tokens"""
    allt = q + ' ' + ' '.join(a for g in answers for a in g)
    words = set(re.findall(r"[a-z']+", allt.lower()))
    hit = set(m.group(1) for m in RX_NAME.finditer(allt))
    cities = [x for x in CITY if x in hit]; ctrys = [x for x in CTRY if x in hit]; langs = [x for x in LANG if x in hit]
    geo_ok = not FACT.search(allt)
    if cities and ctrys: geo_ok = False
    if (ctrys or cities) and langs: geo_ok = False
    if 'Russia' in hit and 'Russian' in hit: geo_ok = False
    slots = {}
    def slot(cat, key):
        d = slots.setdefault(cat, {})
        if key not in d: d[key] = len(d)
        return '{%s%d}' % (cat, d[key])
    def f_name(m):
        t = m.group(1)
        if t in ('Mr Karimov', 'Karimov'):
            return ('Mr ' if t.startswith('Mr') else '') + slot('s', 'K')
        if t in M: return slot('m', t)
        if t in F: return slot('f', t)
        if not geo_ok: return t
        if t in CITY: return slot('c', t)
        if t in CTRY: return slot('k', t)
        return slot('l', t)
    place_ok = not (words & TIED_PLACE) and not FACT.search(allt)
    job_ok = not (words & TIED_JOB)
    def f_place(m): return m.group(1) + ' the ' + slot('p', m.group(2))
    def f_job(m): return m.group(1) + ' ' + slot('j', m.group(2))
    def apply(s):
        s = RX_NAME.sub(f_name, s)
        if place_ok: s = RX_PLACE.sub(f_place, s)
        if job_ok: s = RX_JOB.sub(f_job, s)
        return s
    # first pass over q then answers so slot numbering follows reading order
    q2 = apply(q)
    a2 = [[apply(a) for a in g] for g in answers]
    return q2, a2
