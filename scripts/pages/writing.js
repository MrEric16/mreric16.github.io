var BACK = back('index.html#geography-hub/study', 'Back to Train Your Brain');
var TASKS = { t2: { n: 'Task 2 essay', min: 250 }, t1a: { n: 'Task 1 Academic', min: 150 }, t1g: { n: 'Task 1 General (letter)', min: 150 } };
var st = lsGet('writingUI', { task: 't2' });
var STOP = 'the a an and or but if of to in on at for with by from as is are was were be been being am it its this that these those i you he she we they my your his her our their me him us them not no do does did have has had will would can could should may might must than then so such very more most also just only into about over under again there here what which who whom whose when where why how all any each other some one two'.split(' ');
var LINK = {
  'Addition': ['moreover','furthermore','in addition','besides','additionally','what is more','as well as'],
  'Contrast': ['however','although','though','whereas','while','nevertheless','on the other hand','despite','in spite of','yet','in contrast','by contrast'],
  'Cause and result': ['because','therefore','consequently','as a result','thus','hence','since','due to','owing to','leads to','so that'],
  'Example': ['for example','for instance','such as','namely','in particular','to illustrate'],
  'Sequence': ['firstly','first of all','secondly','thirdly','finally','lastly','to begin with','next','then','meanwhile'],
  'Concluding': ['in conclusion','to conclude','to sum up','in summary','overall','to summarise','all in all']
};
var WEAK = { good: 'beneficial, positive, favourable, effective', bad: 'harmful, negative, detrimental, poor', thing: 'factor, aspect, issue, element', things: 'factors, aspects, issues', people: 'individuals, citizens, the public, residents', important: 'significant, essential, crucial, vital', big: 'considerable, substantial, major, significant', many: 'numerous, a great number of, a wide range of', think: 'believe, argue, consider, maintain', show: 'demonstrate, illustrate, indicate, reveal', problem: 'issue, challenge, drawback, difficulty', get: 'obtain, receive, gain, become', help: 'assist, support, benefit, contribute to', use: 'utilise, employ, make use of', want: 'wish, aim, seek, desire', make: 'create, produce, cause, generate', lot: 'a great deal, a considerable number', kids: 'children, young people', big: 'significant, major' };
var US = { color: 'colour', colors: 'colours', favorite: 'favourite', behavior: 'behaviour', center: 'centre', centers: 'centres', organize: 'organise', organized: 'organised', organization: 'organisation', realize: 'realise', recognize: 'recognise', analyze: 'analyse', analyzed: 'analysed', labor: 'labour', neighbor: 'neighbour', program: 'programme', defense: 'defence', license: 'licence (noun)', traveling: 'travelling', traveled: 'travelled', theater: 'theatre', fiber: 'fibre', meter: 'metre', gray: 'grey', catalog: 'catalogue', dialog: 'dialogue', skeptical: 'sceptical', mom: 'mum', apartment: 'flat', soccer: 'football', vacation: 'holiday', gotten: 'got' };
var SUBORD = ['although','though','whereas','while','because','since','if','unless','which','who','whom','whose','that','when','whenever','where','whether','as long as','even if','so that','provided that'];
var BANDW = null;
function words(t){ return (t.match(/[A-Za-z]+(?:['’-][A-Za-z]+)*/g) || []); }
function sentences(t){ return t.replace(/\n+/g, ' ').replace(/([.!?]["\u201D)]?)\s+(?=["\u201C(]?[A-Z0-9])/g, '$1\u0001').split('\u0001').map(function(s){ return s.trim(); }).filter(function(s){ return words(s).length > 0; }); }
function count(hay, needle){ var re = new RegExp('(^|[^a-z])' + needle.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(?![a-z])', 'gi'); return (hay.match(re) || []).length; }
function ui(){
  var draft = lsGet('writingDraft', '');
  var h = BACK + head('IELTS Writing Checker', 'Paste or type your essay. You get counts and checks, not a band score. A teacher marks the band.');
  h += '<div class="wr-sel">' + Object.keys(TASKS).map(function(k){ return '<button data-t="' + k + '" class="' + (st.task === k ? 'on' : '') + '">' + TASKS[k].n + '</button>'; }).join('') + '</div>';
  h += '<textarea class="wr-ta" id="wrTa" placeholder="Write your answer here..." spellcheck="true" autocapitalize="sentences">' + esc(draft) + '</textarea>';
  h += '<div class="wr-count"><span id="wrWc">0 words</span><span id="wrTarget"></span></div>';
  h += '<div class="v-row"><button class="v-btn" id="wrGo">Check my writing</button><button class="v-btn alt" id="wrClear">Clear</button></div><div id="wrOut" style="margin-top:14px;"></div>';
  h += '<div class="wr-note">Your draft is saved on this device only and is never uploaded.</div>';
  app.innerHTML = h;
  var ta = document.getElementById('wrTa');
  var upd = function(){ var n = words(ta.value).length; document.getElementById('wrWc').textContent = n + ' word' + (n === 1 ? '' : 's'); var m = TASKS[st.task].min; document.getElementById('wrTarget').textContent = n >= m ? 'Target of ' + m + ' reached' : (m - n) + ' to reach ' + m; lsSet('writingDraft', ta.value); };
  ta.oninput = upd; upd();
  app.querySelectorAll('[data-t]').forEach(function(b){ b.onclick = function(){ st.task = b.getAttribute('data-t'); lsSet('writingUI', st); ui(); }; });
  document.getElementById('wrClear').onclick = function(){ if(!ta.value || confirm('Clear your draft?')){ ta.value = ''; upd(); document.getElementById('wrOut').innerHTML = ''; } };
  document.getElementById('wrGo').onclick = function(){ analyse(ta.value); };
}
function ensureBank(cb){
  if(BANDW) return cb();
  fetch('data/vocab/words.json').then(function(r){ return r.json(); }).then(function(d){
    BANDW = {}; d.w.forEach(function(w){ if((w[1] === 'n' || w[1] === 'v' || w[1] === 'adj' || w[1] === 'adv') && w[0].indexOf(' ') < 0) BANDW[w[0].toLowerCase()] = w[3] + 5; });
    cb();
  }).catch(function(){ BANDW = {}; cb(); });
}
function advanced(ws){
  var found = {};
  ws.forEach(function(w){
    var l = w.toLowerCase(), cands = [l, l.replace(/(ing|ed|es|s|ly)$/, ''), l.replace(/ies$/, 'y'), l.replace(/ied$/, 'y'), l.replace(/ing$/, 'e'), l.replace(/ed$/, 'e'), l.replace(/(.)\1ing$/, '$1'), l.replace(/(.)\1ed$/, '$1')];
    for(var i = 0; i < cands.length; i++){ if(BANDW[cands[i]]){ found[cands[i]] = BANDW[cands[i]]; break; } }
  });
  return Object.keys(found).sort();
}
function analyse(text){
  var out = document.getElementById('wrOut'), T = TASKS[st.task], ws = words(text), n = ws.length;
  if(n < 30){ out.innerHTML = '<div class="empty-card">Write at least 30 words first.</div>'; return; }
  ensureBank(function(){
    var low = text.toLowerCase(), sents = sentences(text), paras = text.split(/\n\s*\n/).map(function(p){ return p.trim(); }).filter(Boolean);
    var sl = sents.map(function(s){ return words(s).length; });
    var avg = sl.reduce(function(a, b){ return a + b; }, 0) / sl.length, longest = Math.max.apply(null, sl), shortest = Math.min.apply(null, sl);
    var uniq = new Set(ws.map(function(w){ return w.toLowerCase(); })).size;
    var prio = [], ok = [], cards = '';
    // length
    if(n < T.min) prio.push('Add about ' + (T.min - n) + ' more words. Under ' + T.min + ' words loses marks for Task Achievement.');
    else ok.push('Length is fine: ' + n + ' words (minimum ' + T.min + ').');
    if(st.task === 't2'){
      if(paras.length < 4) prio.push('Use 4 or 5 paragraphs: introduction, two body paragraphs, conclusion. You have ' + paras.length + '. Leave a blank line between paragraphs.');
      else ok.push(paras.length + ' paragraphs.');
      var last = (paras[paras.length - 1] || '').toLowerCase();
      var hasConc = LINK['Concluding'].some(function(c){ return last.indexOf(c) >= 0; });
      if(paras.length >= 2 && !hasConc) prio.push('The last paragraph has no clear concluding signal (In conclusion, To sum up, Overall).');
      else if(hasConc) ok.push('Clear conclusion.');
    } else if(paras.length < 2) prio.push('Task 1: separate an overview paragraph from the detail paragraphs.');
    // linking
    var used = {}, total = 0, over = [];
    Object.keys(LINK).forEach(function(cat){ LINK[cat].forEach(function(w){ var c = count(low, w); if(c){ (used[cat] = used[cat] || []).push(w + (c > 1 ? ' x' + c : '')); total += c; if(c >= 3) over.push(w + ' (' + c + ' times)'); } }); });
    var missingCats = Object.keys(LINK).filter(function(c){ return !used[c]; });
    if(over.length) prio.push('You overuse: ' + over.join(', ') + '. Vary your linkers.');
    if(total < 4) prio.push('Very few linking words (' + total + '). Aim for variety, not quantity: about 1 per 40 words.');
    else if(total > n / 15) prio.push('Too many linking words (' + total + '). The essay can sound mechanical.');
    // repetition
    var freq = {}; ws.forEach(function(w){ var l = w.toLowerCase(); if(l.length > 3 && STOP.indexOf(l) < 0) freq[l] = (freq[l] || 0) + 1; });
    var rep = Object.keys(freq).filter(function(k){ return freq[k] >= (n >= 200 ? 5 : 4); }).sort(function(a, b){ return freq[b] - freq[a]; }).slice(0, 8);
    // weak and informal
    var flags = [];
    var contr = (text.match(/\b\w+(n't|'re|'ve|'ll|'m|'d)\b/gi) || []).length + (text.match(/\b\w+(n’t|’re|’ve|’ll|’m|’d)\b/gi) || []).length;
    if(contr) flags.push('Contractions (' + contr + '). Write them in full in formal writing: do not, it is.');
    ['a lot of','lots of','kids','stuff','really','etc','and so on','nowadays'].forEach(function(w){ var c = count(low, w); if(c) flags.push('"' + w + '" (' + c + ') is informal or vague' + (w === 'nowadays' ? ' and overused in essays' : '') + '.'); });
    var very = count(low, 'very'); if(very >= 3) flags.push('"very" appears ' + very + ' times. Use a stronger adjective (very important becomes crucial).');
    if(/!/.test(text)) flags.push('Exclamation marks do not belong in formal writing.');
    if(/\?/.test(text)) flags.push('Direct questions are risky in an essay. Turn them into statements.');
    var starters = {}; sents.forEach(function(s){ var f = (words(s)[0] || '').toLowerCase(); starters[f] = (starters[f] || 0) + 1; });
    Object.keys(starters).forEach(function(k){ if(starters[k] >= 4 && k !== 'the') flags.push('Four or more sentences start with "' + k + '".'); if(starters[k] >= 5 && k === 'the') flags.push('Five or more sentences start with "The".'); });
    if(/(^|[.!?]\s+)(and|but|so)\s/i.test(text)) flags.push('A sentence starts with And, But or So. Use Moreover, However, Therefore in formal writing.');
    var iThink = count(low, 'i think') + count(low, 'i believe') + count(low, 'in my opinion') + count(low, 'i feel');
    if(iThink >= 3) flags.push('Opinion phrases (I think, I believe, in my opinion) appear ' + iThink + ' times. State your position once clearly, then argue.');
    var usf = []; ws.forEach(function(w){ var l = w.toLowerCase(); if(US[l] && usf.indexOf(l) < 0) usf.push(l); });
    if(usf.length) flags.push('Spelling: ' + usf.map(function(w){ return w + ' becomes ' + US[w]; }).join(', ') + '. Be consistent: British spelling in this course.');
    if(flags.length) prio.push(flags.length + ' style issue' + (flags.length === 1 ? '' : 's') + ' below.');
    // sentence structure
    var complex = sents.filter(function(s){ var l = s.toLowerCase(); return SUBORD.some(function(w){ return count(l, w) > 0; }); }).length;
    var pct = Math.round(complex / sents.length * 100);
    if(avg < 12) prio.push('Sentences are short (average ' + avg.toFixed(1) + ' words). Combine ideas with although, which, because.');
    if(avg > 28) prio.push('Sentences are very long (average ' + avg.toFixed(1) + '). Split some to keep control of grammar.');
    if(longest > 45) flags.push('One sentence has ' + longest + ' words. Check it is clear.');
    if(pct < 35) prio.push('Only ' + pct + '% of sentences are complex. Aim for a mix: about half should contain a subordinate clause.');
    else ok.push(pct + '% complex sentences. Good mix.');
    var passive = (text.match(/\b(am|is|are|was|were|be|been|being)\s+(\w+ed|\w+en|built|made|done|taken|given|seen|known|shown|found|held|kept|set|put|told|sold|paid|brought|thought)\b/gi) || []).length;
    // vocabulary
    var adv = advanced(ws).filter(function(w){ return BANDW[w] >= 7; });
    var ttr = uniq / n;
    if(ttr < 0.45 && n > 150) prio.push('Vocabulary range is narrow (' + Math.round(ttr * 100) + '% of words are different). Replace repeated words.');
    // render
    cards += '<div class="wr-card"><h3>Counts</h3><div class="wr-stats">' +
      [[n, 'words'], [sents.length, 'sentences'], [paras.length, 'paragraphs'], [avg.toFixed(1), 'words per sentence'], [pct + '%', 'complex sentences'], [Math.round(ttr * 100) + '%', 'different words']].map(function(x){ return '<div class="wr-stat"><b>' + x[0] + '</b><span>' + x[1] + '</span></div>'; }).join('') + '</div>' +
      '<div class="wr-note">Shortest sentence ' + shortest + ' words, longest ' + longest + '. Passive verbs found: about ' + passive + '.</div></div>';
    cards = '<div class="wr-card wr-prio"><h3>Fix these first</h3>' + (prio.length ? prio.slice(0, 5).map(function(p){ return '<div class="wr-li no">' + esc(p) + '</div>'; }).join('') : '<div class="wr-li ok">Nothing major found by these checks.</div>') + (ok.length ? ok.map(function(p){ return '<div class="wr-li ok">' + esc(p) + '</div>'; }).join('') : '') + '</div>' + cards;
    cards += '<div class="wr-card"><h3>Linking words used (' + total + ')</h3>' + (Object.keys(used).length ? Object.keys(used).map(function(c){ return '<div class="wr-li"><b>' + c + ':</b> ' + esc(used[c].join(', ')) + '</div>'; }).join('') : '<div class="wr-li no">None found.</div>') +
      (missingCats.length ? '<div class="wr-li tip">Not used yet: ' + missingCats.join(', ') + '.</div>' : '') + '</div>';
    if(rep.length) cards += '<div class="wr-card"><h3>Repeated words</h3>' + rep.map(function(w){ return '<span class="wr-chip">' + esc(w) + ' x' + freq[w] + '</span>'; }).join('') +
      rep.filter(function(w){ return WEAK[w]; }).map(function(w){ return '<div class="wr-li tip">' + esc(w) + ' &rarr; ' + esc(WEAK[w]) + '</div>'; }).join('') + '</div>';
    if(flags.length) cards += '<div class="wr-card"><h3>Style and accuracy flags</h3>' + flags.map(function(f){ return '<div class="wr-li no">' + esc(f) + '</div>'; }).join('') + '</div>';
    cards += '<div class="wr-card"><h3>Advanced vocabulary you used (' + adv.length + ')</h3>' + (adv.length ? adv.slice(0, 24).map(function(w){ return '<span class="wr-chip">' + esc(w) + '</span>'; }).join('') : '<div class="wr-li tip">No Band 7+ words from the IELTS Vocabulary list found. Learn and use a few topic words.</div>') + '</div>';
    cards += '<div class="wr-note">These are automatic checks of form, not of meaning. They cannot judge whether your argument answers the question. Ask your teacher for a band.</div>';
    out.innerHTML = cards;
    var d = new Date().toISOString().slice(0, 10);
    if(n >= T.min && localStorage.getItem('writingXpDay') !== d){ localStorage.setItem('writingXpDay', d); award(5, 'writing'); }
    out.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
}
ui();
