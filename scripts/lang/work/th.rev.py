_m = {}
import os
for _l in open(os.path.join('/home/claude/repo_clone/scripts/lang/work', 'th.map.txt'), encoding='utf-8'):
    if ' = ' in _l:
        _a, _b = _l.rstrip('\n').split(' = ', 1); _m[_a.strip()] = _b.strip()
def rev(s):
    s = s.strip()
    if s not in _m: raise SystemExit('TH MISSING: ' + s)
    return _m[s]
