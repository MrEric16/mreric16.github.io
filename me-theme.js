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
  /* real recorded samples (sounds/me-monkey.mp3, sounds/me-donkey.mp3), decoded once and played through Web Audio */
  var bufs = {}, loading = {};
  var FILES = { good: ['sounds/me-monkey.mp3', 1.1], bad: ['sounds/me-donkey.mp3', 1.6] };
  function base(){ try{ var sc = document.querySelector('script[src$="me-theme.js"]'); return sc ? sc.src.replace(/me-theme\.js.*$/, '') : ''; }catch(e){ return ''; } }
  function load(kind, cb){
    if(bufs[kind]) return cb(bufs[kind]);
    if(loading[kind]) { loading[kind].push(cb); return; }
    var c = audio(); if(!c) return;
    loading[kind] = [cb];
    fetch(base() + FILES[kind][0]).then(function(r){ return r.arrayBuffer(); }).then(function(ab){
      return new Promise(function(res, rej){ c.decodeAudioData(ab, res, rej); });
    }).then(function(b){ bufs[kind] = b; var q = loading[kind]; loading[kind] = null; q.forEach(function(f){ f(b); }); })
      .catch(function(){ loading[kind] = null; });
  }
  function preload(){ if(on() && soundOn()){ load('good', function(){}); load('bad', function(){}); } }
  function play(kind, force){
    if(!on() || !soundOn() || document.hidden) return;
    var nowMs = Date.now();
    if(!force && nowMs - last < 1100) return;
    var c = audio(); if(!c) return;
    if(c.state === 'suspended') try{ c.resume(); }catch(e){}
    last = nowMs;
    window.__meLast = kind;
    load(kind, function(b){
      var src = c.createBufferSource(); src.buffer = b;
      var g = c.createGain(); g.gain.value = FILES[kind][1] * 0.8;
      src.connect(g); g.connect(c.destination); src.start();
    });
  }
  window.MEplay = play;

  /* tappable mascots in the header (index.html only): monkey left, donkey right */
  function mascots(){
    var h = document.querySelector('header');
    var want = on() && h && document.getElementById('app') !== null && /(^|\/)(index\.html)?$/.test(location.pathname);
    var ex = document.querySelectorAll('.me-mascot');
    if(!want){ ex.forEach(function(e){ e.remove(); }); var pl = document.querySelector('.me-pill'); if(pl) pl.remove(); return; }
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
    var pill = document.createElement('button'); pill.type = 'button'; pill.className = 'me-pill'; pill.setAttribute('aria-label', 'Banana Catch game');
    pill.addEventListener('click', function(ev){ ev.stopPropagation(); openGame(); });
    h.appendChild(pill); paintPill();
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
    if(kind){ record(kind); play(kind); }
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


  /* ---------- shared extra CSS (pill, falling bananas, game, cross-header swing) ---------- */
  (function(){
    if(document.getElementById('me-extra')) return;
    var st = document.createElement('style'); st.id = 'me-extra';
    st.textContent =
      '.me-pill{position:absolute;z-index:3;top:12px;left:50%;transform:translateX(-50%);padding:3px 10px;border-radius:999px;border:0;background:rgba(0,0,0,.26);color:#fff8e1;font:700 12px/1.4 "Nunito",system-ui,sans-serif;white-space:pre;cursor:pointer;-webkit-tap-highlight-color:transparent}' +
      '.me-fall{position:fixed;top:-40px;z-index:9998;pointer-events:none;animation:me-fall 2.6s ease-in forwards}' +
      '@keyframes me-fall{to{transform:translateY(110vh) rotate(260deg);opacity:.9}}' +
      '.me-monkey.me-cross{animation:me-cross 2.4s ease-in-out}' +
      '@keyframes me-cross{0%{transform:translateX(0) rotate(0)}25%{transform:translateX(calc(50vw - 40px)) rotate(-25deg) translateY(14px)}50%{transform:translateX(calc(100vw - 100px)) rotate(20deg)}75%{transform:translateX(calc(50vw - 40px)) rotate(-20deg) translateY(10px)}100%{transform:translateX(0) rotate(0)}}' +
      '.me-game{position:fixed;inset:0;z-index:10000;background:#1f3a17;display:flex;flex-direction:column;color:#fff8e1;font-family:"Nunito",system-ui,sans-serif;touch-action:manipulation;user-select:none;-webkit-user-select:none}' +
      '.me-g-bar{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;font-weight:800;font-size:22px}' +
      '.me-g-x{background:none;border:0;color:inherit;font-size:24px;cursor:pointer;padding:4px 10px}' +
      '.me-g-area{position:relative;flex:1;overflow:hidden}' +
      '.me-g-msg{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center;font-size:18px}' +
      '.me-g-h{font-size:34px;font-weight:900}.me-g-b{opacity:.75;font-size:15px}' +
      '.me-g-go{padding:10px 30px;border-radius:999px;border:0;background:#F4C430;color:#2B3A1F;font:800 18px inherit;cursor:pointer}' +
      '.me-g-item{position:absolute;top:-60px;width:54px;height:54px;font-size:44px;line-height:54px;text-align:center;background:center/contain no-repeat;animation:me-gfall 3s linear forwards;cursor:pointer;touch-action:manipulation}' +
      '@keyframes me-gfall{to{transform:translateY(calc(100vh + 60px))}}' +
      '.me-g-pop{transition:transform .15s,opacity .15s;opacity:0;scale:1.4}';
    (document.head || document.documentElement).appendChild(st);
  })();
  /* ---------- scoreboard + streak (items 3 & 4) ---------- */
  var recLast = 0, tapN = 0, tapT = 0;
  function dayKey(){ var d = new Date(); return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate(); }
  function stats(){
    var o; try{ o = JSON.parse(localStorage.getItem('me_stats') || '{}'); }catch(e){ o = {}; }
    if(o.day !== dayKey()){ o.day = dayKey(); o.g = 0; o.b = 0; }
    o.streak = o.streak || 0; o.best = o.best || 0; return o;
  }
  function saveStats(o){ try{ localStorage.setItem('me_stats', JSON.stringify(o)); }catch(e){} }
  function paintPill(){
    var el = document.querySelector('.me-pill'); if(!el) return;
    var o = stats();
    el.textContent = '🐒 ' + o.g + '  ·  🐴 ' + o.b + (o.streak >= 2 ? '  ·  🔥 ' + o.streak : '');
  }
  function boing(cls){
    var m = document.querySelector('.' + cls); if(!m) return;
    m.classList.remove('me-boing'); void m.offsetWidth; m.classList.add('me-boing');
  }
  function record(kind){
    var t = Date.now(); if(t - recLast < 1100) return; recLast = t;
    var o = stats();
    if(kind === 'bad'){ o.b++; o.streak = 0; boing('me-donkey'); }
    else { o.g++; o.streak++; if(o.streak > o.best) o.best = o.streak; boing('me-monkey'); if(o.streak && o.streak % 5 === 0) rain(6); }
    saveStats(o); paintPill();
  }

  /* ---------- banana rain on level-up (item 6) and the swing-across easter egg (item 5) ---------- */
  var reduced = false; try{ reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches; }catch(e){}
  function rain(n){
    if(reduced || !document.body) return;
    for(var i = 0; i < n; i++){
      var b = document.createElement('div'); b.className = 'me-fall'; b.textContent = '🍌';
      b.style.left = (4 + Math.random() * 88) + '%'; b.style.animationDelay = (Math.random() * .9) + 's'; b.style.fontSize = (20 + Math.random() * 14) + 'px';
      b.addEventListener('animationend', function(){ this.remove(); });
      document.body.appendChild(b);
    }
  }
  function watchLevel(){
    var chip = document.getElementById('xpChip'); if(!chip){ if(++lvTries < 20) setTimeout(watchLevel, 1000); return; }
    var read = function(){ var m = /Lv\s*(\d+)/.exec(chip.textContent || ''); return m ? +m[1] : 0; };
    var lv = read();
    new MutationObserver(function(){ var n = read(); if(n && lv && n > lv){ rain(16); if(on()) play('good', true); } if(n) lv = n; })
      .observe(chip, { childList: true, subtree: true, characterData: true });
  }
  var lvTries = 0;
  function swingAcross(){
    var m = document.querySelector('.me-monkey'); if(!m || reduced) return;
    m.classList.remove('me-cross'); void m.offsetWidth; m.classList.add('me-cross');
    play('good', true);
    setTimeout(function(){ m.classList.remove('me-cross'); }, 2600);
  }
  // 10 quick taps on either mascot
  document.addEventListener('click', function(ev){
    var t = ev.target && ev.target.closest && ev.target.closest('.me-mascot'); if(!t) return;
    var n = Date.now(); tapN = (n - tapT < 1500) ? tapN + 1 : 1; tapT = n;
    if(tapN >= 10){ tapN = 0; swingAcross(); }
  }, true);

  /* ---------- Banana Catch (item 2) ---------- */
  function openGame(){
    if(document.getElementById('meGame')) return;
    var best = 0; try{ best = +localStorage.getItem('me_catch_best') || 0; }catch(e){}
    var don = ''; var dn = document.querySelector('.me-donkey'); if(dn) don = getComputedStyle(dn).backgroundImage;
    var ov = document.createElement('div'); ov.id = 'meGame'; ov.className = 'me-game';
    ov.innerHTML = '<div class="me-g-bar"><span id="meGS">0</span><span id="meGT">30</span><button type="button" class="me-g-x" aria-label="Close">✕</button></div>' +
      '<div class="me-g-area" id="meGA"><div class="me-g-msg" id="meGM"><div class="me-g-h">Banana Catch</div><div>Tap 🍌   Avoid the donkey</div><div class="me-g-b">Best: ' + best + '</div><button type="button" class="me-g-go">Start</button></div></div>';
    document.body.appendChild(ov);
    var area = ov.querySelector('#meGA'), msg = ov.querySelector('#meGM'), sEl = ov.querySelector('#meGS'), tEl = ov.querySelector('#meGT');
    var score = 0, left = 30, tick = 0, spawn = 0, run = false;
    function stop(){ run = false; clearInterval(tick); clearTimeout(spawn); }
    function close(){ stop(); ov.remove(); }
    ov.querySelector('.me-g-x').onclick = close;
    function put(){
      if(!run) return;
      var isD = Math.random() < .2, e = document.createElement('div');
      e.className = 'me-g-item' + (isD ? ' me-g-d' : '');
      if(isD){ if(don) e.style.backgroundImage = don; else e.textContent = '🐴'; } else e.textContent = '🍌';
      e.style.left = (4 + Math.random() * 80) + '%'; e.style.animationDuration = (2.2 + Math.random() * 1.2) + 's';
      e.addEventListener('animationend', function(){ e.remove(); });
      e.addEventListener('pointerdown', function(ev){
        ev.preventDefault(); if(!run || e.dataset.hit) return; e.dataset.hit = 1;
        if(isD){ score = Math.max(0, score - 3); play('bad', true); e.classList.add('me-g-pop'); }
        else { score++; e.classList.add('me-g-pop'); }
        sEl.textContent = score; setTimeout(function(){ e.remove(); }, 160);
      });
      area.appendChild(e);
      spawn = setTimeout(put, 380 + Math.random() * 380);
    }
    var startRound = function(){
      msg.style.display = 'none'; area.querySelectorAll('.me-g-item').forEach(function(x){ x.remove(); });
      score = 0; left = 30; sEl.textContent = 0; tEl.textContent = 30; run = true; put();
      tick = setInterval(function(){
        left -= .1; tEl.textContent = Math.max(0, Math.ceil(left));
        if(left <= 0){
          stop(); area.querySelectorAll('.me-g-item').forEach(function(x){ x.remove(); });
          var nb = score > best; if(nb){ best = score; try{ localStorage.setItem('me_catch_best', best); }catch(e){} play('good', true); }
          msg.innerHTML = '<div class="me-g-h">' + score + ' 🍌</div><div>' + (nb ? 'New best!' : 'Best: ' + best) + '</div><button type="button" class="me-g-go">Again</button>';
          msg.style.display = ''; msg.querySelector('.me-g-go').onclick = startRound;
        }
      }, 100);
    };
    ov.querySelector('.me-g-go').onclick = startRound;
  }
  window.MEgame = openGame;

  /* ---------- ambience (item 9): very quiet crickets (night) / birds (day), off by default ---------- */
  var ambT = 0;
  function ambOn(){ try{ return localStorage.getItem('me_amb') === '1'; }catch(e){ return false; } }
  function chirp(c, t, f0, f1, dur, g){
    var o = c.createOscillator(), a = c.createGain(); o.type = 'sine';
    o.frequency.setValueAtTime(f0, t); o.frequency.linearRampToValueAtTime(f1, t + dur);
    a.gain.setValueAtTime(0.0001, t); a.gain.linearRampToValueAtTime(g, t + dur * .3); a.gain.linearRampToValueAtTime(0.0001, t + dur);
    o.connect(a); a.connect(c.destination); o.start(t); o.stop(t + dur + .02);
  }
  function ambTick(){
    clearTimeout(ambT);
    if(!on() || !ambOn()) return;
    var c = ctx;
    if(c && c.state === 'running' && !document.hidden){
      var t = c.currentTime + .02, night = themeKey() === 'dme';
      if(night){ for(var i = 0; i < 3; i++) chirp(c, t + i * .075, 4300, 4500, .045, .012); }
      else { var f = 2200 + Math.random() * 900; chirp(c, t, f, f + 700, .11, .014); chirp(c, t + .15, f + 500, f - 150, .13, .012); }
    }
    ambT = setTimeout(ambTick, night_gap());
  }
  function night_gap(){ return themeKey() === 'dme' ? 1800 + Math.random() * 2600 : 3500 + Math.random() * 5500; }
  window.MEtheme.ambOn = ambOn;
  window.MEtheme.setAmb = function(v){ try{ localStorage.setItem('me_amb', v ? '1' : '0'); }catch(e){} if(v){ audio(); if(ctx && ctx.state === 'suspended') try{ ctx.resume(); }catch(e){} ambTick(); } else clearTimeout(ambT); };

  // index.html switches themes live: begin listening the moment M&E is picked
  window.addEventListener('themechange', function(){ if(on()) start(); mascots(); ambTick(); preload(); });
  if(on()){ start(); ambTick(); preload(); }
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', watchLevel); else watchLevel();
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mascots); else mascots();
})();
