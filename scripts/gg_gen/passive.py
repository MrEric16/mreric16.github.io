from lib import *
from cond import FORMS_C
PRAW = """
the cleaner|clean|the rooms|pl
the chef|cook|the meals|pl
a thief|steal|my bike|sg
the storm|break|the window|sg
the teacher|check|the homework|sg
the workers@pl|build|the bridge|sg
farmers@pl|grow|rice|sg
the mechanic|repair|the car|sg
the manager|sign|the letters|pl
the company|produce|these cars|pl
my mum|bake|the bread|sg
the children@pl|eat|all the cakes|pl
the postman|deliver|the parcels|pl
the police@pl|arrest|the thief|sg
the students@pl|write|the essays|pl
the artist|paint|the picture|sg
the council|clean|the streets|pl
the doctor|examine|the patients|pl
the gardener|water|the flowers|pl
the secretary|send|the emails|pl
the bakery|sell|fresh bread|sg
the waiter|serve|the meals|pl
the electrician|fix|the lights|pl
the director|announce|the results|pl
the team|win|the cup|sg
the workers@pl|paint|the walls|pl
the coach|train|the players|pl
the museum|display|the paintings|pl
the girl|draw|the map|sg
the boy|break|the plate|sg
the architect|design|the building|sg
the printer|print|the tickets|pl
the dog|bite|the postman|sg
the librarian|check|the books|pl
the committee|choose|the winner|sg
the machine|make|the parts|pl
the author|write|the book|sg
the singer|sing|the song|sg
the scientist|discover|a new planet|sg
the shop assistant|wrap|the gifts|pl
the government|build|new roads|pl
the baker|bake|the cakes|pl
the tailor|make|the suits|pl
the porter|carry|the bags|pl
the farmer|pick|the apples|pl
the school|hold|the exams|pl
the translator|translate|the documents|pl
the photographer|take|the photos|pl
the staff@pl|serve|breakfast|sg
the mayor|open|the new library|sg
the girls@pl|decorate|the hall|sg
the vet|treat|the animals|pl
the publisher|print|the books|pl
the technician|repair|the computers|pl
the minister|sign|the agreement|sg
the neighbour|feed|the cat|sg
the cleaners@pl|sweep|the floors|pl
the guards@pl|lock|the gates|pl
the nurse|wash|the sheets|pl
the firefighters@pl|save|the family|sg
the lifeguard|rescue|the swimmer|sg
the plumber|fix|the tap|sg
the organisers@pl|cancel|the concert|sg
the referee|stop|the match|sg
the driver|carry|the passengers|pl
the company|employ|new workers|pl
the owner|sell|the house|sg
the doctor|give|the medicine|sg
the agency|book|the flights|pl
the mechanic|check|the engines|pl
the pupils@pl|plant|the trees|pl
the flood|destroy|many houses|pl
the fire|destroy|the old factory|sg
the committee|approve|the plan|sg
the editor|correct|the mistakes|pl
the judge|announce|the verdict|sg
the waiters@pl|set|the tables|pl
the farmers@pl|sell|the vegetables|pl
the builders@pl|finish|the house|sg
the men@pl|carry|the boxes|pl
the cook|prepare|the soup|sg
the rain|ruin|the picnic|sg
the artists@pl|design|the posters|pl
the girl|win|the prize|sg
the thieves@pl|take|the jewellery|sg
the scouts@pl|clean|the park|sg
the teacher|mark|the tests|pl
the guide|show|the museum|sg
"""
EXTRA = {
 'steal':('steals','stole','stolen','stealing'),'break':('breaks','broke','broken','breaking'),'check':('checks','checked','checked','checking'),
 'build':('builds','built','built','building'),'grow':('grows','grew','grown','growing'),'repair':('repairs','repaired','repaired','repairing'),
 'sign':('signs','signed','signed','signing'),'produce':('produces','produced','produced','producing'),'bake':('bakes','baked','baked','baking'),
 'eat':('eats','ate','eaten','eating'),'deliver':('delivers','delivered','delivered','delivering'),'arrest':('arrests','arrested','arrested','arresting'),
 'write':('writes','wrote','written','writing'),'paint':('paints','painted','painted','painting'),'examine':('examines','examined','examined','examining'),
 'water':('waters','watered','watered','watering'),'send':('sends','sent','sent','sending'),'sell':('sells','sold','sold','selling'),'serve':('serves','served','served','serving'),
 'fix':('fixes','fixed','fixed','fixing'),'announce':('announces','announced','announced','announcing'),'win':('wins','won','won','winning'),'train':('trains','trained','trained','training'),
 'display':('displays','displayed','displayed','displaying'),'draw':('draws','drew','drawn','drawing'),'design':('designs','designed','designed','designing'),
 'print':('prints','printed','printed','printing'),'bite':('bites','bit','bitten','biting'),'choose':('chooses','chose','chosen','choosing'),'make':('makes','made','made','making'),
 'sing':('sings','sang','sung','singing'),'land':('lands','landed','landed','landing'),'discover':('discovers','discovered','discovered','discovering'),
 'wrap':('wraps','wrapped','wrapped','wrapping'),'carry':('carries','carried','carried','carrying'),'pick':('picks','picked','picked','picking'),'hold':('holds','held','held','holding'),
 'translate':('translates','translated','translated','translating'),'take':('takes','took','taken','taking'),'decorate':('decorates','decorated','decorated','decorating'),
 'treat':('treats','treated','treated','treating'),'employ':('employs','employed','employed','employing'),'give':('gives','gave','given','giving'),'book':('books','booked','booked','booking'),
 'plant':('plants','planted','planted','planting'),'ruin':('ruins','ruined','ruined','ruining'),'destroy':('destroys','destroyed','destroyed','destroying'),
 'approve':('approves','approved','approved','approving'),'correct':('corrects','corrected','corrected','correcting'),'rescue':('rescues','rescued','rescued','rescuing'),
 'save':('saves','saved','saved','saving'),'open':('opens','opened','opened','opening'),'cancel':('cancels','cancelled','cancelled','cancelling'),'stop':('stops','stopped','stopped','stopping'),
 'lock':('locks','locked','locked','locking'),'sweep':('sweeps','swept','swept','sweeping'),'wash':('washes','washed','washed','washing'),'feed':('feeds','fed','fed','feeding'),
 'clean':('cleans','cleaned','cleaned','cleaning'),'cook':('cooks','cooked','cooked','cooking'),'set':('sets','set','set','setting'),'finish':('finishes','finished','finished','finishing'),
 'mark':('marks','marked','marked','marking'),'show':('shows','showed','shown','showing'),'park':('parks','parked','parked','parking'),'learn':('learns','learned','learned','learning'),
 'prepare':('prepares','prepared','prepared','preparing'),'lend':('lends','lent','lent','lending'),
}
F = dict(FORMS_C); F.update(EXTRA)
class P: pass
def sn(tok):
    if tok.endswith('@pl'): return tok[:-3],'pl'
    return tok,'sg'
