var BACK = back('index.html#geography-hub/study', 'Back to Train Your Brain');
var FAM = [], ITEMS = [], ROUND = 15;
var PN = { n: 'noun', v: 'verb', adj: 'adjective', adv: 'adverb' };
function famHtml(f){ return '<div class="wf-fam"><b>' + esc(f.b) + '</b><br>' + ['n', 'v', 'adj', 'adv'].filter(function(p){ return f.f[p]; }).map(function(p){ return '<span><em>' + PN[p] + '</em> ' + esc(f.f[p]) + '</span>'; }).join('') + '</div>'; }
function hub(){
  app.innerHTML = BACK + head('Word Forms', 'Change the word in capitals into the form the sentence needs. A key skill for IELTS and TOEFL writing.') +
    '<div class="sport-hub-grid"><a class="sport-hub-tile" href="#choose"><span class="name" style="flex-direction:column;gap:2px;"><span>Choose the form</span><span style="font-size:12px;color:var(--ink-soft);font-weight:700;">multiple choice</span></span></a>' +
    '<a class="sport-hub-tile" href="#type"><span class="name" style="flex-direction:column;gap:2px;"><span>Type the form</span><span style="font-size:12px;color:var(--ink-soft);font-weight:700;">harder</span></span></a>' +
    '<a class="sport-hub-tile" href="#families" style="grid-column:1 / -1;"><span class="name">Word family list</span></a></div>' +
    '<div class="v-hint" style="margin-top:12px;">' + FAM.length + ' word families, ' + ITEMS.length + ' sentences.</div>';
}
function options(it){
  var f = it.fam.f, ans = f[it.p], opts = ['n', 'v', 'adj', 'adv'].filter(function(p){ return f[p]; }).map(function(p){ return f[p]; });
  opts = opts.filter(function(x, i){ return opts.indexOf(x) === i; });
  var pool = shuffle(FAM).filter(function(x){ return x !== it.fam; });
  for(var i = 0; i < pool.length && opts.length < 4; i++){
    var o = pool[i].f[it.p === 'n' ? 'adj' : 'n'] || pool[i].f.n; if(o && opts.indexOf(o) < 0 && o !== ans) opts.push(o);
  }
  return shuffle(opts);
}
function practice(kind){
  var qs = shuffle(ITEMS).slice(0, ROUND), i = 0, score = 0, busy = false, bestKey = 'wordformsBest_' + kind;
  function sentence(it){ return esc(it.s).replace('___', '<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>'); }
  function q(){
    if(i >= qs.length) return end();
    busy = false;
    var it = qs[i], h = BACK.replace('Back to Train Your Brain', 'Quit round').replace(/href="[^"]*"/, 'href="#"') + '<div class="v-meta"><span>Question ' + (i + 1) + ' / ' + qs.length + '</span><span>Score ' + score + '</span></div><div class="v-bar"><i style="width:' + (i / qs.length * 100) + '%"></i></div>' +
      '<div class="v-card random-tile" style="text-align:left;"><span class="wf-base">' + esc(it.fam.b.toUpperCase()) + '</span><div class="wf-sent">' + esc(it.s).replace('___', '<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>') + '</div><div class="wf-pos">Needed: ' + PN[it.p] + '</div></div>';
    if(kind === 'choose'){
      var opts = options(it);
      h += '<div class="v-opts">' + opts.map(function(o, n){ return '<button class="v-opt sport-hub-tile" data-n="' + n + '">' + esc(o) + '</button>'; }).join('') + '</div><div id="vFb"></div>';
      app.innerHTML = h;
      var btns = app.querySelectorAll('.v-opt');
      btns.forEach(function(b){ b.onclick = function(){
        if(busy) return; busy = true; var pick = opts[+b.getAttribute('data-n')], ok = pick === it.fam.f[it.p];
        btns.forEach(function(x, n){ if(opts[n] === it.fam.f[it.p]) x.classList.add('ok'); }); if(ok){ score++; award(1, 'wf'); } else { b.classList.add('bad'); amend(it); }
        done(it);
      }; });
    } else {
      h += '<input class="wf-in" id="wfIn" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" placeholder="Type the form"><button class="v-btn" id="wfGo">Check</button><div id="vFb"></div>';
      app.innerHTML = h;
      var inp = document.getElementById('wfIn'); inp.focus();
      var check = function(){
        if(busy) return; var v = inp.value.trim().toLowerCase(); if(!v) return; busy = true;
        var ok = v === it.fam.f[it.p].toLowerCase(); inp.classList.add(ok ? 'ok' : 'bad'); inp.readOnly = true;
        if(ok){ score++; award(2, 'wf'); } else { inp.value = v + '  →  ' + it.fam.f[it.p]; amend(it); }
        document.getElementById('wfGo').style.display = 'none'; done(it);
      };
      document.getElementById('wfGo').onclick = check; inp.onkeydown = function(e){ if(e.key === 'Enter') check(); };
    }
  }
  function amend(it){ var f = it.fam.f, L = { n: 'noun', v: 'verb', adj: 'adjective', adv: 'adverb' }; var rest = ['n', 'v', 'adj', 'adv'].filter(function(p){ return f[p] && p !== it.p && f[p] !== f[it.p]; }).map(function(p){ return L[p] + ' ' + f[p]; }).join(', '); if(window.LoungeAmend) LoungeAmend.add(f[it.p], L[it.p].charAt(0).toUpperCase() + L[it.p].slice(1) + ' form. Same family: ' + (rest || 'none'), 'Word Forms'); }
  function done(it){
    var fb = document.getElementById('vFb');
    fb.innerHTML = '<div class="v-ex" style="text-align:center;margin:8px 0 0;">“' + esc(it.s).replace('___', '<b>' + esc(it.fam.f[it.p]) + '</b>') + '”</div>' + famHtml(it.fam);
    var nb = document.createElement('button'); nb.className = 'v-btn'; nb.textContent = i + 1 >= qs.length ? 'See results' : 'Next'; fb.appendChild(nb);
    nb.onclick = function(){ i++; window.scrollTo(0, 0); q(); }; nb.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  }
  function end(){
    var best = lsGet(bestKey, 0), pct = Math.round(score / qs.length * 100), isBest = pct > best; if(isBest) lsSet(bestKey, pct); award(10, 'round');
    app.innerHTML = BACK.replace('Back to Train Your Brain', 'Back').replace(/href="[^"]*"/, 'href="#"') + '<div class="v-card random-tile"><div class="v-big">' + score + ' / ' + qs.length + '</div><div class="v-def" style="margin-top:6px;">' + pct + '%' + (isBest ? ' • new best' : ' • best ' + best + '%') + '</div></div><button class="v-btn" id="again" style="margin-top:12px;">Another round</button>';
    document.getElementById('again').onclick = function(){ practice(kind); };
  }
  window.scrollTo(0, 0); q();
}
function families(){
  app.innerHTML = BACK.replace('Back to Train Your Brain', 'Back').replace(/href="[^"]*"/, 'href="#"') + head('Word family list') + '<input class="cl-search" id="fq" placeholder="Search a word..." autocomplete="off" style="width:100%;padding:12px 14px;border-radius:14px;border:none;background:var(--card);color:var(--ink);font:700 16px Nunito,sans-serif;margin-bottom:10px;"><div id="fl"></div>';
  var draw = function(){ var q = document.getElementById('fq').value.trim().toLowerCase(); var l = FAM.filter(function(f){ return !q || Object.keys(f.f).some(function(p){ return f.f[p].toLowerCase().indexOf(q) >= 0; }); }).sort(function(a, b){ return a.b.localeCompare(b.b); }); document.getElementById('fl').innerHTML = l.map(famHtml).join('') || '<div class="empty-card">Nothing found.</div>'; };
  document.getElementById('fq').oninput = draw; draw();
}
function route(){ var h = (location.hash || '#').slice(1); if(h === 'choose' || h === 'type') practice(h); else if(h === 'families') families(); else hub(); }
window.addEventListener('hashchange', route);
getJson('data/games/wordforms.json').then(function(d){
  FAM = d; d.forEach(function(f){ f.i.forEach(function(x){ ITEMS.push({ fam: f, p: x[0], s: x[1] }); }); }); route();
}).catch(function(){ app.innerHTML = BACK + '<div class="empty-card">Could not load the data. Check your connection.</div>'; });
