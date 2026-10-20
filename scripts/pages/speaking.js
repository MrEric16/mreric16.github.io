var BACK = back('index.html#geography-hub/study', 'Back to Train Your Brain');
var D = null, rec = null, tm = null, stream = null, chunks = [], recUrl = null;
function stopAll(){ if(tm){ clearInterval(tm); tm = null; } if(rec && rec.state !== 'inactive'){ try{ rec.stop(); }catch(e){} } if(stream){ stream.getTracks().forEach(function(t){ t.stop(); }); stream = null; } }
function mmss(s){ s = Math.max(0, s); return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); }
function hub(){
  stopAll();
  var done = lsGet('speakDone', 0);
  app.innerHTML = BACK + head('Speaking Practice', 'IELTS style. Part 1 short answers, Part 2 the long turn with a cue card, Part 3 discussion. Record yourself and listen back.') +
    '<div class="sport-hub-grid"><a class="sport-hub-tile" href="#p1"><span class="name" style="flex-direction:column;gap:2px;"><span>Part 1</span><span style="font-size:12px;color:var(--ink-soft);font-weight:700;">' + D.p1.length + ' topics</span></span></a>' +
    '<a class="sport-hub-tile" href="#p2"><span class="name" style="flex-direction:column;gap:2px;"><span>Part 2 and 3</span><span style="font-size:12px;color:var(--ink-soft);font-weight:700;">' + D.p2.length + ' cue cards</span></span></a></div>' +
    '<div class="v-hint" style="margin-top:12px;">Sessions finished: ' + done + '. Your recording stays on your device and is never uploaded.</div>';
}
function recorder(){
  if(!(navigator.mediaDevices && window.MediaRecorder)) return '<div class="v-hint">Recording is not supported in this browser. You can still use the timer.</div>';
  return '<div class="v-row"><button class="v-btn alt" id="spRec">Record myself</button></div><div id="spPlay"></div>';
}
function wireRec(){
  var b = document.getElementById('spRec'); if(!b) return;
  b.onclick = function(){
    if(rec && rec.state === 'recording'){ rec.stop(); b.textContent = 'Record myself'; return; }
    navigator.mediaDevices.getUserMedia({ audio: true }).then(function(s){
      stream = s; chunks = []; rec = new MediaRecorder(s);
      rec.ondataavailable = function(e){ if(e.data.size) chunks.push(e.data); };
      rec.onstop = function(){
        if(recUrl) URL.revokeObjectURL(recUrl);
        recUrl = URL.createObjectURL(new Blob(chunks, { type: rec.mimeType || 'audio/webm' }));
        var p = document.getElementById('spPlay'); if(p) p.innerHTML = '<audio controls src="' + recUrl + '" style="width:100%;margin-top:8px;"></audio>';
        if(stream){ stream.getTracks().forEach(function(t){ t.stop(); }); stream = null; }
      };
      rec.start(); b.textContent = 'Stop recording';
    }).catch(function(){ var p = document.getElementById('spPlay'); if(p) p.innerHTML = '<div class="v-hint">Microphone blocked. Allow it in your browser settings.</div>'; });
  };
}
var p1 = null;
function part1(){
  stopAll();
  if(!p1){ p1 = { t: Math.floor(Math.random() * D.p1.length), i: 0 }; }
  var T = D.p1[p1.t], q = T.q[p1.i];
  app.innerHTML = BACK + head('Part 1: ' + esc(T.t), 'Answer in 2 to 3 sentences. Give a reason and an example. Do not answer with one word.') +
    '<div class="sp-card"><div class="sp-q">' + esc(q) + '</div><div class="v-hint">Question ' + (p1.i + 1) + ' of ' + T.q.length + '</div></div>' +
    '<div class="sp-clock" id="spClk">0:00</div>' + recorder() +
    '<div class="v-row"><button class="v-btn" id="spNext">' + (p1.i + 1 < T.q.length ? 'Next question' : 'Finish topic') + '</button><button class="v-btn alt" id="spTopic">Other topic</button></div>';
  var t0 = Date.now(); tm = setInterval(function(){ var c = document.getElementById('spClk'); if(c) c.textContent = mmss(Math.floor((Date.now() - t0) / 1000)); }, 500);
  wireRec();
  document.getElementById('spNext').onclick = function(){
    if(p1.i + 1 < T.q.length){ p1.i++; part1(); }
    else { lsSet('speakDone', lsGet('speakDone', 0) + 1); award(10, 'speaking'); p1 = null; location.hash = ''; hub(); }
  };
  document.getElementById('spTopic').onclick = function(){ p1 = null; part1(); };
}
var p2 = null;
function part2(){
  stopAll();
  if(!p2) p2 = { i: Math.floor(Math.random() * D.p2.length), ph: 'show' };
  var C = D.p2[p2.i];
  var card = '<div class="sp-card"><div class="sp-q">' + esc(C.c) + '</div><div style="font-weight:800;margin-top:8px;">You should say:</div><ul class="sp-ul">' + C.b.map(function(x){ return '<li>' + esc(x) + '</li>'; }).join('') + '</ul></div>';
  if(p2.ph === 'show'){
    app.innerHTML = BACK + head('Part 2: the long turn', 'You get 1 minute to prepare (make notes on paper) and then speak for 1 to 2 minutes.') + card +
      '<div class="v-row"><button class="v-btn" id="spGo">Start 1 minute prep</button><button class="v-btn alt" id="spOther">Other card</button></div>';
    document.getElementById('spGo').onclick = function(){ p2.ph = 'prep'; part2(); };
    document.getElementById('spOther').onclick = function(){ p2 = null; part2(); };
  } else if(p2.ph === 'prep' || p2.ph === 'talk'){
    var prep = p2.ph === 'prep', total = prep ? 60 : 120;
    app.innerHTML = BACK + head(prep ? 'Prepare' : 'Speak now', prep ? 'Write key words only. Do not write full sentences.' : 'Keep going until the timer ends. Aim for at least 1 minute 30.') + card +
      '<div class="sp-clock" id="spClk">' + mmss(total) + '</div>' + (prep ? '' : recorder()) +
      '<div class="v-row"><button class="v-btn" id="spSkip">' + (prep ? 'Start speaking now' : 'I have finished') + '</button></div>';
    var t0 = Date.now();
    function end(){ stopAll(); p2.ph = prep ? 'talk' : 'part3'; part2(); }
    tm = setInterval(function(){ var left = total - Math.floor((Date.now() - t0) / 1000), c = document.getElementById('spClk'); if(c) c.textContent = mmss(left); if(left <= 0 && prep) end(); if(left <= 0 && !prep){ clearInterval(tm); tm = null; if(c) c.textContent = '0:00'; } }, 500);
    if(!prep) wireRec();
    document.getElementById('spSkip').onclick = function(){ if(!prep && rec && rec.state === 'recording'){ rec.stop(); } var keep = recUrl; if(tm){ clearInterval(tm); tm = null; } p2.ph = prep ? 'talk' : 'part3'; p2.keep = keep; part2(); };
  } else {
    app.innerHTML = BACK + head('Part 3: discussion', 'Give longer, more abstract answers. Use phrases like "On the whole", "It depends on", "One reason is".') +
      (recUrl ? '<div class="sp-card"><div class="v-hint">Your Part 2 recording</div><audio controls src="' + recUrl + '" style="width:100%;"></audio></div>' : '') +
      C.q.map(function(x, i){ return '<div class="sp-card"><div class="sp-q">' + (i + 1) + '. ' + esc(x) + '</div></div>'; }).join('') +
      '<div class="sp-card"><b>Self-check</b><ul class="sp-ul"><li>Did you speak for 90 seconds or more?</li><li>Did you cover every bullet?</li><li>Did you pause to search for words, or use fillers like "erm" often?</li><li>Did you use at least two less common words or idioms?</li><li>Did you use past, present and future structures where they fit?</li></ul></div>' +
      '<div class="v-row"><button class="v-btn" id="spDone">Finish and next card</button></div>';
    document.getElementById('spDone').onclick = function(){ lsSet('speakDone', lsGet('speakDone', 0) + 1); award(20, 'speaking'); p2 = null; stopAll(); if(recUrl){ URL.revokeObjectURL(recUrl); recUrl = null; } location.hash = ''; hub(); };
  }
}
function route(){
  var h = location.hash.replace('#', '');
  if(h === 'p1') part1(); else if(h === 'p2') part2(); else { p1 = null; p2 = null; hub(); }
}
window.addEventListener('hashchange', route);
getJson('data/games/speaking.json').then(function(d){ D = d; route(); }).catch(function(){ app.innerHTML = BACK + '<div class="v-hint">Could not load. Check your connection.</div>'; });
