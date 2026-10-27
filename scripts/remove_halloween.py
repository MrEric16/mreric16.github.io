#!/usr/bin/env python3
"""Remove the Halloween 2026 theme. Run from the repo root on/after 1 Nov 2026:  python3 scripts/remove_halloween.py
Then: bump nothing by hand (this bumps sw.js), test the home page loads, commit, push."""
import glob, re, sys
def cut(s, start, end, keep_end=False):
    i = s.index(start); j = s.index(end, i) + (0 if keep_end else len(end))
    # also swallow the trailing newline
    if s[j:j+1] == '\n': j += 1
    return s[:i].rstrip(' ') + s[j:]
def sub1(s, a, b):
    assert s.count(a) == 1, ('not found once', a[:70], s.count(a))
    return s.replace(a, b)

s = open('index.html', encoding='utf8').read()
# CSS block + JS tap block
s = cut(s, '  /* ===== HALLOWEEN 2026 - self-expires', '/* ===== END HALLOWEEN 2026 ===== */')
s = cut(s, '// ===== HALLOWEEN 2026: tap surprises', '// ===== END HALLOWEEN 2026 =====')
# forced-default block
s = cut(s, '  // HALLOWEEN 2026: every app open starts on Halloween', '  // END HALLOWEEN 2026')
# one-liners tagged HALLOWEEN 2026
out = []
for line in s.split('\n'):
    if 'HALLOWEEN 2026' in line:
        if line.strip().startswith(('const HW_END', 'const HW_ON', "if(HW_ON()) base.unshift", "{ key:'dhalloween'", 'setInterval(() => { if(!HW_ON()', 'try{ if(HW_ON()){ if(key === ')):
            continue
    out.append(line)
s = '\n'.join(out)
s = sub1(s, ",'dhalloween'].forEach(k => document.body.classList.remove('usertheme-' + k));   // HALLOWEEN 2026", "].forEach(k => document.body.classList.remove('usertheme-' + k));")
s = sub1(s, "      if(key === 'ihl' || key === 'dihl' || key === 'dhalloween'){\n        titleEl.style.setProperty('color', key === 'dhalloween' ? '#FF8A1F' : '#FF9E2C', 'important');   // HALLOWEEN 2026 (ternary)",
            "      if(key === 'ihl' || key === 'dihl'){\n        titleEl.style.setProperty('color', '#FF9E2C', 'important');")
s = sub1(s, "    const available = THEME_SWATCHES.filter(t => t.key !== 'dhalloween' || HW_ON());   // HALLOWEEN 2026", "    const available = THEME_SWATCHES;")
# anyone still saved on halloween goes to IHL Dark
s = sub1(s, "  if(THEME_ORDER.indexOf(initial) === -1) initial = 'default';", "  if(initial === 'dhalloween') initial = 'dihl';\n  if(THEME_ORDER.indexOf(initial) === -1) initial = 'default';")
open('index.html', 'w', encoding='utf8').write(s)

# sub-pages
for f in glob.glob('*.html'):
    if f == 'index.html': continue
    t = open(f, encoding='utf8').read()
    u = t.replace(",'dhalloween']", "]")
    u = '\n'.join(l for l in u.split('\n') if 'HALLOWEEN 2026' not in l)
    if u != t:
        u = u.replace("  if(key !== 'default' && key !== 'nationalday' && USER_THEME_KEYS.indexOf(key) === -1){", "  if(key === 'dhalloween') key = 'dihl';\n  if(key !== 'default' && key !== 'nationalday' && USER_THEME_KEYS.indexOf(key) === -1){", 1)
        open(f, 'w', encoding='utf8').write(u)

# theme-pages.css
c = open('theme-pages.css', encoding='utf8').read()
i = c.index('/* ===== HALLOWEEN 2026 - self-expires'); j = c.index('/* ===== END HALLOWEEN 2026 ===== */') + len('/* ===== END HALLOWEEN 2026 ===== */')
open('theme-pages.css', 'w', encoding='utf8').write((c[:i].rstrip() + '\n' + c[j:].lstrip('\n')))

# cache bump
w = open('sw.js', encoding='utf8').read()
m = re.search(r"erics-lounge-v(\d+)", w)
w = w.replace(m.group(0), 'erics-lounge-v%d' % (int(m.group(1)) + 1), 1)
open('sw.js', 'w', encoding='utf8').write(w)

# leftovers check
left = []
for f in glob.glob('*.html') + ['theme-pages.css', 'sw.js']:
    for n, line in enumerate(open(f, encoding='utf8'), 1):
        if re.search(r'dhalloween|HALLOWEEN 2026|hw26Applied|HW_ON|hw-boo', line) and 'dhalloween' not in line.split("key === 'dhalloween'")[0:1][0] + '':
            left.append((f, n, line.strip()[:90]))
for x in left:
    if "key === 'dhalloween'" in x[2] or "initial === 'dhalloween'" in x[2]: continue
    print('LEFTOVER', x)
print('done')
