#!/usr/bin/env python3
"""Builds uae-lab.html: a copy of the real home page (index.html) with the UAE National Day
theme + a floating time simulator injected. index.html is never modified."""
import re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import uae_sky
root = pathlib.Path(__file__).resolve().parent.parent
src = (root/'index.html').read_text(encoding='utf-8')

CSS = r'''
<style id="uae-lab-css">
/* ===== UAE National Day theme (lab) ===== */
body.theme-uae{ background:#0E1417 !important; }
body.theme-uae::before{ content:""; position:fixed; inset:0; z-index:0; pointer-events:none; opacity:.55;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='64' height='64' viewBox='0 0 64 64'><g fill='none' stroke='%23D4AF37' stroke-opacity='.13' stroke-width='1'><path d='M32 4 L40 24 L60 32 L40 40 L32 60 L24 40 L4 32 L24 24 Z'/><rect x='18' y='18' width='28' height='28' transform='rotate(45 32 32)'/></g></svg>");
  background-size:64px 64px; }
body.theme-uae .aurora-layer, body.theme-uae .flag-emblem{ display:none !important; }
body.theme-uae header{ background:linear-gradient(180deg,#0C1613,#0E1417) !important; border-bottom:4px solid #D4AF37 !important; box-shadow:none !important; }
body.theme-uae header::before, body.theme-uae header::after{ content:none !important; }
body.theme-uae h1.title, body.theme-uae h1.title *{ color:#F1D77A !important; -webkit-text-fill-color:#F1D77A !important; background:none !important; letter-spacing:.02em; }
body.theme-uae .subtitle{ color:#EADFC3 !important; }
body.theme-uae .board{ background:linear-gradient(180deg,#14201B,#0B1511) !important; border:2px solid #D4AF37 !important; box-shadow:0 0 0 3px #0B1511,0 0 0 5px rgba(241,215,122,.6) !important; }
body.theme-uae .board *{ color:#F7F1E1 !important; }

/* the flag IS the header (like the Uzbekistan theme): red band = 1/4 of width, three equal stripes, official colours.
   Title + subtitle removed; clock board sits at the bottom so the emblem stays visible, dead centre of the white stripe. */
.uae-flagwrap{ display:none; position:absolute; left:0; right:0; top:0; bottom:58px; z-index:0; overflow:hidden; touch-action:pan-y; cursor:pointer; -webkit-tap-highlight-color:transparent; }
.uae-flagbox, .uae-fbox{ transition:transform .55s cubic-bezier(.4,0,.2,1); }
.uae-fbox{ position:absolute; inset:0; background:#fff; --k:1; transform:translateX(calc((var(--k) - var(--i,0)) * 100%)); }
.uae-flagbox{ --k:0; transform:translateX(calc((var(--k) - var(--i,0)) * 100%)); }
.uae-zr{ --k:2; background:#111; }
.uae-zr img{ object-fit:cover !important; object-position:50% 35% !important; }
.uae-zr small{ position:absolute; left:8px; bottom:7px; font:600 10px/1 system-ui,sans-serif; color:rgba(255,255,255,.85); text-shadow:0 1px 2px #000; }
.uae-fbox img{ width:100%; height:100%; object-fit:contain; object-position:50% 100%; display:block; user-select:none; -webkit-user-drag:none; }
.uae-dots{ position:absolute; left:0; right:0; bottom:6px; display:flex; justify-content:center; gap:7px; z-index:3; pointer-events:none; }
.uae-dots i{ width:7px; height:7px; border-radius:50%; background:rgba(255,255,255,.55); box-shadow:0 0 0 1px rgba(0,0,0,.45); }
.uae-flagwrap[data-i="0"] .uae-dots i:nth-child(1), .uae-flagwrap[data-i="1"] .uae-dots i:nth-child(2), .uae-flagwrap[data-i="2"] .uae-dots i:nth-child(3){ background:#D4AF37; }
body.theme-uae .uae-flagwrap{ display:block; }
.uae-flagbox{ position:absolute; inset:0; }
.uae-flagbox .fl{ position:absolute; inset:0; display:grid; grid-template-columns:25% 1fr; }
.uae-flagbox .fl i{ display:block; background:#FF0000; }
.uae-flagbox .fl div{ display:grid; grid-template-rows:1fr 1fr 1fr; }
.uae-flagbox .fl b{ display:block; }
.uae-flagbox .fl b:nth-child(1){ background:#00732F; }
.uae-flagbox .fl b:nth-child(2){ background:#FFFFFF; }
.uae-flagbox .fl b:nth-child(3){ background:#000000; }
.uae-flagbox img{ position:absolute; left:62.5%; top:50%; height:28%; aspect-ratio:360/463; transform:translate(-50%,-50%); object-fit:contain; display:block; }
body.theme-uae header{ position:relative !important; height:306px; overflow:hidden; background:transparent !important; }
body.theme-uae header > *:not(.uae-flagwrap){ position:relative; z-index:1; }
body.theme-uae header > .masthead{ position:absolute !important; left:0; right:0; bottom:4px; }
body.theme-uae .title-row, body.theme-uae .subtitle, body.theme-uae .board{ display:none !important; }

/* countdown ribbon under the header */
.uae-ribbon{ display:none; text-align:center; padding:8px 12px; background:transparent; border-bottom:2px solid #D4AF37; position:relative; z-index:2; }
body.theme-uae .uae-ribbon{ display:block; }
.uae-ribbon span{ display:inline-block; padding:3px 14px; border-radius:99px; background:rgba(8,14,12,.92); border:1.5px solid #D4AF37; color:#F1D77A; font-weight:800; letter-spacing:.06em; font-size:14px; }
.uae-ribbon.big span{ font-size:16px; }
#uaeFx{ position:fixed; left:0; top:0; width:100vw; height:100vh; z-index:99990; pointer-events:none; }

/* tiles: green/gold cards (red for sport-like), gold frame, diamond corner */
body.theme-uae .fac-tile, body.theme-uae .sport-hub-tile, body.theme-uae .random-tile, body.theme-uae a[class$="-tile"]{
  position:relative; overflow:hidden; border:2px solid #D4AF37 !important; border-radius:12px !important;
  background:linear-gradient(135deg,#0D3F2A,#0A2A1D) !important; box-shadow:0 4px 0 rgba(0,0,0,.45) !important; }
body.theme-uae .sport-hub-tile, body.theme-uae .goodnews-tile, body.theme-uae .watch-tile{ background:linear-gradient(135deg,#7A0E22,#4D0914) !important; }
body.theme-uae .fac-tile::after, body.theme-uae .sport-hub-tile::after, body.theme-uae .random-tile::after, body.theme-uae a[class$="-tile"]::after{
  content:""; position:absolute; right:-18px; top:-18px; width:70px; height:70px; border:2px solid rgba(212,175,55,.28); transform:rotate(45deg); pointer-events:none; }
body.theme-uae .fac-tile, body.theme-uae .fac-tile *, body.theme-uae .sport-hub-tile, body.theme-uae .sport-hub-tile *, body.theme-uae .random-tile, body.theme-uae .random-tile *, body.theme-uae a[class$="-tile"], body.theme-uae a[class$="-tile"] *{ color:#FFF7E3 !important; }
/* section headings: gold plaque + sand-dune strip */
body.theme-uae .section-head h2{ color:#F1D77A !important; letter-spacing:.03em; }
body.theme-uae .section-head{ position:relative; padding-bottom:16px; }
body.theme-uae .section-head::after{ content:""; position:absolute; left:0; right:0; bottom:0; height:12px; pointer-events:none; opacity:.9;
  background: radial-gradient(40px 10px at 20px 100%,#EBD9B4 98%,transparent 100%) 0 0/40px 12px repeat-x, radial-gradient(60px 8px at 50px 100%,#C9A96A 98%,transparent 100%) 0 3px/60px 12px repeat-x;
  border-bottom:2px solid #D4AF37; }
body.theme-uae #app ul:not([class]){ list-style:none; padding-left:4px; }
body.theme-uae #app ul:not([class]) > li{ position:relative; padding-left:28px; }
body.theme-uae #app ul:not([class]) > li::before{ content:"\1F334"; position:absolute; left:0; }
body.theme-uae #app ul:not([class]) > li:nth-child(2n)::before{ content:"\26F5"; }


/* ---- more UAE: nothing below touches the flag ---- */
.uae-only{ display:none; }
body.theme-uae .uae-only{ display:block; }
/* Sadu weave divider under the ribbon */
.uae-sadu{ height:14px; background:
  linear-gradient(135deg,transparent 40%,#E4002B 40% 60%,transparent 60%) 0 0/14px 14px,
  linear-gradient(45deg,transparent 40%,#D4AF37 40% 60%,transparent 60%) 0 0/14px 14px, #1A1410;
  border-bottom:2px solid #D4AF37; position:relative; z-index:2; }
/* majlis tiles: Sadu stripe on top, gold tassel bottom-right, lattice texture */
body.theme-uae .fac-tile, body.theme-uae .sport-hub-tile, body.theme-uae .random-tile, body.theme-uae a[class$="-tile"]{
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='28' height='28'><path d='M14 2 L26 14 L14 26 L2 14Z' fill='none' stroke='%23D4AF37' stroke-opacity='.16'/><circle cx='14' cy='14' r='3' fill='none' stroke='%23D4AF37' stroke-opacity='.16'/></svg>"), linear-gradient(135deg,#0D3F2A,#0A2A1D) !important; }
body.theme-uae .sport-hub-tile, body.theme-uae .goodnews-tile, body.theme-uae .watch-tile{
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='28' height='28'><path d='M14 2 L26 14 L14 26 L2 14Z' fill='none' stroke='%23D4AF37' stroke-opacity='.16'/><circle cx='14' cy='14' r='3' fill='none' stroke='%23D4AF37' stroke-opacity='.16'/></svg>"), linear-gradient(135deg,#7A0E22,#4D0914) !important; }
body.theme-uae .fac-tile::before, body.theme-uae .sport-hub-tile::before, body.theme-uae .random-tile::before, body.theme-uae a[class$="-tile"]::before{
  content:""; position:absolute; left:0; right:0; top:0; height:7px; pointer-events:none; z-index:0;
  background:linear-gradient(135deg,transparent 40%,#E4002B 40% 60%,transparent 60%) 0 0/8px 7px,linear-gradient(45deg,transparent 40%,#D4AF37 40% 60%,transparent 60%) 0 0/8px 7px,#1A1410; }
body.theme-uae .fac-tile::after, body.theme-uae .sport-hub-tile::after, body.theme-uae .random-tile::after, body.theme-uae a[class$="-tile"]::after{
  content:""; position:absolute; right:12px; bottom:-10px; top:auto; width:10px; height:26px; transform:none; border:none;
  background:linear-gradient(#D4AF37,#A8861C); border-radius:5px 5px 3px 3px; box-shadow:0 0 0 2px #1A1410; pointer-events:none; }
/* gold foil shimmer on section headings */
body.theme-uae .section-head h2{
  background:linear-gradient(100deg,#B8921F 0%,#F1D77A 35%,#FFF6CF 50%,#F1D77A 65%,#B8921F 100%) 0 0/250% 100%;
  -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent !important; color:transparent !important;
  animation:uaeFoil 7s linear infinite; }
@keyframes uaeFoil{ 0%{background-position:150% 0} 100%{background-position:-100% 0} }
/* dhow on the ribbon */
.uae-ribbon{ position:relative; overflow:hidden; }
.uae-ribbon span{ position:relative; z-index:2; }
.uae-dhow{ position:absolute; z-index:1; bottom:2px; left:-70px; width:54px; height:34px; cursor:pointer; animation:uaeSail 38s linear infinite; -webkit-tap-highlight-color:transparent; }
.uae-dhow svg{ width:100%; height:100%; display:block; animation:uaeBob 3s ease-in-out infinite; }
.uae-dhow.toot{ animation-play-state:paused; }
@keyframes uaeSail{ 0%{transform:translateX(0)} 100%{transform:translateX(calc(100vw + 140px))} }
@keyframes uaeBob{ 0%,100%{transform:translateY(0) rotate(-1.5deg)} 50%{transform:translateY(-2px) rotate(1.5deg)} }
/* desert horizon above the bottom nav */
#uaeDunes{ position:fixed; left:0; right:0; bottom:56px; height:110px; z-index:0; pointer-events:none; opacity:.5; overflow:hidden; display:none; }
body.theme-uae #uaeDunes{ display:block; }
#uaeDunes svg{ position:absolute; left:0; bottom:0; width:200%; height:100%; }
#uaeDunes .d1{ animation:uaeDrift 90s linear infinite; } #uaeDunes .d2{ animation:uaeDrift 60s linear infinite reverse; }
@keyframes uaeDrift{ 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
#uaeDunes[data-sky=dawn] .c1{fill:#C98A5B}#uaeDunes[data-sky=dawn] .c2{fill:#9A6446}
#uaeDunes[data-sky=day]  .c1{fill:#E3C48A}#uaeDunes[data-sky=day]  .c2{fill:#C9A16A}
#uaeDunes[data-sky=dusk] .c1{fill:#B8643F}#uaeDunes[data-sky=dusk] .c2{fill:#7E3F2B}
#uaeDunes[data-sky=night] .c1{fill:#3A3A4E}#uaeDunes[data-sky=night] .c2{fill:#25263A}
/* incense smoke, bottom-right (nowhere near the flag) */
.uae-smoke{ position:fixed; right:70px; bottom:64px; width:30px; height:90px; z-index:90; pointer-events:none; display:none; }
body.theme-uae .uae-smoke{ display:block; }
.uae-smoke i{ position:absolute; bottom:0; left:50%; width:14px; height:14px; border-radius:50%; background:rgba(235,225,205,.38); filter:blur(5px); animation:uaeSmoke 5s ease-in infinite; opacity:0; }
.uae-smoke i:nth-child(2){ animation-delay:1.6s } .uae-smoke i:nth-child(3){ animation-delay:3.2s }
@keyframes uaeSmoke{ 0%{transform:translate(-50%,0) scale(.6);opacity:0} 20%{opacity:.7} 100%{transform:translate(-10%,-90px) scale(2.4);opacity:0} }
.uae-smoke b{ position:absolute; bottom:-6px; left:50%; transform:translateX(-50%); font-size:18px; }
/* camel + dallah (fixed, bottom) */
#uaeCamel{ position:fixed; right:8px; bottom:64px; z-index:95; display:none; align-items:flex-end; gap:6px; }
body.theme-uae #uaeCamel{ display:flex; }
#uaeCamel .cam{ font-size:34px; cursor:pointer; user-select:none; -webkit-tap-highlight-color:transparent; }
#uaeCamel .bub{ background:#F4E6C3; color:#2B2112; padding:7px 11px; border-radius:12px 12px 3px 12px; font:600 13px/1.3 system-ui,sans-serif; max-width:190px; box-shadow:0 2px 0 rgba(0,0,0,.4); opacity:0; transform:translateY(6px); transition:opacity .25s, transform .25s; }
#uaeCamel .bub.show{ opacity:1; transform:none; }
#uaeDallah{ position:fixed; left:8px; bottom:124px; z-index:99998; display:none; width:44px; height:44px; border-radius:50%; background:#111; border:2px solid #D4AF37; font-size:22px; cursor:pointer; align-items:center; justify-content:center; }
body.theme-uae #uaeDallah{ display:flex; }
#uaeDallah.steam::after{ content:"\2615"; position:absolute; top:-24px; left:8px; font-size:20px; animation:uaeSmoke 2s ease-out 1; }
/* seven emirates strip */
.uae-emirates{ display:none; overflow-x:auto; scroll-snap-type:x mandatory; gap:10px; padding:12px 14px; position:relative; z-index:2; -webkit-overflow-scrolling:touch; scrollbar-width:none; }
body.theme-uae .uae-emirates{ display:flex; }
.uae-emirates::-webkit-scrollbar{ display:none; }
.uae-em{ flex:0 0 196px; scroll-snap-align:start; padding:10px 12px; border:2px solid #D4AF37; border-radius:12px; color:#FFF7E3; background:linear-gradient(135deg,#0D3F2A,#0A2A1D); box-shadow:0 3px 0 rgba(0,0,0,.45); }
.uae-em{ min-height:96px; transition:opacity .45s ease; }
.uae-em.fade{ opacity:0; }
.uae-em b{ display:block; color:#F1D77A; font-size:15px; margin-bottom:3px; }
.uae-em span{ display:block; font-size:12px; opacity:.92; line-height:1.4; }
.uae-em span i{ color:#EADFC3; }


/* night skyline backdrop: three depth rows, outline style, fixed behind the content */
#uaeSplash{ position:fixed; inset:0; z-index:100000; background:#fff; display:none; flex-direction:column; align-items:center; justify-content:center; gap:14px; padding:12px; opacity:0; transition:opacity .6s ease; }
#uaeSplash.show{ display:flex; } #uaeSplash.in{ opacity:1; }
#uaeSplash img{ max-width:min(96vw,1000px); max-height:68vh; width:auto; height:auto; object-fit:contain; }
#uaeSplash .t{ font:800 clamp(16px,3.6vw,26px)/1.2 system-ui,sans-serif; color:#111; text-align:center; letter-spacing:.02em; }
#uaeSplash .t small{ display:block; font-weight:600; font-size:.7em; color:#00732F; margin-top:4px; }
#uaeSplash button{ appearance:none; border:0; border-radius:999px; padding:12px 30px; font:800 17px system-ui,sans-serif; background:#C9A646; color:#111; cursor:pointer; }
#uaeSky{ position:fixed; left:50%; transform:translateX(-50%); top:260px; height:540px; width:380px; z-index:-1; pointer-events:none; display:none; opacity:1; }
body.theme-uae #uaeSky{ display:block; }
body.theme-uae #uaeDunes{ display:none; }
#uaeSky svg{ width:100%; height:100%; display:block; }
#uaeSky .lw{ fill:#FFE29A; stroke:none; opacity:.95; animation:uaeTwinkle 5s ease-in-out infinite; }
#uaeSky .lw:nth-child(3n){ animation-delay:1.3s; } #uaeSky .lw:nth-child(4n+1){ animation-delay:2.7s; }
@keyframes uaeTwinkle{ 0%,100%{opacity:.95} 50%{opacity:.4} }
#uaeSky .cab{ fill:#FFF3CF; stroke:none; }
#uaeSky .beacon{ fill:#FF2A2A; stroke:none; opacity:.15; animation:uaeBeacon 2.4s ease-in-out infinite; }
#uaeSky .beacon.glow{ fill:#FF2A2A; opacity:.12; }
@keyframes uaeBeacon{ 0%,45%,100%{opacity:.12} 12%,28%{opacity:1} }
#uaeSky svg > g{ animation:uaeGleam 6s ease-in-out infinite; }
@keyframes uaeGleam{ 0%,100%{stroke:#FFF3CF} 50%{stroke:#FFFFFF} }


#uaeBg{ position:fixed; left:0; top:0; width:100vw; height:100vh; z-index:-2; pointer-events:none; display:none; }
body.theme-uae #uaeBg{ display:block; }
#uaeBg.over{ z-index:99989; }

/* ===== simulator (floating, collapsible) ===== */
#uaeLab{ position:fixed; left:8px; bottom:78px; z-index:99999; font:13px/1.35 system-ui,sans-serif; color:#eee; }
#uaeLab .pill{ padding:7px 12px; border-radius:99px; background:#111; border:2px solid #555; cursor:pointer; font-weight:700; color:#fff; }
#uaeLab .pill.forced{ background:#b3001f; border-color:#ff7a8d; } #uaeLab .pill.opt{ background:#7a5d00; border-color:#F1D77A; }
#uaeLab .panel{ display:none; margin-bottom:8px; width:min(300px,86vw); padding:10px; border-radius:12px; background:#111; border:2px solid #555; box-shadow:0 8px 24px rgba(0,0,0,.6); }
#uaeLab.open .panel{ display:block; }
#uaeLab select, #uaeLab button.b{ width:100%; margin:4px 0; padding:8px; border-radius:8px; border:1px solid #666; background:#222; color:#fff; font:inherit; }
#uaeLab .n{ color:#aaa; font-size:11.5px; margin-top:4px; }
</style>
'''