ITEMS = []
for ln in PRAW.strip().split('\n'):
    a,v,o,n = ln.split('|'); at,an = sn(a)
    assert v in F, v
    ITEMS.append(dict(agent=at, anum=an, verb=v, obj=o, onum=n))

def be_p(n, past=False): return ('was' if n=='sg' else 'were') if past else ('is' if n=='sg' else 'are')
def have_p(n): return 'has' if n=='sg' else 'have'
def P_group(tn, it, neg=False):
    v = it['verb']; s3,past,pp,ing = F[v]; n = it['onum']
    if tn == 'ps':
        b = be_p(n); return ([f"{b}n't {pp}", f"{b} not {pp}"] if neg else [f"{b} {pp}"])
    if tn == 'pas':
        b = be_p(n,True); return ([f"{b}n't {pp}", f"{b} not {pp}"] if neg else [f"{b} {pp}"])
    if tn == 'pc':
        b = be_p(n); return ([f"{b}n't being {pp}", f"{b} not being {pp}"] if neg else [f"{b} being {pp}"])
    if tn == 'pcp':
        b = be_p(n,True); return ([f"{b}n't being {pp}", f"{b} not being {pp}"] if neg else [f"{b} being {pp}"])
    if tn == 'pf':
        h = have_p(n); return ([f"{h}n't been {pp}", f"{h} not been {pp}"] if neg else [f"{h} been {pp}"])
    if tn == 'pap':
        return ["hadn't been "+pp, "had not been "+pp] if neg else ["had been "+pp]
    if tn == 'fw':
        return ["won't be "+pp, "will not be "+pp] if neg else ["will be "+pp, "'ll be "+pp]
    raise KeyError(tn)
