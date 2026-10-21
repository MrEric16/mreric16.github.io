var BACK = back('writing-hub.html', 'Back to IELTS Writing');
var DATA = null;
var st = lsGet('wb9UI', { roles: true, tab: 'essays' });
var scores = lsGet('wb9Scores', {});
function save(){ lsSet('wb9UI', st); }
function essays(key){ return DATA.essays.filter(function(m){ return m.etype === key; }); }
function typeOf(key){ return DATA.guides.types.filter(function(t){ return t.key === key; })[0]; }
function bullets(a, cls){ return a.map(function(x){ return '<div class="wr-li ' + (cls || 'tip') + '">' + esc(x) + '</div>'; }).join(''); }
var TABS = [['essays', 'Essays'], ['skills', 'Skills'], ['practice', 'Practice'], ['phrases', 'Phrases']];
function home(){
  var G = DATA.guides, h = BACK + head('Writing Band 9', 'Task 2: learn the skills, study annotated Band 9 target essays, then practise.');
  h += '<div class="wm-warn">Everything here was written for this site. It is not official IELTS material and was not marked by an examiner. Study the structure and the language. Never memorise a whole essay.</div>';
  h += '<div class="wr-sel">' + TABS.map(function(t){ return '<button data-tab="' + t[0] + '" class="' + (st.tab === t[0] ? 'on' : '') + '">' + t[1] + '</button>'; }).join('') + '</div>';
  if(st.tab === 'essays'){
    h += '<div class="wm-grid">' + G.types.map(function(t){ return '<a class="wm-tile" href="#type/' + t.key + '"><span class="wm-type">' + essays(t.key).length + ' essays</span><b>' + esc(t.name) + '</b><span class="wm-w">' + esc(t.asks[0]) + '</span></a>'; }).join('') + '</div>';
    h += '<div class="wr-card" style="margin-top:12px;"><h3>Ground rules for every essay</h3>' + bullets(G.principles) + '</div>';
  } else if(st.tab === 'skills'){
    h += '<div class="wm-grid">' + DATA.lessons.map(function(l, i){ return '<a class="wm-tile" href="#skill/' + l.id + '"><span class="wm-type">Lesson ' + (i + 1) + ' · ' + esc(l.time) + '</span><b>' + esc(l.title) + '</b></a>'; }).join('') + '</div>';
  } else if(st.tab === 'practice'){
    h += '<div class="wm-grid">' + DATA.drills.map(function(d){ return drillTile(d.id, d.title, d.desc, d.items.length); }).join('') + drillTile('jobs', 'What job does this paragraph do?', 'Read a paragraph from a Band 9 essay and name its job.', 8) + '</div>';
  } else {
    h += '<div class="wr-card"><h3>Phrase bank by job</h3>' + G.phrases.map(function(p){ return '<div class="wr-li"><b>' + esc(p[0]) + '</b></div><div>' + p[1].map(function(x){ return '<span class="wr-chip">' + esc(x) + '</span>'; }).join('') + '</div>'; }).join('') + '</div>';
  }
  h += '<div class="v-row" style="margin-top:10px;"><a class="v-btn alt wm-nav" href="writing.html">Writing Checker</a></div>';
  app.innerHTML = h; window.scrollTo(0, 0);
  app.querySelectorAll('[data-tab]').forEach(function(b){ b.onclick = function(){ st.tab = b.getAttribute('data-tab'); save(); home(); }; });
}
function drillTile(id, title, desc, n){
  var sc = scores[id];
  return '<a class="wm-tile" href="#practice/' + id + '"><span class="wm-type">' + n + ' questions' + (sc ? ' · best ' + sc + '%' : '') + '</span><b>' + esc(title) + '</b><span class="wm-w">' + esc(desc) + '</span></a>';
}
function typeView(key){
  var t = typeOf(key); if(!t){ location.hash = ''; return; }
  var h = back('#', 'Back to Writing Band 9') + head(esc(t.name), 'How to build this essay, then examples to study.');
  h += '<div class="wr-card"><h3>Typical question wording</h3>' + t.asks.map(function(a){ return '<div class="wr-li">' + esc(a) + '</div>'; }).join('') + '</div>';
  h += '<div class="wr-card"><h3>Plan: one job per paragraph</h3><ol class="wm-proc">' + t.plan.map(function(p){ return '<li>' + esc(p) + '</li>'; }).join('') + '</ol></div>';
  h += '<div class="wr-card"><h3>What earns marks</h3>' + bullets(t.tips) + '</div>';
  h += '<div class="wr-card"><h3>What loses marks</h3>' + bullets(t.traps, 'no') + '</div>';
  h += '<div class="section-head" style="margin-top:14px;"><h2>Band 9 essays</h2></div><div class="wm-grid">' + essays(key).map(function(m){ return '<a class="wm-tile" href="#' + m.id + '"><span class="wm-type">' + m.words + ' words</span><b>' + esc(m.title) + '</b></a>'; }).join('') + '</div>';
  app.innerHTML = h; window.scrollTo(0, 0);
}
function essayView(id){
  var m = DATA.essays.filter(function(x){ return x.id === id; })[0];
  if(!m){ location.hash = ''; return; }
  var list = essays(m.etype), ix = list.indexOf(m), t = typeOf(m.etype);
  var h = back('#type/' + m.etype, esc(t.name)) + head(esc(m.title), esc(t.name) + ' · ' + m.words + ' words');
  h += '<div class="wr-card"><h3>The question</h3>' + m.prompt.split('\n').map(function(p){ return '<p class="wm-p">' + esc(p) + '</p>'; }).join('') + '</div>';
  h += '<div class="wr-card"><div class="wm-try">Plan it in five minutes, write it, then compare.</div><div class="v-row"><button class="v-btn" id="wbTry">Write it in the Checker</button><button class="v-btn alt" id="wbRoles">' + (st.roles ? 'Hide paragraph jobs' : 'Show paragraph jobs') + '</button></div></div>';
  h += '<div class="wr-card wm-model"><h3>Band 9 target essay</h3>' + m.model.map(function(p, i){ return (st.roles ? '<div class="wb-role">' + (i + 1) + '. ' + esc(m.roles[i]) + '</div>' : '') + '<p class="wm-p">' + esc(p) + '</p>'; }).join('') + '<div class="wr-note">' + m.words + ' words (numbers count as words).</div></div>';
  h += '<div class="wr-card"><h3>Why it scores Band 9</h3>' + Object.keys(m.notes).map(function(k){ return '<div class="wr-li"><b>' + esc(k) + ':</b> ' + esc(m.notes[k]) + '</div>'; }).join('') + '</div>';
  h += '<div class="wr-card"><h3>First-sentence test</h3><p class="wm-p">Read only the first sentence of each paragraph:</p>' + m.model.map(function(p, i){ return '<div class="wr-li tip">' + esc(p.split(/(?<=[.!?])\s+/)[0]) + '</div>'; }).join('') + '<div class="wr-note">If these five sentences tell the story of the essay, the structure is working.</div></div>';
  h += '<div class="wr-card"><h3>Language to learn</h3>' + m.lang.map(function(w){ return '<span class="wr-chip">' + esc(w) + '</span>'; }).join('') + '</div>';
  h += '<div class="v-row">' + (ix > 0 ? '<a class="v-btn alt wm-nav" href="#' + list[ix - 1].id + '">← Previous</a>' : '') + (ix < list.length - 1 ? '<a class="v-btn alt wm-nav" href="#' + list[ix + 1].id + '">Next →</a>' : '') + '</div>';
  app.innerHTML = h; window.scrollTo(0, 0);
  document.getElementById('wbRoles').onclick = function(){ st.roles = !st.roles; save(); essayView(id); };
  document.getElementById('wbTry').onclick = function(){ lsSet('writingUI', { task: 't2' }); location.href = 'writing.html'; };
}
function skillView(id){
  var ix = -1, l = DATA.lessons.filter(function(x, i){ if(x.id === id) ix = i; return x.id === id; })[0];
  if(!l){ location.hash = ''; return; }
  var h = back('#', 'Back to Writing Band 9') + head(esc(l.title), 'Lesson ' + (ix + 1) + ' of ' + DATA.lessons.length + ' · ' + esc(l.time));
  h += '<div class="wr-card">' + l.intro.map(function(p){ return '<p class="wm-p">' + esc(p) + '</p>'; }).join('') + '</div>';
  if(l.points.length) h += '<div class="wr-card">' + l.points.map(function(p){ return '<div class="wr-li"><b>' + esc(p[0]) + ':</b> ' + esc(p[1]) + '<div class="wr-note">' + esc(p[2]) + '</div></div>'; }).join('') + '</div>';
  if(l.steps.length) h += '<div class="wr-card"><h3>How to do it</h3><ol class="wm-proc">' + l.steps.map(function(s){ return '<li>' + esc(s) + '</li>'; }).join('') + '</ol></div>';
  if(l.pairs.length) h += '<div class="wr-card"><h3>Before and after</h3>' + l.pairs.map(function(p){ return '<div class="wb-pair"><div class="wr-li no">' + esc(p[0]) + '</div><div class="wr-li ok">' + esc(p[1]) + '</div><div class="wr-note">' + esc(p[2]) + '</div></div>'; }).join('') + '</div>';
  var drill = { open: 'open', connect: 'link', nouns: 'noun', hedge: 'hedge', read: 'qtype' }[id];
  h += '<div class="v-row">' + (drill ? '<a class="v-btn wm-nav" href="#practice/' + drill + '">Practise this</a>' : '') + (ix < DATA.lessons.length - 1 ? '<a class="v-btn alt wm-nav" href="#skill/' + DATA.lessons[ix + 1].id + '">Next lesson →</a>' : '') + '</div>';
  app.innerHTML = h; window.scrollTo(0, 0);
}
function jobsItems(){
  var all = [];
  DATA.essays.forEach(function(m){ m.roles.forEach(function(r, i){ all.push(r); }); });
  var uniq = all.filter(function(r, i){ return all.indexOf(r) === i; });
  var pool = [];
  DATA.essays.forEach(function(m){ m.model.forEach(function(p, i){ if(i === 0 || i === m.model.length - 1) return; pool.push({ p: p, role: m.roles[i], et: m.etype }); }); });
  return shuffle(pool).slice(0, 8).map(function(x){
    var wrong = shuffle(uniq.filter(function(r){ return r !== x.role; })).slice(0, 3), opts = shuffle(wrong.concat([x.role]));
    return { q: 'Read this body paragraph. What is its job in the essay?|' + x.p, opts: opts, a: opts.indexOf(x.role), why: 'This paragraph\'s job is: ' + x.role + '.' };
  });
}
var run = null;
function practice(id){
  var d = id === 'jobs' ? { id: 'jobs', title: 'What job does this paragraph do?', items: jobsItems() } : DATA.drills.filter(function(x){ return x.id === id; })[0];
  if(!d){ location.hash = ''; return; }
  run = { d: d, items: id === 'jobs' ? d.items : shuffle(d.items).slice(0, 10), i: 0, right: 0, done: false };
  step();
}
function step(){
  var r = run, h = back('#', 'Back to Writing Band 9');
  if(r.i >= r.items.length){
    var pct = Math.round(100 * r.right / r.items.length);
    if(!scores[r.d.id] || scores[r.d.id] < pct){ scores[r.d.id] = pct; lsSet('wb9Scores', scores); }
    var day = new Date().toISOString().slice(0, 10), key = 'wb9Xp_' + r.d.id;
    if(pct >= 80 && localStorage.getItem(key) !== day){ localStorage.setItem(key, day); award(3, 'writing'); }
    h += head(esc(r.d.title), 'Finished') + '<div class="wr-card"><h3>' + r.right + ' out of ' + r.items.length + ' (' + pct + '%)</h3><p class="wm-p">' + (pct >= 80 ? 'Strong. Try a different practice set, or write an essay in the Checker.' : 'Read the explanations again and have another go. Each round mixes the questions.') + '</p><div class="v-row"><button class="v-btn" id="wbAgain">Another round</button><a class="v-btn alt wm-nav" href="#">Back</a></div></div>';
    app.innerHTML = h; window.scrollTo(0, 0);
    document.getElementById('wbAgain').onclick = function(){ practice(r.d.id); };
    return;
  }
  var it = r.items[r.i], parts = it.q.split('|'), q = parts[0], ctx = parts[1];
  h += head(esc(r.d.title), 'Question ' + (r.i + 1) + ' of ' + r.items.length + ' · ' + r.right + ' correct');
  h += '<div class="wr-card"><p class="wm-p"><b>' + esc(q) + '</b></p>' + (ctx ? '<p class="wm-p wb-ctx">' + esc(ctx) + '</p>' : '') + '<div id="wbOpts">' + it.opts.map(function(o, k){ return '<button class="wb-opt" data-k="' + k + '">' + esc(o) + '</button>'; }).join('') + '</div><div id="wbFb"></div></div>';
  app.innerHTML = h; window.scrollTo(0, 0);
  app.querySelectorAll('.wb-opt').forEach(function(b){ b.onclick = function(){
    var k = +b.getAttribute('data-k'), ok = k === it.a;
    app.querySelectorAll('.wb-opt').forEach(function(x, j){ x.disabled = true; x.classList.toggle('good', j === it.a); if(j === k && !ok) x.classList.add('bad'); });
    if(ok) r.right++;
    document.getElementById('wbFb').innerHTML = '<div class="wr-li ' + (ok ? 'ok' : 'no') + '"><b>' + (ok ? 'Correct.' : 'Not quite.') + '</b> ' + esc(it.why) + '</div><div class="v-row"><button class="v-btn" id="wbNext">' + (r.i + 1 >= r.items.length ? 'See score' : 'Next') + '</button></div>';
    document.getElementById('wbNext').onclick = function(){ r.i++; step(); };
  }; });
}
function route(){
  if(!DATA) return;
  var r = decodeURIComponent(location.hash.replace(/^#/, ''));
  if(!r) home(); else if(r.indexOf('type/') === 0) typeView(r.slice(5)); else if(r.indexOf('skill/') === 0) skillView(r.slice(6)); else if(r.indexOf('practice/') === 0) practice(r.slice(9)); else essayView(r);
}
app.innerHTML = BACK + '<div class="empty-card">Loading…</div>';
getJson('data/writing/band9.json').then(function(d){ DATA = d; window.addEventListener('hashchange', route); route(); }).catch(function(){ app.innerHTML = BACK + '<div class="empty-card">Could not load. Check your connection and reload.</div>'; });
