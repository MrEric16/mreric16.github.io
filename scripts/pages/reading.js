var BACK = back('index.html#geography-hub/study', 'Back to Train Your Brain');
var BASE = 'data/reading/';
var TYPES = [
  ['tfng', 'True / False / Not given', ['tfng']], ['mcq', 'Multiple choice', ['mcq', 'multi']], ['head', 'Matching headings', ['head']], ['info', 'Matching information', ['info']],
  ['feat', 'Matching features and classification', ['feat']], ['end', 'Matching sentence endings', ['end']], ['sent', 'Sentence completion', ['sent']],
  ['summ', 'Summary and note completion', ['summ']], ['table', 'Table completion', ['table']], ['flow', 'Flow-chart completion', ['flow']],
  ['diag', 'Diagram labelling', ['diag']], ['pic', 'Picture matching', ['pic']], ['short', 'Short answer questions', ['short']]
];
var ROMAN = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv'];
var NUMW = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE'];
var S = lsGet('readSet', { timed: true });
var IDX = null, CACHE = {}, T = null, tmr = null;
function stats(){ return lsGet('readStats', { single: { n: 0, c: 0, t: 0 }, full: { n: 0, c: 0, t: 0, best: 0 }, ty: {} }); }
function seenP(){ return lsGet('readSeen', []); }
function seenG(){ return lsGet('readSeenG', {}); }
function loadIndex(){ if(IDX) return Promise.resolve(IDX); return getJson(BASE + 'index.json').then(function(d){ IDX = d.passages; return IDX; }); }
function loadP(id){ if(CACHE[id]) return Promise.resolve(JSON.parse(JSON.stringify(CACHE[id]))); return getJson(BASE + id + '.json').then(function(d){ CACHE[id] = d; return JSON.parse(JSON.stringify(d)); }); }
function pick1(a){ return a[Math.floor(Math.random() * a.length)]; }
function stopTimer(){ if(tmr){ clearInterval(tmr); tmr = null; } }

/* ---------- assembling a task from a passage ---------- */
var FIXED = { summ: 1, table: 1, flow: 1, diag: 1, multi: 1 };
function gsize(g){ return g.t === 'multi' ? 2 : (g.items ? g.items.length : g.a.length); }
function gmin(g){ return FIXED[g.t] ? gsize(g) : Math.min(3, gsize(g)); }
function choose(p, want, target){
  var sg = seenG(), used = sg[p.id] || [];
  var gs = p.groups.filter(function(g){ return !want || want.indexOf(g.t) >= 0; });
  var best = null;
  for(var tries = 0; tries < 400; tries++){
    var order = shuffle(gs).sort(function(a, b){ return (used.indexOf(a.id) >= 0 ? 1 : 0) - (used.indexOf(b.id) >= 0 ? 1 : 0); });
    if(tries % 2) order = shuffle(gs);
    var sel = [], types = {}, mn = 0, mx = 0;
    for(var i = 0; i < order.length && sel.length < 4; i++){
      var g = order[i]; if(types[g.t] && !want) continue;
      if(mn + gmin(g) > target) continue;
      sel.push(g); types[g.t] = 1; mn += gmin(g); mx += gsize(g);
      if(mx >= target && sel.length >= (want ? 1 : 2)) break;
    }
    if(sel.length && mn <= target && (mx >= target || tries > 300)){ best = sel; if(mx >= target) break; }
  }
  if(!best) best = [gs[0]];
  // sizes: start at min, grow randomly until target
  var sz = best.map(gmin), tot = sz.reduce(function(a, b){ return a + b; }, 0), guard = 0;
  while(tot < target && guard++ < 200){
    var k = Math.floor(Math.random() * best.length);
    if(!FIXED[best[k].t] && sz[k] < gsize(best[k])){ sz[k]++; tot++; }
    else if(best.every(function(g, i){ return FIXED[g.t] || sz[i] >= gsize(g); })) break;
  }
  return best.map(function(g, i){ return trim(g, sz[i], p); });
}
function diverse(items, k, key){
  if(k >= items.length) return shuffle(items);
  for(var t = 0; t < 40; t++){ var s = shuffle(items).slice(0, k); if(k < 4 || new Set(s.map(key)).size >= 2 + (k >= 6 ? 1 : 0)) return s; }
  return shuffle(items).slice(0, k);
}
function trim(g0, k, p){
  var g = JSON.parse(JSON.stringify(g0)), t = g.t;
  if(t === 'multi'){ var m = shuffle(g.o.map(function(x, i){ return i; })); g.a = g.a.map(function(a){ return m.indexOf(a); }); g.o = m.map(function(i){ return g0.o[i]; }); return g; }
  if(t === 'tfng') g.items = diverse(g.items, k, function(x){ return x.a; });
  else if(t === 'head'){ g.items = shuffle(g.items).slice(0, k).sort(function(a, b){ return a.p < b.p ? -1 : 1; }); var hm = shuffle(g.heads.map(function(x, i){ return i; })); g.items.forEach(function(it){ it.a = hm.indexOf(it.a); }); g.heads = hm.map(function(i){ return g0.heads[i]; }); }
  else if(t === 'mcq'){ g.items = shuffle(g.items).slice(0, k); g.items.forEach(function(it){ var m = shuffle([0, 1, 2, 3]), oo = it.o.slice(); it.o = m.map(function(i){ return oo[i]; }); it.a = m.indexOf(it.a); }); }
  else if(t === 'end'){ g.items = shuffle(g.items).slice(0, k); var em = shuffle(g.endings.map(function(x, i){ return i; })); g.items.forEach(function(it){ it.a = em.indexOf(it.a); }); g.endings = em.map(function(i){ return g0.endings[i]; }); }
  else if(t === 'pic'){ g.items = shuffle(g.items).slice(0, k); var pm = shuffle(g.pics.map(function(x, i){ return i; })); g.items.forEach(function(it){ it.a = pm.indexOf(it.a); }); g.pics = pm.map(function(i){ return g0.pics[i]; }); }
  else if(g.items) g.items = (t === 'feat' ? diverse(g.items, k, function(x){ return x.a; }) : shuffle(g.items).slice(0, k));
  if(t === 'info') g.letters = p.paras.map(function(x){ return x.l; });
  return g;
}
function slots(g){ // flat list of questions for a group
  var t = g.t;
  if(t === 'multi') return [{ e: g.e[0] }, { e: g.e[1] }];
  if(g.items) return g.items.map(function(it){ return { it: it, e: it.e }; });
  return g.a.map(function(a, i){ return { a: a, e: g.e[i] }; });
}
function build(mode, parts){ // parts: [{p, groups}]
  var n = 1;
  parts.forEach(function(pt){ pt.groups.forEach(function(g){ g.s = n; g.q = slots(g); g.q.forEach(function(q, i){ q.n = n + i; q.g = g; }); n += g.q.length; }); });
  return n - 1;
}

