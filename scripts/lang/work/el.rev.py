import unicodedata
def rev(s):
    t = unicodedata.normalize('NFD', s.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn' or c == '̈')
    t = unicodedata.normalize('NFC', t)
    # diaeresis breaks digraphs: mark
    t = t.replace('ϊ', 'i\x00').replace('ϋ', 'y\x00')
    T = [('αυ','af'),('ευ','ef'),('ου','ou'),('αι','e'),('ει','i'),('οι','i'),('υι','i'),('γγ','ng'),('γκ','g'),('γχ','nch'),('μπ','b'),('ντ','d'),('τσ','ts'),('τζ','dz'),
         ('θ','th'),('χ','ch'),('ψ','ps'),('ξ','x'),('α','a'),('β','v'),('γ','g'),('δ','d'),('ε','e'),('ζ','z'),('η','i'),('ι','i'),('κ','k'),('λ','l'),('μ','m'),('ν','n'),('ο','o'),('π','p'),('ρ','r'),('σ','s'),('ς','s'),('τ','t'),('υ','i'),('φ','f'),('ω','o')]
    # voiced contexts for αυ/ευ
    out = []; i = 0
    voiced = set('αεηιουωβγδζλμνρ') | set('\x00')
    while i < len(t):
        if t.startswith('αυ', i) or t.startswith('ευ', i):
            nxt = t[i+2] if i+2 < len(t) else ' '
            base = 'a' if t[i] == 'α' else 'e'
            unv = nxt in 'κξπςστφχψθ '
            out.append(base + ('f' if unv else 'v')); i += 2; continue
        if t[i] == 'γ' and not t.startswith(('γγ','γκ','γχ'), i) and i+1 < len(t) and (t[i+1] in 'ειηυ' or t.startswith(('αι','οι'), i+1)):
            out.append('y'); i += 1; continue
        for a, b in T:
            if t.startswith(a, i):
                # μπ/ντ at start -> b/d; inside word -> mb/nd
                if a in ('μπ','ντ') and i > 0 and t[i-1].isalpha():
                    b = 'mb' if a == 'μπ' else 'nd'
                out.append(b); i += len(a); break
        else:
            out.append(t[i]); i += 1
    return ''.join(out).replace('\x00', '').replace(';', '?').replace('·', ';')
