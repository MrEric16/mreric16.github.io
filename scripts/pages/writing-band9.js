var BACK = back('writing-hub.html', 'Back to IELTS Writing');
var DATA = null, PR = null;
var st = lsGet('wb9UI', { roles: true, tab: 'essays' });
var prog = lsGet('wb9Prog', {}), drafts = lsGet('wb9Draft', {});
function saveProg(){ lsSet('wb9Prog', prog); }
function saveDrafts(){ lsSet('wb9Draft', drafts); }
function save(){ lsSet('wb9UI', st); }
function essays(key){ return DATA.essays.filter(function(m){ return m.etype === key; }); }
function typeOf(key){ return DATA.guides.types.filter(function(t){ return t.key === key; })[0]; }
function bullets(a, cls){ return a.map(function(x){ return '<div class="wr-li ' + (cls || 'tip') + '">' + esc(x) + '</div>'; }).join(''); }
var TABS = [['essays', 'Essays'], ['skills', 'Skills'], ['practice', 'Practice'], ['phrases', 'Phrases']];
function home(){
  var G = DATA.guides, h = BACK + head('Writing Band 9');
  h += '<div class="wr-sel">' + TABS.map(function(t){ return '<button data-tab="' + t[0] + '" class="' + (st.tab === t[0] ? 'on' : '') + '">' + t[1] + '</button>'; }).join('') + '</div>';
  if(st.tab === 'essays'){
    h += '<div class="wm-grid">' + G.types.map(function(t){ return '<a class="wm-tile" href="#type/' + t.key + '"><span class="wm-type">' + essays(t.key).length + ' essays</span><b>' + esc(t.name) + '</b><span class="wm-w">' + esc(t.asks[0]) + '</span></a>'; }).join('') + '</div>';
    h += '<div class="wr-card" style="margin-top:12px;"><h3>Ground rules for every essay</h3>' + bullets(G.principles) + '</div>';
  } else if(st.tab === 'skills'){
    h += '<div class="wm-grid">' + DATA.lessons.map(function(l, i){ return '<a class="wm-tile" href="#skill/' + l.id + '"><span class="wm-type">Lesson ' + (i + 1) + ' · ' + esc(l.time) + '</span><b>' + esc(l.title) + '</b></a>'; }).join('') + '</div>';
  } else if(st.tab === 'practice'){
    h += prHome();
  } else {
    h += '<div class="wr-card"><h3>Phrase bank by job</h3>' + G.phrases.map(function(p){ return '<div class="wr-li"><b>' + esc(p[0]) + '</b></div><div>' + p[1].map(function(x){ return '<span class="wr-chip">' + esc(x) + '</span>'; }).join('') + '</div>'; }).join('') + '</div>';
  }
  h += '<div class="v-row" style="margin-top:10px;"><a class="v-btn alt wm-nav" href="writing.html">Writing Checker</a></div>';
  app.innerHTML = h; window.scrollTo(0, 0);
  app.querySelectorAll('[data-tab]').forEach(function(b){ b.onclick = function(){ st.tab = b.getAttribute('data-tab'); save(); if(st.tab === 'practice' && !PR) withPr(home); else home(); }; });
}
function typeView(key){
  var t = typeOf(key); if(!t){ location.hash = ''; return; }
  var h = back('#', 'Back to Writing Band 9') + head(esc(t.name));
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
  h += '<div class="wr-card"><div class="v-row"><button class="v-btn" id="wbTry">Write it in the Checker</button><button class="v-btn alt" id="wbRoles">' + (st.roles ? 'Hide paragraph jobs' : 'Show paragraph jobs') + '</button></div></div>';
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
  var drill = { read: 't2-intro', open: 't2-intro', connect: 'cause', nouns: 'nominal', hedge: 't2-body', efficient: 't2-concl', plan: 't2-body' }[id];
  h += '<div class="v-row">' + (drill ? '<a class="v-btn wm-nav" href="#practice/' + drill + '">Write it now</a>' : '') + (ix < DATA.lessons.length - 1 ? '<a class="v-btn alt wm-nav" href="#skill/' + DATA.lessons[ix + 1].id + '">Next lesson →</a>' : '') + '</div>';
  app.innerHTML = h; window.scrollTo(0, 0);
}
var US_RE = /\b(colors?|colored|favorites?|organiz\w*|centers?|behaviors?|realiz\w*|analyz\w*|gotten|neighbors?|labor|defense|traveled|traveling|labeled|catalog)\b/i;
var CONTR_RE = /\b\w+n['’]t\b|\b\w+['’](re|ve|ll|d|m)\b/i;
function wordsOf(t){ return t.match(/[A-Za-z]+(?:['’-][A-Za-z]+)*|\d[\d,.]*/g) || []; }
function sentsOf(t){ return t.trim().replace(/([.!?])\s+/g, '$1\n').split('\n').filter(function(x){ return x.trim(); }); }
function gramsOf(w, n){ var o = {}; for(var i = 0; i + n <= w.length; i++) o[w.slice(i, i + n).join(' ')] = 1; return o; }
function lower(a){ return a.map(function(x){ return x.toLowerCase(); }); }
function runChecks(ex, text){
  var res = [], w = lower(wordsOf(text)), ss = sentsOf(text);
  res.push([w.length + ' words (needed ' + ex.min + ' to ' + ex.max + ')', w.length >= ex.min && w.length <= ex.max]);
  res.push([ss.length + ' sentence' + (ss.length === 1 ? '' : 's') + ' (needed ' + (ex.smin === ex.smax ? ex.smin : ex.smin + ' to ' + ex.smax) + ')', ss.length >= ex.smin && ss.length <= ex.smax]);
  res.push(['every sentence starts with a capital letter', ss.every(function(x){ return /^[A-Z0-9$']/.test(x.trim()); })]);
  res.push(['the text ends with a full stop (or ? or !)', /[.!?]$/.test(text.trim())]);
  res.push(['no contractions (write do not, it is ...)', !CONTR_RE.test(text)]);
  res.push(['British spelling only', !US_RE.test(text)]);
  var fn = {}; PR.func.forEach(function(x){ fn[x] = 1; });
  var fr = w.length >= 12 ? w.filter(function(x){ return fn[x]; }).length / w.length : 1;
  res.push(['reads as connected English prose', fr >= 0.15]);
  if(ex.noDigits) res.push(['no digits in this part of the essay', !/\d/.test(text)]);
  if(ex.source){
    var n = ex.n, sg = gramsOf(lower(wordsOf(ex.source)), n), hit = '';
    for(var i = 0; i + n <= w.length && !hit; i++){ var g = w.slice(i, i + n).join(' '); if(sg[g]) hit = g; }
    res.push([hit ? 'copied ' + n + ' words in a row from the task: "' + hit + '"' : 'no ' + n + ' words in a row copied from the task', !hit]);
  }
  ex.checks.forEach(function(c){
    var hit = false; try{ hit = new RegExp(c[1], 'i').test(text); }catch(e){}
    res.push([c[0], c[2] === 'must' ? hit : !hit]);
  });
  return res;
}
function setOf(key){ return PR.sets.filter(function(x){ return x.key === key; })[0]; }
function exInfo(id){ for(var i = 0; i < PR.sets.length; i++){ var s = PR.sets[i]; for(var j = 0; j < s.items.length; j++) if(s.items[j].id === id) return { set: s, ex: s.items[j], ix: j }; } return null; }
function doneIn(s){ return s.items.filter(function(e){ return prog[e.id] && prog[e.id].r; }).length; }
function prTile(s){
  return '<a class="wm-tile" href="#practice/' + s.key + '"><span class="wm-type">' + doneIn(s) + ' of ' + s.items.length + ' written</span><b>' + esc(s.title) + '</b><span class="wm-w">' + esc(s.blurb) + '</span></a>';
}
function prHome(){
  var h = '';
  [['build', 'Build the sentence (grammar and punctuation)'], ['task1', 'Task 1 parts'], ['task2', 'Task 2 parts']].forEach(function(g){
    h += '<div class="section-head" style="margin-top:14px;"><h2>' + g[1] + '</h2></div><div class="wm-grid">' + PR.sets.filter(function(s){ return s.group === g[0]; }).map(prTile).join('') + '</div>';
  });
  var all = 0, dn = 0; PR.sets.forEach(function(s){ all += s.items.length; dn += doneIn(s); });
  return h + '<div class="wr-note" style="margin-top:12px;">Progress: ' + dn + ' of ' + all + ' exercises written. Saved on this device only.</div>';
}
function setView(key){
  var s = setOf(key); if(!s){ location.hash = ''; return; }
  var h = back('#', 'Back to Writing Band 9') + head(esc(s.title), esc(s.blurb));
  h += '<div class="wr-card"><p class="wm-p"><b>' + esc(s.task) + '</b></p>' + (s.why ? '<p class="wm-p">' + esc(s.why) + '</p>' : '') + (s.formula ? '<div class="wr-li tip">' + esc(s.formula) + '</div>' : '') + '</div>';
  h += '<div class="wm-grid">' + s.items.map(function(e, i){
    var p = prog[e.id], mark = p && p.r === 2 ? '★ written twice' : p && p.r ? '✓ written' : 'not written';
    var label = e.title || (e.facts ? e.facts[0] : e.question || e.idea || 'Exercise');
    return '<a class="wm-tile" href="#ex/' + e.id + '"><span class="wm-type">' + (i + 1) + ' · ' + mark + '</span><b>' + esc(label.length > 70 ? label.slice(0, 68) + '…' : label) + '</b></a>';
  }).join('') + '</div>';
  app.innerHTML = h; window.scrollTo(0, 0);
}
function listHtml(a){ return a.map(function(x){ return '<div class="wr-li tip">' + esc(x) + '</div>'; }).join(''); }
function exView(id){
  var info = exInfo(id); if(!info){ location.hash = ''; return; }
  var s = info.set, e = info.ex, ix = info.ix, p = prog[id] || { r: 0, att: 0 };
  var h = back('#practice/' + s.key, esc(s.title)) + head(esc(s.title), 'Exercise ' + (ix + 1) + ' of ' + s.items.length);
  h += '<div class="wr-card"><p class="wm-p"><b>' + esc(e.task || s.task) + '</b></p>' + (e.task ? '<p class="wm-p wb-sub">' + esc(s.task) + '</p>' : '') + '</div>';
  if(e.facts) h += '<div class="wr-card"><h3>' + (s.group === 'build' ? 'Facts to use' : 'Fact sheet') + '</h3>' + listHtml(e.facts) + '</div>';
  if(e.table) h += '<div class="wr-card"><h3>' + esc(e.title) + '</h3>' + (e.note ? '<div class="wr-note" style="margin:0 0 6px;">' + esc(e.note) + '</div>' : '') + '<div class="wb-tw"><table class="wb-tab"><thead><tr>' + e.table.head.map(function(c){ return '<th>' + esc(c) + '</th>'; }).join('') + '</tr></thead><tbody>' + e.table.rows.map(function(r){ return '<tr>' + r.map(function(c){ return '<td>' + esc(c) + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table></div></div>';
  if(e.question) h += '<div class="wr-card"><h3>The question</h3><p class="wm-p">' + esc(e.question) + '</p>' + (e.summary ? '<h3 style="margin-top:10px;">Your essay so far</h3>' + listHtml(e.summary) : '') + '</div>';
  if(e.idea) h += '<div class="wr-card"><h3>Your paragraph</h3><p class="wm-p"><b>' + esc(e.idea) + '</b></p>' + listHtml(e.support) + '</div>';
  if(s.formula || s.hint) h += '<div class="wr-card"><div class="v-row"><button class="v-btn alt" id="wbHint">Show hint</button></div><div id="wbHintBox" hidden>' + (s.formula ? '<div class="wr-li tip"><b>Pattern:</b> ' + esc(s.formula) + '</div>' : '') + (s.hint ? '<p class="wm-p">' + esc(s.hint) + '</p>' : '') + '</div></div>';
  h += '<div class="wr-card"><h3 id="wbRound">' + (p.r ? 'Write it again in a different way' : 'Your answer') + '</h3><textarea id="wbTa" class="wb-ta" rows="' + (e.max > 90 ? 9 : e.max > 45 ? 6 : 4) + '" autocomplete="off" autocorrect="off" autocapitalize="sentences" spellcheck="false" placeholder="Type here. Pasting is switched off."></textarea><div class="wb-count" id="wbCount"></div><div class="v-row"><button class="v-btn" id="wbCheck">Check my answer</button></div><div id="wbRes"></div></div>';
  h += '<div id="wbAfter"></div><div class="v-row" style="margin-top:8px;">' + (ix > 0 ? '<a class="v-btn alt wm-nav" href="#ex/' + s.items[ix - 1].id + '">← Previous</a>' : '') + '<a class="v-btn alt wm-nav" href="#practice/' + s.key + '">All exercises</a></div>';
  app.innerHTML = h; window.scrollTo(0, 0);
  var ta = document.getElementById('wbTa'), round = p.r >= 1 ? 2 : 1, first = p.first || '';
  if(p.r < 1) ta.value = drafts[id] || '';
  function count(){ document.getElementById('wbCount').textContent = wordsOf(ta.value).length + ' words · needed ' + e.min + ' to ' + e.max; }
  function stop(ev){ ev.preventDefault(); document.getElementById('wbRes').innerHTML = '<div class="wr-li no">Pasting is switched off. Type it yourself.</div>'; }
  ['paste', 'drop', 'cut'].forEach(function(n){ ta.addEventListener(n, stop); });
  ta.addEventListener('beforeinput', function(ev){ if(/^insertFrom(Paste|Drop|Yank)/.test(ev.inputType || '')) stop(ev); });
  ta.addEventListener('input', function(){ count(); if(round === 1){ drafts[id] = ta.value; saveDrafts(); } });
  count();
  var hb = document.getElementById('wbHint'); if(hb) hb.onclick = function(){ var b = document.getElementById('wbHintBox'); b.hidden = !b.hidden; hb.textContent = b.hidden ? 'Show hint' : 'Hide hint'; };
  function after(){
    var nx = s.items[ix + 1];
    var a = '<div class="wr-card wm-model"><h3>Model answer</h3><p class="wm-p">' + esc(e.model) + '</p><div class="wr-note">Compare, do not copy. Where is your version weaker: precision, structure or punctuation? A model is one good answer, not the only one.</div></div>';
    if(round === 1) a += '<div class="wr-card"><p class="wm-p"><b>Now write it again.</b> A second, different version that still passes every check. It must not repeat your first sentences.</p><div class="v-row"><button class="v-btn" id="wbRe">Write a second version</button></div></div>';
    a += '<div class="v-row">' + (nx ? '<a class="v-btn wm-nav" href="#ex/' + nx.id + '">Next exercise →</a>' : '') + '</div>';
    document.getElementById('wbAfter').innerHTML = a;
    var re = document.getElementById('wbRe');
    if(re) re.onclick = function(){ round = 2; first = ta.value; ta.value = ''; ta.readOnly = false; document.getElementById('wbRound').textContent = 'Second version'; document.getElementById('wbRes').innerHTML = ''; document.getElementById('wbAfter').innerHTML = ''; count(); ta.focus(); };
  }
  document.getElementById('wbCheck').onclick = function(){
    var text = ta.value.trim(), res = document.getElementById('wbRes');
    if(!text){ res.innerHTML = '<div class="wr-li no">Write something first.</div>'; return; }
    var r = runChecks(e, text);
    if(round === 2 && first){
      var g = gramsOf(lower(wordsOf(first)), 3), b = lower(wordsOf(text)), tot = 0, same = 0;
      for(var i = 0; i + 3 <= b.length; i++){ tot++; if(g[b.slice(i, i + 3).join(' ')]) same++; }
      r.push(['clearly different from your first version', tot === 0 || same / tot < 0.5]);
    }
    var ok = r.every(function(x){ return x[1]; });
    p.att = (p.att || 0) + 1;
    res.innerHTML = r.map(function(x){ return '<div class="wr-li ' + (x[1] ? 'ok' : 'no') + '">' + esc(x[0]) + '</div>'; }).join('') + (ok ? '<div class="wr-li ok"><b>Every check passed.</b> Attempts so far: ' + p.att + '.</div>' : '<div class="wr-li no"><b>Not yet.</b> Fix the lines marked ✗ and check again. The model answer stays locked until you pass.</div>');
    if(ok){
      if(round === 1){ if(!p.r){ p.r = 1; p.first = text; award(3, 'writing'); } }
      else { if(p.r < 2) award(2, 'writing'); p.r = 2; }
      delete drafts[id]; saveDrafts(); ta.readOnly = true; after();
    }
    prog[id] = p; saveProg();
  };
}

function route(){
  if(!DATA) return;
  var r = decodeURIComponent(location.hash.replace(/^#/, ''));
  if(!r){ if(st.tab === 'practice' && !PR) withPr(home); else home(); return; }
  if(r.indexOf('type/') === 0) typeView(r.slice(5));
  else if(r.indexOf('skill/') === 0) skillView(r.slice(6));
  else if(r.indexOf('practice/') === 0 || r.indexOf('ex/') === 0) withPr(function(){ if(r.indexOf('ex/') === 0) exView(r.slice(3)); else setView(r.slice(9)); });
  else essayView(r);
}
function withPr(fn){
  if(PR){ fn(); return; }
  app.innerHTML = BACK + '<div class="empty-card">Loading\u2026</div>';
  getJson('data/writing/practice.json').then(function(d){ PR = d; fn(); }).catch(function(){ app.innerHTML = BACK + '<div class="empty-card">Could not load the exercises. Check your connection and reload.</div>'; });
}
app.innerHTML = BACK + '<div class="empty-card">Loading\u2026</div>';
getJson('data/writing/band9.json').then(function(d){ DATA = d; window.addEventListener('hashchange', route); if(st.tab === 'practice' && !location.hash) withPr(home); else route(); }).catch(function(){ app.innerHTML = BACK + '<div class="empty-card">Could not load. Check your connection and reload.</div>'; });