def A_group(tn, it):
    v = it['verb']; s3,past,pp,ing = F[v]; an = it['anum']
    if tn == 'ps': return s3 if an=='sg' else v
    if tn == 'pas': return past
    if tn == 'pc': return f"{be_p(an)} {ing}"
    if tn == 'pcp': return f"{be_p(an,True)} {ing}"
    if tn == 'pf': return f"{have_p(an)} {pp}"
    if tn == 'pap': return f"had {pp}"
    if tn == 'fw': return f"will {v}"
def Q_parts(tn, it):
    v = it['verb']; s3,past,pp,ing = F[v]; n = it['onum']
    return {'ps':(be_p(n),pp),'pas':(be_p(n,True),pp),'pc':(be_p(n),f"being {pp}"),'pcp':(be_p(n,True),f"being {pp}"),
            'pf':(have_p(n),f"been {pp}"),'pap':('had',f"been {pp}"),'fw':('will',f"be {pp}")}[tn]

CUES = {
 'ps': ['every day','every week','every morning','twice a week','every year','on Mondays','every month','every weekend'],
 'pas': ['yesterday','last week','last night','two days ago','last month','in 2015','in 2010','last year','on Monday','three weeks ago'],
 'pc': ['now','at the moment','right now','this week'],
 'pcp': ['when I arrived','when the manager came in','when the bell rang','at six o\'clock yesterday','all morning yesterday','at ten o\'clock last night'],
 'pf': ['already','this week','so far','recently','twice this year'],
 'pap': ['before we arrived','by the time the guests came','before the lesson started','when I got there','before the manager came'],
 'fw': ['tomorrow','next week','next month','next year','by Friday','soon','on Monday','tonight','in two days'],
}
MODALS = [('must','must'),('should','should'),('can','can'),('could','could'),('may','may'),('might','might'),('has to',None),('ought to',None),("can't",None),("mustn't",None)]
MCUE = ['today','tomorrow','before Friday','by the end of the week','immediately','as soon as possible','this week','before the exam']

def cuefor(tn, pol, rng):
    pool = CUES[tn]
    if tn == 'pf' and pol != 'aff': pool = ['yet','this week','so far','recently']
    if tn == 'pf' and pol == 'q': pool = ['yet','this week','so far']
    return rng.pick(pool)
def NP(it): return it['obj']
def by(it, rng, use): return f" by {it['agent']}" if use else ''
def passive_sentence(tn, it, group, cue, agent=False, lead=''):
    core = ' '.join(x for x in [cap(NP(it)), group, ('by ' + it['agent']) if agent else '', cue] if x) + '.'
    return core
def passive_q(tn, it, aux, rest, cue, agent=False):
    if tn == 'pf' and cue == 'yet': pass
    return cap(' '.join(x for x in [aux, NP(it), rest, ('by ' + it['agent']) if agent else '', cue] if x)) + '?'
def active_sentence(tn, it, cue, neg=False):
    # affirmative active (agent as subject)
    return cap(' '.join(x for x in [it['agent'], A_group(tn,it), it['obj'], cue] if x)) + '.'

def mod_item(rng):
    it = rng.pick(ITEMS); v = it['verb']; s3,past,pp,ing = F[v]
    mdl = rng.pick(['must','should','can','could','may','might','ought to','has to','can\'t'])
    return it, mdl
def modal_text(mdl, n):
    if mdl == 'has to': return 'has to' if n=='sg' else 'have to'
    return mdl

