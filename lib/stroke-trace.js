/* Stroke trainer for KanjiVG centre-line strokes (CC BY-SA 3.0, kanjivg.tagaini.net). Watch, guide arrows, trace with direction check. */
(function(){
var NS = 'http://www.w3.org/2000/svg';
function el(n, a, p){ var e = document.createElementNS(NS, n); for(var k in a) e.setAttribute(k, a[k]); if(p) p.appendChild(e); return e; }
function d2(a, b){ var x = a[0] - b[0], y = a[1] - b[1]; return Math.sqrt(x * x + y * y); }
function create(host, strokes, o){
  o = o || {}; var VW = o.w || 109, VH = o.h || 109, tol = o.tol || 17, size = o.size || 260, say = o.say || function(){};
  host.innerHTML = '';
  var svg = el('svg', { viewBox: (o.vx || 0) + ' 0 ' + VW + ' ' + VH, width: size, height: Math.round(size * VH / VW) }, host);
  svg.style.cssText = 'touch-action:none;display:block;background:#fff;border-radius:10px;max-width:100%;';
  var bg = el('g', { transform: 'translate(' + (o.vx || 0) + ' 0)' }, svg);
  if(o.base){ el('path', { d: 'M0 ' + o.base + 'H' + VW, stroke: '#e3d9cb', 'stroke-width': .8, 'stroke-dasharray': '3 3', fill: 'none' }, bg); } else el('path', { d: 'M' + VW / 2 + ' 4v' + (VH - 8) + 'M4 ' + VH / 2 + 'h' + (VW - 8), stroke: '#e3d9cb', 'stroke-width': .8, 'stroke-dasharray': '3 3', fill: 'none' }, bg);
  el('rect', { x: .5, y: .5, width: VW - 1, height: VH - 1, fill: 'none', stroke: '#d9cdbd', 'stroke-width': 1 }, bg);
  var SW = o.sw || 4;
  var ghost = el('g', { fill: 'none', stroke: '#e0e0e0', 'stroke-width': SW, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, svg);
  var guide = el('g', {}, svg), ink = el('g', { fill: 'none', stroke: '#2b2b2b', 'stroke-width': SW, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, svg);
  var live = el('g', { fill: 'none', stroke: '#85389F', 'stroke-width': SW * .8, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, svg), mark = el('g', {}, svg);
  var info = strokes.map(function(d){
    var gp = el('path', { d: d }, ghost), len = gp.getTotalLength(), pts = [], i;
    if(len < 1) gp.setAttribute('stroke-width', SW * 1.8);
    for(i = 0; i <= 40; i++){ var q = gp.getPointAtLength(len * i / 40); pts.push([q.x, q.y]); }
    var a = gp.getPointAtLength(Math.max(0, len - 7)), e = gp.getPointAtLength(len);
    return { d: d, len: len, pts: pts, s: pts[0], e: pts[40], ang: Math.atan2(e.y - a.y, e.x - a.x) * 180 / Math.PI };
  });
  if(o.fit){
    var ymin = 1e9, ymax = -1e9; info.forEach(function(x){ x.pts.forEach(function(q){ if(q[1] < ymin) ymin = q[1]; if(q[1] > ymax) ymax = q[1]; }); });
    var by = o.base || 0; ymin = Math.max(0, Math.min(ymin, by) - 9); ymax = Math.min(VH, Math.max(ymax, by) + 9);
    var h2 = ymax - ymin, px = size; if(o.maxH && px * h2 / VW > o.maxH) px = Math.round(o.maxH * VW / h2);
    svg.setAttribute('viewBox', (o.vx || 0) + ' ' + ymin + ' ' + VW + ' ' + h2); svg.setAttribute('width', px); svg.setAttribute('height', Math.round(px * h2 / VW));
    bg.innerHTML = ''; bg.removeAttribute('transform');
    if(o.base) el('path', { d: 'M' + (o.vx || 0) + ' ' + o.base + 'H' + ((o.vx || 0) + VW), stroke: '#e3d9cb', 'stroke-width': .8, 'stroke-dasharray': '3 3', fill: 'none' }, bg);
    el('rect', { x: (o.vx || 0) + .5, y: ymin + .5, width: VW - 1, height: h2 - 1, fill: 'none', stroke: '#d9cdbd', 'stroke-width': 1 }, bg);
  }
  var timer = 0, run = 0, cur = 0, tracing = false, fails = 0, mistakes = 0, onDone = null;
  function stopAll(){ run++; tracing = false; cancelAnimationFrame(timer); }
  function clearLayers(){ ink.innerHTML = ''; live.innerHTML = ''; mark.innerHTML = ''; guide.innerHTML = ''; }
  function dot(g, i, hi){
    var s = info[i].s, c = el('circle', { cx: s[0], cy: s[1], r: o.dr || 3.4, fill: hi ? '#d63a2f' : '#e8837a' }, g);
    var tx = Math.min(VW - 9, Math.max(9, s[0] - 7)), ty = Math.min(VH - 7, Math.max(9, s[1] - 5));
    var t = el('text', { x: tx, y: ty, 'font-size': o.fs || 9, 'font-weight': 700, fill: '#d63a2f', 'text-anchor': 'middle', 'font-family': 'sans-serif' }, g); t.textContent = i + 1;
  }
  function arrow(g, i){
    var e = info[i].e; if(info[i].len < 9) return;
    el('path', { d: 'M-4.5 -3.6L1 0L-4.5 3.6z', fill: '#d63a2f', transform: 'translate(' + e[0] + ' ' + e[1] + ') rotate(' + info[i].ang + ')' }, g);
  }
  function showGuide(){ stopAll(); clearLayers(); info.forEach(function(x, i){ el('path', { d: x.d, stroke: '#cfcfcf', 'stroke-width': x.len < 1 ? SW * 1.8 : SW, fill: 'none', 'stroke-linecap': 'round' }, guide); });
    info.forEach(function(x, i){ arrow(guide, i); dot(guide, i, false); }); }
  function drawStroke(i, ms, cb, my){
    var p = el('path', { d: info[i].d }, ink), L = info[i].len; if(L < 1) p.setAttribute('stroke-width', SW * 1.8); p.style.strokeDasharray = L + ' ' + (L + 2); p.style.strokeDashoffset = L;
    var t0 = 0;
    function step(t){ if(my !== run) return; if(!t0) t0 = t; var f = Math.min(1, (t - t0) / ms); p.style.strokeDashoffset = L * (1 - f); if(f < 1) timer = requestAnimationFrame(step); else { p.style.strokeDasharray = ''; cb && cb(); } }
    timer = requestAnimationFrame(step);
  }
  function watch(cb, perStroke){
    stopAll(); clearLayers(); var my = run; svg.onpointerdown = null;
    (function go(i){ if(my !== run) return;
      if(i >= info.length){ mark.innerHTML = ''; cb && cb(); return; }
      mark.innerHTML = ''; dot(mark, i, true); arrow(mark, i); perStroke && perStroke(i);
      setTimeout(function(){ if(my !== run) return; drawStroke(i, 500 + info[i].len * 12, function(){ setTimeout(function(){ go(i + 1); }, 220); }, my); }, 380);
    })(0);
  }
  function hint(i){ mark.innerHTML = ''; var my = run; var h = el('path', { d: info[i].d, fill: 'none', stroke: '#d63a2f', 'stroke-width': 4, 'stroke-linecap': 'round', opacity: .55 }, mark), L = info[i].len; h.style.strokeDasharray = L + ' ' + (L + 2); h.style.strokeDashoffset = L; var t0 = 0;
    (function step(t){ if(my !== run || !tracing) return; if(!t0) t0 = t; var f = Math.min(1, (t - t0) / (600 + L * 10)); h.style.strokeDashoffset = L * (1 - f); if(f < 1) timer = requestAnimationFrame(step); })(performance.now()); dot(mark, i, true); arrow(mark, i); }
  function pt(e){ var m = svg.getScreenCTM().inverse(), p = svg.createSVGPoint(); p.x = e.clientX; p.y = e.clientY; p = p.matrixTransform(m); return [p.x, p.y]; }
  function nearDist(p, pts){ var m = 1e9, i; for(i = 0; i < pts.length; i++){ var d = d2(p, pts[i]); if(d < m) m = d; } return m; }
  function judge(u, i){
    var S = info[i], dotS = S.len < 11, R = tol;
    if(dotS) return d2(u[0], S.s) <= tol * 1.4 || d2(u[u.length - 1], S.s) <= tol * 1.4 ? 'ok' : 'far';
    if(u.length < 3) return 'short';
    var a = u[0], b = u[u.length - 1], ulen = 0, k, sum = 0;
    for(k = 1; k < u.length; k++) ulen += d2(u[k - 1], u[k]);
    if(ulen < S.len * 0.45) return 'short';
    if(d2(S.s, S.e) > R * 1.5 && d2(a, S.e) < R && d2(b, S.s) < R) return 'rev';
    if(d2(a, S.s) > R + 3) return 'start';
    if(d2(b, S.e) > R + 5) return 'end';
    for(k = 0; k < u.length; k++) sum += nearDist(u[k], S.pts);
    return sum / u.length <= tol * .7 ? 'ok' : 'off';
  }
  var MSG = { short: 'Longer', far: 'Tap the red dot', rev: 'Wrong direction. Start at the red dot', start: 'Start at the red dot', end: 'Go to the arrow', off: 'Follow the line' };
  function next(){
    mark.innerHTML = ''; fails = 0;
    if(cur >= info.length){ tracing = false; svg.onpointerdown = null; onDone && onDone(mistakes); return; }
    dot(mark, cur, true); arrow(mark, cur);
  }
  function trace(cb){
    stopAll(); clearLayers(); tracing = true; cur = 0; mistakes = 0; onDone = cb; var drawing = null, u = [], pl = null;
    el('g', {}, guide); info.forEach(function(x){ });
    svg.onpointerdown = function(e){ if(!tracing) return; e.preventDefault(); try{ svg.setPointerCapture(e.pointerId); }catch(x){} drawing = e.pointerId; u = [pt(e)]; live.innerHTML = ''; pl = el('polyline', { points: u[0].join(','), fill: 'none' }, live); };
    svg.onpointermove = function(e){ if(drawing !== e.pointerId) return; var p = pt(e); u.push(p); pl.setAttribute('points', pl.getAttribute('points') + ' ' + p.join(',')); };
    function up(e){ if(drawing !== e.pointerId) return; drawing = null; var r = judge(u, cur); live.innerHTML = '';
      if(r === 'ok'){ var p = el('path', { d: info[cur].d }, ink); if(info[cur].len < 1) p.setAttribute('stroke-width', SW * 1.8); cur++; say(''); next(); }
      else { mistakes++; fails++; say(MSG[r] || 'Try again'); if(fails >= 2){ hint(cur); } } }
    svg.onpointerup = up; svg.onpointercancel = up;
    next();
  }
  function clear(){ stopAll(); clearLayers(); svg.onpointerdown = null; }
  return { watch: watch, guide: showGuide, trace: trace, clear: clear, stop: stopAll, count: info.length };
}
window.StrokeTrace = { create: create };
})();
