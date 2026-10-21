"""Reusable SVG builders for Reading pic and diag questions (theme classes l f s c w g)."""
import math
def _pl(pts, cls='l', extra=''):
    return '<path class="%s" %sd="M%s"/>' % (cls, extra, 'L'.join('%d %d' % (x, y) for x, y in pts))
AX = '<path class="l" d="M22 14V100H150"/>'
GRAPH = {
 'rise': [(22, 92), (60, 74), (100, 50), (146, 22)],
 'fall': [(22, 22), (60, 44), (100, 70), (146, 92)],
 'peak': [(22, 88), (60, 52), (86, 20), (116, 52), (146, 88)],
 'dip': [(22, 24), (60, 56), (86, 88), (116, 56), (146, 24)],
 'plateau': [(22, 90), (56, 56), (84, 30), (116, 30), (146, 30)],
 'level': [(22, 56), (60, 56), (100, 56), (146, 56)],
 'fluct': [(22, 60), (48, 26), (72, 78), (98, 30), (122, 82), (146, 46)],
 'drop': [(22, 30), (60, 30), (88, 30), (100, 86), (146, 86)],
 'sharp': [(22, 84), (70, 82), (100, 80), (122, 30), (146, 24)],
}
def graph(kind):
    return AX + _pl(GRAPH[kind], 'lc')
def bars(vals):
    n = len(vals); w = 120 // n; out = AX
    for i, v in enumerate(vals):
        h = int(v * 80 / max(vals)); out += '<rect class="c" x="%d" y="%d" width="%d" height="%d"/>' % (30 + i * (w + 2), 100 - h, w - 4, h)
    return out
def pie(parts):
    tot = float(sum(parts)); a0 = -math.pi / 2; out = ''; cls = ['c', 'w', 'g', 's', 'f']
    for i, p in enumerate(parts):
        a1 = a0 + 2 * math.pi * p / tot; x0, y0 = 80 + 46 * math.cos(a0), 60 + 46 * math.sin(a0); x1, y1 = 80 + 46 * math.cos(a1), 60 + 46 * math.sin(a1)
        big = 1 if (a1 - a0) > math.pi else 0
        out += '<path class="%s" d="M80 60L%.1f %.1fA46 46 0 %d 1 %.1f %.1fZ"/>' % (cls[i % 5], x0, y0, big, x1, y1); a0 = a1
    return out
def chain(n, w=520, h=120):
    gap = 26; bw = (w - 20 - gap * (n - 1)) // n; svg = ''; pts = []
    for i in range(n):
        x = 10 + i * (bw + gap)
        svg += '<rect class="%s" x="%d" y="52" width="%d" height="50" rx="8"/>' % ('c' if i % 2 == 0 else 'w', x, bw)
        svg += '<path class="l" d="M%d 52V30"/>' % (x + bw // 2)
        pts.append([x + bw // 2, 20])
        if i < n - 1: svg += '<path class="l" d="M%d 77H%dM%d 71L%d 77L%d 83"/>' % (x + bw + 3, x + bw + gap - 3, x + bw + gap - 9, x + bw + gap - 3, x + bw + gap - 9)
    return svg, pts, w, h
def layers(n, w=420, h=260):
    bh = (h - 20) // n; cl = ['g', 's', 'f', 'c', 'w', 's']; svg = ''; pts = []
    for i in range(n):
        y = 10 + i * bh
        svg += '<rect class="%s" x="30" y="%d" width="250" height="%d"/>' % (cl[i % 6], y, bh)
        svg += '<path class="l" d="M280 %dH350"/>' % (y + bh // 2); pts.append([370, y + bh // 2])
    return svg, pts, w, h
def cycle(n, w=420, h=300):
    cx, cy, r = 210, 150, 90; svg = ''; pts = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n; x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        b = -math.pi / 2 + 2 * math.pi * (i + 1) / n; x2, y2 = cx + r * math.cos(b), cy + r * math.sin(b)
        svg += '<path class="l" d="M%.0f %.0fA%d %d 0 0 1 %.0f %.0f"/>' % (x, y, r, r, x2, y2)
        mx, my = cx + r * math.cos((a + b) / 2), cy + r * math.sin((a + b) / 2); ang = (a + b) / 2 + math.pi / 2
        svg += '<path class="l" d="M%.0f %.0fL%.0f %.0fM%.0f %.0fL%.0f %.0f"/>' % (mx, my, mx - 8 * math.cos(ang - 0.5), my - 8 * math.sin(ang - 0.5), mx, my, mx - 8 * math.cos(ang + 0.5), my - 8 * math.sin(ang + 0.5)) if False else ''
        svg += '<circle class="%s" cx="%.0f" cy="%.0f" r="18"/>' % ('c' if i % 2 == 0 else 'w', x, y)
        pts.append([cx + (r + 52) * math.cos(a), cy + (r + 52) * math.sin(a)])
        svg += '<path class="l" d="M%.0f %.0fL%.0f %.0f"/>' % (x + 18 * math.cos(a), y + 18 * math.sin(a), cx + (r + 38) * math.cos(a), cy + (r + 38) * math.sin(a))
    return svg, [[round(a), round(b)] for a, b in pts], w, h
def roof(kind):
    g = '<path class="l" d="M10 108H150"/><rect class="s" x="40" y="62" width="80" height="46"/>'
    if kind == 'flat': return g + '<rect class="f" x="36" y="54" width="88" height="8"/>'
    if kind == 'pitched': return g + '<path class="c" d="M32 62L80 22L128 62Z"/>'
    if kind == 'dome': return g + '<path class="c" d="M40 62A40 40 0 0 1 120 62Z"/>'
    if kind == 'spire': return g + '<path class="c" d="M50 62L80 8L110 62Z"/>'
def wave(kind):
    base = '<path class="l" d="M8 60H152" style="stroke-width:1"/>'
    if kind == 'sine': return base + '<path class="l" d="M10 60Q30 20 50 60T90 60T130 60T150 60"/>'
    if kind == 'tight': return base + '<path class="l" d="M10 60Q20 30 30 60T50 60T70 60T90 60T110 60T130 60T150 60"/>'
    if kind == 'flat': return base + '<path class="l" d="M10 56Q40 52 80 56T150 58"/>'
    if kind == 'tall': return base + '<path class="l" d="M10 60Q35 -5 60 60T110 60T150 60"/>'
def dots(n):
    return ''.join('<circle class="c" cx="%d" cy="%d" r="8"/>' % (30 + (i % 4) * 34, 30 + (i // 4) * 34) for i in range(n))