def gen_passive(tn, level, rng):
    it = rng.pick(ITEMS); v = it['verb']; s3,past,pp,ing = F[v]; n = it['onum']
    pol = 'aff'; agent = rng.pick([False,False,True])
    r = rng.r.random()
    if tn == 'mod':
        return gen_modal_passive(it, level, rng)
    if level == 'easy':
        pol = 'aff' if r < .55 else ('neg' if r < .78 else 'q')
        cue = cuefor(tn, pol, rng)
        if pol == 'aff': return line(passive_sentence(tn, it, f"___ ({v})", cue, agent), P_group(tn,it))
        if pol == 'neg': return line(passive_sentence(tn, it, f"___ (not / {v})", cue, agent), P_group(tn,it,True))
        a,rest = Q_parts(tn,it); return line(passive_q(tn, it, '___', rest, cue, agent), [cap(a)])
    if level == 'medium':
        k = rng.pick(['q2','q2','short','two','wh','act2pas','act2pas','neg'])
        if k == 'q2':
            cue = cuefor(tn,'q',rng); a,rest = Q_parts(tn,it)
            return line(passive_q(tn, it, '___', f"___ ({v})", cue, agent), [cap(a)], [rest])
        if k == 'short':
            cue = cuefor(tn,'q',rng); a,rest = Q_parts(tn,it); qq = passive_q(tn, it, cap(a), rest, cue, agent)
            p = 'it' if n=='sg' else 'they'
            if rng.pick([0,1]): return line(f"{qq} Yes, {p} ___.", [a])
            return line(f"{qq} No, {p} ___.", [a+"n't", a+" not"] if a not in ('will',) else ["won't","will not"])
        if k == 'two':
            it2 = rng.pick([x for x in ITEMS if x is not it]); cue = cuefor(tn,'aff',rng)
            if tn in ('pf',) and cue == 'recently': cue = 'so far'
            g1 = P_group(tn,it); g2 = P_group(tn,it2)
            q = cap(f"{NP(it)} ___ ({v}) and {it2['obj']} ___ ({it2['verb']}) {cue}") + '.'
            return line(q, g1, g2)
        if k == 'wh':
            if tn not in ('ps','pas','fw'): return None
            a,rest = Q_parts(tn,it)
            w = {'ps':'How often','pas':'When','fw':'When'}[tn]
            return line(f"{w} ___ {NP(it)} ___ ({v})?", [a], [rest])
        if k == 'neg':
            cue = cuefor(tn,'neg',rng); return line(passive_sentence(tn, it, f"___ (not / {v})", cue, False), P_group(tn,it,True))
        # act2pas
        cue = cuefor(tn,'aff',rng)
        act = active_sentence(tn,it,cue)
        pas = passive_sentence(tn, it, P_group(tn,it)[0], cue, True)
        pas2 = passive_sentence(tn, it, P_group(tn,it)[0], cue, False)
        return line('Make it passive: ' + act, [pas, pas2])
    k = rng.pick(['act2pas','act2pas','pas2act','neg','q','fix','fix','fix'])
    if k == 'act2pas':
        cue = cuefor(tn,'aff',rng); act = active_sentence(tn,it,cue)
        return line('Make it passive: ' + act, [passive_sentence(tn,it,P_group(tn,it)[0],cue,True), passive_sentence(tn,it,P_group(tn,it)[0],cue,False)])
    if k == 'pas2act':
        cue = cuefor(tn,'aff',rng)
        return line('Make it active: ' + passive_sentence(tn,it,P_group(tn,it)[0],cue,True), [active_sentence(tn,it,cue)])
    if k == 'neg':
        cue = cuefor(tn,'aff',rng)
        if cue in ('already',): return None
        return line('Make a negative sentence: ' + passive_sentence(tn,it,P_group(tn,it)[0],cue,False), [passive_sentence(tn,it,P_group(tn,it,True)[0],cue,False)])
    if k == 'q':
        cue = cuefor(tn,'q',rng); a,rest = Q_parts(tn,it)
        s = passive_sentence(tn,it,P_group(tn,it)[0],cue,False)
        return line('Make a question: ' + s, [passive_q(tn,it,cap(a),rest,cue,False)])
    # fix
    cue = cuefor(tn,'aff',rng)
    good = passive_sentence(tn,it,P_group(tn,it)[0],cue,rng.pick([False,True]))
    b = be_p(n); ob = be_p('pl' if n=='sg' else 'sg'); bp = be_p(n,True); obp = be_p('pl' if n=='sg' else 'sg',True)
    wr = {
     'ps': [f"{b} {v}", f"{ob} {pp}", f"{v if n=='pl' else s3}", f"{b} {ing}"],
     'pas': [f"{bp} {v}", f"{obp} {pp}", f"{past}", f"{bp} {ing}"] ,
     'pc': [f"{b} {ing}", f"{b} been {pp}", f"{ob} being {pp}", f"{b} being {v}"],
     'pcp': [f"{bp} {ing}", f"{bp} been {pp}", f"{obp} being {pp}", f"{bp} being {v}"],
     'pf': [f"{have_p(n)} {pp}", f"{have_p(n)} be {pp}", f"{have_p('pl' if n=='sg' else 'sg')} been {pp}", f"{have_p(n)} been {v}"],
     'pap': [f"had {pp}", f"had be {pp}", f"has been {pp}", f"had been {v}"],
     'fw': [f"will {pp}", f"will been {pp}", f"will be {v}", f"will {v}"],
    }[tn]
    for _ in range(6):
        w = rng.pick(wr)
        bad = passive_sentence(tn,it,w,cue,False)
        gold = passive_sentence(tn,it,P_group(tn,it)[0],cue,False)
        if bad != gold and good.replace(' by '+it['agent'],'') == gold:
            return line('Correct the mistake: ' + bad, [gold])
        if bad != gold:
            return line('Correct the mistake: ' + bad, [gold])
    return None

