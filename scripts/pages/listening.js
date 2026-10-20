var BACK = back('index.html#geography-hub/study', 'Back to Train Your Brain');
var D = [], cur = null, plays = 0, ans = {}, checked = false, speaking = false, tok = 0;
var S = lsGet('listenSet', { exam: true, rate: 1 }), AU = null;
function stopSpeech(){ tok++; speaking = false; if(AU){ try{ AU.pause(); }catch(e){} AU = null; } }
function speak(i, done){
  stopSpeech(); var my = tok; AU = new Audio('data/audio/listening/' + String(i).padStart(2, '0') + '.mp3');
  AU.playbackRate = S.rate; speaking = true;
  AU.onended = function(){ if(my === tok){ speaking = false; done(); } };
  AU.onerror = function(){ if(my === tok){ speaking = false; done(); var o = document.getElementById('lsErr'); if(o) o.textContent = 'Audio could not load. Check your connection and try again.'; } };
  var pr = AU.play(); if(pr && pr.catch) pr.catch(function(){ if(my === tok){ speaking = false; done(); } });
}
function hub(){
  stopSpeech(); var best = lsGet('listenBest', {});
  app.innerHTML = BACK + head('Listening Practice', 'Listen, then answer five questions. In exam mode the audio plays once, like the real test.') +
    '<div class="ls-set"><label><input type="checkbox" id="lsExam"' + (S.exam ? ' checked' : '') + '> Exam mode (play once)</label><label>Speed <select id="lsRate"><option value="0.85">Slow</option><option value="1">Normal</option><option value="1.15">Fast</option></select></label></div>' +
    D.map(function(x, i){ return '<a class="ls-item" href="#t' + i + '"><b>' + esc(x.t) + '</b><small>' + esc(x.l) + (best[i] !== undefined ? '. Best: ' + best[i] + '/5' : '') + '</small></a>'; }).join('');
  var r = document.getElementById('lsRate'); r.value = String(S.rate); if(r.value !== String(S.rate)) r.value = '1';
  r.onchange = function(){ S.rate = +r.value; lsSet('listenSet', S); };
  document.getElementById('lsExam').onchange = function(){ S.exam = this.checked; lsSet('listenSet', S); };
}
function shuf(q){ var idx = shuffle([0, 1, 2, 3]); return { q: q.q, o: idx.map(function(i){ return q.o[i]; }), a: idx.indexOf(q.a) }; }
function task(i){
  stopSpeech(); var x = D[i]; cur = { i: i, t: x, qs: x.q.map(shuf) }; plays = 0; ans = {}; checked = false; drawTask();
}
function drawTask(){
  var x = cur.t, max = S.exam ? 1 : 99, can = plays < max;
  var h = BACK + head(esc(x.t), esc(x.l)) +
    '<div class="sp-card" style="text-align:center;"><button class="v-btn" id="lsPlay"' + (can || speaking ? '' : ' disabled') + '>' + (speaking ? 'Stop' : (plays ? 'Play again' : 'Play audio')) + '</button><div class="v-hint" style="margin-top:8px;">' + (S.exam ? (plays ? 'Exam mode: already played.' : 'Plays once.') : 'Play as often as you like.') + '</div><div class="v-hint" id="lsErr" style="color:#C0392B;"></div></div>';
  h += cur.qs.map(function(q, qi){
    return '<div class="sp-card"><div class="sp-q" style="font-size:17px;">' + (qi + 1) + '. ' + esc(q.q) + '</div>' + q.o.map(function(o, oi){
      var cls = 'ls-opt' + (ans[qi] === oi ? ' on' : '') + (checked ? (oi === q.a ? ' ok' : (ans[qi] === oi ? ' bad' : '')) : '');
      return '<button class="' + cls + '" data-q="' + qi + '" data-o="' + oi + '"' + (checked ? ' disabled' : '') + '>' + esc(o) + '</button>'; }).join('') + '</div>';
  }).join('');
  if(!checked) h += '<div class="v-row"><button class="v-btn" id="lsCheck">Check answers</button></div>';
  else {
    var sc = cur.qs.reduce(function(n, q, qi){ return n + (ans[qi] === q.a ? 1 : 0); }, 0);
    h += '<div class="sp-card"><b>Score: ' + sc + '/5</b><details style="margin-top:8px;"><summary style="font-weight:800;cursor:pointer;">Show transcript</summary><p style="line-height:1.55;">' + esc(x.s) + '</p></details></div><div class="v-row"><button class="v-btn" id="lsNext">Another recording</button><button class="v-btn alt" id="lsRetry">Try again</button></div>';
  }
  app.innerHTML = h;
  var pb = document.getElementById('lsPlay');
  pb.onclick = function(){
    if(speaking){ stopSpeech(); drawTask(); return; }
    plays++; drawTask(); speak(cur.i, function(){ drawTask(); });
  };
  app.querySelectorAll('.ls-opt').forEach(function(b){ b.onclick = function(){ ans[+b.getAttribute('data-q')] = +b.getAttribute('data-o'); var y = window.scrollY; var sp = speaking; drawTaskKeep(sp); window.scrollTo(0, y); }; });
  var c = document.getElementById('lsCheck');
  if(c) c.onclick = function(){
    stopSpeech(); checked = true;
    var sc = cur.qs.reduce(function(n, q, qi){ return n + (ans[qi] === q.a ? 1 : 0); }, 0);
    var best = lsGet('listenBest', {}); if(best[cur.i] === undefined || sc > best[cur.i]){ best[cur.i] = sc; lsSet('listenBest', best); }
    award(sc, 'listening'); award(10, 'listening'); drawTask();
  };
  var n = document.getElementById('lsNext'); if(n) n.onclick = function(){ var k = D.length > 1 ? (cur.i + 1 + Math.floor(Math.random() * (D.length - 1))) % D.length : 0; location.hash = '#t' + k; };
  var rt = document.getElementById('lsRetry'); if(rt) rt.onclick = function(){ task(cur.i); };
}
function drawTaskKeep(sp){ var was = speaking; drawTask(); speaking = was; }
function route(){
  var m = /^#t(\d+)$/.exec(location.hash);
  if(m && D[+m[1]]) task(+m[1]); else hub();
}
window.addEventListener('hashchange', route);
getJson('data/games/listening.json').then(function(d){ D = d; route(); }).catch(function(){ app.innerHTML = BACK + '<div class="v-hint">Could not load. Check your connection.</div>'; });
