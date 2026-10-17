import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tense import gen_tense_topic
from ortopics import gen_or_topic
from be import gen_be_topic
from future import gen_wg_topic, gen_all_topic
from cond import gen_cond_topic
N = int(os.environ.get('GG_N', 200))
C = {'easy': N, 'medium': N, 'hard': N}
jobs = {
 'present-simple-be': lambda: gen_be_topic(False, C, 11),
 'present-simple-other': lambda: gen_tense_topic('ps','ps',C,12),
 'present-continuous': lambda: gen_tense_topic('pc','pc',C,13),
 'present-simple-vs-continuous': lambda: gen_or_topic('ps_pc',C,14),
 'past-simple-be': lambda: gen_be_topic(True, C, 15),
 'past-simple-other': lambda: gen_tense_topic('pas','pas',C,16),
 'past-continuous': lambda: gen_tense_topic('pac','pac',C,17),
 'past-simple-vs-continuous': lambda: gen_or_topic('pas_pac',C,18),
 'present-perfect-simple': lambda: gen_tense_topic('pp','pp',C,19),
 'present-perfect-continuous': lambda: gen_tense_topic('ppc','ppc',C,20),
 'present-perfect-simple-vs-continuous': lambda: gen_or_topic('pp_ppc',C,21),
 'present-perfect-vs-past-simple': lambda: gen_or_topic('pp_pas',C,22),
 'past-perfect': lambda: gen_tense_topic('pap','pap',C,23),
 'future-will': lambda: gen_tense_topic('fw','fw',C,24),
 'future-going-to': lambda: gen_tense_topic('fg','fg',C,25),
 'future-present-continuous': lambda: gen_tense_topic('fpc','fpc',C,26),
 'future-perfect': lambda: gen_tense_topic('fp','fp',C,107),
 'future-perfect-continuous': lambda: gen_tense_topic('fpn','fpn',C,108),
 'future-perfect-simple-vs-continuous': lambda: gen_or_topic('fp_fpn',C,109),
 'past-perfect-continuous': lambda: gen_tense_topic('papn','papn',C,110),
 'past-perfect-simple-vs-continuous': lambda: gen_or_topic('pap_papn',C,111),
 'past-perfect-vs-past-simple': lambda: gen_or_topic('pap_pas',C,112),
 'present-perfect-vs-past-perfect': lambda: gen_or_topic('pp_pap',C,113),
 'future-will-vs-going-to': lambda: gen_wg_topic(C,27),
 'future-all-forms': lambda: gen_all_topic(C,28),
 'zero-conditional': lambda: gen_cond_topic('zero',C,29),
 'first-conditional': lambda: gen_cond_topic('first',C,30),
 'second-conditional': lambda: gen_cond_topic('second',C,31),
 'third-conditional': lambda: gen_cond_topic('third',C,32),
 'conditionals-which-type': lambda: gen_cond_topic(None,C,33,which=True),
}
try:
    from passive import gen_passive_jobs; jobs.update(gen_passive_jobs(C))
except ImportError: pass
try:
    from reported import gen_reported_jobs; jobs.update(gen_reported_jobs(C))
except ImportError: pass
try:
    from modals import gen_modal_jobs; jobs.update(gen_modal_jobs(C))
except ImportError: pass
try:
    from stative import gen_stative_jobs; jobs.update(gen_stative_jobs(C))
except ImportError: pass
try:
    from relcl import gen_rel_jobs; jobs.update(gen_rel_jobs(C))
except ImportError: pass
try:
    from gerinf import gen_gi_jobs; jobs.update(gen_gi_jobs(C))
except ImportError: pass
try:
    from comp import gen_comp_jobs; jobs.update(gen_comp_jobs(C))
except ImportError: pass
try:
    from asas import gen_asas_jobs; jobs.update(gen_asas_jobs(C))
except ImportError: pass
try:
    from art import gen_art_jobs; jobs.update(gen_art_jobs(C))
