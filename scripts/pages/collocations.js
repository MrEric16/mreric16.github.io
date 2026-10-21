var BACK = back('index.html#geography-hub/study', 'Back to Train Your Brain');
var POS = { phr: 'Phrasal verbs', col: 'Collocations', idm: 'Idioms' };
var ROUND = 20, ALL = [], BYK = {};
var ui = lsGet('collUI', { cat: 'phr' });
function saved(){ return lsGet('vocabSaved', []); }
function setSaved(k, on){ var s = saved().filter(function(x){ return x !== k; }); if(on) s.unshift(k); lsSet('vocabSaved', s); }
function pool(needGap){
  return ALL.filter(function(w){ return (ui.cat === 'all' || w.pos === ui.cat) && (!needGap || w.gap); });
}
function hub(){
  var n = pool(false).length, g = pool(true).length;
  app.innerHTML = BACK + head('Collocations and Phrasal Verbs', 'Choose a type, then a way to practise.') +
    '<div class="cl-tabs">' + [['phr', 'Phrasal verbs'], ['col', 'Collocations'], ['idm', 'Idioms'], ['all', 'All']].map(function(t){ return '<button data-c="' + t[0] + '" class="' + (ui.cat === t[0] ? 'on' : '') + '">' + t[1] + '</button>'; }).join('') + '</div>' +
    '<div class="sport-hub-grid">' +
    '<a class="sport-hub-tile" href="#gap"><span class="name" style="flex-direction:column;gap:2px;"><span>Complete the sentence</span><span style="font-size:12px;color:var(--ink-soft);font-weight:700;">fill the gap</span></span></a>' +
    '<a class="sport-hub-tile" href="#m2p"><span class="name" style="flex-direction:column;gap:2px;"><span>Meaning to phrase</span><span style="font-size:12px;color:var(--ink-soft);font-weight:700;">find the expression</span></span></a>' +
    '<a class="sport-hub-tile" href="#p2m"><span class="name" style="flex-direction:column;gap:2px;"><span>Phrase to meaning</span><span style="font-size:12px;color:var(--ink-soft);font-weight:700;">what does it mean?</span></span></a>' +
    '<a class="sport-hub-tile" href="#browse"><span class="name" style="flex-direction:column;gap:2px;"><span>Browse and search</span><span style="font-size:12px;color:var(--ink-soft);font-weight:700;">study the list</span></span></a>' +
    '</div><div class="v-hint" style="margin-top:12px;">Wrong answers are saved automatically to your Saved words in IELTS Vocabulary.</div>';
  app.querySelectorAll('[data-c]').forEach(function(b){ b.onclick = function(){ ui.cat = b.getAttribute('data-c'); lsSet('collUI', ui); hub(); }; });
}
var STOPW = 'a an the to of in on at or and is are be was it its that this who which with for from by as not very more most than into up out do does doing your you one someone something their they them his her we our just can may so such have has had been being when what while about over also but if'.split(' ');
function toks(t){
  var o = {}; (t.toLowerCase().match(/[a-z]+/g) || []).forEach(function(x){ if(x.length > 2 && STOPW.indexOf(x) < 0) o[x.replace(/(ing|ed|es|s|ly)$/, '')] = 1; });
  return o;
}
// Two items clash when their meanings share content words, or they share the noun or the rest of the phrase,
// so a wrong option can never also be a correct answer.
function clash(a, b){
  var wa = a.w.toLowerCase().split(' '), wb = b.w.toLowerCase().split(' ');
  if(wa[wa.length - 1] === wb[wb.length - 1] && wa.length > 1 && wb.length > 1) return true;
  if(wa.length > 1 && wa.slice(1).join(' ') === wb.slice(1).join(' ')) return true;
  var ta = a._t || (a._t = toks(a.d)), tb = b._t || (b._t = toks(b.d)), n = 0, u = 0, k;
  for(k in ta){ u++; if(tb[k]) n++; }
  for(k in tb){ if(!ta[k]) u++; }
  return n >= 2 || (n >= 1 && n / u >= 0.2);
}
function distract(w, n, byDef){
  var c = shuffle(ALL.filter(function(x){ return x.pos === w.pos && x.k !== w.k; })), out = [], used = {};
  for(var i = 0; i < c.length && out.length < n; i++){
    var x = c[i], f = x.w.split(' ')[0];
    if(f === w.w.split(' ')[0] || used[f]) continue;
    if(byDef && x.d.toLowerCase().indexOf(w.w.split(' ')[0].toLowerCase()) >= 0) continue;
    if(clash(w, x)) continue;
    used[f] = 1; out.push(x);
  }
  return out;
}
function practice(kind){
  var p = pool(kind === 'gap');
  if(p.length < 8){ app.innerHTML = BACK + '<div class="empty-card">Not enough items in this selection.</div>'; return; }
  var qs = shuffle(p).slice(0, ROUND), i = 0, score = 0, miss = [], busy = false;
  var bestKey = 'collocBest_' + kind;
  function q(){
    if(i >= qs.length) return end();
    busy = false;
    var w = qs[i], opts = shuffle([w].concat(distract(w, 3, kind === 'm2p' || kind === 'gap'))), prompt;
    if(kind === 'gap') prompt = '<div class="cl-gap">' + esc(w.e).replace(new RegExp(w.w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i'), '<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>') + '</div><div class="cl-hint">Meaning: ' + esc(w.d) + '</div>';
    else if(kind === 'm2p') prompt = '<div class="v-def" style="margin-top:0;">' + esc(w.d) + '</div>';
    else prompt = '<div class="v-word">' + esc(w.w) + '</div>';
    app.innerHTML = BACK.replace('Back to Train Your Brain', 'Quit round').replace(/href="[^"]*"/, 'href="#"') + '<div class="v-meta"><span>Question ' + (i + 1) + ' / ' + qs.length + '</span><span>Score ' + score + '</span></div><div class="v-bar"><i style="width:' + (i / qs.length * 100) + '%"></i></div>' +
      '<div class="v-card random-tile">' + prompt + '</div><div class="v-opts">' +
      opts.map(function(o, n){ return '<button class="v-opt sport-hub-tile" data-n="' + n + '">' + esc(kind === 'p2m' ? o.d : o.w) + '</button>'; }).join('') + '</div><div id="vFb"></div>';
    var btns = app.querySelectorAll('.v-opt');
    btns.forEach(function(b){ b.onclick = function(){
      if(busy) return; busy = true;
      var ok = opts[+b.getAttribute('data-n')] === w;
      btns.forEach(function(x, n){ if(opts[n] === w) x.classList.add('ok'); });
      if(ok){ score++; award(1, 'coll'); } else { b.classList.add('bad'); miss.push(w); if(window.LoungeAmend) LoungeAmend.add(w.w, w.d, 'Collocations'); }
      var fb = document.getElementById('vFb');
      fb.innerHTML = '<div class="v-ex" style="text-align:center;margin:4px 0 0;"><b>' + esc(w.w) + '</b>: ' + esc(w.d) + '<br>“' + esc(w.e) + '”</div>';
      var nb = document.createElement('button'); nb.className = 'v-btn'; nb.textContent = i + 1 >= qs.length ? 'See results' : 'Next'; fb.appendChild(nb);
      nb.onclick = function(){ i++; window.scrollTo(0, 0); q(); }; nb.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    }; });
  }
  function end(){
    var best = lsGet(bestKey, 0), pct = Math.round(score / qs.length * 100), isBest = pct > best;
    if(isBest) lsSet(bestKey, pct);
    award(10, 'round');
    app.innerHTML = BACK.replace('Back to Train Your Brain', 'Back').replace(/href="[^"]*"/, 'href="#"') + '<div class="v-card random-tile"><div class="v-big">' + score + ' / ' + qs.length + '</div><div class="v-def" style="margin-top:6px;">' + pct + '%' + (isBest ? ' • new best' : ' • best ' + best + '%') + '</div></div>' +
      (miss.length ? '<div class="v-hint">Missed expressions are saved automatically.</div>' + miss.map(function(w){ return '<div class="v-miss"><b>' + esc(w.w) + '</b><div>' + esc(w.d) + '</div></div>'; }).join('') : '') +
      '<button class="v-btn" id="again" style="margin-top:12px;">Another round</button>';
    document.getElementById('again').onclick = function(){ practice(kind); };
  }
  window.scrollTo(0, 0); q();
}
function browse(){
  var p = pool(false).slice().sort(function(a, b){ return a.w.localeCompare(b.w); });
  app.innerHTML = BACK.replace('Back to Train Your Brain', 'Back').replace(/href="[^"]*"/, 'href="#"') + head('Browse', POS[ui.cat] || 'All expressions') +
    '<input class="cl-search" id="clQ" placeholder="Search..." autocomplete="off"><div id="clList"></div>';
  var draw = function(){
    var q = document.getElementById('clQ').value.trim().toLowerCase();
    var f = q ? p.filter(function(w){ return w.k.indexOf(q) >= 0 || w.d.toLowerCase().indexOf(q) >= 0; }) : p;
    document.getElementById('clList').innerHTML = f.slice(0, 120).map(function(w){
      var on = saved().indexOf(w.k) >= 0;
      return '<div class="cl-item"><b>' + esc(w.w) + '</b> <button class="v-save' + (on ? ' on' : '') + '" data-save="' + esc(w.k) + '">' + (on ? '★ Saved' : '☆ Save') + '</button><div>' + esc(w.d) + '</div><i>“' + esc(w.e) + '”</i></div>';
    }).join('') + (f.length > 120 ? '<div class="v-hint">Showing 120 of ' + f.length + '. Search to narrow down.</div>' : '') + (f.length ? '' : '<div class="empty-card">Nothing found.</div>');
    document.querySelectorAll('[data-save]').forEach(function(b){ b.onclick = function(){ var k = b.getAttribute('data-save'), on = saved().indexOf(k) < 0; setSaved(k, on); b.classList.toggle('on', on); b.textContent = on ? '★ Saved' : '☆ Save'; }; });
  };
  document.getElementById('clQ').oninput = draw; draw();
}
function route(){
  var h = (location.hash || '#').slice(1);
  if(h === 'gap' || h === 'm2p' || h === 'p2m') practice(h); else if(h === 'browse') browse(); else hub();
}
window.addEventListener('hashchange', route);
fetch('data/vocab/words.json', { cache: 'no-cache' }).then(function(r){ return r.json(); }).then(function(d){
  ALL = d.w.filter(function(r){ return r[1] === 'phr' || r[1] === 'col' || r[1] === 'idm'; }).map(function(r){
    return { w: r[0], pos: r[1], d: r[4], e: r[5], k: r[0].toLowerCase(), gap: r[5].toLowerCase().indexOf(r[0].toLowerCase()) >= 0 };
  });
  route();
}).catch(function(){ app.innerHTML = BACK + '<div class="empty-card">Could not load the data. Check your connection.</div>'; });
