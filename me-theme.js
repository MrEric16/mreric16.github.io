/* M&E theme (Maymun & Eshak = Monkey & Donkey) - shared by index.html and every sub-page.
   Does NOTHING unless the saved theme is 'me' (jungle) or 'dme' (night barn), so all other themes are untouched.
   1. Palette for sub-pages (index.html carries its own, richer CSS).
   2. Answer sounds: a short monkey chirp for a right answer, a donkey hee-haw for a wrong one - synthesised
      with Web Audio (no audio files, nothing to download), quiet, throttled, only after a tap/keypress.
   3. Bananas instead of XP (read by lounge-core.js through window.MEUnit).
   Sound on/off: localStorage 'me_sound' ('0' = off), switchable from the theme picker. */
(function(){
  'use strict';
  function themeKey(){ try{ return localStorage.getItem('themeChoice') || ''; }catch(e){ return ''; } }
  function on(){ var k = themeKey(); return k === 'me' || k === 'dme'; }
  function soundOn(){ try{ return localStorage.getItem('me_sound') !== '0'; }catch(e){ return true; } }
  window.MEUnit = function(){ return on() ? '🍌' : 'XP'; };
  window.MEtheme = { on: on, soundOn: soundOn, setSound: function(v){ try{ localStorage.setItem('me_sound', v ? '1' : '0'); }catch(e){} } };
  var started = false;

  /* ---------- 1. palette for sub-pages ---------- */
  if(on() && !/(^|\/)(index\.html)?$/.test(location.pathname) && !document.getElementById('me-palette')){
    var st = document.createElement('style'); st.id = 'me-palette';
    st.textContent =
      'body.usertheme-me:not(.dark-mode){--cream:#EFF3DA;--cream-2:#E4EBC4;--card:#FBFCEF;--ink:#2B3A1F;--ink-soft:#5C6B3F;--coral:#3F8F4B;--coral-dark:#2D6B38;--gold:#F2C230;--teal:#B8793A;--line:rgba(63,143,75,.32);--board-bg:rgba(251,252,239,.9)}' +
      'body.usertheme-dme.dark-mode{--cream:#241A12;--cream-2:#1B130D;--card:#33251A;--ink:#F3E6CF;--ink-soft:#CDB48A;--coral:#D9923F;--coral-dark:#B3741F;--gold:#F2C230;--teal:#8FB58A;--line:rgba(217,146,63,.35);--board-bg:rgba(36,26,18,.92)}';
    (document.head || document.documentElement).appendChild(st);
  }

  /* ---------- 2. sounds ---------- */
  var ctx = null, last = 0, gestureAt = 0, pend = { good: false, bad: false }, timer = 0;
  function audio(){
    if(ctx) return ctx;
    var C = window.AudioContext || window.webkitAudioContext;
    if(!C) return null;
    try{ ctx = new C(); }catch(e){ ctx = null; }
    return ctx;
  }
  /* One animal voice: a buzzy (sawtooth) source whose pitch follows a curve, wobbled by jitter, chopped by a
     rough amplitude flutter (the "rattle" of a bray / chatter), pushed through two or three formant filters
     (the throat/mouth shape) and a touch of breath noise. pts = [[seconds, Hz], ...] */
  var noiseBuf = null;
  function noise(c){
    if(noiseBuf) return noiseBuf;
    noiseBuf = c.createBuffer(1, c.sampleRate, c.sampleRate);
    var d = noiseBuf.getChannelData(0); for(var i = 0; i < d.length; i++) d[i] = Math.random() * 2 - 1;
    return noiseBuf;
  }
  function animal(c, out, t0, dur, pts, o){
    var src = c.createOscillator(); src.type = 'sawtooth';
    src.frequency.setValueAtTime(pts[0][1], t0);
    for(var i = 1; i < pts.length; i++) src.frequency.linearRampToValueAtTime(pts[i][1], t0 + pts[i][0]);
    // pitch jitter
    var jl = c.createOscillator(), jg = c.createGain(); jl.frequency.value = o.jit || 9; jg.gain.value = (o.jitDepth || 0.025) * pts[0][1] * 2;
    jl.connect(jg); jg.connect(src.frequency);
    // rough flutter (amplitude)
    var amp = c.createGain(); amp.gain.value = 1 - (o.rough || 0) / 2;
    if(o.rough){
      var rl = c.createOscillator(), rg = c.createGain(); rl.type = 'square'; rl.frequency.value = o.roughHz || 28; rg.gain.value = o.rough / 2;
      rl.connect(rg); rg.connect(amp.gain); rl.start(t0); rl.stop(t0 + dur + .05);
    }
    // grit
    var sh = c.createWaveShaper(), n = 256, cu = new Float32Array(n);
    for(var k = 0; k < n; k++){ var x = k * 2 / n - 1; cu[k] = Math.tanh(x * (o.drive || 2.2)); }
    sh.curve = cu;
    // envelope
    var env = c.createGain();
    env.gain.setValueAtTime(0.0001, t0);
    env.gain.exponentialRampToValueAtTime(o.peak, t0 + Math.min(.06, dur * .3));
    env.gain.setValueAtTime(o.peak, t0 + dur * .72);
    env.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
    src.connect(sh); sh.connect(amp);
    // parallel formants
    (o.formants || [[800, 1]]).forEach(function(fm){
      var f = c.createBiquadFilter(); f.type = 'bandpass'; f.Q.value = fm[2] || 4;
      if(fm[3]){ f.frequency.setValueAtTime(fm[0], t0); f.frequency.linearRampToValueAtTime(fm[3], t0 + dur); } else f.frequency.value = fm[0];
      var g = c.createGain(); g.gain.value = fm[1];
      amp.connect(f); f.connect(g); g.connect(env);
    });
    // breath
    if(o.breath){
      var ns = c.createBufferSource(); ns.buffer = noise(c); ns.loop = true;
      var nf = c.createBiquadFilter(); nf.type = 'bandpass'; nf.frequency.value = o.breathHz || 1800; nf.Q.value = .8;
      var ng = c.createGain(); ng.gain.value = o.breath;
      ns.connect(nf); nf.connect(ng); ng.connect(env); ns.start(t0); ns.stop(t0 + dur + .05);
    }
    env.connect(out);
    src.start(t0); src.stop(t0 + dur + .05); jl.start(t0); jl.stop(t0 + dur + .05);
  }
  /* right answer: monkey - "oo-oo-oo" hoots then excited "ee-ee-ee-ee" chatter */
  function monkey(c, out, t){
    [0, .21, .42].forEach(function(d, i){
      animal(c, out, t + d, .17, [[0, 360 + i * 25], [.17, 300 + i * 20]], { peak: .5, rough: .25, roughHz: 40, drive: 1.6, jit: 7, jitDepth: .03,
        formants: [[420, 1, 5], [950, .7, 5]], breath: .05, breathHz: 900 });
    });
    [0, .1, .2, .3].forEach(function(d, i){
      animal(c, out, t + .70 + d, .085, [[0, 850 + i * 60], [.085, 1500 + i * 70]], { peak: .45, rough: .3, roughHz: 55, drive: 2, jit: 14, jitDepth: .035,
        formants: [[1100, .8, 6], [2700, 1, 6]], breath: .08, breathHz: 3200 });
    });
  }
  /* wrong answer: donkey - "hee" (inhaled, rising squeal) then a long, rattly, falling "HAW", then a short echo "haw" */
  function donkey(c, out, t){
    animal(c, out, t, .50, [[0, 420], [.30, 880], [.50, 760]], { peak: .5, rough: .5, roughHz: 34, drive: 3, jit: 11, jitDepth: .03,
      formants: [[850, 1, 4], [2100, .8, 5, 1700]], breath: .10, breathHz: 2400 });
    animal(c, out, t + .52, .78, [[0, 500], [.10, 440], [.45, 260], [.78, 170]], { peak: .62, rough: .6, roughHz: 26, drive: 3.4, jit: 8, jitDepth: .04,
      formants: [[520, 1, 3.5], [1250, .8, 4, 800]], breath: .06, breathHz: 1200 });
    animal(c, out, t + 1.38, .34, [[0, 330], [.34, 190]], { peak: .34, rough: .55, roughHz: 28, drive: 3, jit: 8, jitDepth: .04,
      formants: [[520, 1, 3.5], [1100, .8, 4]] });
  }
  function play(kind, force){
    if(!on() || !soundOn() || document.hidden) return;
    var nowMs = Date.now();
    if(!force && nowMs - last < 1100) return;
    var c = audio(); if(!c) return;
    if(c.state === 'suspended') try{ c.resume(); }catch(e){}
    last = nowMs;
    var comp = c.createDynamicsCompressor(); comp.connect(c.destination);
    var out = c.createGain(); out.gain.value = .85; out.connect(comp);
    var t = c.currentTime + .03;
    if(kind === 'bad') donkey(c, out, t); else monkey(c, out, t);
    window.__meLast = kind;
  }
  window.MEplay = play;

  /* tappable mascots in the header (index.html only): monkey left, donkey right */
  function mascots(){
    var h = document.querySelector('header');
    var want = on() && h && document.getElementById('app') !== null && /(^|\/)(index\.html)?$/.test(location.pathname);
    var ex = document.querySelectorAll('.me-mascot');
    if(!want){ ex.forEach(function(e){ e.remove(); }); return; }
    if(ex.length) return;
    [['me-monkey', '🐒', 'good', 'Monkey'], ['me-donkey', '', 'bad', 'Donkey']].forEach(function(d){
      var b = document.createElement('button'); b.type = 'button'; b.className = 'me-mascot ' + d[0]; b.textContent = d[1]; b.setAttribute('aria-label', d[3]);
      b.addEventListener('click', function(ev){
        ev.stopPropagation();
        b.classList.remove('me-boing'); void b.offsetWidth; b.classList.add('me-boing');
        play(d[2], true);
      });
      h.appendChild(b);
    });
  }

  var GOOD = /(^|-)(correct|ok|good|right)$/;
  var BAD  = /(^|-)(wrong|incorrect|bad)$/;
  var SKIP = /^(gg-banner-ok|fg-review-wrong|safety-ok|save-good|top-right|bottom-right|tetris-right|down-right|up-right|margin-right|padding-right|border-right|text-right|float-right|align-right|justify-right)$/;
  function scan(cls){
    if(!cls) return;
    var parts = String(cls).split(/\s+/);
    for(var i = 0; i < parts.length; i++){
      var p = parts[i];
      if(!p || SKIP.test(p)) continue;
      if(BAD.test(p)) pend.bad = true;
      else if(GOOD.test(p)) pend.good = true;
    }
  }
  function scanNode(n){
    if(n.nodeType !== 1) return;
    scan(n.className && n.className.baseVal !== undefined ? n.className.baseVal : n.className);
    if(n.querySelectorAll && n.children && n.children.length && n.children.length < 60){
      var q = n.querySelectorAll('[class*="correct"],[class*="wrong"],[class*="incorrect"],[class*="-ok"],[class*="-bad"],.ok,.bad,.good,.right');
      for(var i = 0; i < q.length && i < 40; i++) scan(q[i].className && q[i].className.baseVal !== undefined ? q[i].className.baseVal : q[i].className);
    }
  }
  function flush(){
    timer = 0;
    var kind = pend.bad ? 'bad' : (pend.good ? 'good' : '');
    pend.bad = pend.good = false;
    if(kind) play(kind);
  }
  function stamp(){ gestureAt = Date.now(); }
  ['pointerdown', 'keydown', 'touchstart', 'click'].forEach(function(ev){ document.addEventListener(ev, stamp, true); });
  document.addEventListener('pointerdown', function(){ var c = audio(); if(c && c.state === 'suspended') try{ c.resume(); }catch(e){} }, true);
  document.addEventListener('keydown', function(){ var c = audio(); if(c && c.state === 'suspended') try{ c.resume(); }catch(e){} }, true);

  function start(){
    if(started) return;
    if(!document.body) return setTimeout(start, 50);
    started = true;
    var mo = new MutationObserver(function(list){
      // only react to marks that appear shortly after the student's own tap / keypress
      if(Date.now() - gestureAt > 1800) return;
      for(var i = 0; i < list.length; i++){
        var m = list[i];
        if(m.type === 'attributes'){
          var now = m.target.className && m.target.className.baseVal !== undefined ? m.target.className.baseVal : m.target.className;
          var was = m.oldValue || '';
          if(now !== was) scan(String(now).split(/\s+/).filter(function(x){ return was.split(/\s+/).indexOf(x) === -1; }).join(' '));
        } else {
          for(var j = 0; j < m.addedNodes.length; j++) scanNode(m.addedNodes[j]);
        }
      }
      if((pend.good || pend.bad) && !timer) timer = setTimeout(flush, 120);
    });
    mo.observe(document.body, { subtree: true, childList: true, attributes: true, attributeFilter: ['class'], attributeOldValue: true });
  }
  // index.html switches themes live: begin listening the moment M&E is picked
  window.addEventListener('themechange', function(){ if(on()) start(); mascots(); });
  if(on()) start();
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mascots); else mascots();
})();
