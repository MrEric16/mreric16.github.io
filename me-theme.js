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
  function voice(c, out, type, t0, dur, f0, f1, peak, formant, vib){
    var o = c.createOscillator(), g = c.createGain(), f = c.createBiquadFilter();
    o.type = type;
    o.frequency.setValueAtTime(f0, t0);
    o.frequency.exponentialRampToValueAtTime(Math.max(30, f1), t0 + dur);
    if(vib){
      var l = c.createOscillator(), lg = c.createGain();
      l.frequency.value = vib; lg.gain.value = f0 * 0.018; l.connect(lg); lg.connect(o.frequency); l.start(t0); l.stop(t0 + dur + .05);
    }
    f.type = 'bandpass'; f.frequency.value = formant; f.Q.value = 2.2;
    g.gain.setValueAtTime(0.0001, t0);
    g.gain.exponentialRampToValueAtTime(peak, t0 + Math.min(.05, dur * .25));
    g.gain.setValueAtTime(peak, t0 + dur * .7);
    g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
    o.connect(f); f.connect(g); g.connect(out);
    o.start(t0); o.stop(t0 + dur + .05);
  }
  /* right answer: "oo-oo-ah!" - three quick rising monkey chirps */
  function monkey(c, out, t){
    voice(c, out, 'triangle', t,        .11, 520, 780, .65, 1500);
    voice(c, out, 'triangle', t + .15,  .11, 560, 840, .65, 1600);
    voice(c, out, 'triangle', t + .30,  .20, 620, 1050, .72, 1900, 9);
  }
  /* wrong answer: "hee-HAW" - inhale glide up, then a long falling bray */
  function donkey(c, out, t){
    voice(c, out, 'sawtooth', t,       .26, 330, 700, .4, 1300, 7);
    voice(c, out, 'sawtooth', t + .30, .50, 560, 215, .48, 900, 8);
  }
  function play(kind){
    if(!on() || !soundOn() || document.hidden) return;
    var nowMs = Date.now();
    if(nowMs - last < 1100) return;
    var c = audio(); if(!c) return;
    if(c.state === 'suspended') try{ c.resume(); }catch(e){}
    last = nowMs;
    var out = c.createGain(); out.gain.value = 1; out.connect(c.destination);
    var t = c.currentTime + .02;
    if(kind === 'bad') donkey(c, out, t); else monkey(c, out, t);
    window.__meLast = kind;
  }
  window.MEplay = play;

  /* tokens that mark a checked answer. A wrong mark beats a right mark in the same moment
     (a wrong tap usually also highlights the right option in green). */
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
  window.addEventListener('themechange', function(){ if(on()) start(); });
  if(on()) start();
})();