HTML = r'''
<canvas id="uaeBg"></canvas>
__SKY__
<div class="uae-sadu uae-only" id="uaeSadu"></div>
<div class="uae-emirates" id="uaeEm"><div class="uae-em"></div><div class="uae-em"></div><div class="uae-em"></div><div class="uae-em"></div><div class="uae-em"></div><div class="uae-em"></div><div class="uae-em"></div></div>
<div id="uaeDunes" data-sky="night"><svg class="d1" viewBox="0 0 800 110" preserveAspectRatio="none"><path class="c1" d="M0 80 C100 40 200 90 300 60 C400 30 500 85 600 55 C700 30 750 70 800 80 L800 110 L0 110Z"/></svg><svg class="d2" viewBox="0 0 800 110" preserveAspectRatio="none"><path class="c2" d="M0 95 C120 65 230 100 340 80 C450 60 560 100 680 78 C740 68 780 88 800 95 L800 110 L0 110Z"/></svg></div>
<div class="uae-smoke"><i></i><i></i><i></i><b>🪔</b></div>
<div id="uaeCamel"><div class="bub" id="uaeBub"></div><div class="cam" id="uaeCam">🐪</div></div>
<button id="uaeDallah" title="Qahwa">☕</button>
<div class="uae-ribbon" id="uaeRibbon"><span id="uaeRib">…</span></div>
<canvas id="uaeFx"></canvas>
<div id="uaeSplash"><img alt="The seven Founding Fathers of the UAE beneath the flag"><div class="t">Happy 55th National Day, UAE<small>Eid Al Etihad · 2 December</small></div><button id="uaeSplashGo">Enter</button></div>
<div id="uaeLab">
  <div class="panel">
    <b>UAE theme lab</b>
    <select id="uaeSim">
      <option value="">Real time</option>
      <option value="2026-11-29T12:00">29 Nov (before window)</option>
      <option value="2026-11-30T00:00">30 Nov 00:00 (opens, optional)</option>
      <option value="2026-12-01T18:00">1 Dec 18:00 (tomorrow)</option>
      <option value="2026-12-01T23:59">1 Dec 23:59</option>
      <option value="2026-12-02T00:00">2 Dec 00:00 (FORCED)</option>
      <option value="2026-12-02T23:59">2 Dec 23:59 (FORCED)</option>
      <option value="2026-12-03T00:00">3 Dec 00:00 (back to optional)</option>
      <option value="2026-12-04T00:00">4 Dec 00:00 (window closed)</option>
    </select>
    <button class="b" id="uaePick">Use UAE theme</button>
    <button class="b" id="uaeFw">Fireworks</button>
    <button class="b" id="uaeSpl">Splash</button>
    <div class="n">Lab copy of the home page. Optional 30 Nov 00:00 to 3 Dec 00:00, forced 2 Dec 00:00 to 24:00 (Tashkent time). Your normal theme is never changed.</div>
  </div>
  <div class="pill" id="uaePill">UAE lab</div>
</div>
'''