/* ---------- picking passages ---------- */
function choosePassages(idx, lv, nPick, avoidTopics){
  var sn = seenP(), pool = idx.slice();
  var fresh = pool.filter(function(x){ return sn.indexOf(x.id) < 0; });
  return { fresh: fresh, all: pool };
}
function pickOne(idx, lv, exclude, topics, needTypes){
  var sn = seenP(), ok = idx.filter(function(x){ return exclude.indexOf(x.id) < 0 && (!lv || x.lv === lv) && (!needTypes || x.types.some(function(t){ return needTypes.indexOf(t) >= 0; })); });
  var nt = ok.filter(function(x){ return topics.indexOf(x.topic) < 0; }); if(nt.length) ok = nt;
  var fr = ok.filter(function(x){ return sn.indexOf(x.id) < 0; });
  if(!fr.length && ok.length){ var keep = sn.filter(function(id){ return !ok.some(function(x){ return x.id === id; }); }); lsSet('readSeen', keep); fr = ok; }
  return fr.length ? pick1(fr) : null;
}
function markSeen(parts){
  var sn = seenP(), sg = seenG();
  parts.forEach(function(pt){ if(sn.indexOf(pt.p.id) < 0) sn.push(pt.p.id); var u = sg[pt.p.id] || []; pt.groups.forEach(function(g){ if(u.indexOf(g.id) < 0) u.push(g.id); }); if(u.length >= pt.p.groups.length) u = []; sg[pt.p.id] = u; });
  lsSet('readSeen', sn.slice(-200)); lsSet('readSeenG', sg);
}
function start(mode, arg){
  stopTimer(); app.innerHTML = BACK + head('Reading Practice', '') + '<div class="v-hint">Preparing your test...</div>';
  loadIndex().then(function(idx){
    var metas = [];
    if(mode === 'full'){
      var topics = [], ex = [];
      [1, 2, 3].forEach(function(lv){ var m = pickOne(idx, lv, ex, topics) || pickOne(idx, 0, ex, topics); if(m){ metas.push(m); ex.push(m.id); topics.push(m.topic); } });
    } else if(mode === 'drill'){
      var m = pickOne(idx, 0, [], [], arg.want); if(m) metas.push(m);
    } else { var m2 = pickOne(idx, arg.lv || 0, [], [], null) || pickOne(idx, 0, [], [], null); if(m2) metas.push(m2); }
    if(!metas.length) throw new Error('none');
    return Promise.all(metas.map(function(m){ return loadP(m.id); }));
  }).then(function(ps){
    var tg = mode === 'full' ? shuffle([13, 13, 14]) : [mode === 'drill' ? 14 : pick1([13, 14])];
    var parts = ps.map(function(p, i){ return { p: p, groups: choose(p, mode === 'drill' ? arg.want : null, tg[i]) }; });
    var total = build(mode, parts);
    markSeen(parts);
    var secs = mode === 'full' ? 3600 : 1200;
    T = { mode: mode, drill: mode === 'drill' ? arg : null, parts: parts, total: total, ans: {}, checked: false, cur: 0, pane: 'q', showAll: false, secs: secs, endAt: S.timed ? Date.now() + secs * 1000 : 0, res: null, t0: Date.now() };
    draw(); window.scrollTo(0, 0);
    if(S.timed) tmr = setInterval(tick, 500);
  }).catch(function(){ app.innerHTML = BACK + head('Reading Practice', '') + '<div class="v-hint">Could not load a test. Check your connection and try again.</div>'; });
}

