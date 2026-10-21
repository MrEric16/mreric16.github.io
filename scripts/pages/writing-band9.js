var BACK = back('index.html#geography-hub/study', 'Back to Train Your Brain');
var DATA = null;
var st = lsGet('wb9UI', { roles: true });
function save(){ lsSet('wb9UI', st); }
function essays(key){ return DATA.models.filter(function(m){ return m.task === 't2' && m.etype === key; }); }
function typeOf(key){ return DATA.guides.types.filter(function(t){ return t.key === key; })[0]; }
function bullets(a){ return a.map(function(x){ return '<div class="wr-li tip">' + esc(x) + '</div>'; }).join(''); }
function home(){
  var G = DATA.guides;
  var h = BACK + head('Writing Band 9', 'Task 2 essays: how each question type works, then annotated Band 9 target essays to study.');
  h += '<div class="wm-warn">Model essays and guidance written for this site, not official IELTS material and not examiner-marked. Study the structure and language. Never memorise a whole essay.</div>';
  h += '<div class="wm-grid">' + G.types.map(function(t){
    return '<a class="wm-tile" href="#type/' + t.key + '"><span class="wm-type">' + essays(t.key).length + ' essays</span><b>' + esc(t.name) + '</b><span class="wm-w">' + esc(t.asks[0]) + '</span></a>';
  }).join('') + '</div>';
  h += '<div class="wr-card" style="margin-top:12px;"><h3>Ground rules for every essay</h3>' + bullets(G.principles) + '</div>';
  h += '<div class="wr-card"><h3>Phrase bank by job</h3>' + G.phrases.map(function(p){ return '<div class="wr-li"><b>' + esc(p[0]) + '</b></div><div>' + p[1].map(function(x){ return '<span class="wr-chip">' + esc(x) + '</span>'; }).join('') + '</div>'; }).join('') + '</div>';
  h += '<div class="v-row"><a class="v-btn alt wm-nav" href="writing-models.html">All model answers (Task 1 and 2)</a><a class="v-btn alt wm-nav" href="writing.html">Writing Checker</a></div>';
  app.innerHTML = h; window.scrollTo(0, 0);
}
function typeView(key){
  var t = typeOf(key); if(!t){ location.hash = ''; return; }
  var h = back('#', 'Back to Writing Band 9') + head(esc(t.name), 'How to build this essay, then three examples.');
  h += '<div class="wr-card"><h3>Typical question wording</h3>' + t.asks.map(function(a){ return '<div class="wr-li">' + esc(a) + '</div>'; }).join('') + '</div>';
  h += '<div class="wr-card"><h3>Plan: one job per paragraph</h3><ol class="wm-proc">' + t.plan.map(function(p){ return '<li>' + esc(p) + '</li>'; }).join('') + '</ol></div>';
  h += '<div class="wr-card"><h3>What earns marks</h3>' + bullets(t.tips) + '</div>';
  h += '<div class="wr-card"><h3>What loses marks</h3>' + t.traps.map(function(x){ return '<div class="wr-li no">' + esc(x) + '</div>'; }).join('') + '</div>';
  h += '<div class="section-head" style="margin-top:14px;"><h2>Band 9 essays</h2></div><div class="wm-grid">' + essays(key).map(function(m){
    return '<a class="wm-tile" href="#' + m.id + '"><span class="wm-type">' + m.words + ' words</span><b>' + esc(m.title) + '</b></a>';
  }).join('') + '</div>';
  app.innerHTML = h; window.scrollTo(0, 0);
}
function essayView(id){
  var m = DATA.models.filter(function(x){ return x.id === id && x.task === 't2'; })[0];
  if(!m){ location.hash = ''; return; }
  var list = essays(m.etype), ix = list.indexOf(m), t = typeOf(m.etype);
  var h = back('#type/' + m.etype, esc(t.name)) + head(esc(m.title), esc(t.name) + ' · ' + m.words + ' words');
  h += '<div class="wr-card"><h3>The question</h3>' + m.prompt.split('\n').map(function(p){ return '<p class="wm-p">' + esc(p) + '</p>'; }).join('') + '</div>';
  h += '<div class="wr-card"><div class="wm-try">Plan it in two minutes, write it, then compare.</div><div class="v-row"><button class="v-btn" id="wbTry">Write it in the Checker</button><button class="v-btn alt" id="wbRoles">' + (st.roles ? 'Hide paragraph jobs' : 'Show paragraph jobs') + '</button></div></div>';
  h += '<div class="wr-card wm-model"><h3>Band 9 target essay</h3>' + m.model.map(function(p, i){
    return (st.roles ? '<div class="wb-role">' + (i + 1) + '. ' + esc(m.roles[i]) + '</div>' : '') + '<p class="wm-p">' + esc(p) + '</p>';
  }).join('') + '<div class="wr-note">' + m.words + ' words (numbers count as words).</div></div>';
  h += '<div class="wr-card"><h3>Why it scores Band 9</h3>' + Object.keys(m.notes).map(function(k){ return '<div class="wr-li"><b>' + esc(k) + ':</b> ' + esc(m.notes[k]) + '</div>'; }).join('') + '</div>';
  h += '<div class="wr-card"><h3>Language to learn</h3>' + m.lang.map(function(w){ return '<span class="wr-chip">' + esc(w) + '</span>'; }).join('') + '</div>';
  h += '<div class="v-row">' + (ix > 0 ? '<a class="v-btn alt wm-nav" href="#' + list[ix - 1].id + '">← Previous</a>' : '') + (ix < list.length - 1 ? '<a class="v-btn alt wm-nav" href="#' + list[ix + 1].id + '">Next →</a>' : '') + '</div>';
  app.innerHTML = h; window.scrollTo(0, 0);
  document.getElementById('wbRoles').onclick = function(){ st.roles = !st.roles; save(); essayView(id); };
  document.getElementById('wbTry').onclick = function(){ lsSet('writingUI', { task: 't2' }); location.href = 'writing.html'; };
}
function route(){
  if(!DATA) return;
  var r = decodeURIComponent(location.hash.replace(/^#/, ''));
  if(!r) home(); else if(r.indexOf('type/') === 0) typeView(r.slice(5)); else essayView(r);
}
app.innerHTML = BACK + '<div class="empty-card">Loading…</div>';
getJson('data/writing/models.json').then(function(d){ DATA = d; window.addEventListener('hashchange', route); route(); }).catch(function(){ app.innerHTML = BACK + '<div class="empty-card">Could not load. Check your connection and reload.</div>'; });