def gen_modal_passive(it, level, rng):
    v = it['verb']; s3,past,pp,ing = F[v]; n = it['onum']
    mdl = rng.pick(['must','should','can','could','may','might','ought to','has to',"can't","mustn't"])
    perf = rng.pick([False,False,False,True]) and mdl in ('must','should','could','may','might',"can't")
    cue = rng.pick(MCUE) if not perf else rng.pick(['yesterday','last week','by now','before Friday'])
    mt = modal_text(mdl, n)
    if perf: grp_ = f"have been {pp}"; blank = 'have been ' + pp
    else: grp_ = f"be {pp}"
    agent = rng.pick([False,False,True])
    def sent(blank_txt, m=mt):
        return cap(' '.join(x for x in [NP(it), m, blank_txt, ('by ' + it['agent']) if agent else '', cue] if x)) + '.'
    r = rng.r.random()
    if level == 'easy':
        if r < .7: return line(sent(f"___ ({v})"), [grp_])
        mt2 = modal_text('can',n) if False else 'can'
        # question with modal
        aux = {'must':'Must','should':'Should','can':'Can','could':'Could','may':'May','might':'Might','ought to':'Should','has to':('Does' if n=='sg' else 'Do'),"can't":'Can',"mustn't":'Must'}[mdl]
        return None
    if level == 'medium':
        k = rng.pick(['aff','aff','neg','act2pas','q'])
        if k == 'aff': return line(sent(f"___ ({v})"), [grp_])
        if k == 'neg':
            m2 = {'must':"mustn't",'should':"shouldn't",'can':"can't",'could':"couldn't",'may':'may not','might':'might not','ought to':'ought not to','has to':None,"can't":'can','mustn\'t':'must'}.get(mdl)
            if not m2 or mdl in ('has to',): return None
            if mdl in ("can't","mustn't"): return None
            return line(sent(f"___ ({v})", m2), [grp_])
        if k == 'act2pas':
            if mdl in ("has to","ought to"): pass
            act_m = mt
            act = cap(' '.join(x for x in [it['agent'], act_m, ('have ' + pp) if perf else v, it['obj'], cue] if x)) + '.'
            ans = cap(' '.join(x for x in [NP(it), mt, grp_, cue] if x)) + '.'
            ans2 = cap(' '.join(x for x in [NP(it), mt, grp_, 'by ' + it['agent'], cue] if x)) + '.'
            return line('Make it passive: ' + act, [ans2, ans])
        # q
        if mdl in ('has to',"can't","mustn't","ought to") or perf: return None
        aux = {'must':'Must','should':'Should','can':'Can','could':'Could','may':'May','might':'Might'}[mdl]
        return line(cap(f"{aux} {NP(it)} ___ ({v}) {cue}?"), [grp_])
    k = rng.pick(['act2pas','act2pas','pas2act','fix','fix','neg','q'])
    if k == 'act2pas':
        act = cap(' '.join(x for x in [it['agent'], mt, ('have ' + pp) if perf else v, it['obj'], cue] if x)) + '.'
        ans = cap(' '.join(x for x in [NP(it), mt, grp_, cue] if x)) + '.'
        ans2 = cap(' '.join(x for x in [NP(it), mt, grp_, 'by ' + it['agent'], cue] if x)) + '.'
        return line('Make it passive: ' + act, [ans2, ans])
    if k == 'pas2act':
        src = cap(' '.join(x for x in [NP(it), mt, grp_, 'by ' + it['agent'], cue] if x)) + '.'
        act = cap(' '.join(x for x in [it['agent'], mt, ('have ' + pp) if perf else v, it['obj'], cue] if x)) + '.'
        return line('Make it active: ' + src, [act])
    if k == 'neg':
        m2 = {'must':"mustn't",'should':"shouldn't",'can':"can't",'could':"couldn't",'may':'may not','might':'might not'}.get(mdl)
        if not m2: return None
        src = sent(grp_); ans = sent(grp_, m2)
        return line('Make a negative sentence: ' + src, [ans])
    if k == 'q':
        if mdl in ('has to',"can't","mustn't","ought to") or perf: return None
        aux = {'must':'Must','should':'Should','can':'Can','could':'Could','may':'May','might':'Might'}[mdl]
        return line('Make a question: ' + sent(grp_), [cap(f"{aux} {NP(it)} {grp_} {cue}?")])
    wrongs = [pp, v, f"been {pp}", f"being {pp}", f"{ing}"] if not perf else [f"been {v}", f"be {pp}", pp, f"been {ing}"]
    w = rng.pick(wrongs)
    bad = sent(w)
    if bad == sent(grp_): return None
    return line('Correct the mistake: ' + bad, [sent(grp_)])