FLAG = r'''<div class="uae-flagwrap" id="uaeFlag"><div class="uae-flagbox"><div class="fl"><i></i><div><b></b><b></b><b></b></div></div><img src="uae-emblem.png" alt="Emblem of the United Arab Emirates"></div><div class="uae-fbox"><img alt="The seven Founding Fathers of the UAE beneath the flag" draggable="false"></div><div class="uae-fbox uae-zr"><img alt="Sheikh Zayed bin Sultan Al Nahyan and Sheikh Rashid bin Saeed Al Maktoum" draggable="false"><small>UAE National Library &amp; Archives</small></div><div class="uae-dots"><i></i><i></i><i></i></div></div>
'''

JS = r'''
<script id="uae-lab-js">
(function(){
'use strict';
var OFF=5*3600e3;
function tk(s){var m=s.match(/(\d+)-(\d+)-(\d+)T(\d+):(\d+)/);return Date.UTC(+m[1],+m[2]-1,+m[3],+m[4],+m[5])-OFF;}
var START=tk('2026-11-30T00:00'),F_START=tk('2026-12-02T00:00'),END=tk('2026-12-03T00:00');
var sim=null,picked=false;
function now(){return sim!==null?sim:Date.now();}
function state(){var t=now();if(t>=F_START&&t<END)return 'forced';if(t>=START&&t<END)return 'optional';return 'off';}
function on(){var s=state();return s==='forced'||(s==='optional'&&picked);}

/* place flag as first child of header, ribbon right after header */
var hdr=document.querySelector('header');
var tpl=document.getElementById('uaeFlagTpl');
if(hdr&&tpl){hdr.insertBefore(tpl.content.firstElementChild,hdr.firstChild);}
var rib=document.getElementById('uaeRibbon');
if(hdr&&rib&&hdr.parentNode){hdr.parentNode.insertBefore(rib,hdr.nextSibling);}

var KILL=/(^|\s)(usertheme-[\w-]+|theme-nationalday)(?=\s|$)/g;
var guard=false,saved=new Map();
function enforce(){
  if(guard)return;guard=true;
  var b=document.body,want=on();
  b.classList.toggle('theme-uae',want);
  if(want){
    var c=b.className.replace(KILL,' ').replace(/\s+/g,' ').trim();
    if(c!==b.className)b.className=c;
    b.classList.add('theme-uae','dark-mode');
  }
  var t=document.querySelector('h1.title');
  if(t){
    var els=[t].concat([].slice.call(t.querySelectorAll('*')));
    els.forEach(function(e){
      if(e.classList.contains('tittle-cycle'))return;
      if(want){ if(!saved.has(e))saved.set(e,e.getAttribute('style')); e.style.setProperty('color','#F1D77A','important'); e.style.setProperty('-webkit-text-fill-color','#F1D77A','important'); }
      else if(saved.has(e)){ var v=saved.get(e); if(v===null)e.removeAttribute('style');else e.setAttribute('style',v); saved.delete(e); }
    });
  }
  guard=false;
}
setInterval(enforce,700);

function ribbon(){
  var s=document.getElementById('uaeRib'),r=document.getElementById('uaeRibbon');
  var t=now(),d=Math.ceil((F_START-t)/864e5);
  if(t>=F_START&&t<END){r.classList.add('big');s.textContent='55th Eid Al Etihad · UAE National Day';}
  else if(t<F_START){r.classList.remove('big');s.textContent=d<=1?'Eid Al Etihad · tomorrow':'Eid Al Etihad · '+d+' days to go';}
  else{r.classList.remove('big');s.textContent='Eid Al Etihad · 2 December';}
}
var sub=null,origSub=null;
function subtitle(){
  var el=document.getElementById('subtitleText');if(!el)return;
  if(on()){if(origSub===null)origSub=el.textContent;el.textContent=(now()>=F_START&&now()<END)?'Happy 55th National Day, UAE':'Happy National Day, UAE';}
  else if(origSub!==null){el.textContent=origSub;origSub=null;}
}
function apply(){
  var st=state();
  enforce();ribbon();subtitle();
  var pill=document.getElementById('uaePill');
  pill.className='pill '+(st==='forced'?'forced':st==='optional'?'opt':'');
  pill.textContent=st==='forced'?'UAE · FORCED':st==='optional'?('UAE · optional'+(picked?' · on':'')):'UAE lab';
  var pk=document.getElementById('uaePick');
  pk.style.display=st==='optional'?'block':'none';
  pk.textContent=picked?'Turn UAE theme off':'Use UAE theme';
}

/* fireworks (fixed overlay canvas, capped particles) */
var cv=document.getElementById('uaeFx'),cx=cv.getContext('2d'),parts=[],raf=0,W=0,H=0;
function size(){W=cv.width=innerWidth;H=cv.height=innerHeight;}
addEventListener('resize',size);size();
var COL=['#FF2B2B','#00A84F','#FFFFFF','#F1D77A','#F1D77A'];
function hb(){var h=document.querySelector('header');var r=h?h.getBoundingClientRect().bottom:0;return Math.max(0,Math.min(r,H));}
function burst(x,y,n,pw){if(parts.length>300)return;var c=COL[(Math.random()*COL.length)|0];
  for(var i=0;i<n;i++){var a=Math.PI*2*i/n,v=(.4+Math.random()*.6)*pw;parts.push({x:x,y:y,vx:Math.cos(a)*v,vy:Math.sin(a)*v,l:1,c:Math.random()<.2?'#F1D77A':c});}
  if(!raf)raf=requestAnimationFrame(tick);}
function tick(){cx.clearRect(0,0,W,H);cx.save();cx.beginPath();var _h=hb();cx.rect(0,_h,W,H-_h);cx.clip();parts=parts.filter(function(p){return p.l>0;});
  parts.forEach(function(p){p.x+=p.vx;p.y+=p.vy;p.vy+=.05;p.vx*=.985;p.l-=.013;cx.globalAlpha=Math.max(p.l,0);cx.fillStyle=p.c;cx.fillRect(p.x,p.y,3.4,3.4);});
  cx.restore();cx.globalAlpha=1;raf=(parts.length&&!document.hidden)?requestAnimationFrame(tick):0;}
function small(){size();var _t=hb();burst(W*(.2+Math.random()*.6),_t+30+Math.random()*Math.max(40,(H-_t)*.3),18,2.4);}
function show(n){size();var k=0;(function go(){var _t=hb();burst(W*(.1+Math.random()*.8),_t+30+Math.random()*Math.max(60,(H-_t)*.4),32,3.4);if(++k<n)setTimeout(go,280+Math.random()*260);})();}

document.getElementById('uaePill').onclick=function(){document.getElementById('uaeLab').classList.toggle('open');};
document.getElementById('uaeSim').onchange=function(e){sim=e.target.value?tk(e.target.value):null;apply();};
document.getElementById('uaePick').onclick=function(){picked=!picked;apply();};
document.getElementById('uaeFw').onclick=function(){if(!on()){picked=true;sim=sim===null?START:sim;apply();}overload();};

/* ===== extras: all placed away from the flag ===== */
var rb=document.getElementById('uaeRibbon');
if(rb){var dh=document.createElement('div');dh.className='uae-dhow';dh.innerHTML='<svg viewBox="0 0 60 38" aria-hidden="true"><path d="M3 26 L57 26 L50 33 L11 33Z" fill="#6B3E1B" stroke="#D4AF37" stroke-width="1"/><path d="M30 25 L30 3" stroke="#D4AF37" stroke-width="1.6"/><path d="M30 4 L52 24 L30 24Z" fill="#F7F1E1"/><path d="M29 8 L10 24 L29 24Z" fill="#EADFC3"/></svg>';rb.appendChild(dh);
  dh.onclick=function(){say('Toot toot!');};}
var sadu=document.getElementById('uaeSadu'),emS=document.getElementById('uaeEm');
if(rb&&sadu&&emS){rb.parentNode.insertBefore(sadu,rb.nextSibling);sadu.parentNode.insertBefore(emS,sadu.nextSibling);}
function sky(){var h=new Date(now()+OFF).getUTCHours();var k=(h>=5&&h<8)?'dawn':(h>=8&&h<16)?'day':(h>=16&&h<19)?'dusk':'night';document.getElementById('uaeDunes').setAttribute('data-sky',k);}
var BUB=document.getElementById('uaeBub'),bt=0;
var LINES=['Yalla! Let\'s learn.','Shukran! Correct.','Mashallah! Well done.','Habibi, try again.','Slow camel, still arrives.','Eid Mubarak!','Ya hala!'],li=0;
function say(t){BUB.textContent=t||LINES[(li=(li+1)%LINES.length)];BUB.classList.add('show');clearTimeout(bt);bt=setTimeout(function(){BUB.classList.remove('show');},2600);}
document.getElementById('uaeCam').onclick=function(){say();};
var da=document.getElementById('uaeDallah');
da.onclick=function(){da.classList.remove('steam');void da.offsetWidth;da.classList.add('steam');say('Qahwa? Tfaddal.');};
/* answers + level-up hooks (read-only observers, only while the theme is on) */
var GOOD=/(^|-)(correct|ok|good|right)$/,BAD=/(^|-)(wrong|incorrect|bad)$/,SKIP=/^(gg-banner-ok|fg-review-wrong|safety-ok|save-good|top-right|bottom-right|tetris-right|down-right|up-right|margin-right|padding-right|border-right|text-right|float-right|align-right|justify-right)$/;
var lastG=0,lastS=0,ao=null,xo=null;
addEventListener('pointerdown',function(){lastG=Date.now();},true);addEventListener('keydown',function(){lastG=Date.now();},true);
function watch(){
  if(on()&&!ao){
    ao=new MutationObserver(function(ms){
      if(Date.now()-lastG>1800||Date.now()-lastS<1100)return;
      for(var i=0;i<ms.length;i++){var t=ms[i].target;if(!t.classList||t.closest&&t.closest('#uaeLab'))continue;
        var add=[].slice.call(t.classList).filter(function(c){return !SKIP.test(c);});
        var g=add.some(function(c){return GOOD.test(c);}),b=add.some(function(c){return BAD.test(c);});
        if(g&&ms[i].oldValue!==null&&!(ms[i].oldValue||'').split(/\s+/).some(function(c){return GOOD.test(c);})){lastS=Date.now();small();say('Shukran! Correct.');da.classList.remove('steam');void da.offsetWidth;da.classList.add('steam');return;}
        if(b&&!(ms[i].oldValue||'').split(/\s+/).some(function(c){return BAD.test(c);})){lastS=Date.now();say('Habibi, try again.');return;}
      }
    });
    ao.observe(document.getElementById('app')||document.body,{attributes:true,attributeFilter:['class'],attributeOldValue:true,subtree:true});
    var xp=document.getElementById('xpChip');if(xp){var lv=xp.textContent;xo=new MutationObserver(function(){var n=xp.textContent;if(n!==lv){lv=n;show(6);say('Mashallah! Level up.');}});xo.observe(xp,{childList:true,characterData:true,subtree:true});}
  }else if(!on()&&ao){ao.disconnect();ao=null;if(xo){xo.disconnect();xo=null;}}
}
/* midnight show: the moment 2 Dec 00:00 (Tashkent) arrives while the app is open */
var prevT=Date.now();
setInterval(function(){var t=Date.now();if(sim===null&&prevT<F_START&&t>=F_START){apply();show(10);say('Eid Al Etihad Mubarak!');}prevT=t;},1000);



var SKYF=252;
function flagBottomDoc(){var h=document.querySelector('header'),fw=document.querySelector('.uae-flagwrap');if(!h||!fw)return 252;var y=0,e=h;while(e){y+=e.offsetTop||0;e=e.offsetParent;}return y+fw.offsetHeight;}
/* skyline is sized for the "pinned" state (top of screen to the bottom nav) and scaled down from its bottom edge,
   so at the top of the page the Burj Khalifa tip sits just under the flag; as you scroll it grows up to the top of the screen. */
function layoutSky(){
  var el=document.getElementById('uaeSky');if(!el||!on())return;
  var top1=70,H1=Math.max(260,innerHeight-top1-56);
  el.style.top=top1+'px';el.style.height=H1+'px';el.style.width=Math.min(innerWidth,Math.round(H1*600/980))+'px';
  el.style.transformOrigin='50% 100%';SKYF=flagBottomDoc()+4;scaleSky();
}
function scaleSky(){var el=document.getElementById('uaeSky');if(el)el.style.transform='translateX(-50%)';}
addEventListener('resize',layoutSky);

/* ===== skyline fireworks: Burj Khalifa (tip + cascading sides), Burj Al Arab, behind Ain Dubai ===== */
var bg=document.getElementById('uaeBg'),bx=bg.getContext('2d'),bp=[],braf=0,BW=0,BH=0,overT=0,overEnd=0,ambT=0;
function bsize(){BW=bg.width=innerWidth;BH=bg.height=innerHeight;}
addEventListener('resize',bsize);bsize();
function geo(){
  var r=document.getElementById('uaeSky').getBoundingClientRect(),sc=Math.min(r.width/600,r.height/980);
  var ox=r.left+(r.width-600*sc)/2,oy=r.bottom-980*sc;
  return function(x,y){return [ox+x*sc,oy+y*sc];};
}
var BCOL=['#FFE08A','#FFF3CF','#FF3B3B','#2FD36B','#FFFFFF','#FFC24A'];
function bpart(x,y,vx,vy,c,l,dec){if(bp.length>1100)return;bp.push({x:x,y:y,vx:vx,vy:vy,c:c,l:l||1,d:dec||.0075});}
function bburst(P,n,pw,c){n=Math.round(n*2.5);var c1=c||BCOL[(Math.random()*BCOL.length)|0];for(var i=0;i<n;i++){var a=Math.PI*2*i/n+Math.random()*.1,v=(.5+Math.random()*.5)*pw;bpart(P[0],P[1],Math.cos(a)*v,Math.sin(a)*v,Math.random()<.25?'#FFE08A':c1);}kick();}
function bspark(P,dir,n){n=Math.round(n*2.5);for(var i=0;i<n;i++){bpart(P[0],P[1],dir*(.4+Math.random()*1.1),-(.2+Math.random()*1.0),Math.random()<.5?'#FFC24A':'#FFF3CF',1,.006);}kick();}
function hdrB(){var h=document.querySelector('header');var r=h?h.getBoundingClientRect().bottom:0;return Math.max(0,Math.min(r,BH));}
function kick(){if(!braf)braf=requestAnimationFrame(btick);}
function btick(){
  bx.globalCompositeOperation='destination-out';bx.fillStyle='rgba(0,0,0,.28)';bx.fillRect(0,0,BW,BH);
  bx.globalCompositeOperation='source-over';
  var hh=hdrB();bx.save();bx.beginPath();bx.rect(0,hh,BW,BH-hh);bx.clip();
  bp=bp.filter(function(p){return p.l>0;});
  for(var i=0;i<bp.length;i++){var p=bp[i];p.x+=p.vx;p.y+=p.vy;p.vy+=.04;p.vx*=.988;p.l-=p.d;bx.globalAlpha=Math.max(p.l,0);bx.fillStyle=p.c;bx.fillRect(p.x,p.y,2.6,2.6);}
  bx.restore();bx.globalAlpha=1;
  if(bp.length&&!document.hidden){braf=requestAnimationFrame(btick);}else{braf=0;bx.clearRect(0,0,BW,BH);}
}
var LEDGE=[[22,34],[18,70],[14,108],[11,140],[8,172],[5,198]];
function fkKhTop(P){var t=P(320,980-264*3.6);bburst(t,46,3.4);setTimeout(function(){bburst(P(320,980-264*3.6),26,2,'#FFF3CF');},220);}
function fkKhSides(P){var k=0;(function go(){var L=LEDGE[(Math.random()*LEDGE.length)|0],s=Math.random()<.5?-1:1;
  var pt=P(320+s*L[0]*3.6,980-L[1]*3.6);bspark(pt,s,5);if(++k<30)setTimeout(go,60);})();}
function fkBaa(P){bburst(P(220,475),30,2.6);setTimeout(function(){bburst(P(173,560),22,2.2);},180);
  var k=0;(function go(){var pt=P(182+Math.random()*20,520+Math.random()*50);bspark(pt,-1,3);if(++k<20)setTimeout(go,65);})();}
function fkAin(P){var h=P(480,271),sc=P(585,271)[0]-h[0];var a=Math.random()*6.283,d=Math.random()*sc*.9;bburst([h[0]+Math.cos(a)*d,h[1]+Math.sin(a)*d],40,3);}
var FK=[fkKhTop,fkKhSides,fkBaa,fkAin,fkKhTop,fkAin];
function fire(){if(!on()||document.hidden)return;var P=geo();FK[(Math.random()*FK.length)|0](P);}
function overload(){
  if(!on())return;bsize();bg.classList.add('over');overEnd=Date.now()+17500;clearInterval(overT);
  var n=0;overT=setInterval(function(){fire();fire();fire();if(Date.now()>overEnd)stopOver();},120);
}
function stopOver(){clearInterval(overT);overT=0;bg.classList.remove('over');}
addEventListener('pointerdown',function(){if(overT)stopOver();},true);
clearInterval(ambT);ambT=setInterval(function(){if(!overT&&bp.length<500){fire();if(Math.random()<.5)fire();}},1040);

var FIMG='uae-founders.png';
var fw=document.querySelector('.uae-flagwrap'),si=0,lastUser=0,sx=null,sy=0,moved=false;
function setSlide(i){si=(i+3)%3;if(fw){fw.setAttribute('data-i',si);fw.style.setProperty('--i',si);}}
function slides(){
  if(!fw)return;
  if(on()){var im=fw.querySelector('.uae-fbox img');if(im&&!im.getAttribute('src'))im.src=FIMG;var z=fw.querySelector('.uae-zr img');if(z&&!z.getAttribute('src'))z.src='uae-zayed-rashid.jpg?v=2';}
  if(!fw.hasAttribute('data-i'))setSlide(0);
}
if(fw){
  fw.addEventListener('pointerdown',function(e){sx=e.clientX;sy=e.clientY;moved=false;});
  fw.addEventListener('pointermove',function(e){if(sx!==null&&Math.abs(e.clientX-sx)>12)moved=true;});
  fw.addEventListener('pointerup',function(e){
    if(sx===null)return;var dx=e.clientX-sx,dy=e.clientY-sy;sx=null;
    if(Math.abs(dy)>Math.abs(dx)&&Math.abs(dy)>30)return;
    lastUser=Date.now();
    if(Math.abs(dx)>40){setSlide(si+(dx<0?1:-1));}else{setSlide(si+1);}
  });
  fw.addEventListener('pointercancel',function(){sx=null;});
  setInterval(function(){if(on()&&!document.hidden&&!splOpen&&Date.now()-lastUser>20000)setSlide(si+1);},9000);
}
var spl=document.getElementById('uaeSplash'),splOpen=false;
function dayKey(){return new Date(now()+OFF).toISOString().slice(0,10);}
function splashSeen(){try{return localStorage.getItem('uaeSplashSeen')===dayKey();}catch(e){return false;}}
function openSplash(){
  if(!spl||splOpen)return;splOpen=true;
  var im=spl.querySelector('img');if(!im.getAttribute('src'))im.src=FIMG;
  spl.classList.add('show');void spl.offsetWidth;spl.classList.add('in');
  clearTimeout(openSplash.t);openSplash.t=setTimeout(closeSplash,9000);
}
function closeSplash(){
  if(!splOpen)return;splOpen=false;clearTimeout(openSplash.t);
  if(sim===null){try{localStorage.setItem('uaeSplashSeen',dayKey());}catch(e){}}
  spl.classList.remove('in');setTimeout(function(){spl.classList.remove('show');},650);
  if(on())setTimeout(overload,300);
}
document.getElementById('uaeSplashGo').onclick=closeSplash;
spl.addEventListener('pointerdown',function(e){if(e.target===spl)closeSplash();});
document.getElementById('uaeSpl').onclick=function(){if(!on()){picked=true;sim=sim===null?F_START:sim;apply();}openSplash();};
var _apply=apply,wasOn=false;apply=function(){_apply();slides();sky();watch();setTimeout(layoutSky,0);setTimeout(layoutSky,600);var o=on();if(o&&!wasOn){ if(state()==='forced'&&(sim!==null||!splashSeen())) setTimeout(openSplash,300); else setTimeout(overload,500); }if(!o){stopOver();bx.clearRect(0,0,BW,BH);bp=[];}wasOn=o;};
var UF=[["UAE", "The UAE was formed on 2 December 1971 by six emirates."], ["UAE", "Ras Al Khaimah became the seventh emirate on 10 February 1972."], ["UAE", "Sheikh Zayed bin Sultan Al Nahyan was the first President of the UAE."], ["UAE", "The flag was designed by Abdullah Mohammed Al Maainah in 1971."], ["UAE", "The dirham is pegged to the US dollar at 3.6725."], ["UAE", "The falcon is the national bird of the UAE."], ["UAE", "The Arabian oryx is the national animal of the UAE."], ["UAE", "The ghaf tree is the national tree of the UAE."], ["UAE", "The Hope Probe reached Mars orbit on 9 February 2021, a first for the Arab world."], ["UAE", "Hazza Al Mansouri became the first Emirati in space in September 2019."], ["Abu Dhabi", "Abu Dhabi is the capital and the largest emirate, about 87% of the UAE's land."], ["Abu Dhabi", "Sheikh Zayed Grand Mosque opened in 2007 and holds about 40,000 worshippers."], ["Abu Dhabi", "The Louvre Abu Dhabi opened in 2017 under a dome of 7,850 stars."], ["Abu Dhabi", "Yas Marina Circuit hosts the Formula 1 season finale in Abu Dhabi."], ["Abu Dhabi", "Al Ain's cultural sites became UNESCO World Heritage in 2011."], ["Abu Dhabi", "Al Ain is called the Garden City for its oases and green streets."], ["Dubai", "Burj Khalifa in Dubai is 828 metres tall and opened in 2010."], ["Dubai", "Dubai Metro opened on 9 September 2009, at 9:09 pm."], ["Dubai", "Dubai Creek was the old trading harbour where the city began."], ["Dubai", "Palm Jumeirah is an artificial island shaped like a palm tree."], ["Dubai", "The Museum of the Future in Dubai opened in 2022."], ["Dubai", "Dubai hosted Expo 2020 from October 2021 to March 2022."], ["Dubai", "Dubai International is among the world's busiest airports for international travel."], ["Sharjah", "Sharjah was UNESCO World Book Capital in 2019."], ["Sharjah", "Sharjah has coasts on both the Arabian Gulf and the Gulf of Oman."], ["Sharjah", "The Sharjah International Book Fair is one of the largest in the world."], ["Sharjah", "Sharjah is known as the cultural capital of the UAE."], ["Ajman", "Ajman is the smallest of the seven emirates."], ["Ajman", "Ajman Museum is inside a fort built in the late 1700s."], ["Ajman", "Ajman has a long tradition of building wooden dhows."], ["Umm Al Quwain", "Umm Al Quwain is the second smallest emirate."], ["Umm Al Quwain", "Khor Al Beidah in Umm Al Quwain has mangroves and rich birdlife."], ["Umm Al Quwain", "Ed-Dur in Umm Al Quwain is an ancient trading site about 2,000 years old."], ["Ras Al Khaimah", "Jebel Jais is the UAE's highest peak at about 1,934 metres."], ["Ras Al Khaimah", "Jebel Jais has a 2.83 km zipline, one of the longest in the world."], ["Ras Al Khaimah", "Ras Al Khaimah is the northernmost of the seven emirates."], ["Ras Al Khaimah", "Julfar, near Ras Al Khaimah, was a major trading port in the Middle Ages."], ["Fujairah", "Fujairah is the only emirate entirely on the Gulf of Oman coast."], ["Fujairah", "Al Bidyah Mosque in Fujairah is believed to be the oldest in the UAE."], ["Fujairah", "Fujairah is one of the world's busiest ship refuelling ports."], ["Fujairah", "Snoopy Island near Fujairah is a popular snorkelling spot."]];
(function(){
  var box=document.getElementById('uaeEm');if(!box)return;
  var tiles=[].slice.call(box.querySelectorAll('.uae-em')),q=[],shown=[];
  function sh(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t;}return a;}
  function next(){
    for(var n=0;n<UF.length*2;n++){
      if(!q.length)q=sh(UF.map(function(_,i){return i;}));
      var k=q.shift();if(shown.indexOf(k)<0)return k;
    }
    return 0;
  }
  function put(i,anim){
    var t=tiles[i],old=shown[i],k=next();shown[i]=k;
    function w(){t.innerHTML='<b>'+UF[k][0]+'</b><span>'+UF[k][1]+'</span>';}
    if(anim){t.classList.add('fade');setTimeout(function(){w();t.classList.remove('fade');},460);}else w();
  }
  tiles.forEach(function(_,i){shown[i]=-1;});
  tiles.forEach(function(_,i){put(i,false);});
  var c=0;
  setInterval(function(){if(document.hidden)return;put(c%tiles.length,true);c++;},2600);
})();
apply();

setInterval(function(){subtitle();ribbon();},30000);
})();
</script>
'''

out = src
HTML = HTML.replace('__SKY__', '<div id="uaeSky" aria-hidden="true">' + uae_sky.SVG + '</div>')
out = out.replace('<head>', '<head>\n<meta name="robots" content="noindex,nofollow">', 1)
out = out.replace('</head>', CSS + '</head>', 1)
out = out.replace('</body>', '<template id="uaeFlagTpl">' + FLAG + '</template>' + HTML + JS + '</body>', 1)
(root/'uae-lab.html').write_text(out, encoding='utf-8')
print('uae-lab.html', len(out))