/* ---------- marking ---------- */
function norm(s){ return String(s == null ? '' : s).toLowerCase().replace(/[‘’]/g, "'").replace(/-/g, ' ').replace(/[^a-z0-9' ]/g, ' ').replace(/\s+/g, ' ').trim(); }
function okq(q){
  var g = q.g, t = g.t, a = T.ans[q.n];
  if(t === 'multi'){ var sel = T.ans['m' + g.s] || [], c = sel.filter(function(i){ return g.a.indexOf(i) >= 0; }).length; return q.n === g.s ? c >= 1 : c >= 2; }
  if(t === 'tfng') return a === q.it.a;
  if(t === 'mcq' || t === 'pic' || t === 'head' || t === 'feat' || t === 'end') return a !== undefined && a !== '' && +a === q.it.a;
  if(t === 'info') return a === q.it.a;
  var acc = t === 'sent' || t === 'short' ? q.it.a : q.a, v = norm(a); if(!v) return false;
  if((t === 'summ' || t === 'diag') && g.bank) return acc.some(function(x){ return norm(x) === v; });
  return acc.some(function(x){ return norm(x) === v; });
}
function fixText(q){
  var g = q.g, t = g.t, L = function(i){ return String.fromCharCode(65 + i); };
  if(t === 'tfng') return { T: 'True', F: 'False', Y: 'Yes', N: 'No', NG: 'Not given' }[q.it.a];
  if(t === 'mcq') return L(q.it.a) + '. ' + q.it.o[q.it.a];
  if(t === 'multi') return g.a.map(function(i){ return L(i) + '. ' + g.o[i]; }).join('  and  ');
  if(t === 'head') return ROMAN[q.it.a] + '. ' + g.heads[q.it.a];
  if(t === 'info') return q.it.a;
  if(t === 'feat') return L(q.it.a) + '. ' + g.opts[q.it.a];
  if(t === 'end') return L(q.it.a) + '. ' + g.endings[q.it.a];
  if(t === 'pic') return L(q.it.a);
  return (t === 'sent' || t === 'short' ? q.it.a : q.a)[0];
}
function mine(q){
  var g = q.g, t = g.t, a = T.ans[q.n], L = function(i){ return String.fromCharCode(65 + i); };
  if(t === 'multi') return (T.ans['m' + g.s] || []).map(L).join(', ') || '';
  if(a === undefined || a === '') return '';
  if(t === 'tfng') return { T: 'True', F: 'False', Y: 'Yes', N: 'No', NG: 'Not given' }[a];
  if(t === 'head') return ROMAN[+a]; if(t === 'mcq' || t === 'feat' || t === 'end' || t === 'pic') return L(+a);
  return String(a);
}
function check(auto){
  if(T.checked) return; stopTimer();
  var res = { per: [], c: 0, ty: {} };
  T.parts.forEach(function(pt, pi){ var c = 0, n = 0; pt.groups.forEach(function(g){ g.q.forEach(function(q){ q.ok = okq(q); n++; if(q.ok) c++; var k = g.t === 'multi' ? 'mcq' : g.t; res.ty[k] = res.ty[k] || [0, 0]; res.ty[k][1]++; if(q.ok) res.ty[k][0]++; }); }); res.per.push([c, n]); res.c += c; });
  res.auto = !!auto; res.mins = Math.round((Date.now() - T.t0) / 60000);
  T.res = res; T.checked = true; T.pane = 'q'; T.cur = 0;
  var st = stats(), k = T.mode === 'full' ? st.full : st.single;
  k.n++; k.c += res.c; k.t += T.total; if(T.mode === 'full' && res.c > k.best) k.best = res.c;
  Object.keys(res.ty).forEach(function(t){ var o = st.ty[t] || { c: 0, t: 0 }; o.c += res.ty[t][0]; o.t += res.ty[t][1]; st.ty[t] = o; });
  lsSet('readStats', st); award(res.c, 'reading'); award(10, 'reading');
  draw(); window.scrollTo(0, 0);
}
function band(c){ var t = [[39, 9], [37, 8.5], [35, 8], [33, 7.5], [30, 7], [27, 6.5], [23, 6], [19, 5.5], [15, 5], [13, 4.5], [10, 4], [8, 3.5], [6, 3], [4, 2.5]]; for(var i = 0; i < t.length; i++) if(c >= t[i][0]) return t[i][1]; return 2; }

/* ---------- rendering ---------- */
function rng(g){ return g.q.length > 1 ? 'Questions ' + g.s + ' to ' + (g.s + g.q.length - 1) : 'Question ' + g.s; }
function ctrlCls(q){ return T.checked ? (q.ok ? ' ok' : ' bad') : ''; }
function inp(q, extra){
  var v = T.ans[q.n]; return '<input class="rd-in' + ctrlCls(q) + '" data-n="' + q.n + '" placeholder="' + q.n + '" value="' + esc(v || '') + '"' + (T.checked ? ' disabled' : '') + ' autocomplete="off" autocapitalize="off" spellcheck="false"' + (extra || '') + '>';
}
function sel(q, opts, lab){ // opts: [[value,label]]
  var v = T.ans[q.n];
  return '<select class="rd-sel' + ctrlCls(q) + '" data-n="' + q.n + '"' + (T.checked ? ' disabled' : '') + '><option value="">' + (lab || q.n) + '</option>' + opts.map(function(o){ return '<option value="' + esc(o[0]) + '"' + (String(v) === String(o[0]) ? ' selected' : '') + '>' + esc(o[1]) + '</option>'; }).join('') + '</select>';
}
function lim(n){ return n === 1 ? 'ONE WORD ONLY' : 'NO MORE THAN ' + NUMW[n] + ' WORDS'; }
function fill(txt, g){ // replace [[k]] by controls
  return esc(txt).replace(/\[\[(\d+)\]\]/g, function(m, k){ var q = g.q[+k - 1]; return g.bank ? sel(q, g.bank.map(function(w){ return [w, w]; }), q.n) : inp(q); });
}
function groupHtml(g){
  var t = g.t, h = '<div class="rd-grp"><div class="rd-gh">' + rng(g) + '</div>', L = function(i){ return String.fromCharCode(65 + i); }, pl = T.parts[T.cur].p.paras;
  var ins = function(s){ return '<div class="rd-ins">' + s + '</div>'; };
  if(t === 'tfng'){
    var yn = g.yn;
    h += ins(yn ? 'Do the following statements agree with the views of the writer? Choose <b>YES</b> if the statement agrees with the views of the writer, <b>NO</b> if it contradicts them, <b>NOT GIVEN</b> if it is impossible to say what the writer thinks.' : 'Do the following statements agree with the information given in the passage? Choose <b>TRUE</b> if the statement agrees with the information, <b>FALSE</b> if it contradicts it, <b>NOT GIVEN</b> if there is no information on this.');
    g.q.forEach(function(q){ var a = T.ans[q.n]; h += '<div class="rd-q"><div class="rd-qt"><b>' + q.n + '</b> ' + esc(q.it.s) + '</div><div class="rd-tf">' + (yn ? [['Y', 'Yes'], ['N', 'No'], ['NG', 'Not given']] : [['T', 'True'], ['F', 'False'], ['NG', 'Not given']]).map(function(o){ return '<button class="rd-opt' + (a === o[0] ? ' on' : '') + (T.checked && a === o[0] ? (q.ok ? ' ok' : ' bad') : '') + (T.checked && !q.ok && q.it.a === o[0] ? ' ok' : '') + '" data-n="' + q.n + '" data-v="' + o[0] + '"' + (T.checked ? ' disabled' : '') + '>' + o[1] + '</button>'; }).join('') + '</div></div>'; });
  } else if(t === 'mcq'){
    h += ins('Choose the correct letter, <b>A</b>, <b>B</b>, <b>C</b> or <b>D</b>.');
    g.q.forEach(function(q){ var a = T.ans[q.n]; h += '<div class="rd-q"><div class="rd-qt"><b>' + q.n + '</b> ' + esc(q.it.q) + '</div>' + q.it.o.map(function(o, i){ return '<button class="rd-opt blk' + (a === i ? ' on' : '') + (T.checked && a === i ? (q.ok ? ' ok' : ' bad') : '') + (T.checked && !q.ok && q.it.a === i ? ' ok' : '') + '" data-n="' + q.n + '" data-v="' + i + '"' + (T.checked ? ' disabled' : '') + '><b>' + L(i) + '</b> ' + esc(o) + '</button>'; }).join('') + '</div>'; });
  } else if(t === 'multi'){
    var sl = T.ans['m' + g.s] || [];
    h += ins('Choose <b>TWO</b> letters, <b>A</b> to <b>E</b>.') + '<div class="rd-q"><div class="rd-qt"><b>' + g.s + ' and ' + (g.s + 1) + '</b> ' + esc(g.qt || '') + '</div>' + g.o.map(function(o, i){ var on = sl.indexOf(i) >= 0; return '<button class="rd-opt blk' + (on ? ' on' : '') + (T.checked ? (g.a.indexOf(i) >= 0 ? ' ok' : (on ? ' bad' : '')) : '') + '" data-m="' + g.s + '" data-v="' + i + '"' + (T.checked ? ' disabled' : '') + '><b>' + L(i) + '</b> ' + esc(o) + '</button>'; }).join('') + '</div>';
  } else if(t === 'head'){
    h += ins('The passage has paragraphs lettered <b>A</b> to <b>' + pl[pl.length - 1].l + '</b>. Choose the correct heading for each paragraph from the list of headings. Some headings are not needed.') +
      '<div class="rd-box"><b>List of Headings</b>' + g.heads.map(function(x, i){ return '<div><b>' + ROMAN[i] + '</b> ' + esc(x) + '</div>'; }).join('') + '</div>';
    g.q.forEach(function(q){ h += '<div class="rd-q rd-row"><div class="rd-qt"><b>' + q.n + '</b> Paragraph ' + q.it.p + '</div>' + sel(q, g.heads.map(function(x, i){ return [i, ROMAN[i]]; }), 'Choose') + '</div>'; });
  } else if(t === 'info'){
    h += ins('Which paragraph contains the following information? Choose the correct letter, <b>A</b> to <b>' + pl[pl.length - 1].l + '</b>. You may use any letter more than once.');
    g.q.forEach(function(q){ h += '<div class="rd-q rd-row"><div class="rd-qt"><b>' + q.n + '</b> ' + esc(q.it.s) + '</div>' + sel(q, g.letters.map(function(l){ return [l, l]; }), 'Choose') + '</div>'; });
  } else if(t === 'feat'){
    h += ins(esc(g.title) + ' You may use any letter more than once.') + '<div class="rd-box">' + g.opts.map(function(x, i){ return '<div><b>' + L(i) + '</b> ' + esc(x) + '</div>'; }).join('') + '</div>';
    g.q.forEach(function(q){ h += '<div class="rd-q rd-row"><div class="rd-qt"><b>' + q.n + '</b> ' + esc(q.it.s) + '</div>' + sel(q, g.opts.map(function(x, i){ return [i, L(i)]; }), 'Choose') + '</div>'; });
  } else if(t === 'end'){
    h += ins('Complete each sentence with the correct ending, <b>A</b> to <b>' + L(g.endings.length - 1) + '</b>.') + '<div class="rd-box">' + g.endings.map(function(x, i){ return '<div><b>' + L(i) + '</b> ' + esc(x) + '</div>'; }).join('') + '</div>';
    g.q.forEach(function(q){ h += '<div class="rd-q rd-row"><div class="rd-qt"><b>' + q.n + '</b> ' + esc(q.it.s) + '</div>' + sel(q, g.endings.map(function(x, i){ return [i, L(i)]; }), 'Choose') + '</div>'; });
  } else if(t === 'sent'){
    h += ins('Complete the sentences. Write <b>' + lim(g.lim) + '</b> from the passage for each answer.');
    g.q.forEach(function(q){ var p = q.it.s.split('___'); h += '<div class="rd-q"><div class="rd-qt"><b>' + q.n + '</b> ' + esc(p[0]) + inp(q) + esc(p[1]) + '</div></div>'; });
  } else if(t === 'short'){
    h += ins('Answer the questions. Write <b>' + lim(g.lim) + '</b> from the passage for each answer.');
    g.q.forEach(function(q){ h += '<div class="rd-q"><div class="rd-qt"><b>' + q.n + '</b> ' + esc(q.it.q) + '</div>' + inp(q) + '</div>'; });
  } else if(t === 'summ'){
    h += ins(esc(g.title)) + (g.bank ? '<div class="rd-box rd-bank">' + g.bank.slice().sort().map(function(w){ return '<span>' + esc(w) + '</span>'; }).join('') + '</div>' : '') + '<div class="rd-sum">' + fill(g.text, g) + '</div>';
  } else if(t === 'table'){
    h += ins(esc(g.title)) + '<div class="rd-tw"><table class="rd-tab"><tr>' + g.head.map(function(x){ return '<th>' + esc(x) + '</th>'; }).join('') + '</tr>' + g.rows.map(function(r){ return '<tr>' + r.map(function(c){ return '<td>' + fill(c, g) + '</td>'; }).join('') + '</tr>'; }).join('') + '</table></div>';
  } else if(t === 'flow'){
    h += ins(esc(g.title)) + '<div class="rd-flow">' + g.steps.map(function(s, i){ return (i ? '<div class="rd-arr">&#8595;</div>' : '') + '<div class="rd-step">' + fill(s, g) + '</div>'; }).join('') + '</div>';
  } else if(t === 'diag'){
    h += ins(esc(g.title)) + '<div class="rd-dw"><svg class="rd-svg" viewBox="0 0 ' + g.w + ' ' + g.h + '" role="img">' + g.svg + g.pts.map(function(p, i){ return '<g transform="translate(' + p[0] + ',' + p[1] + ')"><circle r="13" class="dm"/><text class="dn" text-anchor="middle" y="5">' + (g.s + i) + '</text></g>'; }).join('') + '</svg></div>' + (g.bank ? '<div class="rd-box rd-bank">' + g.bank.slice().sort().map(function(w){ return '<span>' + esc(w) + '</span>'; }).join('') + '</div>' : '');
    g.q.forEach(function(q){ h += '<div class="rd-q rd-row"><div class="rd-qt"><b>' + q.n + '</b></div>' + (g.bank ? sel(q, g.bank.map(function(w){ return [w, w]; }), 'Choose') : inp(q)) + '</div>'; });
  } else if(t === 'pic'){
    h += ins(esc(g.prompt || 'Which picture matches each description? Choose the correct letter.')) + '<div class="rd-pics">' + g.pics.map(function(p, i){ return '<figure><svg class="rd-svg" viewBox="0 0 ' + p.w + ' ' + p.h + '" role="img">' + p.svg + '</svg><figcaption><b>' + L(i) + '</b></figcaption></figure>'; }).join('') + '</div>';
    g.q.forEach(function(q){ h += '<div class="rd-q rd-row"><div class="rd-qt"><b>' + q.n + '</b> ' + esc(q.it.s) + '</div>' + sel(q, g.pics.map(function(x, i){ return [i, L(i)]; }), 'Choose') + '</div>'; });
  }
  if(T.checked){
    var bad = g.q.filter(function(q){ return !q.ok; });
    if(t === 'multi' && bad.length === 0) bad = [];
    if(bad.length){
      h += '<div class="rd-fb"><b>Review</b>';
      var done = {};
      bad.forEach(function(q){
        if(t === 'multi'){ if(done.m) return; done.m = 1; h += '<div class="rd-fbi"><b>' + g.s + ' and ' + (g.s + 1) + '</b> Correct: ' + esc(fixText(q)) + (mine(q) ? '. You chose: ' + esc(mine(q)) : '. No answer') + g.e.map(function(e, i){ return '<div class="rd-where">Evidence: paragraph ' + e[0] + ' <button class="rd-go" data-go="' + (g.s + i) + '">Show in passage</button></div>'; }).join('') + '</div>'; return; }
        var e = q.e, why = t === 'tfng' && q.it.w ? '<div class="rd-why">' + esc(q.it.w) + '</div>' : '';
        h += '<div class="rd-fbi"><b>' + q.n + '</b> Correct: <b>' + esc(fixText(q)) + '</b>' + (mine(q) ? '. You wrote: ' + esc(mine(q)) : '. No answer') + why + '<div class="rd-where">' + (t === 'tfng' && q.it.a === 'NG' ? 'Closest text' : 'Evidence') + ': paragraph ' + e[0] + ', &ldquo;' + esc(e[1]) + '&rdquo; <button class="rd-go" data-go="' + q.n + '">Show in passage</button></div></div>';
      });
      h += '</div>';
    }
  }
  return h + '</div>';
}
function paraHtml(pt){
  var marks = {};
  pt.groups.forEach(function(g){ g.q.forEach(function(q){ if(!T.checked) return; if(q.ok && !T.showAll) return; (marks[q.e[0]] = marks[q.e[0]] || []).push(q); }); });
  return pt.p.paras.map(function(para){
    var rs = [];
    (marks[para.l] || []).forEach(function(q){ var i = para.t.indexOf(q.e[1]); if(i < 0) return; var f = rs.filter(function(r){ return r[0] === i && r[1] === i + q.e[1].length; })[0]; if(f) f[2].push(q); else rs.push([i, i + q.e[1].length, [q]]); });
    rs.sort(function(a, b){ return a[0] - b[0]; });
    var out = '', pos = 0;
    rs.forEach(function(r){ if(r[0] < pos) return; out += esc(para.t.slice(pos, r[0])) + '<mark class="rd-ev' + (r[2].every(function(q){ return q.ok; }) ? ' good' : '') + '" id="ev-' + r[2][0].n + '">' + esc(para.t.slice(r[0], r[1])) + '<sup>' + r[2].map(function(q){ return q.n; }).join(',') + '</sup></mark>'; pos = r[1]; });
    out += esc(para.t.slice(pos));
    return '<p class="rd-p"><b class="rd-l">' + para.l + '</b>' + out + '</p>';
  }).join('');
}
function fmt(s){ var m = Math.floor(s / 60), r = s % 60; return (m < 10 ? '0' : '') + m + ':' + (r < 10 ? '0' : '') + r; }
function tick(){
  if(!T || T.checked || !T.endAt){ stopTimer(); return; }
  var left = Math.max(0, Math.round((T.endAt - Date.now()) / 1000)), el = document.getElementById('rdTime');
  if(el){ el.textContent = fmt(left); el.parentNode.classList.toggle('low', left <= 300); }
  if(left <= 0){ check(true); }
}
function answered(pt){ var n = 0, tot = 0; pt.groups.forEach(function(g){ g.q.forEach(function(q){ tot++; var a = T.ans[q.n]; if(g.t === 'multi'){ var s = T.ans['m' + g.s] || []; if(s.length > (q.n - g.s)) n++; } else if(a !== undefined && a !== '') n++; }); }); return [n, tot]; }
function draw(){
  document.body.classList.add('rd-on');
  var pt = T.parts[T.cur], full = T.mode === 'full', left = T.endAt ? Math.max(0, Math.round((T.endAt - Date.now()) / 1000)) : 0;
  var h = '<div class="rd-bar' + (T.endAt && left <= 300 && !T.checked ? ' low' : '') + '"><div class="rd-bt"><b>' + (full ? 'Full test' : (T.drill ? T.drill.name : 'One passage')) + '</b><span class="rd-tm">' + (T.checked ? 'Finished' : (T.endAt ? '<span id="rdTime">' + fmt(left) + '</span>' : 'Untimed')) + '</span>' +
    (T.checked ? '<button class="rd-fin" id="rdHub">Menu</button>' : '<button class="rd-fin" id="rdFin">Finish</button><button class="rd-fin q" id="rdQuit">Quit</button>') + '</div>';
  if(full) h += '<div class="rd-tabs">' + T.parts.map(function(p, i){ var a = answered(p); return '<button class="rd-tab-b' + (i === T.cur ? ' on' : '') + '" data-part="' + i + '">Passage ' + (i + 1) + '<small>' + (T.checked ? T.res.per[i][0] + '/' + T.res.per[i][1] : a[0] + '/' + a[1]) + '</small></button>'; }).join('') + '</div>';
  h += '<div class="rd-pane"><button class="rd-tab-b' + (T.pane === 'p' ? ' on' : '') + '" data-pane="p">Text</button><button class="rd-tab-b' + (T.pane === 'q' ? ' on' : '') + '" data-pane="q">Questions</button></div></div>';
  h += '<div class="rd-main pane-' + T.pane + '"><section class="rd-text"><h3>' + esc(pt.p.title) + '</h3><div class="rd-intro">' + esc(pt.p.intro) + '</div>' + paraHtml(pt) + '</section><section class="rd-qs">';
  if(T.checked){
    var r = T.res, pct = Math.round(r.c / T.total * 100);
    h += '<div class="rd-res"><div class="rd-big">' + r.c + ' / ' + T.total + '</div><div>' + pct + '%' + (T.mode === 'full' ? ' &middot; estimated band ' + band(r.c).toFixed(1) : '') + (r.auto ? ' &middot; time ran out' : '') + '</div>' +
      (full ? '<div class="rd-sub">' + r.per.map(function(x, i){ return 'Passage ' + (i + 1) + ': ' + x[0] + '/' + x[1]; }).join(' &middot; ') + '</div>' : '') +
      '<div class="rd-sub">' + Object.keys(r.ty).map(function(k){ var nm = TYPES.filter(function(x){ return x[0] === k; })[0]; return (nm ? nm[1] : k) + ' ' + r.ty[k][0] + '/' + r.ty[k][1]; }).join(' &middot; ') + '</div>' +
      '<label class="rd-chk"><input type="checkbox" id="rdAll"' + (T.showAll ? ' checked' : '') + '> Highlight the evidence for every answer, not only the wrong ones</label></div>';
  }
  h += pt.groups.map(groupHtml).join('');
  if(!T.checked) h += '<div class="v-row"><button class="v-btn" id="rdCheck">Finish and check</button></div>';
  else h += '<div class="v-row"><button class="v-btn" id="rdAgain">' + (full ? 'New full test' : 'New passage') + '</button><button class="v-btn alt" id="rdHub2">Menu</button></div>';
  h += '</section></div>';
  var y = window.scrollY, rq = document.querySelector('.rd-qs'), qs = rq ? rq.scrollTop : 0, rt = document.querySelector('.rd-text'), ts = rt ? rt.scrollTop : 0;
  app.innerHTML = h;
  rq = document.querySelector('.rd-qs'); if(rq) rq.scrollTop = qs; rt = document.querySelector('.rd-text'); if(rt) rt.scrollTop = ts; window.scrollTo(0, y);
  wire();
}
function wire(){
  app.querySelectorAll('.rd-in').forEach(function(i){ i.oninput = function(){ T.ans[+i.getAttribute('data-n')] = i.value; var a = i.closest('.rd-main') ? 0 : 0; }; });
  app.querySelectorAll('.rd-sel').forEach(function(s){ s.onchange = function(){ T.ans[+s.getAttribute('data-n')] = s.value; }; });
  app.querySelectorAll('.rd-opt[data-n]').forEach(function(b){ b.onclick = function(){
    var n = +b.getAttribute('data-n'), v = b.getAttribute('data-v'), gq = b.parentNode.querySelectorAll('.rd-opt[data-n="' + n + '"]');
    T.ans[n] = /^\d+$/.test(v) ? +v : v; gq.forEach(function(x){ x.classList.remove('on'); }); b.classList.add('on'); }; });
  app.querySelectorAll('.rd-opt[data-m]').forEach(function(b){ b.onclick = function(){
    var s = +b.getAttribute('data-m'), v = +b.getAttribute('data-v'), a = T.ans['m' + s] || [], i = a.indexOf(v);
    if(i >= 0) a.splice(i, 1); else { if(a.length >= 2) a.shift(); a.push(v); }
    T.ans['m' + s] = a; b.parentNode.querySelectorAll('.rd-opt[data-m]').forEach(function(x){ x.classList.toggle('on', a.indexOf(+x.getAttribute('data-v')) >= 0); }); }; });
  app.querySelectorAll('[data-part]').forEach(function(b){ b.onclick = function(){ T.cur = +b.getAttribute('data-part'); draw(); window.scrollTo(0, 0); }; });
  app.querySelectorAll('[data-pane]').forEach(function(b){ b.onclick = function(){ T.pane = b.getAttribute('data-pane'); var m = document.querySelector('.rd-main'); m.className = 'rd-main pane-' + T.pane; app.querySelectorAll('[data-pane]').forEach(function(x){ x.classList.toggle('on', x === b); }); }; });
  app.querySelectorAll('[data-go]').forEach(function(b){ b.onclick = function(){
    var n = b.getAttribute('data-go'), q = null; T.parts.forEach(function(pt, pi){ pt.groups.forEach(function(g){ g.q.forEach(function(x){ if(x.n === +n) { q = x; T.cur = pi; } }); }); });
    T.pane = 'p'; draw();
    var el = document.getElementById('ev-' + n) || document.querySelector('.rd-ev'); if(!el) return;
    var box = document.querySelector('.rd-text'); if(box && box.scrollHeight > box.clientHeight + 2 && getComputedStyle(box).overflowY !== 'visible') box.scrollTop = Math.max(0, el.offsetTop - box.offsetTop - 80); else el.scrollIntoView({ block: 'center' });
    el.classList.add('flash'); }; });
  var f = function(id, fn){ var e = document.getElementById(id); if(e) e.onclick = fn; };
  f('rdCheck', function(){ var a = T.parts.reduce(function(n, p){ var x = answered(p); return n + (x[1] - x[0]); }, 0); if(a && !confirm(a + ' question' + (a > 1 ? 's' : '') + ' unanswered. Finish and check?')) return; check(false); });
  f('rdFin', function(){ var a = T.parts.reduce(function(n, p){ var x = answered(p); return n + (x[1] - x[0]); }, 0); if(a && !confirm(a + ' question' + (a > 1 ? 's' : '') + ' unanswered. Finish and check?')) return; check(false); });
  f('rdQuit', function(){ if(confirm('Quit this test? Your answers will be lost.')) toHub(); });
  f('rdHub', toHub); f('rdHub2', toHub);
  f('rdAgain', function(){ var m = T.mode, d = T.drill, lv = T.lv; if(m === 'full') start('full'); else if(m === 'drill') start('drill', d); else start('single', { lv: 0 }); });
  var al = document.getElementById('rdAll'); if(al) al.onchange = function(){ T.showAll = al.checked; draw(); };
}
function toHub(){ stopTimer(); T = null; document.body.classList.remove('rd-on'); location.hash = ''; hub(); }
function hub(){
  stopTimer(); document.body.classList.remove('rd-on'); var st = stats();
  app.innerHTML = BACK + head('Reading Practice', 'Academic-style passages and every common question type. Each sitting draws a fresh mix of questions, and you get the answer and the evidence in the text for everything you miss.') +
    '<div class="ls-set"><label><input type="checkbox" id="rdTimed"' + (S.timed ? ' checked' : '') + '> Timer (20 minutes a passage, 60 for a full test)</label></div>' +
    '<a class="ls-item" href="#full"><b>Full test</b><small>Three passages, 40 questions, 60 minutes.' + (st.full.n ? ' Done: ' + st.full.n + ', best ' + st.full.best + '/40.' : '') + '</small></a>' +
    '<div class="rd-lv">' + [['Any level', 0], ['Easier', 1], ['Medium', 2], ['Harder', 3]].map(function(x){ return '<a class="ls-item" href="#one' + x[1] + '"><b>One passage</b><small>' + x[0] + ', about 13 questions, 20 minutes</small></a>'; }).join('') + '</div>' +
    '<div class="rd-h3">Practise one question type</div><div id="rdTypes"><div class="v-hint">Loading...</div></div>' +
    '<div class="v-hint" style="margin-top:8px;">Passages are written for practice. Names of researchers and figures in them are invented.' + (navigator.onLine ? ' Needs an internet connection.' : ' You are offline. Reading needs a connection.') + '</div>';
  document.getElementById('rdTimed').onchange = function(){ S.timed = this.checked; lsSet('readSet', S); };
  loadIndex().then(function(idx){
    var box = document.getElementById('rdTypes'); if(!box) return;
    box.innerHTML = TYPES.filter(function(t){ return idx.some(function(p){ return p.types.some(function(x){ return t[2].indexOf(x) >= 0; }); }); }).map(function(t){ var o = st.ty[t[0]]; return '<a class="ls-item" href="#type-' + t[0] + '"><b>' + t[1] + '</b><small>' + (o && o.t ? 'Your accuracy: ' + Math.round(o.c / o.t * 100) + '% (' + o.c + '/' + o.t + ')' : 'Not tried yet') + '</small></a>'; }).join('');
  }).catch(function(){ var box = document.getElementById('rdTypes'); if(box) box.innerHTML = '<div class="v-hint">Could not load passages. Check your connection.</div>'; });
}
function route(){
  var h = location.hash, m;
  if(h === '#full') start('full');
  else if((m = /^#one(\d)$/.exec(h))) start('single', { lv: +m[1] });
  else if((m = /^#type-(\w+)$/.exec(h))){ var t = TYPES.filter(function(x){ return x[0] === m[1]; })[0]; if(t) start('drill', { want: t[2], name: t[1] }); else hub(); }
  else hub();
}
window.addEventListener('hashchange', route);
route();
window.RD_TEST = { loadIndex: loadIndex, loadP: loadP, choose: choose, slots: slots, T: function(){ return T; }, check: check };