def gen_active_or_passive(level, rng):
    it = rng.pick(ITEMS); v = it['verb']; s3,past,pp,ing = F[v]; n = it['onum']
    tn = rng.pick(['ps','pas','pc','pf','fw','pap'])
    cue = cuefor(tn,'aff',rng)
    if tn == 'pf' and cue == 'recently': cue = 'so far'
    # active/passive forms
    act = A_group(tn,it); pas = P_group(tn,it)
    k_act = rng.pick([True, False])
    if tn == 'pc': cue = rng.pick(['now','at the moment','right now'])
    ag = it['agent']; ob = it['obj']
    def active_blank(): return cap(' '.join([ag, f"___ ({v})", ob, cue])) + '.', [ [act] ]
    def passive_blank(): return cap(' '.join([ob, f"___ ({v})", 'by ' + ag, cue])) + '.', [ pas ]
    r = rng.r.random()
    if level in ('easy','medium'):
        if k_act: q,a = active_blank()
        else: q,a = passive_blank()
        # active needs raw form: A_group gives a string
        if k_act: return line(q,[act])
        return line(q,pas)
    k = rng.pick(['topas','toact','fix','neg'])
    if k == 'topas':
        src = cap(' '.join([ag, act, ob, cue])) + '.'
        return line('Make it passive: ' + src, [cap(' '.join([ob, pas[0], 'by ' + ag, cue])) + '.', cap(' '.join([ob, pas[0], cue])) + '.'])
    if k == 'toact':
        src = cap(' '.join([ob, pas[0], 'by ' + ag, cue])) + '.'
        return line('Make it active: ' + src, [cap(' '.join([ag, act, ob, cue])) + '.'])
    if k == 'neg':
        if tn == 'ps' or True:
            if k_act: return None
            src = cap(' '.join([ob, pas[0], 'by ' + ag, cue])) + '.'
            return line('Make a negative sentence: ' + src, [cap(' '.join([ob, P_group(tn,it,True)[0], 'by ' + ag, cue])) + '.'])
    # fix: passive written as active or active written as passive
    if k_act:
        bad = cap(' '.join([ag, pas[0], ob, cue])) + '.'
        return line('Correct the mistake: ' + bad, [cap(' '.join([ag, act, ob, cue])) + '.'])
    bad = cap(' '.join([ob, act, 'by ' + ag, cue])) + '.'
    return line('Correct the mistake: ' + bad, [cap(' '.join([ob, pas[0], 'by ' + ag, cue])) + '.'])

def gen_topic(fn, counts, seed):
    rng = Rng(seed); out = {}
    for level, n in counts.items():
        seen, lines, tries = set(), [], 0
        while len(lines) < n and tries < n * 200:
            tries += 1
            l = fn(level, rng)
            if not l or bad_prompt(l): continue
            q = l.split(' => ')[0]
            if q in seen: continue
            seen.add(q); lines.append(l)
        out[level] = lines
    return out
def gen_passive_jobs(C):
    j = {}
    for i,(tid,tns) in enumerate([('passive-present-simple',['ps']),('passive-past-simple',['pas']),('passive-continuous',['pc','pcp']),
                                  ('passive-perfect',['pf','pap']),('passive-future',['fw']),('passive-modals',['mod'])]):
        j[tid] = (lambda tns=tns, i=i: gen_topic(lambda lv, rng: gen_passive(rng.pick(tns), lv, rng), C, 40+i))
    j['active-or-passive'] = lambda: gen_topic(gen_active_or_passive, C, 47)
    return j
