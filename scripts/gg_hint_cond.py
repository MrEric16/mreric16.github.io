# One-off: put the conditional name in brackets on every hand-written item of conditionals-which-type (no "real/unreal" wording).
import re, sys
P = 'scripts/grammar-bank-src/t24.txt'
src = open(P, encoding='utf-8').read().split('\n')
REN = [("Make it likely (first conditional):", "Change to the first conditional:"), ("Make it past (third conditional):", "Change to the third conditional:"),
       ("Make it general (zero conditional):", "Change to the zero conditional:"), ("Make it unreal (second conditional):", "Change to the second conditional:")]
HAS = re.compile(r'\((zero|first|second|third) conditional\)\s*$')
PP = r"left|known|taken|told|gone|seen|come|given|bought|brought|done|found|made|won|lost|met|heard|written|eaten|been|flown|driven|spoken|chosen|sold|paid|taught|had|forgotten|broken|begun|run|read|put|got|gotten|felt|kept|thought"
def classify(t):
    t = t.lower()
    if re.search(r"would (not )?have|wouldn't have|'d have|would you have|hadn't|had not|\bhad (not )?(\w+ed|%s)\b" % PP, t): return 'third'
    if re.search(r"\bwould\b|'d\b|\bwere\b|wasn't|\bwas\b|weren't|\bcould\b|wouldn't", t): return 'second'
    if re.search(r"\bwill\b|'ll\b|won't|\bgoing to\b", t): return 'first'
    return 'zero'
out = []; skipped = []
section = False
for ln in src:
    for a, b in REN: ln = ln.replace(a, b)
    if ln.startswith('@') or not ln.strip() or ' => ' not in ln:
        out.append(ln); continue
    q, a = ln.split(' => ', 1)
    if HAS.search(q) or q.startswith('Change to the') or q.startswith('Rewrite with I wish'):
        out.append(ln); continue
    ans = ' '.join(g.split('|')[0] for g in a.split(' ;; '))
    basis = ans if re.match(r'(Correct the mistake|Make a|Rewrite)', q) else q.replace('___', ' ') + ' ' + ans
    if re.match(r'(Correct the mistake|Make a|Rewrite)', q) is None and False: pass
    typ = classify(basis)
    out.append(f"{q} ({typ} conditional) => {a}")
open(P, 'w', encoding='utf-8').write('\n'.join(out))
