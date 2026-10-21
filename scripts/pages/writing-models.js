var BACK = back('index.html#geography-hub/study', 'Back to Train Your Brain');
var TABS = [['t1a', 'Task 1 Academic'], ['t1g', 'Task 1 Letters'], ['t2', 'Task 2 Essays']];
var CRIT = { t1a: 'Task Achievement', t1g: 'Task Achievement', t2: 'Task Response' };
var st = lsGet('wmUI', { tab: 't1a', open: null, notes: false });
var DATA = null;
var PAL = ['var(--coral)', 'var(--teal)', 'var(--gold)'];
function save(){ lsSet('wmUI', st); }
function svgWrap(w, h, inner){ return '<svg class="wm-svg" viewBox="0 0 ' + w + ' ' + h + '" role="img" xmlns="http://www.w3.org/2000/svg">' + inner + '</svg>'; }
function legend(names){ return '<div class="wm-leg">' + names.map(function(n, i){ return '<span><i style="background:' + PAL[i % 3] + '"></i>' + esc(n) + '</span>'; }).join('') + '</div>'; }
function axes(c, W, H, L, B, T, R){
  var max = c.max, h = '';
  for(var i = 0; i <= 5; i++){
    var v = max * i / 5, y = H - B - (H - B - T) * i / 5;
    h += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + y + '" y2="' + y + '" stroke="currentColor" stroke-opacity=".15"/><text x="' + (L - 6) + '" y="' + (y + 4) + '" text-anchor="end" class="wm-t">' + Math.round(v) + '</text>';
  }
  return h + '<text x="14" y="' + ((H - B + T) / 2) + '" transform="rotate(-90 14 ' + ((H - B + T) / 2) + ')" text-anchor="middle" class="wm-t">' + esc(c.y) + '</text>';
}
function lineChart(c){
  var W = 560, H = 300, L = 54, B = 34, T = 12, R = 14, n = c.x.length, h = axes(c, W, H, L, B, T, R);
  var px = function(i){ return L + (W - L - R) * i / (n - 1); }, py = function(v){ return H - B - (H - B - T) * v / c.max; };
  c.x.forEach(function(x, i){ h += '<text x="' + px(i) + '" y="' + (H - 12) + '" text-anchor="middle" class="wm-t">' + esc(x) + '</text>'; });
  c.series.forEach(function(s, k){
    h += '<polyline fill="none" stroke="' + PAL[k % 3] + '" stroke-width="3" stroke-linejoin="round" points="' + s.data.map(function(v, i){ return px(i) + ',' + py(v); }).join(' ') + '"/>';
    s.data.forEach(function(v, i){ h += '<circle cx="' + px(i) + '" cy="' + py(v) + '" r="4" fill="' + PAL[k % 3] + '"/>'; });
  });
  return svgWrap(W, H, h) + legend(c.series.map(function(s){ return s.name; }));
}
function barChart(c){
  var W = 560, H = 300, L = 54, B = 34, T = 12, R = 14, g = c.groups.length, ns = c.series.length, h = axes(c, W, H, L, B, T, R);
  var gw = (W - L - R) / g, bw = Math.min(34, (gw - 16) / ns);
  c.groups.forEach(function(name, i){
    h += '<text x="' + (L + gw * i + gw / 2) + '" y="' + (H - 12) + '" text-anchor="middle" class="wm-t">' + esc(name) + '</text>';
    c.series.forEach(function(s, k){
      var v = s.data[i], bh = (H - B - T) * v / c.max, x = L + gw * i + gw / 2 - (bw * ns) / 2 + bw * k;
      h += '<rect x="' + x + '" y="' + (H - B - bh) + '" width="' + (bw - 2) + '" height="' + bh + '" rx="3" fill="' + PAL[k % 3] + '"/><text x="' + (x + bw / 2 - 1) + '" y="' + (H - B - bh - 4) + '" text-anchor="middle" class="wm-t">' + v + '</text>';
    });
  });
  return svgWrap(W, H, h) + legend(c.series.map(function(s){ return s.name; }));
}
function pieChart(c){
  var cols = ['var(--coral)', 'var(--teal)', 'var(--gold)', '#6c5ce7', '#8d6e63'], names = c.charts[0].parts.map(function(p){ return p[0]; });
  var W = 560, H = 240, h = '';
  c.charts.forEach(function(ch, ci){
    var cx = 150 + ci * 260, cy = 120, r = 82, a0 = -Math.PI / 2, tot = ch.parts.reduce(function(a, p){ return a + p[1]; }, 0);
    ch.parts.forEach(function(p, i){
      var a1 = a0 + 2 * Math.PI * p[1] / tot, big = (a1 - a0) > Math.PI ? 1 : 0, am = (a0 + a1) / 2;
      h += '<path d="M' + cx + ' ' + cy + 'L' + (cx + r * Math.cos(a0)) + ' ' + (cy + r * Math.sin(a0)) + 'A' + r + ' ' + r + ' 0 ' + big + ' 1 ' + (cx + r * Math.cos(a1)) + ' ' + (cy + r * Math.sin(a1)) + 'Z" fill="' + cols[i % 5] + '" stroke="var(--card)" stroke-width="2"/>';
      var small = p[1] / tot < .12;
      h += '<text x="' + (cx + r * (small ? 1.2 : .62) * Math.cos(am)) + '" y="' + (cy + r * (small ? 1.2 : .62) * Math.sin(am) + 4) + '" text-anchor="middle" class="' + (small ? 'wm-t' : 'wm-pt') + '">' + p[1] + '%</text>';
      a0 = a1;
    });
    h += '<text x="' + cx + '" y="' + (H - 6) + '" text-anchor="middle" class="wm-t" style="font-weight:800">' + esc(ch.label) + '</text>';
  });
  return svgWrap(W, H, h) + '<div class="wm-leg">' + names.map(function(n, i){ return '<span><i style="background:' + cols[i % 5] + '"></i>' + esc(n) + '</span>'; }).join('') + '</div>';
}
function tableChart(c){
  return '<div class="wm-tw"><table class="wm-table"><thead><tr>' + c.head.map(function(x){ return '<th>' + esc(x) + '</th>'; }).join('') + '</tr></thead><tbody>' +
    c.rows.map(function(r){ return '<tr>' + r.map(function(x, i){ return i ? '<td>' + esc(x) + '</td>' : '<th>' + esc(x) + '</th>'; }).join('') + '</tr>'; }).join('') + '</tbody></table></div>' + (c.foot ? '<div class="wm-foot">' + esc(c.foot) + '</div>' : '');
}
function processChart(c){
  return '<ol class="wm-proc">' + c.steps.map(function(s){ return '<li>' + esc(s) + '</li>'; }).join('') + '</ol>';
}
function chartHtml(c){
  if(!c) return '';
  var f = { line: lineChart, bar: barChart, pie: pieChart, table: tableChart, process: processChart }[c.type];
  return '<div class="wm-chart"><div class="wm-ct">' + esc(c.title) + '</div>' + f(c) + '</div>';
}
function list(){
  var items = DATA.models.filter(function(m){ return m.task === st.tab; });
  var h = BACK + head('IELTS Writing Models', 'Band 9 target answers for Task 1 and Task 2, with notes on why each one works.');
  h += '<div class="wm-warn">Written for this site to match the Band 9 descriptors. They are not official IELTS material and were not marked by an examiner. Learn the structure and the language, never memorise a whole answer.</div>';
  h += '<div class="wr-sel">' + TABS.map(function(t){ return '<button data-tab="' + t[0] + '" class="' + (st.tab === t[0] ? 'on' : '') + '">' + t[1] + '</button>'; }).join('') + '</div>';
  h += '<div class="wm-grid">' + items.map(function(m){
    return '<a class="wm-tile" href="#' + m.id + '"><span class="wm-type">' + esc(m.type) + '</span><b>' + esc(m.title) + '</b><span class="wm-w">' + m.words + ' words</span></a>';
  }).join('') + '</div>';
  app.innerHTML = h;
  app.querySelectorAll('[data-tab]').forEach(function(b){ b.onclick = function(){ st.tab = b.getAttribute('data-tab'); save(); list(); }; });
}
function openModel(id){
  var m = DATA.models.filter(function(x){ return x.id === id; })[0];
  if(!m){ location.hash = ''; return; }
  var all = DATA.models.filter(function(x){ return x.task === m.task; }), ix = all.indexOf(m);
  var h = back('#', 'Back to models') + head(esc(m.title), esc(m.type) + ' · ' + (m.task === 't2' ? 'Task 2' : m.task === 't1a' ? 'Task 1 Academic' : 'Task 1 General') + ' · ' + m.words + ' words');
  h += '<div class="wr-card"><h3>The task</h3>' + m.prompt.split('\n').map(function(p){ return '<p class="wm-p">' + esc(p) + '</p>'; }).join('') + '</div>';
  h += chartHtml(m.chart);
  h += '<div class="wr-card"><div class="wm-try">Try it yourself first. Then compare.</div><div class="v-row"><button class="v-btn" id="wmTry">Write it in the Checker</button><button class="v-btn alt" id="wmShow">' + (st.shown === id ? 'Hide model answer' : 'Show model answer') + '</button></div></div>';
  if(st.shown === id){
    h += '<div class="wr-card wm-model"><h3>Model answer</h3>' + m.model.map(function(p, i){
      var small = m.task === 't1g' && (i === 0 || i >= m.model.length - 2);
      return '<p class="wm-p' + (small ? ' wm-sm' : '') + '">' + esc(p) + '</p>';
    }).join('') + '<div class="wr-note">' + m.words + ' words (numbers count as words).</div></div>';
    h += '<div class="wr-card"><h3>Why it scores Band 9</h3>' + Object.keys(m.notes).map(function(k){ return '<div class="wr-li"><b>' + esc(k) + ':</b> ' + esc(m.notes[k]) + '</div>'; }).join('') + '</div>';
    h += '<div class="wr-card"><h3>Language to learn</h3>' + m.lang.map(function(w){ return '<span class="wr-chip">' + esc(w) + '</span>'; }).join('') + '</div>';
  }
  h += '<div class="v-row" style="margin-top:6px;">' + (ix > 0 ? '<a class="v-btn alt wm-nav" href="#' + all[ix - 1].id + '">← Previous</a>' : '') + (ix < all.length - 1 ? '<a class="v-btn alt wm-nav" href="#' + all[ix + 1].id + '">Next →</a>' : '') + '</div>';
  app.innerHTML = h; window.scrollTo(0, 0);
  document.getElementById('wmShow').onclick = function(){ st.shown = st.shown === id ? null : id; save(); openModel(id); };
  document.getElementById('wmTry').onclick = function(){ lsSet('writingUI', { task: m.task }); location.href = 'writing.html'; };
}
function route(){
  var id = decodeURIComponent(location.hash.replace(/^#/, ''));
  if(!DATA) return;
  if(id) openModel(id); else { window.scrollTo(0, 0); list(); }
}
app.innerHTML = BACK + '<div class="empty-card">Loading…</div>';
getJson('data/writing/models.json').then(function(d){ DATA = d; window.addEventListener('hashchange', route); route(); }).catch(function(){ app.innerHTML = BACK + '<div class="empty-card">Could not load the models. Check your connection and reload.</div>'; });
