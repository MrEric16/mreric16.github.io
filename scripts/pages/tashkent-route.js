var BACK = back('index.html#events-hub', 'Back to Tashkent');
var T = null, G = null, map = null, layerBase = null, layerRoute = null, pins = { from: null, to: null }, P = { from: null, to: null }, active = 'to', results = [], openIdx = 0;
var WALK_MIN_PER_KM = 12.5 * 1.3, BUS_MIN_PER_KM = 3.75 * 1.3, METRO_MIN_PER_KM = 1.58, METRO_DWELL = 0.5, BUS_DWELL = 0.35;
var HOURS = { start: 5, end: 24 };
function km(a, b, c, d){ var x = (a - c) * 111.2, y = (b - d) * 84.0; return Math.sqrt(x * x + y * y); }
function norm(s){ return String(s || '').toLowerCase().replace(/[ʻʼ’‘`'´]/g, '').replace(/\s+/g, ' ').trim(); }
var WHEN = null; // minutes after midnight (Tashkent time) chosen by the user, or null for now
function nowMin(){
  try{ var parts = new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Tashkent', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()), h = 0, m = 0;
    parts.forEach(function(p){ if(p.type === 'hour') h = +p.value % 24; if(p.type === 'minute') m = +p.value; }); return h * 60 + m;
  }catch(e){ var d = new Date(); return d.getHours() * 60 + d.getMinutes(); }
}
function baseMin(){ return WHEN === null ? nowMin() : WHEN; }
function metroClosed(li, min){ var open = li === 2 ? 360 : 300, close = li === 2 ? 1380 : 1440; return min < open || min >= close - 15; }
function rush(){ var h = baseMin() / 60; return (h >= 7.5 && h < 9.5) || (h >= 17 && h < 19.5); }
function fmtMin(m){ m = Math.round(m); if(m < 60) return m + ' min'; return Math.floor(m / 60) + ' h ' + (m % 60 ? (m % 60) + ' min' : ''); }
function clock(min){ var t = Math.round(baseMin() + min) % 1440; return String(Math.floor(t / 60)).padStart(2, '0') + ':' + String(t % 60).padStart(2, '0'); }
// ---------- graph ----------
function buildGraph(){
  var nodes = [], adj = [];
  function addNode(o){ nodes.push(o); adj.push([]); return nodes.length - 1; }
  function edge(a, b, c, meta){ adj[a].push({ to: b, c: c, m: meta }); }
  var interchange = [['Paxtakor', 'Alisher Navoiy', 4, 0], ['Amir Temur Xiyoboni', 'Yunus Rajabiy', 4, 0], ['Oybek', 'Ming Oʻrik', 4, 0], ['Doʻstlik', 'Texnopark', 5, 0], ['Chinor', 'Qipchoq', 9, 1]];
  var mStation = {}, mLines = [];
  T.metro.forEach(function(l, li){
    var sIds = [], pIds = [];
    l.st.forEach(function(s, i){
      var sid = addNode({ la: s.la, lo: s.lo, name: s.n, kind: 'm', line: li });
      mStation[s.n] = sid; sIds.push(sid);
    });
    l.st.forEach(function(s, i){ pIds.push(addNode({ la: s.la, lo: s.lo, name: s.n, kind: 'mp', line: li, i: i })); });
    mLines.push({ s: sIds, p: pIds });
  });
  var busStops = [], busLegs = [];
  T.bus.forEach(function(r, ri){
    var sIds = [], pIds = [], seenCoord = {};
    r.st.forEach(function(s, i){
      var key = s[0] + ',' + s[1], sid;
      sid = addNode({ la: s[0], lo: s[1], name: s[2], kind: 'b' }); busStops.push(sid); sIds.push(sid);
    });
    r.st.forEach(function(s, i){ pIds.push(addNode({ la: s[0], lo: s[1], name: s[2], kind: 'bp', route: ri, i: i })); });
    busLegs.push({ s: sIds, p: pIds });
  });
  return { nodes: nodes, adj: adj, edge: edge, addNode: addNode, mStation: mStation, mLines: mLines, busLegs: busLegs, busStops: busStops, interchange: interchange };
}
function prepare(){
  var g = buildGraph(), nodes = g.nodes, bm = baseMin();
  var peak = rush();
  // metro rides and boardings
  T.metro.forEach(function(l, li){
    var ml = g.mLines[li], head = (li === 3) ? 7 : (peak ? 3 : 9), wait = head / 2;
    var closedNow = metroClosed(li, bm);
    l.st.forEach(function(s, i){
      var sid = ml.s[i], pid = ml.p[i];
      if(!closedNow) g.edge(sid, pid, wait + 1.0, { t: 'board', mode: 'metro', line: li });
      g.edge(pid, sid, 0.3, { t: 'alight' });
      [-1, 1].forEach(function(dd){
        var j = i + dd; if(j < 0 || j >= l.st.length) return;
        var d = km(s.la, s.lo, l.st[j].la, l.st[j].lo);
        g.edge(pid, ml.p[j], d * METRO_MIN_PER_KM + METRO_DWELL, { t: 'ride', mode: 'metro', line: li, dir: dd });
      });
    });
  });
  g.interchange.forEach(function(x){
    var a = g.mStation[x[0]], b = g.mStation[x[1]]; if(a === undefined || b === undefined) return;
    g.edge(a, b, x[2], { t: 'xfer', paid: x[3] }); g.edge(b, a, x[2], { t: 'xfer', paid: x[3] });
  });
  // bus rides
  var bwait = 8, bf = peak ? 1.25 : 1.0;
  T.bus.forEach(function(r, ri){
    var bl = g.busLegs[ri];
    r.st.forEach(function(s, i){
      g.edge(bl.s[i], bl.p[i], bwait + 1.0, { t: 'board', mode: 'bus', route: ri });
      g.edge(bl.p[i], bl.s[i], 0.3, { t: 'alight' });
      if(i + 1 < r.st.length){
        var d = km(s[0], s[1], r.st[i + 1][0], r.st[i + 1][1]);
        g.edge(bl.p[i], bl.p[i + 1], (d * BUS_MIN_PER_KM + BUS_DWELL) * bf, { t: 'ride', mode: 'bus', route: ri });
      }
    });
  });
  // walking links between stop-type nodes (stations and bus stops)
  var cell = 0.004, grid = {};
  var stopIds = [];
  nodes.forEach(function(n, id){ if(n.kind === 'm' || n.kind === 'b') stopIds.push(id); });
  stopIds.forEach(function(id){ var n = nodes[id], k = Math.floor(n.la / cell) + ':' + Math.floor(n.lo / cell); (grid[k] = grid[k] || []).push(id); });
  stopIds.forEach(function(id){
    var n = nodes[id], cx = Math.floor(n.la / cell), cy = Math.floor(n.lo / cell);
    for(var dx = -1; dx <= 1; dx++) for(var dy = -1; dy <= 1; dy++){
      var arr = grid[(cx + dx) + ':' + (cy + dy)]; if(!arr) continue;
      arr.forEach(function(o){
        if(o === id) return; var m = nodes[o]; if(n.kind === 'm' && m.kind === 'm') return;
        var d = km(n.la, n.lo, m.la, m.lo), lim = (n.kind === 'm' || m.kind === 'm') ? 0.45 : 0.25;
        if(d <= lim) g.edge(id, o, d * WALK_MIN_PER_KM + 0.5, { t: 'walk', d: d });
      });
    }
  });
  g.stopIds = stopIds; g.peak = peak;
  return g;
}
function Heap(){ this.a = []; }
Heap.prototype.push = function(k, v){ var a = this.a; a.push([k, v]); var i = a.length - 1; while(i > 0){ var p = (i - 1) >> 1; if(a[p][0] <= a[i][0]) break; var t = a[p]; a[p] = a[i]; a[i] = t; i = p; } };
Heap.prototype.pop = function(){ var a = this.a, top = a[0], last = a.pop(); if(a.length){ a[0] = last; var i = 0; for(;;){ var l = 2 * i + 1, r = l + 1, s = i; if(l < a.length && a[l][0] < a[s][0]) s = l; if(r < a.length && a[r][0] < a[s][0]) s = r; if(s === i) break; var t = a[s]; a[s] = a[i]; a[i] = t; i = s; } } return top; };
function plan(from, to, prof){
  var nodes = G.nodes, n = nodes.length, O = n, D = n + 1;
  var dist = new Float64Array(n + 2).fill(Infinity), prev = new Int32Array(n + 2).fill(-1), pm = new Array(n + 2);
  var extraOut = {}; // O -> stops
  var heap = new Heap(); dist[O] = 0; heap.push(0, O);
  var dd = km(from.la, from.lo, to.la, to.lo);
  var originLinks = [], destLinks = {};
  G.stopIds.forEach(function(id){
    var s = nodes[id], d1 = km(from.la, from.lo, s.la, s.lo), d2 = km(to.la, to.lo, s.la, s.lo);
    if(d1 <= 1.6) originLinks.push([id, d1 * WALK_MIN_PER_KM * prof.walk + 0.5, d1]);
    if(d2 <= 1.6) destLinks[id] = [d2 * WALK_MIN_PER_KM * prof.walk + 0.5, d2];
  });
  var directWalk = dd <= 3.5 ? dd * WALK_MIN_PER_KM * prof.walk : Infinity;
  while(heap.a.length){
    var top = heap.pop(), du = top[0], u = top[1];
    if(du > dist[u]) continue; if(u === D) break;
    var list;
    if(u === O){
      list = originLinks.map(function(x){ return { to: x[0], c: x[1], m: { t: 'walk', d: x[2], first: true } }; });
      if(directWalk < Infinity) list.push({ to: D, c: directWalk, m: { t: 'walk', d: dd, direct: true } });
    } else list = G.adj[u];
    for(var i = 0; i < list.length; i++){
      var e = list[i], c = e.c;
      if(e.m.t === 'board') c += (e.m.mode === 'bus' ? prof.board + prof.busBoard : prof.board);
      if(e.m.t === 'ride' && e.m.mode === 'bus') c *= prof.busSlow;
      if(e.m.t === 'walk') c *= prof.walk;
      var nd = du + c;
      if(nd < dist[e.to]){ dist[e.to] = nd; prev[e.to] = u; pm[e.to] = { m: e.m, c: e.c }; heap.push(nd, e.to); }
    }
    if(destLinks[u]){ var dl = destLinks[u], nd2 = du + dl[0]; if(nd2 < dist[D]){ dist[D] = nd2; prev[D] = u; pm[D] = { m: { t: 'walk', d: dl[1], last: true }, c: dl[0] / prof.walk }; heap.push(nd2, D); } }
  }
  if(!isFinite(dist[D])) return null;
  var chain = [], x = D; while(x !== -1 && x !== O){ chain.push({ node: x, via: pm[x] }); x = prev[x]; } chain.reverse();
  return summarise(chain, from, to);
}
function summarise(chain, from, to){
  var nodes = G.nodes, legs = [], cur = null, total = 0;
  function push(l){ legs.push(l); cur = l; }
  chain.forEach(function(st){
    var m = st.via.m, c = st.via.c; total += c;
    var nd = st.node >= nodes.length ? null : nodes[st.node];
    if(m.t === 'walk'){
      if(cur && cur.type === 'walk'){ cur.d += m.d; cur.min += c; cur.to = nd ? nd.name : 'destination'; cur.toNode = st.node; }
      else push({ type: 'walk', d: m.d, min: c, to: nd ? (nd.kind === 'm' ? nd.name + ' station' : (nd.name || 'bus stop')) : 'destination', toNode: st.node });
      if(nd) cur.toKind = nd.kind;
    } else if(m.t === 'xfer'){
      push({ type: 'xfer', min: c, to: nd.name, paid: m.paid, toNode: st.node });
    } else if(m.t === 'board'){
      var nd2 = nd; push({ type: m.mode, min: c, mode: m.mode, line: m.line, route: m.route, from: nd2.name, stops: 0, ride: 0, wait: c, fromNode: st.node, path: [st.node] });
    } else if(m.t === 'ride'){
      cur.stops++; cur.min += c; cur.ride += c; cur.path.push(st.node); cur.toNode = st.node; cur.to = nd.name;
      if(m.dir) cur.dir = m.dir;
    } else if(m.t === 'alight'){ cur.min += c; }
  });
  // fares: paid boardings
  var nb = 0, price = 0, inMetro = false;
  legs.forEach(function(l){
    if(l.type === 'bus'){ nb++; price += nb === 1 ? 2500 : (nb === 2 ? 1500 : 0); inMetro = false; }
    else if(l.type === 'metro'){ if(!inMetro){ nb++; price += nb === 1 ? 2500 : 1500; } inMetro = true; }
    else if(l.type === 'xfer'){ if(l.paid) inMetro = false; }
    else if(l.type === 'walk'){ inMetro = false; }
  });
  var walkMin = 0, walkKm = 0; legs.forEach(function(l){ if(l.type === 'walk'){ walkMin += l.min; walkKm += l.d; } });
  var sig = legs.map(function(l){ return l.type + (l.line !== undefined ? l.line : '') + (l.route !== undefined ? 'b' + l.route : '') + (l.fromNode || ''); }).join('|');
  return { legs: legs, total: total, fare: price, walkMin: walkMin, walkKm: walkKm, transfers: legs.filter(function(l){ return l.type === 'metro' || l.type === 'bus'; }).length - 1, sig: sig, from: from, to: to };
}
var PROFILES = [
  { key: 'Fastest', walk: 1, board: 1, busBoard: 0, busSlow: 1 },
  { key: 'Fewer changes', walk: 1, board: 9, busBoard: 3, busSlow: 1 },
  { key: 'Metro first', walk: 1, board: 1, busBoard: 7, busSlow: 1.6 },
  { key: 'Less walking', walk: 2.2, board: 1, busBoard: 0, busSlow: 1 }
];
function run(){
  if(!P.from || !P.to) return;
  var out = [], seen = {};
  PROFILES.forEach(function(p){
    var r = plan(P.from, P.to, p); if(!r || seen[r.sig]) return; seen[r.sig] = 1; r.label = p.key; out.push(r);
  });
  out.sort(function(a, b){ return a.total - b.total; });
  if(out.length) out[0].label = 'Fastest';
  results = out.slice(0, 3); openIdx = 0; drawResults(); drawRoute(results[0]);
}
// ---------- ui ----------
function chipFor(l){
  if(l.type === 'walk' && l.d < 0.04) return '';
  if(l.type === 'walk') return '<span class="tr-chip w">Walk ' + Math.max(1, Math.round(l.min)) + '</span>';
  if(l.type === 'metro') return '<span class="tr-chip m" style="background:' + T.metro[l.line].color + ';color:' + (l.line === 3 ? '#222' : '#fff') + ';">Metro ' + esc(T.metro[l.line].name) + '</span>';
  if(l.type === 'bus') return '<span class="tr-chip b">Bus ' + esc(T.bus[l.route].ref) + '</span>';
  return '';
}
function toward(l){
  if(l.type === 'metro'){ var L = T.metro[l.line], last = L.st[L.st.length - 1].n, first = L.st[0].n; return l.dir > 0 ? last : first; }
  var R = T.bus[l.route]; return R.to || R.st[R.st.length - 1][2] || '';
}
function stepsHtml(r){
  var h = '<ol class="tr-steps">';
  r.legs.forEach(function(l){
    if(l.type === 'walk' && l.d < 0.04) return;
    if(l.type === 'walk') h += '<li><b>Walk</b> ' + Math.max(1, Math.round(l.min)) + ' min (' + (l.d < 1 ? Math.round(l.d * 1000 / 10) * 10 + ' m' : l.d.toFixed(1) + ' km') + ') to ' + esc(l.to) + '</li>';
    else if(l.type === 'xfer') h += '<li><b>Change</b> to ' + esc(l.to) + ', about ' + Math.round(l.min) + ' min on foot' + (l.paid ? '. This is outside the paid area, so you tap in again.' : '.') + '</li>';
    else if(l.type === 'metro') h += '<li><b>Metro ' + esc(T.metro[l.line].name) + ' line</b> from ' + esc(l.from) + ' toward ' + esc(toward(l)) + ', ' + l.stops + ' stop' + (l.stops === 1 ? '' : 's') + ' to ' + esc(l.to) + '. About ' + Math.round(l.ride) + ' min riding, plus ' + Math.round(l.wait - 1) + ' min wait.</li>';
    else if(l.type === 'bus') h += '<li><b>Bus ' + esc(T.bus[l.route].ref) + '</b> from ' + esc(l.from || 'stop') + ' toward ' + esc(toward(l) || 'end of route') + ', get off at ' + esc(l.to || 'stop') + ' (about ' + Math.round(l.ride) + ' min; map data may be missing some stops in between). About ' + Math.round(l.ride) + ' min riding, plus ~' + Math.round(l.wait - 1) + ' min wait (frequency is a guess).</li>';
  });
  return h + '</ol>';
}
function drawResults(){
  var box = document.getElementById('trOut'); if(!box) return;
  if(!results.length){ box.innerHTML = '<div class="v-hint">No route found. Try a point closer to a bus stop or metro station.</div>'; return; }
  var h = '';
  var bm = baseMin(), closedLines = T.metro.filter(function(l, li){ return metroClosed(li, bm); }).map(function(l){ return l.name; }), warn = closedLines.length ? '<div class="v-hint" style="color:#C0392B;">Metro closed at this time: ' + esc(closedLines.join(', ')) + '. Routes avoid it. Metro runs about 05:00 to midnight (Yunusobod 06:00 to 23:00). Bus times assume buses are running, which late at night they may not be.</div>' : '';
  h += warn + (G.peak ? '<div class="v-hint">Rush hour: times include extra delay.</div>' : '');
  results.forEach(function(r, i){
    h += '<div class="tr-card' + (i === openIdx ? ' on' : '') + '" data-i="' + i + '"><div class="tr-top"><b class="tr-min">' + fmtMin(r.total) + '</b><span>arrive about ' + clock(r.total) + '</span><span class="tr-tag">' + esc(r.label) + '</span></div>' +
      '<div class="tr-chips">' + r.legs.map(chipFor).filter(Boolean).join('<i>›</i>') + '</div>' +
      '<div class="v-hint" style="margin:6px 0 0;">Walking ' + Math.round(r.walkMin) + ' min. ' + (r.fare ? 'Fare about ' + r.fare.toLocaleString('en-GB') + ' soum with a card.' : 'Free.') + '</div>' + (i === openIdx ? stepsHtml(r) : '') + '</div>';
  });
  h += '<div class="v-hint" style="margin-top:10px;">Times are estimates from distance and typical speeds. There is no live traffic or timetable. Bus routes come from OpenStreetMap and may be incomplete or out of date. Fares from 1 October 2026: 2,500 soum card for the first ride, 1,500 for a second within 60 minutes, 3,000 cash per ride.</div>';
  box.innerHTML = h;
  box.querySelectorAll('.tr-card').forEach(function(c){ c.onclick = function(){ openIdx = +c.getAttribute('data-i'); drawResults(); drawRoute(results[openIdx]); }; });
}
function ensureLeaflet(cb){
  if(window.L){ cb(); return; }
  var l = document.createElement('link'); l.rel = 'stylesheet'; l.href = 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css'; document.head.appendChild(l);
  var s = document.createElement('script'); s.src = 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js'; s.onload = cb; s.onerror = function(){ var m = document.getElementById('trMap'); if(m) m.innerHTML = '<div class="v-hint" style="padding:16px;">Map unavailable offline. Type places or pick a metro station instead.</div>'; }; document.head.appendChild(s);
}
function initMap(){
  var el = document.getElementById('trMap'); if(!el || !window.L) return;
  map = L.map(el, { zoomControl: true, attributionControl: true }).setView([41.3111, 69.2797], 12);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '© OpenStreetMap' }).addTo(map);
  layerBase = L.layerGroup().addTo(map); layerRoute = L.layerGroup().addTo(map);
  T.metro.forEach(function(l){
    L.polyline(l.st.map(function(s){ return [s.la, s.lo]; }), { color: l.color, weight: 4, opacity: .85 }).addTo(layerBase);
    l.st.forEach(function(s){
      var c = L.circleMarker([s.la, s.lo], { radius: 5, color: '#222', weight: 1.5, fillColor: '#fff', fillOpacity: 1 }).addTo(layerBase);
      c.bindTooltip(s.n, { direction: 'top' });
      c.on('click', function(e){ L.DomEvent.stopPropagation(e); setPoint(active, { la: s.la, lo: s.lo, label: s.n + ' (metro)' }); });
    });
  });
  map.on('click', function(e){ setPoint(active, { la: e.latlng.lat, lo: e.latlng.lng, label: 'Pinned point' }); });
}
function pinIcon(t, col){ return L.divIcon({ className: '', html: '<div class="tr-pin" style="background:' + col + '">' + t + '</div>', iconSize: [28, 28], iconAnchor: [14, 14] }); }
function setPoint(which, p){
  P[which] = p;
  var inp = document.getElementById(which === 'from' ? 'trFrom' : 'trTo'); if(inp) inp.value = p.label;
  if(map){ if(pins[which]) map.removeLayer(pins[which]); pins[which] = L.marker([p.la, p.lo], { icon: pinIcon(which === 'from' ? 'A' : 'B', which === 'from' ? '#2E9B3E' : '#E4002B') }).addTo(map); }
  var sg = document.getElementById(which === 'from' ? 'trSugF' : 'trSugT'); if(sg) sg.innerHTML = '';
  if(which === 'from' && !P.to) active = 'to';
  if(P.from && P.to) run();
}
function drawRoute(r){
  if(!map || !r) return; layerRoute.clearLayers(); var pts = [[r.from.la, r.from.lo]], b = [];
  var cur = [r.from.la, r.from.lo];
  r.legs.forEach(function(l){
    var line;
    if(l.type === 'metro' || l.type === 'bus'){
      var ps = l.path.map(function(id){ return [G.nodes[id].la, G.nodes[id].lo]; });
      var fs = G.nodes[l.fromNode]; ps.unshift([fs.la, fs.lo]);
      L.polyline([cur, [fs.la, fs.lo]], { color: '#555', weight: 3, dashArray: '4 6' }).addTo(layerRoute);
      line = L.polyline(ps, { color: l.type === 'metro' ? T.metro[l.line].color : '#1E6FD9', weight: 7, opacity: .95 }).addTo(layerRoute);
      cur = ps[ps.length - 1]; b = b.concat(ps);
    } else {
      var tn = l.toNode >= G.nodes.length ? [r.to.la, r.to.lo] : [G.nodes[l.toNode].la, G.nodes[l.toNode].lo];
      L.polyline([cur, tn], { color: '#555', weight: 3, dashArray: '4 6' }).addTo(layerRoute); cur = tn; b.push(tn);
    }
  });
  L.polyline([cur, [r.to.la, r.to.lo]], { color: '#555', weight: 3, dashArray: '4 6' }).addTo(layerRoute);
  b.push([r.from.la, r.from.lo], [r.to.la, r.to.lo]);
  try{ map.fitBounds(b, { padding: [24, 24] }); }catch(e){}
}
// ---------- search ----------
var IDX = null;
function buildIdx(){
  IDX = [];
  T.metro.forEach(function(l){ l.st.forEach(function(s){ IDX.push({ n: s.n, k: norm(s.n), la: s.la, lo: s.lo, tag: 'Metro, ' + l.name + ' line', pri: 0 }); }); });
  var seen = {};
  T.bus.forEach(function(r){ r.st.forEach(function(s){ if(!s[2]) return; var k = norm(s[2]) + (Math.round(s[0] * 200)) + (Math.round(s[1] * 200)); if(seen[k]) return; seen[k] = 1; IDX.push({ n: s[2], k: norm(s[2]), la: s[0], lo: s[1], tag: 'Bus stop', pri: 1 }); }); });
}
function localSearch(q){
  q = norm(q); if(q.length < 2) return [];
  var a = [], b = [];
  IDX.forEach(function(x){ var i = x.k.indexOf(q); if(i === 0) a.push(x); else if(i > 0) b.push(x); });
  a.sort(function(x, y){ return x.pri - y.pri; }); b.sort(function(x, y){ return x.pri - y.pri; });
  return a.concat(b).slice(0, 6);
}
var timers = { from: 0, to: 0 };
function wireField(which){
  var inp = document.getElementById(which === 'from' ? 'trFrom' : 'trTo'), sg = document.getElementById(which === 'from' ? 'trSugF' : 'trSugT');
  inp.addEventListener('focus', function(){ active = which; document.getElementById('trAct').textContent = 'Tap the map to set ' + (which === 'from' ? 'the start (A)' : 'the destination (B)') + '.'; });
  inp.addEventListener('input', function(){
    P[which] = null; var q = inp.value, loc = localSearch(q);
    function show(list){ sg.innerHTML = list.map(function(x, i){ return '<button class="tr-sug" data-i="' + i + '"><b>' + esc(x.n) + '</b><small>' + esc(x.tag) + '</small></button>'; }).join(''); sg.querySelectorAll('.tr-sug').forEach(function(b){ b.onclick = function(){ var x = list[+b.getAttribute('data-i')]; setPoint(which, { la: x.la, lo: x.lo, label: x.n }); }; }); }
    show(loc);
    clearTimeout(timers[which]);
    if(q.trim().length >= 3 && navigator.onLine){
      timers[which] = setTimeout(function(){
        fetch('https://nominatim.openstreetmap.org/search?format=json&limit=5&accept-language=en&viewbox=69.05,41.45,69.45,41.15&bounded=1&q=' + encodeURIComponent(q.trim())).then(function(r){ return r.json(); }).then(function(js){
          if(inp.value !== q) return;
          var ex = js.map(function(j){ return { n: (j.display_name || '').split(',').slice(0, 2).join(','), la: +j.lat, lo: +j.lon, tag: 'Place (OpenStreetMap)' }; });
          show(loc.concat(ex).slice(0, 9));
        }).catch(function(){});
      }, 650);
    }
  });
}
function myLoc(){
  var msg = document.getElementById('trAct');
  if(!navigator.geolocation){ msg.textContent = 'Location is not available in this browser.'; return; }
  msg.textContent = 'Finding you...';
  navigator.geolocation.getCurrentPosition(function(p){
    var la = p.coords.latitude, lo = p.coords.longitude;
    if(km(la, lo, 41.3111, 69.2797) > 40){ msg.textContent = 'You seem to be outside Tashkent. Pick the start manually.'; return; }
    setPoint('from', { la: la, lo: lo, label: 'My location' }); msg.textContent = '';
  }, function(){ msg.textContent = 'Location blocked or unavailable.'; }, { enableHighAccuracy: true, timeout: 12000 });
}
function view(){
  app.innerHTML = BACK + head('Getting Around Tashkent', 'Pick a start and a destination by name, by tapping the map, or by tapping a metro station. Get the route with approximate travel time.') +
    '<div class="tr-form"><div class="tr-f"><span class="tr-ab" style="background:#2E9B3E">A</span><input id="trFrom" placeholder="From (place, station, stop)" autocomplete="off"><button class="tr-loc" id="trLoc" title="Use my location">My location</button></div><div id="trSugF"></div>' +
    '<div class="tr-f"><span class="tr-ab" style="background:#E4002B">B</span><input id="trTo" placeholder="To (place, station, stop)" autocomplete="off"><button class="tr-loc" id="trSwap" title="Swap">Swap</button></div><div id="trSugT"></div></div>' +
    '<div class="tr-time"><label>Leave <select id="trWhen"><option value="now">now</option><option value="at">at</option></select></label><input type="time" id="trAt" style="display:none;"></div><div class="v-hint" id="trAct">Tap the map to set the destination (B).</div><div id="trMap" class="tr-map"></div><div id="trOut" style="margin-top:12px;"></div>';
  wireField('from'); wireField('to');
  var tw = document.getElementById('trWhen'), ta = document.getElementById('trAt');
  function whenChanged(){
    if(tw.value === 'now'){ WHEN = null; ta.style.display = 'none'; }
    else { ta.style.display = ''; if(!ta.value){ var n = nowMin(); ta.value = String(Math.floor(n / 60)).padStart(2, '0') + ':' + String(n % 60).padStart(2, '0'); } var q = ta.value.split(':'); WHEN = (+q[0]) * 60 + (+q[1]); }
    G = prepare(); if(P.from && P.to) run();
  }
  tw.onchange = whenChanged; ta.onchange = whenChanged;
  document.getElementById('trLoc').onclick = myLoc;
  document.getElementById('trSwap').onclick = function(){ var a = P.from, b = P.to; P.from = null; P.to = null; ['from', 'to'].forEach(function(w){ if(pins[w] && map){ map.removeLayer(pins[w]); pins[w] = null; } }); document.getElementById('trFrom').value = ''; document.getElementById('trTo').value = ''; if(b) setPoint('from', b); if(a) setPoint('to', a); };
  ensureLeaflet(initMap);
}
getJson('data/tashkent-transit.json').then(function(d){ T = d; G = prepare(); buildIdx(); view(); }).catch(function(e){ app.innerHTML = BACK + '<div class="v-hint">Could not load transit data. Check your connection.</div>'; });
