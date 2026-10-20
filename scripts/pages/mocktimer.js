var BACK = back('index.html#geography-hub/study', 'Back to Train Your Brain');
var EXAMS = {
  ielts: { label: 'IELTS', secs: [
    { n: 'Listening', m: 30, s: 'Audio plays once. Paper test adds 10 min to copy answers.' },
    { n: 'Reading', m: 60, s: '3 passages, 40 questions' },
    { n: 'Writing', m: 60, s: 'Task 1 and Task 2' },
    { n: 'Writing Task 1', m: 20, s: 'At least 150 words' },
    { n: 'Writing Task 2', m: 40, s: 'At least 250 words' },
    { n: 'Speaking Part 2 prep', m: 1, s: '1 minute to prepare' },
    { n: 'Speaking Part 2 talk', m: 2, s: 'Speak for 1 to 2 minutes' },
    { n: 'Speaking (full)', m: 14, s: 'About 11 to 14 minutes' }
  ] },
  toefl: { label: 'TOEFL', secs: [
    { n: 'Reading', m: 30, s: 'About 30 minutes (2026 format)' },
    { n: 'Listening', m: 29, s: 'About 29 minutes (2026 format)' },
    { n: 'Writing', m: 23, s: 'Build a sentence, email, academic discussion' },
    { n: 'Write an Email', m: 7, s: 'Part of Writing' },
    { n: 'Academic Discussion', m: 10, s: 'Part of Writing' },
    { n: 'Speaking', m: 8, s: 'About 8 minutes' }
  ] }
};
var st = lsGet('mockTimerUI', { exam: 'ielts', sec: 0 });
var run = null, tick = null, wake = null, actx = null, warned = {};
function fmt(ms){ var s = Math.max(0, Math.ceil(ms / 1000)), h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), x = s % 60; return (h ? h + ':' + String(m).padStart(2, '0') : String(m).padStart(2, '0')) + ':' + String(x).padStart(2, '0'); }
function cur(){ return EXAMS[st.exam].secs[st.sec] || EXAMS[st.exam].secs[0]; }
function beep(n, hz){
  try{
    actx = actx || new (window.AudioContext || window.webkitAudioContext)();
    for(var i = 0; i < n; i++){
      var o = actx.createOscillator(), g = actx.createGain(); o.frequency.value = hz || 880; o.connect(g); g.connect(actx.destination);
      var t = actx.currentTime + i * 0.3; g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.3, t + 0.02); g.gain.exponentialRampToValueAtTime(0.0001, t + 0.22); o.start(t); o.stop(t + 0.25);
    }
  }catch(e){}
}
function render(){
  var ex = EXAMS[st.exam], s = cur();
  var h = BACK + head('Exam Timer', 'One tap per section. Keep this page open; the screen stays awake while the timer runs.');
  h += '<div class="mt-tabs">' + Object.keys(EXAMS).map(function(k){ return '<button data-ex="' + k + '" class="' + (k === st.exam ? 'on' : '') + '">' + EXAMS[k].label + '</button>'; }).join('') + '</div>';
  h += '<div class="mt-grid">' + ex.secs.map(function(x, i){ return '<button class="mt-sec' + (i === st.sec ? ' on' : '') + '" data-i="' + i + '">' + esc(x.n) + '<small>' + x.m + ' min. ' + esc(x.s) + '</small></button>'; }).join('') + '</div>';
  h += '<div class="mt-cust"><input id="mtMin" type="number" min="1" max="240" inputmode="numeric" placeholder="min"><button class="v-btn alt" id="mtSet" style="width:auto;margin:0;padding:11px 16px;">Set custom time</button></div>';
  h += '<div class="mt-name" id="mtName"></div><div class="mt-clock" id="mtClock"></div><div class="mt-bar"><i id="mtBar"></i></div><div class="mt-msg" id="mtMsg"></div>';
  h += '<div class="v-row"><button class="v-btn" id="mtGo"></button><button class="v-btn alt" id="mtReset">Reset</button></div>';
  app.innerHTML = h;
  app.querySelectorAll('[data-ex]').forEach(function(b){ b.onclick = function(){ if(run) return; st.exam = b.getAttribute('data-ex'); st.sec = 0; st.custom = 0; lsSet('mockTimerUI', st); render(); }; });
  app.querySelectorAll('.mt-sec').forEach(function(b){ b.onclick = function(){ if(run) return; st.sec = +b.getAttribute('data-i'); st.custom = 0; lsSet('mockTimerUI', st); render(); }; });
  document.getElementById('mtSet').onclick = function(){ if(run) return; var v = parseInt(document.getElementById('mtMin').value, 10); if(v > 0 && v <= 240){ st.custom = v; render(); } };
  document.getElementById('mtGo').onclick = toggle;
  document.getElementById('mtReset').onclick = reset;
  paint();
}
function total(){ return (st.custom ? st.custom : cur().m) * 60000; }
function paint(){
  var left = run ? (run.paused ? run.left : run.end - Date.now()) : total();
  var clock = document.getElementById('mtClock'); if(!clock) return;
  clock.textContent = fmt(left);
  clock.className = 'mt-clock' + (run && left <= 60000 ? ' crit' : (run && left <= 300000 ? ' warn' : ''));
  document.getElementById('mtName').textContent = st.custom ? 'Custom: ' + st.custom + ' min' : cur().n;
  document.getElementById('mtBar').style.width = Math.max(0, Math.min(100, left / total() * 100)) + '%';
  var go = document.getElementById('mtGo'); go.textContent = !run ? 'Start' : (run.paused ? 'Resume' : 'Pause');
  document.title = (run && !run.paused ? fmt(left) + ' | ' : '') + 'Exam Timer | Mr Eric’s Lounge';
}
function say(t){ var m = document.getElementById('mtMsg'); if(m) m.textContent = t; }
function toggle(){
  if(!run){ run = { end: Date.now() + total(), paused: false, left: total() }; warned = {}; keepAwake(); say(''); beep(1, 660); loop(); }
  else if(run.paused){ run.end = Date.now() + run.left; run.paused = false; keepAwake(); loop(); }
  else { run.left = run.end - Date.now(); run.paused = true; clearInterval(tick); releaseWake(); }
  paint();
}
function loop(){
  clearInterval(tick);
  tick = setInterval(function(){
    var left = run.end - Date.now();
    [[600000, '10 minutes left'], [300000, '5 minutes left'], [60000, '1 minute left']].forEach(function(w){
      if(!warned[w[0]] && left <= w[0] && total() > w[0] + 5000){ warned[w[0]] = 1; say(w[1]); beep(w[0] === 60000 ? 3 : 2, 880); if(navigator.vibrate) navigator.vibrate(200); }
    });
    if(left <= 0){
      clearInterval(tick); releaseWake(); var done = total(); run = null; say('Time is up. Pens down.'); beep(4, 520); if(navigator.vibrate) navigator.vibrate([300, 150, 300]);
      if(done >= 5 * 60000) award(5, 'timer');
    }
    paint();
  }, 250);
}
function reset(){ clearInterval(tick); releaseWake(); run = null; say(''); paint(); }
function keepAwake(){ try{ if(navigator.wakeLock) navigator.wakeLock.request('screen').then(function(l){ wake = l; }).catch(function(){}); }catch(e){} }
function releaseWake(){ try{ if(wake){ wake.release(); wake = null; } }catch(e){} }
document.addEventListener('visibilitychange', function(){ if(run && !run.paused && document.visibilityState === 'visible') keepAwake(); });
render();
