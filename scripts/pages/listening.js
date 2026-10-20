var BACK = back('index.html#geography-hub/study', 'Back to Train Your Brain');
var REPO = 'https://github.com/MrEric16/mreric16.github.io/releases/download/';
var SECS = { S1: ['Section 1', 'Everyday conversation', 'Two people, a booking or an enquiry. Fill in the details.'], S2: ['Section 2', 'Talk or announcement', 'One speaker giving public information.'], S3: ['Section 3', 'Academic discussion', 'A tutor and students talk about a project or assignment.'], S4: ['Section 4', 'Lecture', 'One speaker on an academic topic.'] };
var IDX = null, SHARDS = {}, cur = null, ans = {}, checked = false, plays = 0, speaking = false, AU = null, tok = 0;
var S = lsGet('listenSet', { exam: true, rate: 1 });
function stopAudio(){ tok++; speaking = false; if(AU){ try{ AU.pause(); }catch(e){} AU = null; } }
function seen(){ return lsGet('listenSeen', []); }
function markSeen(id){ var a = seen(); if(a.indexOf(id) < 0) a.push(id); if(a.length > 4000) a = a.slice(-3000); lsSet('listenSeen', a); }
function stats(){ return lsGet('listenStats', {}); }
function loadIndex(){ if(IDX) return Promise.resolve(IDX); return getJson('data/listening-pool/index.json').then(function(d){ IDX = d; return d; }); }
function loadShard(f){ if(SHARDS[f]) return Promise.resolve(SHARDS[f]); return getJson('data/listening-pool/' + f).then(function(d){ SHARDS[f] = d; return d; }); }
function pickItem(sec){
  return loadIndex().then(function(ix){
    var sh = ix.shards.filter(function(x){ return x.n && x.n[sec]; });
    if(!sh.length) throw new Error('empty');
    var sn = seen(), order = shuffle(sh.map(function(x, i){ return i; }));
    // visit shards in random order weighted by size until an unseen item is found
    var weighted = []; sh.forEach(function(x, i){ for(var k = 0; k < Math.min(x.n[sec], 50); k++) weighted.push(i); });
    var tried = {}, seq = shuffle(weighted).filter(function(i){ if(tried[i]) return false; tried[i] = 1; return true; });
    function next(k){
      if(k >= seq.length){ // everything heard: recycle this section
        var keep = sn.filter(function(id){ return id.indexOf('-' + sec) < 0; }); lsSet('listenSeen', keep); sn = keep;
        var any = sh[Math.floor(Math.random() * sh.length)]; return loadShard(any.f).then(function(d){ var c = d.items.filter(function(x){ return x.s === sec; }); var it = c[Math.floor(Math.random() * c.length)]; it.tag = d.tag; return it; });
      }
      var s = sh[seq[k]];
      return loadShard(s.f).then(function(d){
        var c = d.items.filter(function(x){ return x.s === sec && sn.indexOf(x.id) < 0; });
        if(!c.length) return next(k + 1);
        var it = c[Math.floor(Math.random() * c.length)]; it.tag = d.tag; return it;
      });
    }
    return next(0);
  });
}
function hub(){
  stopAudio(); var st = stats();
  app.innerHTML = BACK + head('Listening Practice', 'Pick a section. Every task is new: fresh names, numbers, dates and topics, so you never run out.') +
    '<div class="ls-set"><label><input type="checkbox" id="lsExam"' + (S.exam ? ' checked' : '') + '> Exam mode (play once)</label><label>Speed <select id="lsRate"><option value="0.85">Slow</option><option value="1">Normal</option><option value="1.15">Fast</option></select></label></div>' +
    Object.keys(SECS).map(function(k){ var x = SECS[k], s = st[k]; return '<a class="ls-item" href="#' + k + '"><b>' + x[0] + ': ' + x[1] + '</b><small>' + x[2] + (s ? ' Done: ' + s.n + ', average ' + Math.round(s.c / s.t * 100) + '%.' : '') + '</small></a>'; }).join('') +
    '<div class="v-hint" style="margin-top:8px;">' + (navigator.onLine ? 'Needs an internet connection.' : 'You are offline. Listening needs a connection.') + '</div>';
  var r = document.getElementById('lsRate'); r.value = String(S.rate); if(r.value !== String(S.rate)) r.value = '1';
  r.onchange = function(){ S.rate = +r.value; lsSet('listenSet', S); };
  document.getElementById('lsExam').onchange = function(){ S.exam = this.checked; lsSet('listenSet', S); };
}
function task(sec){
  stopAudio(); app.innerHTML = BACK + head(SECS[sec][0] + ': ' + SECS[sec][1], '') + '<div class="v-hint">Loading a new task...</div>';
  pickItem(sec).then(function(it){ cur = it; ans = {}; checked = false; plays = 0; markSeen(it.id); draw(); }).catch(function(){ app.innerHTML = BACK + '<div class="v-hint">Could not load a task. Check your connection and try again.</div>'; });
}
function speak(){
  stopAudio(); var my = tok; AU = new Audio(REPO + cur.tag + '/' + cur.id + '.mp3'); AU.playbackRate = S.rate; speaking = true;
  AU.onended = function(){ if(my === tok){ speaking = false; draw(); } };
  AU.onerror = function(){ if(my === tok){ speaking = false; plays = Math.max(0, plays - 1); draw(); var o = document.getElementById('lsErr'); if(o) o.textContent = 'Audio could not load. Check your connection and try again.'; } };
  var pr = AU.play(); if(pr && pr.catch) pr.catch(function(){ if(my === tok){ speaking = false; draw(); } });
}
function norm(s){ return String(s).toLowerCase().replace(/:/g, '.').replace(/[£$,]/g, '').replace(/o'clock/g, '').replace(/\bpounds?\b/g, '').replace(/\b(am|pm)\b/g, '').replace(/\s+/g, ' ').trim(); }
function right(q, i){
  if(q.t === 'mc') return ans[i] === q.a;
  var v = norm(ans[i] || ''); if(!v) return false; return q.acc.indexOf(v) >= 0;
}
function draw(){
  var sec = cur.s, max = S.exam ? 1 : 99, can = plays < max;
  var typed = cur.qs.some(function(q){ return q.t === 'type'; });
  var h = BACK + head(SECS[sec][0] + ': ' + SECS[sec][1], 'Questions 1 to ' + cur.qs.length) +
    '<div class="sp-card" style="text-align:center;"><button class="v-btn" id="lsPlay"' + (can || speaking ? '' : ' disabled') + '>' + (speaking ? 'Stop' : (plays ? (S.exam ? 'Played' : 'Play again') : 'Play audio')) + '</button><div class="v-hint" style="margin-top:8px;">' + (S.exam ? (plays ? 'Exam mode: already played.' : 'Plays once.') : 'Play as often as you like.') + '</div><div class="v-hint" id="lsErr" style="color:#C0392B;"></div></div>';
  if(typed && !checked) h += '<div class="v-hint" style="margin:0 0 8px;">Write numbers as digits. Write names as they are spelled.</div>';
  h += cur.qs.map(function(q, i){
    var body;
    if(q.t === 'mc') body = q.o.map(function(o, oi){
      var cls = 'ls-opt' + (ans[i] === oi ? ' on' : '') + (checked ? (oi === q.a ? ' ok' : (ans[i] === oi ? ' bad' : '')) : '');
      return '<button class="' + cls + '" data-q="' + i + '" data-o="' + oi + '"' + (checked ? ' disabled' : '') + '>' + esc(q.o[oi]) + '</button>'; }).join('');
    else body = '<input class="ls-in' + (checked ? (right(q, i) ? ' ok' : ' bad') : '') + '" data-i="' + i + '" value="' + esc(ans[i] || '') + '"' + (checked ? ' disabled' : '') + ' autocomplete="off" autocapitalize="off">' + (checked && !right(q, i) ? '<div class="ls-fix">Answer: ' + esc(q.ans) + '</div>' : '');
    return '<div class="sp-card"><div class="sp-q" style="font-size:17px;">' + (i + 1) + '. ' + esc(q.q.replace(/\s*_+\s*$/, '')) + '</div>' + body + '</div>';
  }).join('');
  if(!checked) h += '<div class="v-row"><button class="v-btn" id="lsCheck">Check answers</button></div>';
  else {
    var sc = cur.qs.reduce(function(n, q, i){ return n + (right(q, i) ? 1 : 0); }, 0);
    h += '<div class="sp-card"><b>Score: ' + sc + '/' + cur.qs.length + '</b><details style="margin-top:8px;"><summary style="font-weight:800;cursor:pointer;">Show transcript</summary><p style="line-height:1.6;">' + cur.tx.map(function(x){ return esc(x.t); }).join('<br><br>') + '</p></details></div><div class="v-row"><button class="v-btn" id="lsNext">New ' + SECS[sec][0] + ' task</button><button class="v-btn alt" id="lsBack">Sections</button></div>';
  }
  var ae = document.activeElement, fi = ae && ae.classList && ae.classList.contains('ls-in') ? ae.getAttribute('data-i') : null, y = window.scrollY;
  app.innerHTML = h; window.scrollTo(0, y);
  if(fi !== null){ var el = app.querySelector('.ls-in[data-i="' + fi + '"]'); if(el){ el.focus(); try{ el.setSelectionRange(el.value.length, el.value.length); }catch(e){} } }
  document.getElementById('lsPlay').onclick = function(){ if(speaking){ stopAudio(); draw(); return; } plays++; speak(); draw(); };
  app.querySelectorAll('.ls-opt').forEach(function(b){ b.onclick = function(){ ans[+b.getAttribute('data-q')] = +b.getAttribute('data-o'); draw(); }; });
  app.querySelectorAll('.ls-in').forEach(function(inp){ inp.oninput = function(){ ans[+inp.getAttribute('data-i')] = inp.value; }; });
  var c = document.getElementById('lsCheck');
  if(c) c.onclick = function(){
    stopAudio(); checked = true;
    var sc = cur.qs.reduce(function(n, q, i){ return n + (right(q, i) ? 1 : 0); }, 0), st = stats(), k = st[cur.s] || { n: 0, c: 0, t: 0 };
    k.n++; k.c += sc; k.t += cur.qs.length; st[cur.s] = k; lsSet('listenStats', st);
    award(sc, 'listening'); award(10, 'listening'); draw(); window.scrollTo(0, 0);
  };
  var n = document.getElementById('lsNext'); if(n) n.onclick = function(){ task(cur.s); };
  var b = document.getElementById('lsBack'); if(b) b.onclick = function(){ location.hash = ''; hub(); };
}
function route(){
  var m = /^#(S[1-4])$/.exec(location.hash);
  if(m) task(m[1]); else hub();
}
window.addEventListener('hashchange', route);
route();
