def conv(s):
    V = {'a': 'ا', 'e': 'ە', 'é': 'ې', 'i': 'ى', 'o': 'و', 'u': 'ۇ', 'ö': 'ۆ', 'ü': 'ۈ'}
    C = {'b': 'ب', 'p': 'پ', 't': 'ت', 'j': 'ج', 'x': 'خ', 'd': 'د', 'r': 'ر', 'z': 'ز', 's': 'س', 'f': 'ف', 'q': 'ق', 'k': 'ك', 'g': 'گ', 'l': 'ل', 'm': 'م', 'n': 'ن', 'h': 'ھ', 'w': 'ۋ', 'y': 'ي'}
    D = {'ch': 'چ', 'sh': 'ش', 'zh': 'ژ', 'gh': 'غ', 'ng': 'ڭ'}
    P = {'?': '؟', ',': '،', ';': '؛'}
    s = s.lower(); out = []; i = 0; prev_v = False; start = True
    while i < len(s):
        c = s[i]
        if s[i:i+2] in D: out.append(D[s[i:i+2]]); i += 2; prev_v = False; start = False; continue
        if c in V:
            out.append(('ئ' if (start or prev_v) else '') + V[c]); prev_v = True; start = False
        elif c in C: out.append(C[c]); prev_v = False; start = False
        elif c in P: out.append(P[c]); prev_v = False; start = True
        elif c == ' ': out.append(' '); prev_v = False; start = True
        elif c == "'": pass
        elif c in "-.…()/→": out.append('' if c == '-' else c); prev_v = False; start = c != '-'
        else: out.append(c)
        i += 1
    return ''.join(out)
