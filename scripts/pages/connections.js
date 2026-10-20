var BACK = back('index.html#geography-hub', 'Back to Train Your Brain');
var PUZ = null, S = null;
function hub(){
  var won = lsGet('connectionsWins', 0);
  app.innerHTML = BACK + head('Connections', 'Sort 16 words into 4 hidden groups. Four mistakes and it is over.') +
    '<div class="v-card random-tile"><div class="v-def" style="margin-top:0;">Puzzles solved: <b>' + won + '</b></div></div>' +
    '<div class="v-row"><button class="v-btn" id="cDaily">Today’s puzzle</button><button class="v-btn alt" id="cRand">Random puzzle</button></div>' +
    '<div class="v-hint" style="margin-top:12px;">Each group has a theme: a grammar point, a topic or a word type. Colours go from easiest (yellow) to trickiest (purple).</div>';
  document.getElementById('cDaily').onclick = function(){ start(dayNumber() % PUZ.length, true); };
  document.getElementById('cRand').onclick = function(){ start(Math.floor(Math.random() * PUZ.length), false); };
}
function start(idx, daily){
  var p = PUZ[idx];
  var tiles = [];
  p.forEach(function(g, gi){ g.w.forEach(function(w){ tiles.push({ w: w, g: gi }); }); });
  S = { idx: idx, daily: daily, tiles: shuffle(tiles), sel: [], solved: [], lives: 4, guesses: [], over: false };
  draw('');
}
function draw(msg){
  var p = PUZ[S.idx], h = BACK + head('Connections', S.daily ? 'Today’s puzzle' : 'Random puzzle');
  S.solved.forEach(function(gi){
    h += '<div class="cn-done cn-c' + gi + '"><b>' + esc(p[gi].n) + '</b><span>' + p[gi].w.map(esc).join(', ') + '</span></div>';
  });
  var rest = S.tiles.filter(function(t){ return S.solved.indexOf(t.g) < 0; });
  if(!S.over){
    h += '<div class="cn-grid" id="cnGrid">' + rest.map(function(t){
      return '<button class="cn-tile' + (S.sel.indexOf(t.w) >= 0 ? ' sel' : '') + '" data-w="' + esc(t.w) + '">' + esc(t.w) + '</button>'; }).join('') + '</div>';
    h += '<div class="cn-msg" id="cnMsg">' + esc(msg || '') + '</div>';
    h += '<div class="cn-lives">Mistakes left: ' + '●'.repeat(S.lives) + '○'.repeat(4 - S.lives) + '</div>';
    h += '<div class="v-row"><button class="v-btn alt" id="cnShuf">Shuffle</button><button class="v-btn alt" id="cnDes">Deselect</button><button class="v-btn" id="cnGo"' + (S.sel.length === 4 ? '' : ' style="opacity:.45"') + '>Submit</button></div>';
  } else {
    var won = !!S.won;
    h += '<div class="v-card random-tile"><div class="v-big">' + (won ? 'Solved!' : 'Out of mistakes') + '</div><div class="v-def">' + (won ? 'You found all four groups with ' + (4 - S.lives) + ' mistake' + (4 - S.lives === 1 ? '' : 's') + '.' : 'The groups are shown above. Try another puzzle.') + '</div></div>' +
         '<div class="v-row"><button class="v-btn" id="cnAgain">Another puzzle</button><button class="v-btn alt" id="cnHub">Menu</button></div>';
  }
  app.innerHTML = h;
  var g = document.getElementById('cnGrid');
  if(g) g.querySelectorAll('.cn-tile').forEach(function(b){
    b.onclick = function(){
      var w = b.getAttribute('data-w'), i = S.sel.indexOf(w);
      if(i >= 0) S.sel.splice(i, 1); else if(S.sel.length < 4) S.sel.push(w);
      draw('');
    };
  });
  var q = function(id, fn){ var e = document.getElementById(id); if(e) e.onclick = fn; };
  q('cnShuf', function(){ S.tiles = shuffle(S.tiles); draw(''); });
  q('cnDes', function(){ S.sel = []; draw(''); });
  q('cnGo', submit);
  q('cnAgain', function(){ start(Math.floor(Math.random() * PUZ.length), false); });
  q('cnHub', hub);
}
function submit(){
  if(S.sel.length !== 4) return;
  var key = S.sel.slice().sort().join('|');
  if(S.guesses.indexOf(key) >= 0){ draw('Already guessed that one.'); return; }
  S.guesses.push(key);
  var picks = S.tiles.filter(function(t){ return S.sel.indexOf(t.w) >= 0; });
  var counts = {}; picks.forEach(function(t){ counts[t.g] = (counts[t.g] || 0) + 1; });
  var best = Math.max.apply(null, Object.keys(counts).map(function(k){ return counts[k]; }));
  if(best === 4){
    var gi = picks[0].g; S.solved.push(gi); S.sel = []; award(2, 'group');
    if(S.solved.length === 4){
      S.over = true; S.won = true; award(5, 'solved');
      lsSet('connectionsWins', lsGet('connectionsWins', 0) + 1);
    }
    draw('');
  } else {
    S.lives--; S.sel = [];
    if(S.lives <= 0){
      S.over = true;
      PUZ[S.idx].forEach(function(g, gi){ if(S.solved.indexOf(gi) < 0) S.solved.push(gi); });
      draw('');
    } else {
      draw(best === 3 ? 'One away!' : 'Not a group.');
      var gr = document.getElementById('cnGrid'); if(gr){ gr.classList.add('cn-shake'); }
    }
  }
}
getJson('data/games/connections.json').then(function(d){ PUZ = d; hub(); }).catch(function(){
  app.innerHTML = BACK + '<div class="empty-card">Could not load the puzzles. Check your connection and try again.</div>';
});
