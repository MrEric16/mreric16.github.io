"""Original line-art Dubai/Abu Dhabi night skyline (drawn from scratch, not traced from any stock image).
Landmarks: Burj Khalifa, Burj Al Arab, Emirates Towers, Ain Dubai, Museum of the Future,
Sheikh Zayed Grand Mosque, Dubai World Trade Centre. Three depth rows."""
BG = '#0E1417'
_bn = [0]
def beacon(x, y, r=2):
    _bn[0] += 1
    d = round((_bn[0] * 0.53) % 2.4, 2)
    return (f'<circle class="beacon glow" cx="{x}" cy="{y}" r="{r*2.6}" style="animation-delay:{d}s"/>'
            f'<circle class="beacon" cx="{x}" cy="{y}" r="{r}" style="animation-delay:{d}s"/>')
def g(tx, ty, body, op):  # group translated so (0,0) is the building's ground centre
    return f'<g transform="translate({tx},{ty})" opacity="{op}">{body}</g>'
def poly(pts, close=True):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts) + ('Z' if close else '')
    return f'<path d="{d}"/>'
def windows(x0, x1, y0, y1, step=7, dx=6):
    out = []
    y = y0
    while y < y1:
        x = x0
        while x < x1:
            if (int(x * 7 + y * 13)) % 5 < 2: out.append(f'<rect class="lw" x="{x}" y="{y}" width="1.6" height="2.2"/>')
            x += dx
        y += step
    return ''.join(out)

def khalifa():
    tiers = [(22,0),(22,34),(18,34),(18,70),(14,70),(14,108),(11,108),(11,140),(8,140),(8,172),(5,172),(5,198),(2.6,198),(1.2,236)]
    left = [(-hw, -h) for hw, h in tiers]
    right = [(hw, -h) for hw, h in reversed(tiers)]
    body = poly(left + [(0, -252)] + right)
    body += '<path d="M0,-236 L0,-262" />'
    body += windows(-18, 16, -190, -6, 8, 6)
    body += beacon(0, -264, 0.9)
    return body

def burj_al_arab():
    body = '<path d="M-8,0 C-14,-46 0,-92 34,-128 L36,-128 L36,-160 L38,-128 L38,0Z"/>'   # sail + mast
    body += '<path d="M36,-128 L36,-150"/>'
    body += '<path d="M-2,-30 C6,-60 20,-90 36,-118"/><path d="M8,-20 C14,-50 26,-80 36,-100"/>'  # fabric lines
    body += '<path d="M-26,0 L-26,-6 C-10,-14 40,-14 56,-6 L56,0Z"/>'                               # island/base
    body += '<path d="M21,-100 L4,-100"/><circle cx="2" cy="-100" r="3"/>'                          # helipad
    body += beacon(36, -161, 1.8)
    return body

def museum():
    # elongated ring (egg-shaped, a little wider at the bottom, leaning slightly) with an off-centre almond void,
    # on a grass-covered mound. Approximation from written descriptions only (no reference photo available).
    body = '<path d="M-52,0 C-46,-12 -30,-16 0,-16 C30,-16 46,-12 52,0Z"/>'              # mound
    body += ('<g transform="rotate(-6 0 -60)">'
             '<path d="M0,-124 C26,-124 44,-96 44,-62 C44,-30 30,-14 0,-14 C-30,-14 -46,-30 -46,-62 C-46,-96 -26,-124 0,-124Z"/>'   # outer oval
             '<path d="M6,-104 C16,-90 20,-70 16,-48 C13,-34 8,-28 4,-28 C-2,-34 -6,-48 -6,-66 C-6,-84 -2,-98 6,-104Z" transform="rotate(8 6 -66)"/>'  # almond void
             '<path d="M-36,-96 C-42,-76 -41,-52 -33,-34"/><path d="M-27,-104 C-35,-84 -34,-58 -26,-40"/>'     # calligraphy bands (left)
             '<path d="M34,-92 C39,-74 38,-54 31,-38"/><path d="M26,-100 C31,-82 30,-60 24,-44"/>'             # (right)
             '</g>')
    return body

def dwtc():
    body = poly([(-17,0),(-17,-150),(-13,-154),(13,-154),(17,-150),(17,0)])
    body += ''.join(f'<path d="M{x},-150 L{x},0"/>' for x in range(-12, 13, 6))
    body += '<path d="M-17,-150 L17,-150"/><path d="M-3,-154 L-3,-166 L3,-166 L3,-154"/>' + beacon(0, -169, 1.8)
    body += poly([(-40,0),(-40,-26),(-17,-26)], False) + poly([(40,0),(40,-26),(17,-26)], False)
    return body

def emirates_towers():
    def tower(cx, w, h):
        hw = w/2
        return (poly([(cx-hw,0),(cx-hw,-(h-34)),(cx,-h),(cx+hw,-(h-34)),(cx+hw,0)]) +
                f'<path d="M{cx},{-h} L{cx},{-(h+24)}"/>' +
                f'<path d="M{cx-hw},{-(h-34)} L{cx+hw},{-(h-34)}"/>' + f'<path d="M{cx},{-h} L{cx},0"/>')
    body = tower(-12, 36, 170) + tower(26, 32, 136) + beacon(-12, -196, 2) + beacon(26, -162, 2)
    body += '<path d="M-30,0 L-30,-12 L42,-12 L42,0Z"/>'
    return body

