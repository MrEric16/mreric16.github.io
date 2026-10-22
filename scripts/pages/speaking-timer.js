var BACK = back('index.html', 'Back to the Lounge');
var cfg = lsGet('spTimerCfg', { prep: 30, talk: 60 });
var tab = lsGet('spTimerTab', 'timer');
var oops = 0;                       // mistakes this round (not saved: every student starts fresh)
var run = null, tick = null, actx = null;   // run = {phase:'prep'|'talk', end:ms}
var sw = { t0: 0, acc: 0, on: false };
function fmt(ms){ var s = Math.max(0, Math.ceil(ms / 1000)); return String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'); }
function fmtSw(ms){ var t = Math.floor(ms / 10), cs = t % 100, s = Math.floor(t / 100) % 60, m = Math.floor(t / 6000); return String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0') + '.' + String(cs).padStart(2, '0'); }
function beep(n, hz){
  try{
    actx = actx || new (window.AudioContext || window.webkitAudioContext)();
    for(var i = 0; i < n; i++){
      var o = actx.createOscillator(), g = actx.createGain(); o.frequency.value = hz || 880; o.connect(g); g.connect(actx.destination);
      var t = actx.currentTime + i * 0.3; g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.3, t + 0.02); g.gain.exponentialRampToValueAtTime(0.0001, t + 0.22); o.start(t); o.stop(t + 0.25);
    }
  }catch(e){}
}
function num(id, d){ var v = parseInt(document.getElementById(id).value, 10); return v > 0 && v <= 3600 ? v : d; }
function render(){
  var h = BACK + head('Speaking Timer');
  h += '<div class="st-tabs"><button data-t="timer" class="' + (tab === 'timer' ? 'on' : '') + '">Timer</button><button data-t="sw" class="' + (tab === 'sw' ? 'on' : '') + '">Stopwatch</button></div>';
  if(tab === 'timer'){
    h += '<div class="st-set"><label>Prepare (sec)<input id="stPrep" type="number" min="1" max="3600" inputmode="numeric" value="' + cfg.prep + '"></label>' +
         '<label>Speak (sec)<input id="stTalk" type="number" min="1" max="3600" inputmode="numeric" value="' + cfg.talk + '"></label></div>';
    h += '<div class="st-phase" id="stPhase"></div><div class="st-clock" id="stClock"></div><div class="mt-bar"><i id="stBar"></i></div>';
    h += '<div class="v-row"><button class="v-btn" id="stGo">Prepare</button><button class="v-btn alt" id="stReset">Reset</button></div>';
    h += '<div class="st-oops"><div class="st-mark"><b id="stMark"></b><span>/ 10</span></div>' +
         '<div class="st-oops-row"><button class="st-pill" id="stOops">oops</button><button class="st-undo" id="stUndo" aria-label="Undo one oops">−1</button><button class="st-undo" id="stZero">Clear</button></div>' +
         '<div class="st-sub" id="stSub"></div></div>';
  } else {
    h += '<div class="st-clock" id="swClock"></div><div class="v-row"><button class="v-btn" id="swGo"></button><button class="v-btn alt" id="swReset">Reset</button></div>';
  }
  app.innerHTML = h;
  app.querySelectorAll('[data-t]').forEach(function(b){ b.onclick = function(){ tab = b.getAttribute('data-t'); lsSet('spTimerTab', tab); render(); }; });
  if(tab === 'timer'){
    document.getElementById('stGo').onclick = go;
    document.getElementById('stReset').onclick = reset;
    document.getElementById('stOops').onclick = function(){ oops++; paintOops(); if(navigator.vibrate) try{ navigator.vibrate(15); }catch(e){} };
    document.getElementById('stUndo').onclick = function(){ if(oops > 0){ oops--; paintOops(); } };
    document.getElementById('stZero').onclick = function(){ oops = 0; paintOops(); };
    ['stPrep', 'stTalk'].forEach(function(id){ document.getElementById(id).onchange = saveCfg; });
    paint(); paintOops();
  } else {
    document.getElementById('swGo').onclick = function(){ if(sw.on){ sw.acc += Date.now() - sw.t0; sw.on = false; } else { sw.t0 = Date.now(); sw.on = true; } paintSw(); };
    document.getElementById('swReset').onclick = function(){ sw = { t0: 0, acc: 0, on: false }; paintSw(); };
    paintSw();
  }
}
function saveCfg(){ if(run) return; cfg = { prep: num('stPrep', cfg.prep), talk: num('stTalk', cfg.talk) }; lsSet('spTimerCfg', cfg); paint(); }
function paintOops(){
  var m = Math.max(0, 10 - oops);
  var el = document.getElementById('stMark'); if(!el) return;
  el.textContent = m;
  document.getElementById('stSub').textContent = oops ? oops + (oops === 1 ? ' mistake' : ' mistakes') : 'No mistakes yet';
}
function paint(){
  var c = document.getElementById('stClock'); if(!c) return;
  var ph = document.getElementById('stPhase'), bar = document.getElementById('stBar'), go = document.getElementById('stGo');
  var card = c.parentNode;
  if(!run){ ph.textContent = 'Ready'; c.textContent = fmt(cfg.prep * 1000); bar.style.width = '0'; go.textContent = 'Prepare'; card.setAttribute('data-ph', 'idle'); return; }
  var left = run.end - Date.now(), total = (run.phase === 'prep' ? cfg.prep : cfg.talk) * 1000;
  ph.textContent = run.phase === 'prep' ? 'Preparing…' : 'Speak now';
  c.textContent = fmt(left); bar.style.width = Math.min(100, Math.max(0, 100 * (1 - left / total))) + '%';
  go.textContent = 'Stop'; card.setAttribute('data-ph', run.phase);
}
function loop(){
  if(!run) return;
  if(Date.now() >= run.end){
    if(run.phase === 'prep'){ beep(2, 880); run = { phase: 'talk', end: Date.now() + cfg.talk * 1000 }; }
    else { beep(3, 660); stop(); var ph = document.getElementById('stPhase'); if(ph) ph.textContent = 'Time is up'; var c = document.getElementById('stClock'); if(c) c.textContent = '00:00'; return; }
  }
  paint();
}
function go(){
  if(run){ stop(); paint(); return; }
  saveCfg(); beep(1, 600);   // unlocks audio on the tap
  run = { phase: 'prep', end: Date.now() + cfg.prep * 1000 };
  tick = setInterval(loop, 200); paint();
}
function stop(){ run = null; clearInterval(tick); tick = null; var g = document.getElementById('stGo'); if(g) g.textContent = 'Prepare'; var c = document.getElementById('stClock'); if(c && c.parentNode) c.parentNode.setAttribute('data-ph', 'idle'); }
function reset(){ stop(); oops = 0; paint(); paintOops(); }
function paintSw(){
  clearInterval(tick); tick = null;
  var c = document.getElementById('swClock'); if(!c) return;
  var g = document.getElementById('swGo');
  function p(){ c.textContent = fmtSw(sw.acc + (sw.on ? Date.now() - sw.t0 : 0)); }
  p(); g.textContent = sw.on ? 'Stop' : (sw.acc ? 'Resume' : 'Start');
  if(sw.on) tick = setInterval(function(){ if(!document.getElementById('swClock')){ clearInterval(tick); return; } p(); }, 30);
}
render();
