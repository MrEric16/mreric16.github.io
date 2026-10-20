var BACK = back('index.html#geography-hub', 'Back to Train Your Brain');
var PUZ = null, P = null, S = null, cur = '', order = [];
var RANKS = [[0,'Beginner'],[2,'Good start'],[5,'Moving up'],[8,'Good'],[15,'Solid'],[25,'Nice'],[40,'Great'],[50,'Amazing'],[70,'Genius'],[100,'Queen Bee']];
function pts(w){ return (w.length === 4 ? 1 : w.length) + (P.p.indexOf(w) >= 0 ? 7 : 0); }
function maxScore(){ return P.w.reduce(function(a, w){ return a + pts(w); }, 0); }
function score(){ return S.found.reduce(function(a, w){ return a + pts(w); }, 0); }
function rank(){
  var pct = score() / maxScore() * 100, r = RANKS[0][1];
  RANKS.forEach(function(x){ if(pct >= x[0] - 1e-9) r = x[1]; });
  return { name: r, pct: pct };
}
function hub(){
  app.innerHTML = BACK + head('Spelling Bee', 'Make words of 4+ letters. Every word must use the centre letter. Letters can repeat. Find the pangram that uses all 7.') +
    '<div class="v-row"><button class="v-btn" id="bDaily">Today’s hive</button><button class="v-btn alt" id="bRand">Random hive</button></div>' +
    '<div class="v-hint" style="margin-top:12px;">Scoring: 4-letter words score 1 point, longer words score their length, a pangram adds 7.</div>';
  document.getElementById('bDaily').onclick = function(){ open(dayNumber() % PUZ.length); };
  document.getElementById('bRand').onclick = function(){ open(Math.floor(Math.random() * PUZ.length)); };
}
function open(idx){
  P = PUZ[idx];
  var saved = lsGet('beeState_' + idx, null);
  S = saved && saved.l === P.l ? saved : { l: P.l, found: [], gave: false, genius: false };
  S.idx = idx;
  order = shuffle(P.l.split('').filter(function(c){ return c !== P.c; }));
  cur = '';
  draw('');
}
function save(){ lsSet('beeState_' + S.idx, { l: S.l, found: S.found, gave: S.gave, genius: S.genius }); }
function hex(c, cls, x, y){ return '<button class="bee-hex ' + cls + '" style="left:' + x + 'px; top:' + y + 'px;" data-c="' + c + '">' + c + '</button>'; }
function draw(msg){
  var r = rank(), L = order, cx = 106, cy = 104;
  var pos = [[0,-80],[68,-40],[68,40],[0,80],[-68,40],[-68,-40]];
  var h = BACK + head('Spelling Bee');
  h += '<div class="bee-rank"><span>' + esc(r.name) + '</span><div class="bar"><i style="width:' + Math.min(100, r.pct).toFixed(1) + '%"></i></div><span>' + score() + '</span></div>';
  h += '<div class="bee-in" id="beeIn">' + (cur ? cur.split('').map(function(c){ return c === P.c ? '<span class="req">' + c + '</span>' : (P.l.indexOf(c) < 0 ? '<span class="bad">' + c + '</span>' : c); }).join('') : '<span style="opacity:.3">type or tap</span>') + '</div>';
  h += '<div class="bee-msg" id="beeMsg">' + esc(msg) + '</div>';
  h += '<div class="bee-hive">' + hex(P.c, 'mid', cx, cy) + L.map(function(c, i){ return hex(c, '', cx + pos[i][0], cy + pos[i][1]); }).join('') + '</div>';
  h += '<div class="v-row"><button class="v-btn alt" id="bDel">Delete</button><button class="v-btn alt" id="bShuf">Shuffle</button><button class="v-btn" id="bEnter">Enter</button></div>';
  h += '<div class="v-hint" style="margin-top:14px;">Found ' + S.found.length + ' of ' + P.w.length + ' words</div><div class="bee-words">' +
       S.found.slice().sort().map(function(w){ return '<span' + (P.p.indexOf(w) >= 0 ? ' class="pg"' : '') + '>' + esc(w) + '</span>'; }).join('') + '</div>';
  if(S.gave){
    h += '<div class="v-hint">Words you missed</div><div class="bee-words">' + P.w.filter(function(w){ return S.found.indexOf(w) < 0; }).map(function(w){ return '<span class="miss' + (P.p.indexOf(w) >= 0 ? ' pg' : '') + '">' + esc(w) + '</span>'; }).join('') + '</div>';
  }
  h += '<div class="v-row"><button class="v-btn alt" id="bGive">' + (S.gave ? 'Hide answers' : 'Give up and show words') + '</button><button class="v-btn alt" id="bNew">New hive</button></div>';
  app.innerHTML = h;
  app.querySelectorAll('.bee-hex').forEach(function(b){ b.onclick = function(){ cur += b.getAttribute('data-c'); draw(''); }; });
  var q = function(id, fn){ var e = document.getElementById(id); if(e) e.onclick = fn; };
  q('bDel', function(){ cur = cur.slice(0, -1); draw(''); });
  q('bShuf', function(){ order = shuffle(order); draw(''); });
  q('bEnter', enter);
  q('bGive', function(){ S.gave = !S.gave; save(); draw(''); });
  q('bNew', function(){ hub(); });
}
function enter(){
  var w = cur.toLowerCase(); cur = '';
  if(w.length < 4) return draw('Too short');
  for(var i = 0; i < w.length; i++) if(P.l.indexOf(w[i]) < 0) return draw('Bad letters');
  if(w.indexOf(P.c) < 0) return draw('Missing centre letter');
  if(S.found.indexOf(w) >= 0) return draw('Already found');
  if(P.w.indexOf(w) < 0) return draw('Not in word list');
  S.found.push(w);
  var pg = P.p.indexOf(w) >= 0;
  award(pg ? 5 : 1, 'bee');
  var r = rank();
  if(!S.genius && r.pct >= 70){ S.genius = true; award(20, 'genius'); lsSet('beeGenius', lsGet('beeGenius', 0) + 1); }
  save();
  draw(pg ? 'Pangram! +' + pts(w) : (w.length >= 7 ? 'Great! +' + pts(w) : 'Nice! +' + pts(w)));
}
document.addEventListener('keydown', function(e){
  if(!P || !document.getElementById('beeIn')) return;
  if(e.key === 'Enter'){ e.preventDefault(); enter(); }
  else if(e.key === 'Backspace'){ cur = cur.slice(0, -1); draw(''); }
  else if(/^[a-zA-Z]$/.test(e.key) && !e.ctrlKey && !e.metaKey){ cur += e.key.toLowerCase(); draw(''); }
});
getJson('data/games/bee.json').then(function(d){ PUZ = d; hub(); }).catch(function(){
  app.innerHTML = BACK + '<div class="empty-card">Could not load the puzzles. Check your connection and try again.</div>';
});
