/* Stroke trainer for KanjiVG centre-line strokes (CC BY-SA 3.0, kanjivg.tagaini.net). Watch, guide arrows, trace with direction check. */
(function(){
var NS = 'http://www.w3.org/2000/svg';
function el(n, a, p){ var e = document.createElementNS(NS, n); for(var k in a) e.setAttribute(k, a[k]); if(p) p.appendChild(e); return e; }
function d2(a, b){ var x = a[0] - b[0], y = a[1] - b[1]; return Math.sqrt(x * x + y * y); }
function create(host, strokes, o){
  o = o || {}; var size = o.size || 260, say = o.say || function(){};
  host.innerHTML = '';
  var svg = el('svg', { viewBox: '0 0 109 109', width: size, height: size }, host);
  svg.style.cssText = 'touch-action:none;display:block;background:#fff;border-radius:10px;max-width:100%;';
  el('path', { d: 'M54.5 4v101M4 54.5h101', stroke: '#e3d9cb', 'stroke-width': .8, 'stroke-dasharray': '3 3', fill: 'none' }, svg);
  el('rect', { x: .5, y: .5, width: 108, height: 108, fill: 'none', stroke: '#d9cdbd', 'stroke-width': 1 }, svg);
  var ghost = el('g', { fill: 'none', stroke: '#e0e0e0', 'stroke-width': 4, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, svg);
  var guide = el('g', {}, svg), ink = el('g', { fill: 'none', stroke: '#2b2b2b', 'stroke-width': 4, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, svg);
  var live = el('g', { fill: 'none', stroke: '#85389F', 'stroke-width': 3.2, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, svg), mark = el('g', {}, svg);
  var info = strokes.map(function(d){
    var gp = el('path', { d: d }, ghost), len = gp.getTotalLength(), pts = [], i;
    for(i = 0; i <= 40; i++){ var q = gp.getPointAtLength(len * i / 40); pts.push([q.x, q.y]); }
    var a = gp.getPointAtLength(Math.max(0, len - 7)), e = gp.getPointAtLength(len);
    return { d: d, len: len, pts: pts, s: pts[0], e: pts[40], ang: Math.atan2(e.y - a.y, e.x - a.x) * 180 / Math.PI };
  });
  var timer = 0, run = 0, cur = 0, tracing = false, fails = 0, mistakes = 0, onDone = null;
  function stopAll(){ run++; tracing = false; cancelAnimationFrame(timer); }
  function clearLayers(){ ink.innerHTML = ''; live.innerHTML = ''; mark.innerHTML = ''; guide.innerHTML = ''; }
  function dot(g, i, hi){
    var s = info[i].s, c = el('circle', { cx: s[0], cy: s[1], r: 3.4, fill: hi ? '#d63a2f' : '#e8837a' }, g);
    var tx = Math.min(100, Math.max(9, s[0] - 7)), ty = Math.min(102, Math.max(9, s[1] - 5));
    var t = el('text', { x: tx, y: ty, 'font-size': 9, 'font-weight': 700, fill: '#d63a2f', 'text-anchor': 'middle', 'font-family': 'sans-serif' }, g); t.textContent = i + 1;
  }
  function arrow(g, i){
    var e = info[i].e; if(info[i].len < 9) return;
    el('path', { d: 'M-4.5 -3.6L1 0L-4.5 3.6z', fill: '#d63a2f', transform: 'translate(' + e[0] + ' ' + e[1] + ') rotate(' + info[i].ang + ')' }, g);
  }
  function showGuide(){ stopAll(); clearLayers(); info.forEach(function(x, i){ el('path', { d: x.d, stroke: '#cfcfcf', 'stroke-width': 3.5, fill: 'none', 'stroke-linecap': 'round' }, guide); });
    info.forEach(function(x, i){ arrow(guide, i); dot(guide, i, false); }); }
  function drawStroke(i, ms, cb, my){
    var p = el('path', { d: info[i].d }, ink), L = info[i].len; p.style.strokeDasharray = L + ' ' + (L + 2); p.style.strokeDashoffset = L;
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
    var S = info[i], dotS = S.len < 11, R = dotS ? 17 : 17;
    if(dotS) return d2(u[0], S.s) <= 20 || d2(u[u.length - 1], S.s) <= 20 ? 'ok' : 'far';
    if(u.length < 3) return 'short';
    var a = u[0], b = u[u.length - 1], ulen = 0, k, sum = 0;
    for(k = 1; k < u.length; k++) ulen += d2(u[k - 1], u[k]);
    if(ulen < S.len * 0.45) return 'short';
    if(d2(a, S.e) < R && d2(b, S.s) < R) return 'rev';
    if(d2(a, S.s) > R + 3) return 'start';
    if(d2(b, S.e) > R + 5) return 'end';
    for(k = 0; k < u.length; k++) sum += nearDist(u[k], S.pts);
    return sum / u.length <= 12 ? 'ok' : 'off';
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
      if(r === 'ok'){ var p = el('path', { d: info[cur].d }, ink); cur++; say(''); next(); }
      else { mistakes++; fails++; say(MSG[r] || 'Try again'); if(fails >= 2){ hint(cur); } } }
    svg.onpointerup = up; svg.onpointercancel = up;
    next();
  }
  function clear(){ stopAll(); clearLayers(); svg.onpointerdown = null; }
  return { watch: watch, guide: showGuide, trace: trace, clear: clear, stop: stopAll, count: info.length };
}
window.StrokeTrace = { create: create };
})();