except ImportError: pass
try:
    from quant import gen_q_jobs; jobs.update(gen_q_jobs(C))
except ImportError: pass
try:
    from prep import gen_prep_jobs; jobs.update(gen_prep_jobs(C))
except ImportError: pass
try:
    from usedto import gen_used_jobs; jobs.update(gen_used_jobs(C))
except ImportError: pass
try:
    from misc2 import gen_misc2_jobs; jobs.update(gen_misc2_jobs(C))
except ImportError: pass
try:
    from misc3 import gen_misc3_jobs; jobs.update(gen_misc3_jobs(C))
except ImportError: pass
try:
    from nar import gen_nar_jobs; jobs.update(gen_nar_jobs(C))
except ImportError: pass
try:
    from linkers import gen_link_jobs; jobs.update(gen_link_jobs(C))
except ImportError: pass
try:
    from condconn import gen_cc_jobs; jobs.update(gen_cc_jobs(C))
except ImportError: pass
try:
    from repverb import gen_rv_jobs; jobs.update(gen_rv_jobs(C))
except ImportError: pass
try:
    from inversion import gen_inv_jobs; jobs.update(gen_inv_jobs(C))
except ImportError: pass
try:
    from participle import gen_part_jobs; jobs.update(gen_part_jobs(C))
except ImportError: pass
NAMES = {'linkers':'Linkers (although, despite, because, so, however)','conditional-connectors':'Conditional connectors (unless, as long as, provided, otherwise, in case)','passive-reporting-verbs':'Passive with reporting verbs (it is said that / he is said to)','inversion':'Inversion and emphasis (Never have I, Not only, Hardly)','participle-clauses':'Participle clauses (-ing, -ed, having done)','narrative-tenses':'Narrative tenses (past simple, past continuous, past perfect)','past-perfect-continuous':'Past perfect continuous','past-perfect-simple-vs-continuous':'Past perfect simple or continuous','past-perfect-vs-past-simple':'Past perfect or past simple','present-perfect-vs-past-perfect':'Present perfect or past perfect','future-perfect':'Future perfect simple','future-perfect-continuous':'Future perfect continuous','future-perfect-simple-vs-continuous':'Future perfect simple or continuous','question-tags':'Question tags','indirect-questions':'Indirect questions','so-neither-too-and-either':'so, neither, too and either','causative-have-something-done':'Causative (have / get something done)','wish-and-if-only':'wish and If only','phrasal-verbs-separable-and-inseparable':'Phrasal verbs (separable and inseparable)','prepositions-of-time':'Prepositions of time (at, on, in)','prepositions-of-place':'Prepositions of place','prepositions-of-movement':'Prepositions of movement','used-to-would-and-be-used-to':'used to, would and be used to','articles':'Articles (a, an, the, no article)','quantifiers':'Quantifiers (some, any, much, many, few, little, enough)','comparatives':'Comparatives','superlatives':'Superlatives','comparatives-or-superlatives':'Comparatives or superlatives',
         'as-as-too-and-enough':'as ... as, too and enough','relative-clauses-defining':'Relative clauses (defining: who, which, that, whose, where)',
         'relative-clauses-non-defining':'Relative clauses (non-defining)',
         'gerunds-and-infinitives':'Gerunds and infinitives'}
only = sys.argv[1:]
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
outdir = os.path.join(root, 'grammar-bank-src')
for f in os.listdir(outdir):
    if f.startswith('g_') and (not only or f[2:-4] in only): os.remove(os.path.join(outdir, f))
for tid, fn in jobs.items():
    if only and tid not in only: continue
    out = fn()
    with open(os.path.join(outdir, f'g_{tid}.txt'), 'w', encoding='utf-8') as fh:
        fh.write(f'@topic {tid} | {NAMES.get(tid, tid)}\n')
        for lv in ('easy','medium','hard'):
            fh.write(f'@{lv}\n' + '\n'.join(out[lv]) + '\n')
    print(tid, [len(out[l]) for l in ('easy','medium','hard')])
