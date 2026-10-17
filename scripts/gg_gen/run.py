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
NAMES = {'comparatives':'Comparatives','superlatives':'Superlatives','comparatives-or-superlatives':'Comparatives or superlatives',
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