def ain_dubai():
    cx, cy, r = 0, -88, 78
    body = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none"/><circle cx="{cx}" cy="{cy}" r="{r-9}" fill="none"/>'
    import math
    for i in range(24):
        a = math.pi * 2 * i / 24
        body += f'<path d="M{cx},{cy} L{round(cx+(r-9)*math.cos(a),1)},{round(cy+(r-9)*math.sin(a),1)}"/>'
    for i in range(48):
        a = math.pi * 2 * i / 48
        body += f'<circle class="cab" cx="{round(cx+(r+1)*math.cos(a),1)}" cy="{round(cy+(r+1)*math.sin(a),1)}" r="1.4"/>'
    body += f'<path d="M{cx},{cy} L-34,0 M{cx},{cy} L34,0 M-44,0 L44,0"/><circle cx="{cx}" cy="{cy}" r="4"/>'
    return body

def zayed():
    def dome(cx, base, r, fin=10):
        return (f'<path d="M{cx-r},{base} C{cx-r},{base-r*1.15} {cx-r*0.5},{base-r*1.45} {cx},{base-r*1.55} '
                f'C{cx+r*0.5},{base-r*1.45} {cx+r},{base-r*1.15} {cx+r},{base}Z"/>'
                f'<path d="M{cx},{base-r*1.55} L{cx},{base-r*1.55-fin}"/>')
    def minaret(cx, h):
        return (f'<path d="M{cx-3},0 L{cx-3},{-h} L{cx-5},{-h} L{cx-5},{-h-3} L{cx+5},{-h-3} L{cx+5},{-h} L{cx+3},{-h} L{cx+3},0Z"/>'
                f'<path d="M{cx-2},{-h-3} L{cx},{-h-16} L{cx+2},{-h-3}"/>')
    body = '<path d="M-150,0 L-150,-22 L150,-22 L150,0Z"/>'                       # arcade podium
    body += ''.join(f'<path d="M{x},-22 L{x},-8 Q{x+5},-18 {x+10},-8 L{x+10},-22"/>' for x in range(-140, 140, 20))
    body += dome(0, -22, 36) + dome(-66, -22, 22) + dome(66, -22, 22) + dome(-104, -22, 14) + dome(104, -22, 14)
    body += ''.join(dome(x, -22, 8, 5) for x in (-28, 28, -88, 88, -124, 124))
    body += minaret(-138, 92) + minaret(138, 92) + minaret(-40, 78) + minaret(40, 78)
    return body

def block_row(x0, x1, base, seed, hmin, hmax, wins=True):
    import random
    rnd = random.Random(seed)
    x = x0; out = ''
    while x < x1:
        w = rnd.randint(14, 30); h = rnd.randint(hmin, hmax)
        top = base - h
        roof = rnd.random()
        if roof < .25:
            out += poly([(x,base),(x,top),(x+w/2,top-8),(x+w,top),(x+w,base)])
        elif roof < .45:
            out += poly([(x,base),(x,top),(x+w*.3,top),(x+w*.3,top-6),(x+w,top-6),(x+w,base)])
        else:
            out += poly([(x,base),(x,top),(x+w,top),(x+w,base)])
        if wins: out += windows(x+3, x+w-3, top+6, base-4, 8, 6)
        if h >= 88: out += beacon(round(x+w/2,1), top-10 if roof < .25 else top-8, 1.4)
        x += w + rnd.randint(2, 8)
    return out

def build():
    s = []
    # row 1 (far): Zayed Mosque + Ain Dubai
    s.append(g(152, 215, zayed(), .8))
    s.append(g(500, 215, ain_dubai(), .85))
    # row 2 (middle): Museum, Burj Al Arab, WTC, Emirates Towers + filler
    s.append(g(0, 430, block_row(0, 600, 0, 5, 18, 50, False), .45))
    s.append(g(55, 430, museum(), .95))
    s.append(g(130, 430, burj_al_arab(), .95))
    s.append(g(215, 430, dwtc(), .95))
    s.append(g(450, 430, emirates_towers(), .95))
    # row 3 (front): Burj Khalifa + city
    s.append(g(0, 640, block_row(0, 275, 0, 11, 40, 110), .95))
    s.append(g(0, 640, block_row(365, 600, 0, 23, 40, 120), .95))
    s.append('<g transform="translate(320,640) scale(2.3)" stroke-width=".6" opacity="1">%s</g>' % khalifa())
    return ''.join(s)

SVG = ('<svg viewBox="0 0 600 640" preserveAspectRatio="xMidYMax meet" xmlns="http://www.w3.org/2000/svg">'
       '<g fill="%s" stroke="#FFF3CF" stroke-width="1.35" stroke-linejoin="round" stroke-linecap="round">%s</g></svg>') % (BG, build())
