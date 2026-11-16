/* Whiteboard for Mr Eric's Lounge.
   Vector ink on canvas. Strokes are objects (so undo, redo and the eraser are instant and exact), the live stroke is drawn
   on its own canvas every frame (coalesced + predicted points), committed ink is drawn once. Autosaves to IndexedDB. */
(function(){
'use strict';
var $ = function(id){ return document.getElementById(id); };
var stage = $('stage'), cv = $('c'), live = $('live'), tb = $('tb'), pop = $('pop'), ring = $('ring'), toastEl = $('toast');
var ctx = cv.getContext('2d', { alpha:false });
var lctx = live.getContext('2d', { desynchronized:true });
var tail = document.createElement('canvas'); tail.id = 'tail'; stage.appendChild(tail);
var tctx = tail.getContext('2d', { desynchronized:true });
var finI = 0, tailBox = null, lastInkEv = null, inkPresenter = null;
var dpr = 1, W = 0, H = 0;

/* ---------- icons ---------- */
var I = {
  pen:'<path d="M4 20l1-4L16.5 4.5a2.1 2.1 0 013 3L8 19l-4 1z"/><path d="M14.5 6.5l3 3"/>',
  hl:'<path d="M9 3l6 6-7 7H4v-4z"/><path d="M12.5 5.5l6 6"/><path d="M3 21h18" stroke-width="3" opacity=".5"/>',
  eraser:'<path d="M8 20h11"/><path d="M5 14l8-9a2 2 0 013 0l3 3a2 2 0 010 3l-7 7H8l-3-3a2 2 0 010-1z"/><path d="M9 9l6 6"/>',
  select:'<path d="M5 3l5 15 2.5-6 6-2.5z"/><path d="M13 13l6 6"/>',
  hand:'<path d="M8 12V6a1.5 1.5 0 013 0v5V4.5a1.5 1.5 0 013 0V11V6a1.5 1.5 0 013 0v8a6 6 0 01-6 6h-1a6 6 0 01-4.6-2.2L4 14a1.6 1.6 0 012.4-2.1L8 14"/>',
  shapes:'<rect x="3" y="11" width="10" height="9" rx="1"/><circle cx="16" cy="8" r="5"/>',
  image:'<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-8 9"/>',
  undo:'<path d="M9 14L4 9l5-5"/><path d="M4 9h10a6 6 0 010 12h-3"/>',
  redo:'<path d="M15 14l5-5-5-5"/><path d="M20 9H10a6 6 0 000 12h3"/>',
  pages:'<rect x="6" y="3" width="14" height="14" rx="2"/><path d="M3 7v12a2 2 0 002 2h12"/>',
  plus:'<path d="M12 5v14M5 12h14"/>',
  curtain:'<path d="M3 4h18"/><path d="M5 4c0 6-1 10-2 16h8c-1-6-2-10-2-16"/><path d="M13 4c0 6-1 10-2 16h10c-1-6-2-10-2-16"/>',
  bg:'<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18"/>',
  save:'<path d="M12 4v11"/><path d="M7 11l5 5 5-5"/><path d="M4 20h16"/>',
  boards:'<path d="M4 6h16M4 12h16M4 18h16"/>',
  full:'<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>',
  collapse:'<path d="M7 10l5 5 5-5"/>',
  grip:'<circle cx="8" cy="8" r="1.4"/><circle cx="16" cy="8" r="1.4"/><circle cx="8" cy="12" r="1.4"/><circle cx="16" cy="12" r="1.4"/><circle cx="8" cy="16" r="1.4"/><circle cx="16" cy="16" r="1.4"/>',
  trash:'<path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/>',
  copy:'<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V6a2 2 0 00-2-2H6a2 2 0 00-2 2v8a2 2 0 002 2h2"/>',
  left:'<path d="M15 6l-6 6 6 6"/>', right:'<path d="M9 6l6 6-6 6"/>',
  grab:'<path d="M5 9h14M5 15h14"/>',
  up:'<path d="M12 4v16M6 10l6-6 6 6"/>',
  line:'<path d="M5 19L19 5"/>', arrow:'<path d="M5 19L19 5M10 5h9v9"/>', rect:'<rect x="4" y="6" width="16" height="12" rx="1"/>',
  ellipse:'<ellipse cx="12" cy="12" rx="9" ry="6.5"/>', tri:'<path d="M12 4l9 16H3z"/>'
};
function ic(n){ return '<svg viewBox="0 0 24 24">' + (I[n] || '') + '</svg>'; }

/* ---------- state ---------- */
var COLORS = ['#111111', '#FFFFFF', '#E53935', '#1E66F5', '#2E9E4F', '#F5C400', '#F57C00', '#8E44AD'];
var QUICK = ['#111111', '#FFFFFF', '#E53935', '#1E66F5', '#2E9E4F'];
var BGS = [
  ['white', 'White'], ['black', 'Black'], ['green', 'Green board'], ['teal', 'Blue grid'], ['grid', 'Grid'], ['dots', 'Dots'], ['ruled', 'Ruled'], ['four', 'Handwriting lines']
];
var DARKBG = { black:1, green:1, teal:1 };
var uidN = 0; function uid(){ return Date.now().toString(36) + (uidN++).toString(36) + Math.floor(Math.random() * 1e5).toString(36); }
var S = {
  tool:'pen', color:'#111111', w:4, hlOn:false, eraser:'stroke', esize:36, shape:'line', dock:'b', left:false, collapsed:false,
  board:null
};
try{ var sv = JSON.parse(localStorage.getItem('boardPrefs') || '{}'); ['color','w','eraser','esize','shape','dock','left','ink','dc','sharp','dcv'].forEach(function(k){ if(sv[k] !== undefined) S[k] = sv[k]; }); }catch(e){}
if(['b','l','r'].indexOf(S.dock) < 0) S.dock = 'b';
if(S.ink === undefined) S.ink = true;
if(!(S.dc >= 1 && S.dc <= 2.5) || S.dcv !== 2){ S.dc = 1.5; S.dcv = 2; }   /* v2: earlier builds mistook a 30 Hz screen for a slow page */
      /* resolution cap: big panels at 250% scaling paint millions of pixels per frame */
function savePrefs(){ try{ localStorage.setItem('boardPrefs', JSON.stringify({ color:S.color, w:S.w, eraser:S.eraser, esize:S.esize, shape:S.shape, dock:S.dock, left:S.left, ink:S.ink, dc:S.dc, sharp:S.sharp, dcv:S.dcv })); }catch(e){} }

function newPage(bg){ return { id:uid(), bg:bg || 'white', items:[], undo:[], redo:[], view:{ x:0, y:0, s:1 } }; }
function newBoard(name){ var p = newPage('white'); return { id:uid(), name:name || 'Board', created:Date.now(), updated:Date.now(), pages:[p], cur:0 }; }
function page(){ return S.board.pages[S.board.cur]; }
function view(){ return page().view; }

/* ---------- storage (IndexedDB) ---------- */
var db = null, saveTimer = 0, dirtyFlag = false, canSave = true;
function openDb(){
  return new Promise(function(res){
    try{
      var r = indexedDB.open('loungeBoard', 1);
      r.onupgradeneeded = function(){ r.result.createObjectStore('boards', { keyPath:'id' }); };
      r.onsuccess = function(){ db = r.result; res(db); };
      r.onerror = function(){ canSave = false; res(null); };
    }catch(e){ canSave = false; res(null); }
  });
}
function strip(o){ var r = {}; for(var k in o){ if(k.charAt(0) !== '_' && k !== 'undo' && k !== 'redo') r[k] = o[k]; } return r; }
/* shallow copies only: IndexedDB clones the rest natively (the old JSON round trip stalled the main thread on big boards) */
function ser(b){ var r = strip(b); r.pages = b.pages.map(function(pg){ var q = strip(pg); q.items = pg.items.map(strip); return q; }); return r; }
function dbPut(b){
  return new Promise(function(res){
    if(!db){ res(false); return; }
    try{ var tx = db.transaction('boards', 'readwrite'); tx.objectStore('boards').put(ser(b)); tx.oncomplete = function(){ res(true); }; tx.onerror = tx.onabort = function(){ res(false); }; }catch(e){ res(false); }
  });
}
function dbGet(id){ return new Promise(function(res){ if(!db){ res(null); return; } try{ var r = db.transaction('boards').objectStore('boards').get(id); r.onsuccess = function(){ res(r.result || null); }; r.onerror = function(){ res(null); }; }catch(e){ res(null); } }); }
function dbAll(){ return new Promise(function(res){ if(!db){ res([]); return; } try{ var r = db.transaction('boards').objectStore('boards').getAll(); r.onsuccess = function(){ res(r.result || []); }; r.onerror = function(){ res([]); }; }catch(e){ res([]); } }); }
function dbDel(id){ return new Promise(function(res){ if(!db){ res(); return; } try{ var tx = db.transaction('boards', 'readwrite'); tx.objectStore('boards').delete(id); tx.oncomplete = tx.onerror = function(){ res(); }; }catch(e){ res(); } }); }
function markDirty(){
  dirtyFlag = true; S.board.updated = Date.now();
  clearTimeout(saveTimer); saveTimer = setTimeout(flushSave, 900);
}
function flushSave(){
  if(!dirtyFlag) return;
  if(cur || eras || Object.keys(ptrs).length){ clearTimeout(saveTimer); saveTimer = setTimeout(flushSave, 500); return; }   /* never save while a finger or pen is down */
  dirtyFlag = false; clearTimeout(saveTimer);
  var b = S.board; saveState('Saving');
  dbPut(b).then(function(ok){ saveState(ok ? 'Saved' : 'Not saved'); });
  try{ localStorage.setItem('boardLast', b.id); }catch(e){}
}
var saveStateTimer = 0;
function saveState(t){ var el = $('savestate'); el.textContent = t; el.classList.add('show'); clearTimeout(saveStateTimer); saveStateTimer = setTimeout(function(){ el.classList.remove('show'); }, t === 'Not saved' ? 4000 : 1200); }
window.addEventListener('pagehide', flushSave);
document.addEventListener('visibilitychange', function(){ if(document.hidden) flushSave(); });

function toast(t){ toastEl.textContent = t; toastEl.style.display = 'block'; clearTimeout(toast._t); toast._t = setTimeout(function(){ toastEl.style.display = 'none'; }, 1800); }

/* ---------- geometry helpers ---------- */
function bbox(it){
  if(it._bb) return it._bb;
  var b;
  if(it.type === 'pen'){
    var a = it.pts, x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    for(var i = 0; i < a.length; i += 2){ if(a[i] < x0) x0 = a[i]; if(a[i] > x1) x1 = a[i]; if(a[i + 1] < y0) y0 = a[i + 1]; if(a[i + 1] > y1) y1 = a[i + 1]; }
    var r = it.w / 2 + 1; b = [x0 - r, y0 - r, x1 + r, y1 + r];
  } else if(it.type === 'shape'){
    var r2 = it.w / 2 + 2 + (it.kind === 'arrow' ? it.w * 3 : 0);
    b = [Math.min(it.x1, it.x2) - r2, Math.min(it.y1, it.y2) - r2, Math.max(it.x1, it.x2) + r2, Math.max(it.y1, it.y2) + r2];
  } else b = [it.x, it.y, it.x + it.w, it.y + it.h];
  return (it._bb = b);
}
function segD2(px, py, ax, ay, bx, by){
  var dx = bx - ax, dy = by - ay, l = dx * dx + dy * dy, t = l ? ((px - ax) * dx + (py - ay) * dy) / l : 0;
  t = t < 0 ? 0 : t > 1 ? 1 : t; var cx = ax + t * dx - px, cy = ay + t * dy - py; return cx * cx + cy * cy;
}
function shapeSegs(it){
  var x1 = it.x1, y1 = it.y1, x2 = it.x2, y2 = it.y2, k = it.kind;
  if(k === 'line' || k === 'arrow') return [[x1, y1, x2, y2]];
  if(k === 'rect') return [[x1, y1, x2, y1], [x2, y1, x2, y2], [x2, y2, x1, y2], [x1, y2, x1, y1]];
  if(k === 'tri'){ var mx = (x1 + x2) / 2; return [[mx, y1, x2, y2], [x2, y2, x1, y2], [x1, y2, mx, y1]]; }
  var cx = (x1 + x2) / 2, cy = (y1 + y2) / 2, rx = Math.abs(x2 - x1) / 2, ry = Math.abs(y2 - y1) / 2, out = [], n = 28, px = cx + rx, py = cy;
  for(var i = 1; i <= n; i++){ var a = i / n * Math.PI * 2, qx = cx + Math.cos(a) * rx, qy = cy + Math.sin(a) * ry; out.push([px, py, qx, qy]); px = qx; py = qy; }
  return out;
}
function hitItem(it, x, y, r){
  var b = bbox(it); if(x < b[0] - r || x > b[2] + r || y < b[1] - r || y > b[3] + r) return false;
  if(it.type === 'img') return x >= b[0] && x <= b[2] && y >= b[1] && y <= b[3];
  var rr = r + it.w / 2;
  if(it.type === 'shape'){ var sg = shapeSegs(it); for(var i = 0; i < sg.length; i++){ if(segD2(x, y, sg[i][0], sg[i][1], sg[i][2], sg[i][3]) <= rr * rr) return true; } return false; }
  var a = it.pts, n = a.length;
  if(n === 2) return (a[0] - x) * (a[0] - x) + (a[1] - y) * (a[1] - y) <= rr * rr;
  for(var j = 0; j < n - 2; j += 2){ if(segD2(x, y, a[j], a[j + 1], a[j + 2], a[j + 3]) <= rr * rr) return true; }
  return false;
}
function cloneItem(it){
  var c = {}; for(var k in it){ if(k.charAt(0) !== '_') c[k] = it[k]; }
  if(it.pts) c.pts = it.pts.slice();
  c._img = it._img; return c;
}
function toWorld(sx, sy){ var v = view(); return [(sx - v.x) / v.s, (sy - v.y) / v.s]; }

/* ---------- drawing ---------- */
function penPath(it){
  if(it._p) return it._p;
  var p = new Path2D(), a = it.pts, n = a.length / 2;
  if(n === 1){ p.moveTo(a[0] + it.w / 2, a[1]); p.arc(a[0], a[1], it.w / 2, 0, 6.2832); }
  else {
    p.moveTo(a[0], a[1]);
    if(n === 2) p.lineTo(a[2], a[3]);
    else { for(var i = 1; i < n - 1; i++){ p.quadraticCurveTo(a[2 * i], a[2 * i + 1], (a[2 * i] + a[2 * i + 2]) / 2, (a[2 * i + 1] + a[2 * i + 3]) / 2); } p.lineTo(a[2 * n - 2], a[2 * n - 1]); }
  }
  return (it._p = p);
}
function drawShape(c, it){
  c.lineWidth = it.w; c.strokeStyle = it.color; c.lineCap = 'round'; c.lineJoin = 'round';
  var x1 = it.x1, y1 = it.y1, x2 = it.x2, y2 = it.y2;
  c.beginPath();
  if(it.kind === 'line' || it.kind === 'arrow'){
    c.moveTo(x1, y1); c.lineTo(x2, y2);
    if(it.kind === 'arrow'){
      var ang = Math.atan2(y2 - y1, x2 - x1), hl = Math.max(14, it.w * 4);
      c.moveTo(x2, y2); c.lineTo(x2 - hl * Math.cos(ang - 0.45), y2 - hl * Math.sin(ang - 0.45));
      c.moveTo(x2, y2); c.lineTo(x2 - hl * Math.cos(ang + 0.45), y2 - hl * Math.sin(ang + 0.45));
    }
  } else if(it.kind === 'rect') c.rect(Math.min(x1, x2), Math.min(y1, y2), Math.abs(x2 - x1), Math.abs(y2 - y1));
  else if(it.kind === 'ellipse') c.ellipse((x1 + x2) / 2, (y1 + y2) / 2, Math.abs(x2 - x1) / 2, Math.abs(y2 - y1) / 2, 0, 0, 6.2832);
  else if(it.kind === 'tri'){ c.moveTo((x1 + x2) / 2, y1); c.lineTo(x2, y2); c.lineTo(x1, y2); c.closePath(); }
  c.stroke();
}
function drawItem(c, it){
  if(it.type === 'pen'){
    var p = penPath(it);
    if(it.hl){ c.globalAlpha = 0.38; c.lineCap = 'butt'; } else c.lineCap = 'round';
    c.lineJoin = 'round'; c.lineWidth = it.w; c.strokeStyle = it.color; c.fillStyle = it.color;
    if(it.pts.length === 2) c.fill(p); else c.stroke(p);
    c.globalAlpha = 1;
  } else if(it.type === 'shape') drawShape(c, it);
  else if(it.type === 'img'){
    if(!it._img){ var im = new Image(); im.onload = function(){ it._ready = true; scheduleRender(); }; im.src = it.src; it._img = im; }
    if(it._img.complete && it._img.naturalWidth) c.drawImage(it._img, it.x, it.y, it.w, it.h);
  }
}
function drawBg(c, bg, v, w, h){
  c.fillStyle = bgFill(bg); c.fillRect(0, 0, w, h);
  var s = v.s;
  function lines(sp, col, lw, horiz, vert, dash){
    var step = sp * s; if(step < 7) return;
    c.strokeStyle = col; c.lineWidth = lw; c.beginPath();
    if(dash) c.setLineDash(dash);
    if(vert){ var x0 = ((v.x % step) + step) % step; for(var x = x0; x < w; x += step){ c.moveTo(Math.round(x) + .5, 0); c.lineTo(Math.round(x) + .5, h); } }
    if(horiz){ var y0 = ((v.y % step) + step) % step; for(var y = y0; y < h; y += step){ c.moveTo(0, Math.round(y) + .5); c.lineTo(w, Math.round(y) + .5); } }
    c.stroke(); c.setLineDash([]);
  }
  if(bg === 'grid') lines(40, 'rgba(60,110,200,.25)', 1, true, true);
  else if(bg === 'teal'){ lines(40, 'rgba(255,255,255,.28)', 1, true, true); lines(200, 'rgba(255,255,255,.18)', 2, true, true); }
  else if(bg === 'ruled'){ lines(56, 'rgba(60,110,200,.35)', 1.5, true, false); var mx = v.x + 90 * s; if(mx > 0 && mx < w){ c.strokeStyle = 'rgba(220,60,60,.5)'; c.lineWidth = 2; c.beginPath(); c.moveTo(mx, 0); c.lineTo(mx, h); c.stroke(); } }
  else if(bg === 'dots'){
    var st = 40 * s; if(st >= 9){ c.fillStyle = 'rgba(0,0,0,.35)'; var xa = ((v.x % st) + st) % st, ya = ((v.y % st) + st) % st; for(var y2 = ya; y2 < h; y2 += st) for(var x2 = xa; x2 < w; x2 += st) c.fillRect(Math.round(x2) - 1, Math.round(y2) - 1, 3, 3); }
  } else if(bg === 'four'){
    var gap = 28 * s, grp = 150 * s; if(gap >= 4){
      var y3 = ((v.y % grp) + grp) % grp - grp;
      for(var gy = y3; gy < h + grp; gy += grp){
        [[0, 'rgba(60,110,200,.55)', null], [1, 'rgba(220,60,60,.45)', [10, 8]], [2, 'rgba(60,110,200,.55)', null], [3, 'rgba(60,110,200,.55)', null]].forEach(function(L){
          var yy = Math.round(gy + L[0] * gap) + .5; c.strokeStyle = L[1]; c.lineWidth = 1.5; if(L[2]) c.setLineDash(L[2]); c.beginPath(); c.moveTo(0, yy); c.lineTo(w, yy); c.stroke(); c.setLineDash([]);
        });
      }
    }
  }
}
function paintPage(c, pg, w, h, v, skipBg){
  if(!skipBg) drawBg(c, pg.bg, v, w, h);
  c.save(); c.translate(v.x, v.y); c.scale(v.s, v.s);
  var vx0 = -v.x / v.s, vy0 = -v.y / v.s, vx1 = (w - v.x) / v.s, vy1 = (h - v.y) / v.s, it = pg.items;
  for(var i = 0; i < it.length; i++){ var b = bbox(it[i]); if(b[2] < vx0 || b[0] > vx1 || b[3] < vy0 || b[1] > vy1) continue; drawItem(c, it[i]); }
  c.restore();
}
var rafRender = 0;
function scheduleRender(){ if(rafRender) return; rafRender = requestAnimationFrame(function(){ rafRender = 0; render(); }); }
var snap = null, fastRaf = 0, fastT = 0;
function beginFast(){
  var c = document.createElement('canvas'); c.width = cv.width; c.height = cv.height; c.getContext('2d').drawImage(cv, 0, 0);
  var v = view(); snap = { c:c, x:v.x, y:v.y, s:v.s };
}
function fastRender(){
  if(!snap) return; var v = view(), k = v.s / snap.s;
  ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.fillStyle = bgFill(page().bg); ctx.fillRect(0, 0, cv.width, cv.height);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.translate(v.x - snap.x * k, v.y - snap.y * k); ctx.scale(k, k); ctx.drawImage(snap.c, 0, 0, W, H);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0); positionSel();
}
function fastSchedule(){
  if(!snap) beginFast();
  if(!fastRaf) fastRaf = requestAnimationFrame(function(){ fastRaf = 0; fastRender(); });
  clearTimeout(fastT); fastT = setTimeout(endFast, 140);
}
function endFast(){ clearTimeout(fastT); snap = null; if(fastRaf){ cancelAnimationFrame(fastRaf); fastRaf = 0; } render(); }
function bgFill(bg){ return bg === 'black' ? '#161616' : bg === 'green' ? '#2F5D50' : bg === 'teal' ? '#3F7F95' : '#FFFFFF'; }
function render(){
  if(!S.board) return; snap = null;
  var v = view(), pg = page();
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0); drawBg(ctx, pg.bg, v, W, H);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0); paintPage(ctx, pg, W, H, v, true);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0); positionSel();
}

function resize(){
  if(!S.board) return;
  dpr = Math.min(window.devicePixelRatio || 1, S.sharp ? 2.5 : S.dc); W = window.innerWidth; H = window.innerHeight;
  [cv, live, tail].forEach(function(c){ c.width = Math.round(W * dpr); c.height = Math.round(H * dpr); });
  render(); positionTb(); positionSel();
}
window.addEventListener('resize', function(){ resize(); });

/* ---------- history ---------- */
function snapshot(){ return page().items.slice(); }
function commitDiff(before){
  var pg = page(), after = pg.items, bs = new Set(before), as = new Set(after), rem = [], add = [];
  before.forEach(function(it, i){ if(!as.has(it)) rem.push({ it:it, i:i }); });
  after.forEach(function(it, i){ if(!bs.has(it)) add.push({ it:it, i:i }); });
  if(!rem.length && !add.length) return false;
  pg.undo.push({ rem:rem, add:add }); pg.redo.length = 0; markDirty(); updateUndo(); return true;
}
function applyUndo(a){
  var pg = page(), addSet = new Set(a.add.map(function(x){ return x.it; }));
  pg.items = pg.items.filter(function(it){ return !addSet.has(it); });
  a.rem.slice().sort(function(x, y){ return x.i - y.i; }).forEach(function(x){ pg.items.splice(Math.min(x.i, pg.items.length), 0, x.it); });
}
function applyRedo(a){
  var pg = page(), remSet = new Set(a.rem.map(function(x){ return x.it; }));
  pg.items = pg.items.filter(function(it){ return !remSet.has(it); });
  a.add.slice().sort(function(x, y){ return x.i - y.i; }).forEach(function(x){ pg.items.splice(Math.min(x.i, pg.items.length), 0, x.it); });
}
function undo(){ var pg = page(), a = pg.undo.pop(); if(!a) return; applyUndo(a); pg.redo.push(a); clearSel(); markDirty(); updateUndo(); render(); }
function redo(){ var pg = page(), a = pg.redo.pop(); if(!a) return; applyRedo(a); pg.undo.push(a); clearSel(); markDirty(); updateUndo(); render(); }
function updateUndo(){ var u = $('bUndo'), r = $('bRedo'); if(u) u.disabled = !page().undo.length; if(r) r.disabled = !page().redo.length; }

/* ---------- selection ---------- */
var sel = [];           // item objects
var selBox = $('sel'), selBar = $('selbar');
function clearSel(){ sel = []; positionSel(); }
function selBounds(){
  if(!sel.length) return null; var x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
  sel.forEach(function(it){ var b = bbox(it); x0 = Math.min(x0, b[0]); y0 = Math.min(y0, b[1]); x1 = Math.max(x1, b[2]); y1 = Math.max(y1, b[3]); });
  return [x0, y0, x1, y1];
}
function positionSel(){
  var b = (S.tool === 'select') ? selBounds() : null;
  if(!b){ selBox.style.display = 'none'; selBar.style.display = 'none'; return; }
  var v = view(), l = b[0] * v.s + v.x, t = b[1] * v.s + v.y, w = (b[2] - b[0]) * v.s, h = (b[3] - b[1]) * v.s;
  selBox.style.display = 'block'; selBox.style.left = l + 'px'; selBox.style.top = t + 'px'; selBox.style.width = w + 'px'; selBox.style.height = h + 'px';
  selBar.style.display = 'flex';
  var bw = selBar.offsetWidth || 170, bh = selBar.offsetHeight || 60;
  var bx = Math.max(8, Math.min(W - bw - 8, l + w / 2 - bw / 2)), by = t - bh - 22; if(by < 8) by = Math.min(H - bh - 8, t + h + 22);
  selBar.style.left = bx + 'px'; selBar.style.top = by + 'px';
}
selBar.innerHTML = '<button class="del" data-a="del" aria-label="Delete">' + ic('trash') + '</button><button data-a="dup" aria-label="Duplicate">' + ic('copy') + '</button><button data-a="front" aria-label="Bring to front">' + ic('up') + '</button>';
selBar.querySelector('svg') && selBar.querySelectorAll('svg').forEach(function(s){ s.style.cssText = 'width:26px;height:26px;stroke:currentColor;fill:none;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round'; });
selBar.addEventListener('pointerdown', function(e){ e.stopPropagation(); });
selBar.addEventListener('click', function(e){
  var b = e.target.closest('button'); if(!b || !sel.length) return; var a = b.dataset.a, pg = page(), before = snapshot();
  if(a === 'del'){ var ss = new Set(sel); pg.items = pg.items.filter(function(it){ return !ss.has(it); }); sel = []; }
  else if(a === 'dup'){ var copies = sel.map(function(it){ var c = cloneItem(it); c.id = uid(); shift(c, 30, 30); return c; }); pg.items = pg.items.concat(copies); sel = copies; }
  else if(a === 'front'){ var ss2 = new Set(sel); pg.items = pg.items.filter(function(it){ return !ss2.has(it); }).concat(sel); }
  commitDiff(before); render();
});
function shift(it, dx, dy){
  it._bb = null; it._p = null;
  if(it.type === 'pen') for(var i = 0; i < it.pts.length; i += 2){ it.pts[i] += dx; it.pts[i + 1] += dy; }
  else if(it.type === 'shape'){ it.x1 += dx; it.x2 += dx; it.y1 += dy; it.y2 += dy; } else { it.x += dx; it.y += dy; }
}
function xform(it, ox, oy, sx, sy, dx, dy){
  var c = cloneItem(it); c._bb = null;
  function fx(x){ return ox + (x - ox) * sx + dx; } function fy(y){ return oy + (y - oy) * sy + dy; }
  if(c.type === 'pen'){ for(var i = 0; i < c.pts.length; i += 2){ c.pts[i] = fx(c.pts[i]); c.pts[i + 1] = fy(c.pts[i + 1]); } c.w = it.w * Math.sqrt(Math.abs(sx * sy)); }
  else if(c.type === 'shape'){ c.x1 = fx(it.x1); c.x2 = fx(it.x2); c.y1 = fy(it.y1); c.y2 = fy(it.y2); c.w = it.w * Math.sqrt(Math.abs(sx * sy)); }
  else { var nx = fx(it.x), ny = fy(it.y), nx2 = fx(it.x + it.w), ny2 = fy(it.y + it.h); c.x = Math.min(nx, nx2); c.y = Math.min(ny, ny2); c.w = Math.abs(nx2 - nx); c.h = Math.abs(ny2 - ny); }
  return c;
}
/* transform session: moves or scales the selected items live, one history step at the end */
var tsess = null;
function startTransform(kind, handle, sx, sy){
  var b = selBounds(); if(!b) return;
  tsess = { kind:kind, handle:handle, b:b, before:snapshot(), orig:sel.slice(), sx:sx, sy:sy };
}
function moveTransform(sx, sy){
  if(!tsess) return; var v = view(), dx = (sx - tsess.sx) / v.s, dy = (sy - tsess.sy) / v.s, b = tsess.b, scx = 1, scy = 1, ox = b[0], oy = b[1], mx = 0, my = 0;
  if(tsess.kind === 'move'){ mx = dx; my = dy; }
  else {
    var wd = b[2] - b[0], ht = b[3] - b[1], h = tsess.handle, nw = wd, nh = ht;
    var fixX = (h === 'tl' || h === 'bl') ? b[2] : b[0], fixY = (h === 'tl' || h === 'tr') ? b[3] : b[1];
    var movX = (h === 'tl' || h === 'bl') ? b[0] + dx : b[2] + dx, movY = (h === 'tl' || h === 'tr') ? b[1] + dy : b[3] + dy;
    nw = Math.abs(movX - fixX); nh = Math.abs(movY - fixY);
    var k = Math.max(nw / wd, nh / ht, 0.05); scx = scy = k; ox = fixX; oy = fixY;
  }
  var pg = page(), map = new Map();
  tsess.orig.forEach(function(it){ map.set(it, xform(it, ox, oy, scx, scy, mx, my)); });
  pg.items = tsess.before.map(function(it){ return map.has(it) ? map.get(it) : it; });
  sel = tsess.orig.map(function(it){ return map.get(it); });
  render();
}
function endTransform(){
  if(!tsess) return; commitDiff(tsess.before); tsess = null; render();
}

/* ---------- erasing ---------- */
function densify(a, maxSeg){
  var out = [a[0], a[1]];
  for(var i = 2; i < a.length; i += 2){
    var dx = a[i] - a[i - 2], dy = a[i + 1] - a[i - 1], d = Math.sqrt(dx * dx + dy * dy), n = Math.ceil(d / maxSeg);
    for(var k = 1; k <= n; k++){ out.push(a[i - 2] + dx * k / n, a[i - 1] + dy * k / n); }
  }
  return out;
}
function eraseAt(x, y, r, mode){
  var pg = page(), items = pg.items, out = [], changed = false;
  for(var i = 0; i < items.length; i++){
    var it = items[i], b = bbox(it);
    if(x < b[0] - r || x > b[2] + r || y < b[1] - r || y > b[3] + r){ out.push(it); continue; }
    if(mode === 'stroke' || it.type !== 'pen'){
      if(it.type === 'img' && mode !== 'stroke'){ out.push(it); continue; }
      if(hitItem(it, x, y, mode === 'stroke' ? Math.min(r, 20 / view().s) : r)){ changed = true; continue; }
      out.push(it); continue;
    }
    /* area eraser on ink: cut the stroke where the circle passes */
    var rr = r + it.w / 2;
    if(!hitItem(it, x, y, r)){ out.push(it); continue; }
    changed = true;
    if(it.pts.length === 2) continue;
    var a = densify(it.pts, Math.max(1.5, r * 0.5)), run = [], pieces = [];
    for(var j = 0; j < a.length; j += 2){
      var dx = a[j] - x, dy = a[j + 1] - y;
      if(dx * dx + dy * dy <= rr * rr){ if(run.length >= 4) pieces.push(run); run = []; }
      else run.push(a[j], a[j + 1]);
    }
    if(run.length >= 4) pieces.push(run);
    pieces.forEach(function(pts){ var c = cloneItem(it); c.id = uid(); c.pts = pts; c._p = null; c._bb = null; out.push(c); });
  }
  if(changed){ pg.items = out; return true; }
  return false;
}
function eraseSeg(x0, y0, x1, y1, r, mode){
  var d = Math.hypot(x1 - x0, y1 - y0), step = Math.max(r * 0.6, 2), n = Math.max(1, Math.ceil(d / step)), any = false;
  for(var i = 1; i <= n; i++){ if(eraseAt(x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n, r, mode)) any = true; }
  return any;
}

/* ---------- pointer handling ---------- */
var ptrs = {};            // active pointers
var cur = null;           // current stroke / shape being drawn
var predicted = [];
var gest = null;          // pinch / pan
var eras = null;          // erase session
var lasso = null;
var lastPen = -1e9;
var spaceDown = false;
var holdTimer = 0, lastMoveT = 0;

function setTool(t){
  S.tool = t; if(t !== 'select') sel = [];
  if(t === 'hl'){ S.hlOn = true; } else if(t === 'pen'){ S.hlOn = false; }
  closePop(); buildTb(); positionSel(); updateCursor();
}
function updateCursor(){
  stage.style.cursor = S.tool === 'hand' ? 'grab' : S.tool === 'select' ? 'default' : S.tool === 'eraser' ? 'none' : 'crosshair';
}
function penWidth(){ return S.hlOn ? Math.max(S.w * 3.2, 16) : S.w; }
function eraserR(){ return S.esize / 2 / view().s; }

function startStroke(x, y){
  var it = { id:uid(), type:'pen', color:S.color, w:penWidth(), pts:[x, y] };
  if(S.hlOn) it.hl = 1;
  finI = 0; tailBox = null; lastInkEv = null; fN = 0; fSum = 0; fLast = 0;
  cur = it; lastMoveT = performance.now(); clearTimeout(holdTimer);
  if(!S.hlOn) holdTimer = setTimeout(straighten, 650);
  scheduleLive();
}
function straighten(){
  if(!cur || cur.type !== 'pen' || cur.pts.length < 6) return;
  var a = cur.pts, n = a.length, v = view(), x0 = a[0], y0 = a[1], x1 = a[n - 2], y1 = a[n - 1], L = Math.hypot(x1 - x0, y1 - y0), dev = 0;
  if(L * v.s < 40) return;
  for(var i = 2; i < n - 2; i += 2){ var d = Math.abs((x1 - x0) * (y0 - a[i + 1]) - (x0 - a[i]) * (y1 - y0)) / L; if(d > dev) dev = d; }
  if(dev > L * 0.12) return;
  cur = { id:cur.id, type:'shape', kind:'line', color:cur.color, w:cur.w, x1:a[0], y1:a[1], x2:a[n - 2], y2:a[n - 1], fromPen:1 };
  scheduleLive();
}
var liveRaf = 0;
function scheduleLive(){ if(liveRaf) return; liveRaf = requestAnimationFrame(drawLive); }
var fN = 0, fSum = 0, fLast = 0, refreshMs = 16.7;
(function measure(){ var n = 0, t0 = 0; function f(t){ if(!t0) t0 = t; if(++n < 40) requestAnimationFrame(f); else if(document.visibilityState === 'visible'){ var ms = (t - t0) / (n - 1); if(ms > 6 && ms < 80) refreshMs = ms; } } requestAnimationFrame(f); })();
function drawInk(v){
  var t0 = performance.now(); if(fLast && t0 - fLast < 200){ fN++; fSum += t0 - fLast; } fLast = t0;
  var a = cur.pts, n = a.length / 2, k = dpr * v.s, w = cur.w;
  /* 1. finished curve segments go onto the live canvas once and stay there */
  lctx.setTransform(k, 0, 0, k, dpr * v.x, dpr * v.y); lctx.lineCap = 'round'; lctx.lineJoin = 'round'; lctx.lineWidth = w; lctx.strokeStyle = cur.color;
  if(n >= 3 && finI < n - 2){
    lctx.beginPath();
    for(var i = finI + 1; i <= n - 2; i++){
      if(i === 1) lctx.moveTo(a[0], a[1]); else lctx.moveTo((a[2 * i - 2] + a[2 * i]) / 2, (a[2 * i - 1] + a[2 * i + 1]) / 2);
      lctx.quadraticCurveTo(a[2 * i], a[2 * i + 1], (a[2 * i] + a[2 * i + 2]) / 2, (a[2 * i + 1] + a[2 * i + 3]) / 2);
    }
    lctx.stroke(); finI = n - 2;
  }
  /* 2. the unfinished tip (last bit + predicted points) lives on its own canvas and only its small box is cleared and redrawn */
  var pad = dpr * (w * v.s / 2 + 3);
  if(tailBox){ tctx.setTransform(1, 0, 0, 1, 0, 0); tctx.clearRect(tailBox[0], tailBox[1], tailBox[2], tailBox[3]); tailBox = null; }
  var ex = n >= 3 ? (a[2 * n - 4] + a[2 * n - 2]) / 2 : a[0], ey = n >= 3 ? (a[2 * n - 3] + a[2 * n - 1]) / 2 : a[1];
  var xs = [ex, a[2 * n - 2]], ys = [ey, a[2 * n - 1]], pr = predicted;
  for(var j = 0; j < pr.length; j += 2){ xs.push(pr[j]); ys.push(pr[j + 1]); }
  tctx.setTransform(k, 0, 0, k, dpr * v.x, dpr * v.y); tctx.lineCap = 'round'; tctx.lineJoin = 'round'; tctx.lineWidth = w; tctx.strokeStyle = cur.color; tctx.fillStyle = cur.color;
  if(n === 1 && !pr.length){ tctx.beginPath(); tctx.arc(a[0], a[1], w / 2, 0, 6.2832); tctx.fill(); }
  else { tctx.beginPath(); tctx.moveTo(ex, ey); tctx.lineTo(a[2 * n - 2], a[2 * n - 1]); for(var m = 0; m < pr.length; m += 2) tctx.lineTo(pr[m], pr[m + 1]); tctx.stroke(); }
  var x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
  for(var q = 0; q < xs.length; q++){ var sx = dpr * (v.x + v.s * xs[q]), sy = dpr * (v.y + v.s * ys[q]); if(sx < x0) x0 = sx; if(sx > x1) x1 = sx; if(sy < y0) y0 = sy; if(sy > y1) y1 = sy; }
  tailBox = [Math.floor(x0 - pad), Math.floor(y0 - pad), Math.ceil(x1 - x0 + 2 * pad) + 1, Math.ceil(y1 - y0 + 2 * pad) + 1];
  /* 3. let the OS draw an ink trail from the last drawn point to the pen tip, until this frame reaches the screen */
  if(inkPresenter && S.ink && lastInkEv){ try{ inkPresenter.updateInkTrailStartPoint(lastInkEv, { color:cur.color, diameter:w * v.s }); }catch(er){ inkPresenter = null; } }
  perfNote(t0);
}
function drawLive(){
  liveRaf = 0;
  var v = view();
  if(cur && cur.type === 'pen' && !cur.hl){ drawInk(v); return; }
  if(tailBox){ tctx.setTransform(1, 0, 0, 1, 0, 0); tctx.clearRect(0, 0, tail.width, tail.height); tailBox = null; }
  lctx.setTransform(1, 0, 0, 1, 0, 0); lctx.clearRect(0, 0, live.width, live.height);
  lctx.setTransform(dpr * v.s, 0, 0, dpr * v.s, dpr * v.x, dpr * v.y);
  if(cur){
    if(cur.type === 'pen'){
      var tmp = cur;
      if(predicted.length && cur.pts.length >= 4){ tmp = { type:'pen', color:cur.color, w:cur.w, hl:cur.hl, pts:cur.pts.concat(predicted) }; }
      else tmp = { type:'pen', color:cur.color, w:cur.w, hl:cur.hl, pts:cur.pts };
      drawItem(lctx, tmp);
    } else if(cur.type === 'shape') drawItem(lctx, cur);
  }
  if(lasso){
    lctx.setTransform(dpr, 0, 0, dpr, 0, 0); lctx.strokeStyle = '#4DA3FF'; lctx.fillStyle = 'rgba(77,163,255,.12)'; lctx.lineWidth = 2.5; lctx.setLineDash([9, 7]);
    lctx.beginPath(); var p = lasso.pts; lctx.moveTo(p[0], p[1]); for(var i = 2; i < p.length; i += 2) lctx.lineTo(p[i], p[i + 1]); lctx.closePath(); lctx.fill(); lctx.stroke(); lctx.setLineDash([]);
  }
}
function clearLive(){ lctx.setTransform(1, 0, 0, 1, 0, 0); lctx.clearRect(0, 0, live.width, live.height); tctx.setTransform(1, 0, 0, 1, 0, 0); tctx.clearRect(0, 0, tail.width, tail.height); finI = 0; tailBox = null; }

function commitCur(){
  clearTimeout(holdTimer);
  if(!cur) return; var it = cur; cur = null; predicted = [];
  if(it.type === 'shape'){ var dd = Math.hypot(it.x2 - it.x1, it.y2 - it.y1); if(dd < 3 && !it.fromPen){ clearLive(); return; } }
  var pg = page(), before = snapshot();
  pg.items.push(it);
  /* paint it straight onto the committed canvas, no full redraw */
  var v = view(); ctx.setTransform(dpr * v.s, 0, 0, dpr * v.s, dpr * v.x, dpr * v.y); drawItem(ctx, it); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  if(it.type === 'pen' && !it.hl){ var tok = it; requestAnimationFrame(function(){ requestAnimationFrame(function(){ if(!cur) clearLive(); }); }); }
  else clearLive();
  commitDiff(before);
  adaptRes();
}
/* if strokes were drawn at under ~35 frames a second, drop the resolution one step (never goes up by itself) */
function adaptRes(){
  /* slow means well below what the screen itself can show (a 30 Hz panel is not slow) */
  if(S.sharp || fN < 15 || fSum / fN < Math.max(29, refreshMs * 1.6) || S.dc <= 1) return;
  S.dc = S.dc > 1.25 ? 1.25 : 1; fN = 0; fSum = 0; savePrefs();
  setTimeout(function(){ if(!cur && !Object.keys(ptrs).length){ resize(); toast('Faster drawing: sharpness lowered'); } }, 400);
}
function cancelCur(){ clearTimeout(holdTimer); cur = null; predicted = []; lasso = null; clearLive(); }

function pointInPoly(x, y, p){
  var inside = false;
  for(var i = 0, j = p.length - 2; i < p.length; j = i, i += 2){
    var xi = p[i], yi = p[i + 1], xj = p[j], yj = p[j + 1];
    if(((yi > y) !== (yj > y)) && (x < (xj - xi) * (y - yi) / (yj - yi) + xi)) inside = !inside;
  }
  return inside;
}
function lassoSelect(poly){
  var v = view(), res = [];
  page().items.forEach(function(it){
    var b = bbox(it), cx = (b[0] + b[2]) / 2 * v.s + v.x, cy = (b[1] + b[3]) / 2 * v.s + v.y;
    if(it.type === 'pen' && it.pts.length > 4){
      var a = it.pts, tot = 0, ins = 0; for(var i = 0; i < a.length; i += 2){ tot++; if(pointInPoly(a[i] * v.s + v.x, a[i + 1] * v.s + v.y, poly)) ins++; }
      if(ins / tot > 0.5) res.push(it);
    } else if(pointInPoly(cx, cy, poly)) res.push(it);
  });
  return res;
}
function pickAt(sx, sy){
  var w = toWorld(sx, sy), v = view(), r = 14 / v.s, it = page().items;
  for(var i = it.length - 1; i >= 0; i--){ if(hitItem(it[i], w[0], w[1], r)) return it[i]; }
  return null;
}
function selContains(sx, sy){
  var b = selBounds(); if(!b) return false; var v = view();
  return sx >= b[0] * v.s + v.x - 6 && sx <= b[2] * v.s + v.x + 6 && sy >= b[1] * v.s + v.y - 6 && sy <= b[3] * v.s + v.y + 6;
}

function touchCount(){ var n = 0; for(var k in ptrs){ if(ptrs[k].type === 'touch') n++; } return n; }
function startGesture(){
  var ids = Object.keys(ptrs).filter(function(k){ return ptrs[k].type === 'touch'; });
  if(ids.length < 2) return; var a = ptrs[ids[0]], b = ptrs[ids[1]], v = view();
  gest = { ids:[ids[0], ids[1]], d0:Math.hypot(a.x - b.x, a.y - b.y) || 1, cx0:(a.x + b.x) / 2, cy0:(a.y + b.y) / 2, v0:{ x:v.x, y:v.y, s:v.s } };
}
function updateGesture(){
  if(!gest) return; var a = ptrs[gest.ids[0]], b = ptrs[gest.ids[1]]; if(!a || !b) return;
  var d = Math.hypot(a.x - b.x, a.y - b.y) || 1, cx = (a.x + b.x) / 2, cy = (a.y + b.y) / 2, v = view();
  var ns = Math.min(8, Math.max(0.15, gest.v0.s * d / gest.d0)), k = ns / gest.v0.s;
  v.s = ns; v.x = cx - (gest.cx0 - gest.v0.x) * k; v.y = cy - (gest.cy0 - gest.v0.y) * k;
  fastSchedule();
}

stage.addEventListener('pointerdown', function(e){
  if(e.target.closest && e.target.closest('.h')) return;
  closePop(); e.preventDefault();
  var type = e.pointerType || 'mouse';
  if(type === 'mouse' && e.button !== 0 && e.button !== 1) return;
  ptrs[e.pointerId] = { x:e.clientX, y:e.clientY, type:type, t:performance.now() };
  try{ stage.setPointerCapture(e.pointerId); }catch(er){}
  if(type === 'pen') lastPen = performance.now();
  /* palm rejection: while a pen is in use, touches never draw */
  if(type === 'touch' && performance.now() - lastPen < 1500 && touchCount() < 2){ ptrs[e.pointerId].ignore = true; return; }
  /* two fingers: pinch and pan */
  if(type === 'touch' && touchCount() >= 2){ cancelCur(); if(eras){ endErase(); } if(tsess) endTransform(); startGesture(); return; }
  var big = type === 'touch' && Math.max(e.width || 0, e.height || 0) > 72;
  var penEraser = type === 'pen' && ((e.buttons & 32) || e.button === 5);
  var tool = S.tool;
  if(e.button === 1 || spaceDown || tool === 'hand'){ ptrs[e.pointerId].pan = { sx:e.clientX, sy:e.clientY, vx:view().x, vy:view().y }; stage.style.cursor = 'grabbing'; return; }
  if(big || penEraser) tool = 'eraser-area';
  var w = toWorld(e.clientX, e.clientY);
  if(tool === 'pen' || tool === 'hl'){ startStroke(w[0], w[1]); }
  else if(tool === 'shape'){ cur = { id:uid(), type:'shape', kind:S.shape, color:S.color, w:S.w, x1:w[0], y1:w[1], x2:w[0], y2:w[1] }; }
  else if(tool === 'eraser' || tool === 'eraser-area'){
    var mode = tool === 'eraser-area' ? 'area' : S.eraser, r = tool === 'eraser-area' ? Math.max(44, (Math.max(e.width || 0, e.height || 0) || 80) * 0.8) / 2 / view().s : eraserR();
    eras = { before:snapshot(), lx:w[0], ly:w[1], mode:mode, r:r, any:false, id:e.pointerId, fist:tool === 'eraser-area' };
    if(eraseAt(w[0], w[1], r, mode)){ eras.any = true; render(); }
    showRing(e.clientX, e.clientY, r * view().s * 2);
  } else if(tool === 'select'){
    if(sel.length && selContains(e.clientX, e.clientY)){ startTransform('move', null, e.clientX, e.clientY); ptrs[e.pointerId].moveSel = true; }
    else {
      var hit = pickAt(e.clientX, e.clientY);
      if(hit){ sel = [hit]; positionSel(); startTransform('move', null, e.clientX, e.clientY); ptrs[e.pointerId].moveSel = true; }
      else { sel = []; positionSel(); lasso = { pts:[e.clientX, e.clientY] }; scheduleLive(); }
    }
  }
}, { passive:false });

function onMove(e){
  var p = ptrs[e.pointerId]; if(!p) { if(e.pointerType === 'mouse' && S.tool === 'eraser') showRing(e.clientX, e.clientY, S.esize); return; }
  if(p.ignore) return;
  if(gest && (e.pointerId + '' === gest.ids[0] || e.pointerId + '' === gest.ids[1])){ p.x = e.clientX; p.y = e.clientY; updateGesture(); return; }
  p.x = e.clientX; p.y = e.clientY;
  if(p.pan){ var v = view(); v.x = p.pan.vx + (e.clientX - p.pan.sx); v.y = p.pan.vy + (e.clientY - p.pan.sy); fastSchedule(); return; }
  if(p.moveSel){ moveTransform(e.clientX, e.clientY); return; }
  var evs = (e.getCoalescedEvents && e.getCoalescedEvents()) || [];
  if(!evs.length) evs = [e];
  var v2 = view();
  if(cur && cur.type === 'pen'){
    var a = cur.pts, minD = 0.9 / v2.s;
    for(var i = 0; i < evs.length; i++){
      var w = toWorld(evs[i].clientX, evs[i].clientY), lx = a[a.length - 2], ly = a[a.length - 1];
      if(PERF) pf.ev++;
      if(Math.abs(w[0] - lx) + Math.abs(w[1] - ly) >= minD){ a.push(w[0], w[1]); cur._p = null; lastMoveT = performance.now(); }
    }
    predicted = []; lastInkEv = e; lastEvT = e.timeStamp;
    if(e.getPredictedEvents){ var pe = e.getPredictedEvents(); for(var k = 0; k < Math.min(pe.length, 3); k++){ var pw = toWorld(pe[k].clientX, pe[k].clientY); predicted.push(pw[0], pw[1]); } }
    clearTimeout(holdTimer); if(!S.hlOn) holdTimer = setTimeout(straighten, 650);
    scheduleLive();
  } else if(cur && cur.type === 'shape'){
    var w2 = toWorld(e.clientX, e.clientY);
    if(cur.fromPen){ cur.x2 = w2[0]; cur.y2 = w2[1]; }
    else { cur.x2 = w2[0]; cur.y2 = w2[1]; }
    if(e.shiftKey && (cur.kind === 'line' || cur.kind === 'arrow')){ var ang = Math.round(Math.atan2(cur.y2 - cur.y1, cur.x2 - cur.x1) / (Math.PI / 12)) * (Math.PI / 12), dd = Math.hypot(cur.x2 - cur.x1, cur.y2 - cur.y1); cur.x2 = cur.x1 + Math.cos(ang) * dd; cur.y2 = cur.y1 + Math.sin(ang) * dd; }
    if(e.shiftKey && (cur.kind === 'rect' || cur.kind === 'ellipse')){ var m = Math.max(Math.abs(cur.x2 - cur.x1), Math.abs(cur.y2 - cur.y1)); cur.x2 = cur.x1 + (cur.x2 >= cur.x1 ? m : -m); cur.y2 = cur.y1 + (cur.y2 >= cur.y1 ? m : -m); }
    cur._bb = null; scheduleLive();
  } else if(eras && eras.id === e.pointerId){
    for(var j = 0; j < evs.length; j++){
      var w3 = toWorld(evs[j].clientX, evs[j].clientY);
      if(eraseSeg(eras.lx, eras.ly, w3[0], w3[1], eras.r, eras.mode)) eras.any = true;
      eras.lx = w3[0]; eras.ly = w3[1];
    }
    if(eras.any) scheduleRender(); showRing(e.clientX, e.clientY, eras.r * view().s * 2);
  } else if(lasso){ lasso.pts.push(e.clientX, e.clientY); scheduleLive(); }
}
stage.addEventListener('pointermove', onMove);
/* ---------- low-latency ink (Chrome on Windows/ChromeOS) and the ?perf=1 overlay ---------- */
var lastEvT = 0, PERF = /[?&]perf=1/.test(location.search) || (function(){ try{ return localStorage.getItem('boardPerf') === '1'; }catch(e){ return false; } })(), pf = { n:0, ms:0, mx:0, lag:0, lagMx:0, ev:0, t:performance.now() }, pfEl = null;
try{ if(navigator.ink && navigator.ink.requestPresenter && !/[?&]ink=0/.test(location.search)) navigator.ink.requestPresenter({ presentationArea:stage }).then(function(pr){ inkPresenter = pr; }).catch(function(){}); }catch(er){}
var hz = 0, hzN = 0, hzT = 0, hzRun = false;
function hzStart(){
  if(hzRun || !PERF) return; hzRun = true; hzN = 0; hzT = 0;
  (function loop(){ if(!PERF){ hzRun = false; return; } requestAnimationFrame(function(t){ if(!hzT) hzT = t; hzN++; if(t - hzT >= 1000){ hz = Math.round(hzN * 1000 / (t - hzT)); hzN = 0; hzT = t; } loop(); }); })();
}
hzStart();
function perfNote(t0){
  if(!PERF) return;
  var now = performance.now(), d = now - t0, lag = lastEvT ? now - lastEvT : 0;
  pf.n++; pf.ms += d; if(d > pf.mx) pf.mx = d; pf.lag += lag; if(lag > pf.lagMx) pf.lagMx = lag;
  if(!pfEl){ pfEl = document.createElement('div'); pfEl.style.cssText = 'position:fixed;z-index:99;left:50%;top:8px;transform:translateX(-50%);background:rgba(0,0,0,.75);color:#9f9;font:13px/1.35 monospace;padding:6px 10px;border-radius:8px;pointer-events:none;white-space:pre'; document.body.appendChild(pfEl); }
  if(now - pf.t > 500){
    pfEl.textContent = 'frames ' + Math.round(pf.n * 1000 / (now - pf.t)) + '/s   input pts ' + Math.round(pf.ev * 1000 / (now - pf.t)) + '/s\ndraw avg ' + (pf.ms / pf.n).toFixed(2) + ' ms  max ' + pf.mx.toFixed(1) + '\ninput to draw avg ' + (pf.lag / pf.n).toFixed(1) + ' ms  max ' + pf.lagMx.toFixed(0) + '\ndisplay refresh ' + (hz || '...') + ' Hz\nink trail ' + (inkPresenter && S.ink ? 'on' : (inkPresenter ? 'off (setting)' : 'not supported')) + '   dpr ' + dpr + '  ' + live.width + 'x' + live.height;
    pf.n = 0; pf.ms = 0; pf.mx = 0; pf.lag = 0; pf.lagMx = 0; pf.ev = 0; pf.t = now;
  }
}
stage.addEventListener('pointerrawupdate', function(e){ /* extra input rate where supported: handled through coalesced events */ });

function endErase(){
  if(!eras) return; var s = eras; eras = null; hideRing();
  if(s.any){ commitDiff(s.before); render(); }
}
function onUp(e){
  var p = ptrs[e.pointerId]; delete ptrs[e.pointerId];
  try{ stage.releasePointerCapture(e.pointerId); }catch(er){}
  if(!p) return;
  if(p.ignore) return;
  if(gest && (e.pointerId + '' === gest.ids[0] || e.pointerId + '' === gest.ids[1])){ gest = null; endFast(); /* remaining finger must not start drawing */ var rest = Object.keys(ptrs); rest.forEach(function(k){ ptrs[k].ignore = true; }); return; }
  if(p.pan){ updateCursor(); endFast(); return; }
  if(p.moveSel){ endTransform(); return; }
  if(cur){ if(e.type === 'pointercancel'){ cancelCur(); return; } commitCur(); return; }
  if(eras && eras.id === e.pointerId){ endErase(); return; }
  if(lasso){
    var pts = lasso.pts; lasso = null; clearLive();
    if(pts.length >= 6){ sel = lassoSelect(pts); } else { var h = pickAt(p.x, p.y); sel = h ? [h] : []; }
    positionSel();
  }
}
stage.addEventListener('pointerup', onUp);
stage.addEventListener('pointercancel', onUp);
stage.addEventListener('pointerleave', function(){ if(!eras) hideRing(); });
stage.addEventListener('contextmenu', function(e){ e.preventDefault(); });
stage.addEventListener('wheel', function(e){
  e.preventDefault(); var v = view();
  if(e.ctrlKey || e.metaKey){
    var k = Math.exp(-e.deltaY * 0.01), ns = Math.min(8, Math.max(0.15, v.s * k)), r = ns / v.s;
    v.x = e.clientX - (e.clientX - v.x) * r; v.y = e.clientY - (e.clientY - v.y) * r; v.s = ns;
  } else { v.x -= e.deltaX; v.y -= e.deltaY; }
  fastSchedule();
}, { passive:false });
function showRing(x, y, d){ ring.style.display = 'block'; ring.style.width = d + 'px'; ring.style.height = d + 'px'; ring.style.left = x + 'px'; ring.style.top = y + 'px'; }
function hideRing(){ ring.style.display = 'none'; }
stage.addEventListener('pointerenter', function(e){ if(S.tool === 'eraser' && e.pointerType === 'mouse') showRing(e.clientX, e.clientY, S.esize); });

/* selection handles */
selBox.addEventListener('pointerdown', function(e){
  var h = e.target.closest('.h'); if(!h) return; e.stopPropagation(); e.preventDefault();
  try{ h.setPointerCapture(e.pointerId); }catch(er){}
  startTransform('scale', h.dataset.h, e.clientX, e.clientY);
  var mv = function(ev){ moveTransform(ev.clientX, ev.clientY); };
  var up = function(){ h.removeEventListener('pointermove', mv); h.removeEventListener('pointerup', up); h.removeEventListener('pointercancel', up); endTransform(); };
  h.addEventListener('pointermove', mv); h.addEventListener('pointerup', up); h.addEventListener('pointercancel', up);
});

/* ---------- keyboard ---------- */
window.addEventListener('keydown', function(e){
  if(e.target && (e.target.tagName === 'INPUT' && e.target.type === 'text')) return;
  var k = e.key, c = e.ctrlKey || e.metaKey;
  if(c && (k === 'z' || k === 'Z')){ e.preventDefault(); if(e.shiftKey) redo(); else undo(); return; }
  if(c && (k === 'y' || k === 'Y')){ e.preventDefault(); redo(); return; }
  if(k === ' '){ spaceDown = true; e.preventDefault(); return; }
  if((k === 'Delete' || k === 'Backspace') && sel.length){ e.preventDefault(); selBar.querySelector('[data-a=del]').click(); return; }
  if(c && (k === 'd' || k === 'D') && sel.length){ e.preventDefault(); selBar.querySelector('[data-a=dup]').click(); return; }
  if(c) return;
  if(k === 'p' || k === 'P') setTool('pen'); else if(k === 'h' || k === 'H') setTool('hl'); else if(k === 'e' || k === 'E') setTool('eraser');
  else if(k === 'v' || k === 'V') setTool('select'); else if(k === 'Escape'){ closePop(); closePanels(); clearSel(); }
  else if(k === '+' || k === '='){ zoomBy(1.25); } else if(k === '-'){ zoomBy(0.8); } else if(k === '0'){ resetView(); }
});
window.addEventListener('keyup', function(e){ if(e.key === ' ') spaceDown = false; });
function zoomBy(f){ var v = view(), ns = Math.min(8, Math.max(0.15, v.s * f)), r = ns / v.s; v.x = W / 2 - (W / 2 - v.x) * r; v.y = H / 2 - (H / 2 - v.y) * r; v.s = ns; render(); }
function resetView(){ var v = view(); v.x = 0; v.y = 0; v.s = 1; render(); }

/* ---------- images ---------- */
function addImageFile(f){
  if(!f || !/^image\//.test(f.type)) return;
  var url = URL.createObjectURL(f), im = new Image();
  im.onload = function(){
    var max = 1800, sc = Math.min(1, max / Math.max(im.naturalWidth, im.naturalHeight)), cw = Math.round(im.naturalWidth * sc), ch = Math.round(im.naturalHeight * sc);
    var c = document.createElement('canvas'); c.width = cw; c.height = ch; var cx = c.getContext('2d'); cx.drawImage(im, 0, 0, cw, ch);
    var src = /png|gif|webp|svg/.test(f.type) ? c.toDataURL('image/png') : c.toDataURL('image/jpeg', 0.88);
    URL.revokeObjectURL(url);
    var v = view(), vw = W / v.s, vh = H / v.s, k = Math.min(1, (vw * 0.6) / cw, (vh * 0.6) / ch), w = cw * k, h = ch * k;
    var it = { id:uid(), type:'img', src:src, x:(W / 2 - v.x) / v.s - w / 2, y:(H / 2 - v.y) / v.s - h / 2, w:w, h:h };
    var before = snapshot(); page().items.push(it); commitDiff(before);
    S.tool = 'select'; sel = [it]; buildTb(); render(); toast('Image added. Drag to move, corners to resize.');
  };
  im.onerror = function(){ URL.revokeObjectURL(url); toast('Could not open that image'); };
  im.src = url;
}
$('file').addEventListener('change', function(e){ var f = e.target.files && e.target.files[0]; if(f) addImageFile(f); e.target.value = ''; });
window.addEventListener('paste', function(e){
  var items = (e.clipboardData && e.clipboardData.items) || [];
  for(var i = 0; i < items.length; i++){ if(items[i].type.indexOf('image') === 0){ addImageFile(items[i].getAsFile()); e.preventDefault(); return; } }
});
window.addEventListener('dragover', function(e){ e.preventDefault(); });
window.addEventListener('drop', function(e){ e.preventDefault(); var f = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0]; if(f) addImageFile(f); });

/* ---------- curtain ---------- */
var CUR = { on:false, side:'bottom', amt:1, color:'#2a3550' };
var curEl = $('curtain');
function curRender(){
  if(!CUR.on){ curEl.style.display = 'none'; curEl.innerHTML = ''; return; }
  curEl.style.display = 'block';
  var s = CUR.side, a = Math.max(0, Math.min(1, CUR.amt)), vert = (s === 'top' || s === 'bottom'), size = (vert ? H : W) * a;
  var shade = '<div class="shade" id="shade" style="background:' + CUR.color + ';';
  if(s === 'bottom') shade += 'left:0;right:0;bottom:0;height:' + size + 'px;'; else if(s === 'top') shade += 'left:0;right:0;top:0;height:' + size + 'px;';
  else if(s === 'left') shade += 'top:0;bottom:0;left:0;width:' + size + 'px;'; else shade += 'top:0;bottom:0;right:0;width:' + size + 'px;';
  shade += '"></div>';
  var g = '<div class="grip" id="cgrip" style="';
  var gs = 68;
  function cl(v, max){ return Math.max(8, Math.min(max - gs - 8, v)); }
  if(s === 'bottom') g += 'left:50%;margin-left:-70px;width:140px;height:' + gs + 'px;top:' + cl(H - size - gs / 2, H) + 'px;';
  else if(s === 'top') g += 'left:50%;margin-left:-70px;width:140px;height:' + gs + 'px;top:' + cl(size - gs / 2, H) + 'px;';
  else if(s === 'left') g += 'top:50%;margin-top:-70px;height:140px;width:' + gs + 'px;left:' + cl(size - gs / 2, W) + 'px;';
  else g += 'top:50%;margin-top:-70px;height:140px;width:' + gs + 'px;left:' + cl(W - size - gs / 2, W) + 'px;';
  g += '">' + ic(vert ? 'grab' : 'grab') + '</div>';
  curEl.innerHTML = shade + g;
  var svg = curEl.querySelector('#cgrip svg'); if(svg){ svg.style.cssText = 'width:34px;height:34px;stroke:currentColor;fill:none;stroke-width:2.2;stroke-linecap:round;' + (vert ? '' : 'transform:rotate(90deg)'); }
  if(a <= 0.001){ curEl.querySelector('#shade').style.display = 'none'; }
}
curEl.addEventListener('pointerdown', function(e){
  var gr = e.target.closest('#cgrip'), sh = e.target.closest('#shade'); if(!gr && !sh) return;
  e.preventDefault(); closePop(); try{ curEl.setPointerCapture(e.pointerId); }catch(er){}
  var vert = (CUR.side === 'top' || CUR.side === 'bottom'), start = vert ? e.clientY : e.clientX, a0 = CUR.amt, total = vert ? H : W, dir = (CUR.side === 'bottom' || CUR.side === 'right') ? -1 : 1;
  var moved = false;
  var mv = function(ev){ var d = ((vert ? ev.clientY : ev.clientX) - start) * dir; if(Math.abs(d) > 3) moved = true; CUR.amt = Math.max(0, Math.min(1, a0 + d / total)); curRender(); };
  var up = function(){ curEl.removeEventListener('pointermove', mv); curEl.removeEventListener('pointerup', up); curEl.removeEventListener('pointercancel', up); };
  curEl.addEventListener('pointermove', mv); curEl.addEventListener('pointerup', up); curEl.addEventListener('pointercancel', up);
});
window.addEventListener('resize', curRender);

/* ---------- export ---------- */
function renderPageCanvas(pg, w, h, scale){
  var c = document.createElement('canvas'); c.width = Math.round(w * scale); c.height = Math.round(h * scale); var x = c.getContext('2d');
  x.setTransform(scale, 0, 0, scale, 0, 0); drawBg(x, pg.bg, pg.view, w, h); x.setTransform(scale, 0, 0, scale, 0, 0); paintPage(x, pg, w, h, pg.view, true); return c;
}
function download(blob, name){
  var a = document.createElement('a'), url = URL.createObjectURL(blob); a.href = url; a.download = name; document.body.appendChild(a); a.click();
  setTimeout(function(){ URL.revokeObjectURL(url); a.remove(); }, 4000);
}
function safeName(){ return (S.board.name || 'board').replace(/[^\w\- ]+/g, '').trim().replace(/\s+/g, '-') || 'board'; }
function exportPng(){
  var pg = page(), c = renderPageCanvas(pg, W, H, Math.min(2, 4096 / Math.max(W, H)));
  c.toBlob(function(b){ if(b) download(b, safeName() + '-page' + (S.board.cur + 1) + '.png'); else toast('Export failed'); }, 'image/png');
}
function exportPdf(){
  var pgs = S.board.pages, sc = Math.min(2, 3000 / Math.max(W, H)), jpgs = [];
  pgs.forEach(function(pg){ var c = renderPageCanvas(pg, W, H, sc), d = c.toDataURL('image/jpeg', 0.9); jpgs.push({ w:c.width, h:c.height, bin:atob(d.split(',')[1]) }); });
  var objs = [], offs = [], out = '%PDF-1.4\n', pos = 0, enc = []; function add(s){ enc.push(s); pos += s.length; }
  function obj(n, body){ offs[n] = pos; add(n + ' 0 obj\n' + body + '\nendobj\n'); }
  add(out);
  var n = jpgs.length, kids = []; for(var i = 0; i < n; i++) kids.push((3 + i * 3) + ' 0 R');
  obj(1, '<< /Type /Catalog /Pages 2 0 R >>'); obj(2, '<< /Type /Pages /Kids [' + kids.join(' ') + '] /Count ' + n + ' >>');
  jpgs.forEach(function(j, i){
    var pn = 3 + i * 3, w = Math.round(j.w * 0.75), h = Math.round(j.h * 0.75), content = 'q ' + w + ' 0 0 ' + h + ' 0 0 cm /Im0 Do Q';
    obj(pn, '<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ' + w + ' ' + h + '] /Resources << /XObject << /Im0 ' + (pn + 1) + ' 0 R >> >> /Contents ' + (pn + 2) + ' 0 R >>');
    offs[pn + 1] = pos; add((pn + 1) + ' 0 obj\n<< /Type /XObject /Subtype /Image /Width ' + j.w + ' /Height ' + j.h + ' /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length ' + j.bin.length + ' >>\nstream\n'); add(j.bin); add('\nendstream\nendobj\n');
    obj(pn + 2, '<< /Length ' + content.length + ' >>\nstream\n' + content + '\nendstream');
  });
  var total = 3 + n * 3, xr = pos; add('xref\n0 ' + total + '\n0000000000 65535 f \n');
  for(var k = 1; k < total; k++) add(('0000000000' + offs[k]).slice(-10) + ' 00000 n \n');
  add('trailer\n<< /Size ' + total + ' /Root 1 0 R >>\nstartxref\n' + xr + '\n%%EOF');
  var bytes = new Uint8Array(pos), q = 0; enc.forEach(function(s){ for(var m = 0; m < s.length; m++) bytes[q++] = s.charCodeAt(m) & 255; });
  download(new Blob([bytes], { type:'application/pdf' }), safeName() + '.pdf');
}

/* ---------- toolbar ---------- */
var popFor = null;
function closePop(){ pop.style.display = 'none'; popFor = null; }
function closePanels(){ $('pagesbar').style.display = 'none'; $('boards').style.display = 'none'; }
function tbtn(id, icon, label, cls){ return '<button class="tbb' + (cls ? ' ' + cls : '') + '" id="' + id + '" aria-label="' + label + '" title="' + label + '">' + ic(icon) + '</button>'; }
function buildTb(){
  if(S.collapsed){
    tb.className = S.dock; tb.innerHTML = '<button class="tbb on" id="bExpand" aria-label="Show tools">' + ic('pen') + '</button>'; positionTb(); return;
  }
  tb.className = S.dock;
  var h = '<button class="tbb" id="grip" aria-label="Move toolbar">' + ic('grip') + '</button>';
  h += tbtn('bPen', 'pen', 'Pen', S.tool === 'pen' ? 'on' : '');
  h += '<div class="dots">' + QUICK.map(function(c){ return '<button class="dot' + (S.color.toLowerCase() === c.toLowerCase() ? ' on' : '') + '" data-c="' + c + '" style="background:' + c + '" aria-label="Colour ' + c + '"></button>'; }).join('') + '<button class="dot" id="bMore" style="background:conic-gradient(red,yellow,lime,aqua,blue,magenta,red)" aria-label="More colours"></button></div>';
  h += '<input type="range" id="wslider" min="1" max="40" value="' + S.w + '" aria-label="Thickness">';
  h += '<div class="sep"></div>';
  h += tbtn('bHl', 'hl', 'Highlighter', S.tool === 'hl' ? 'on' : '') + tbtn('bEraser', 'eraser', 'Eraser', S.tool === 'eraser' ? 'on' : '') + tbtn('bSelect', 'select', 'Select', S.tool === 'select' ? 'on' : '');
  h += tbtn('bShape', 'shapes', 'Shapes', S.tool === 'shape' ? 'on' : '') + tbtn('bHand', 'hand', 'Move the board', S.tool === 'hand' ? 'on' : '');
  h += '<div class="sep"></div>' + tbtn('bUndo', 'undo', 'Undo') + tbtn('bRedo', 'redo', 'Redo');
  h += '<div class="sep"></div>' + tbtn('bPages', 'pages', 'Pages') + tbtn('bAdd', 'plus', 'New page') + tbtn('bImg', 'image', 'Insert image') + tbtn('bCurtain', 'curtain', 'Curtain', CUR.on ? 'on' : '');
  h += '<div class="sep"></div>' + tbtn('bMoreMenu', 'boards', 'More') + tbtn('bCollapse', 'collapse', 'Hide tools');
  tb.innerHTML = h; positionTb(); updateUndo();
}
function positionTb(){
  tb.style.left = tb.style.right = tb.style.top = tb.style.bottom = ''; tb.style.transform = '';
  tb.className = S.dock + (S.collapsed ? ' c' : '');
  if(S.collapsed){ tb.style.padding = '6px'; tb.style.borderRadius = '50%'; } else { tb.style.padding = ''; tb.style.borderRadius = ''; }
}
function flipLeft(){ return S.left; }
tb.addEventListener('click', function(e){
  var b = e.target.closest('button'); if(!b) return; var id = b.id;
  if(b.classList.contains('dot') && id !== 'bMore'){ S.color = b.dataset.c; if(S.tool === 'eraser' || S.tool === 'select' || S.tool === 'hand' || S.tool === 'shape' && false){ S.tool = 'pen'; S.hlOn = false; } savePrefs(); buildTb(); return; }
  switch(id){
    case 'bExpand': S.collapsed = false; buildTb(); break;
    case 'bCollapse': S.collapsed = true; closePop(); closePanels(); buildTb(); break;
    case 'bPen': if(S.tool === 'pen') openPop('pen', b); else setTool('pen'); break;
    case 'bHl': if(S.tool === 'hl') openPop('hl', b); else setTool('hl'); break;
    case 'bEraser': if(S.tool === 'eraser') openPop('eraser', b); else setTool('eraser'); break;
    case 'bSelect': setTool('select'); break;
    case 'bHand': setTool('hand'); break;
    case 'bShape': if(S.tool === 'shape') openPop('shape', b); else { S.tool = 'shape'; closePop(); buildTb(); updateCursor(); openPop('shape', $('bShape')); } break;
    case 'bMore': openPop('color', b); break;
    case 'bUndo': undo(); break;
    case 'bRedo': redo(); break;
    case 'bAdd': addPage(); break;
    case 'bPages': togglePages(); break;
    case 'bImg': $('file').click(); break;
    case 'bCurtain': openPop('curtain', b); break;
    case 'bMoreMenu': openPop('more', b); break;
  }
});
tb.addEventListener('input', function(e){ if(e.target.id === 'wslider'){ S.w = +e.target.value; savePrefs(); } });
/* docking: drag the grip to a screen edge */
tb.addEventListener('pointerdown', function(e){
  if(!e.target.closest('#grip')) return; e.preventDefault(); closePop();
  var g = $('grip'); try{ g.setPointerCapture(e.pointerId); }catch(er){}
  var sx = e.clientX, sy = e.clientY, moved = false;
  var mv = function(ev){ var dx = ev.clientX - sx, dy = ev.clientY - sy; if(Math.hypot(dx, dy) > 8) moved = true; if(moved){ tb.style.transition = 'none'; tb.style.left = ev.clientX + 'px'; tb.style.top = ev.clientY + 'px'; tb.style.bottom = tb.style.right = 'auto'; tb.style.transform = 'translate(-50%,-50%)'; } };
  var up = function(ev){
    g.removeEventListener('pointermove', mv); g.removeEventListener('pointerup', up); g.removeEventListener('pointercancel', up);
    if(moved){ var x = ev.clientX / W, y = ev.clientY / H; S.dock = (y > 0.55 && Math.abs(x - 0.5) < 0.38) ? 'b' : (x < 0.5 ? 'l' : 'r'); savePrefs(); }
    tb.style.transition = ''; buildTb();
  };
  g.addEventListener('pointermove', mv); g.addEventListener('pointerup', up); g.addEventListener('pointercancel', up);
});

function toggleFull(){
  var d = document, el = d.documentElement;
  try{ if(!d.fullscreenElement && !d.webkitFullscreenElement){ (el.requestFullscreen || el.webkitRequestFullscreen || function(){ toast('Full screen is not available here'); }).call(el); } else { (d.exitFullscreen || d.webkitExitFullscreen).call(d); } }catch(e){ toast('Full screen is not available here'); }
}

function openPop(kind, anchor){
  if(popFor === kind){ closePop(); return; }
  popFor = kind; var h = '';
  if(kind === 'pen' || kind === 'hl' || kind === 'color' || kind === 'shape'){
    h += '<h4>' + (kind === 'hl' ? 'Highlighter' : kind === 'shape' ? 'Shapes' : 'Pen') + '</h4>';
    if(kind === 'shape'){ h += '<div class="row">' + ['line', 'arrow', 'rect', 'ellipse', 'tri'].map(function(s){ return '<button class="chip' + (S.shape === s ? ' on' : '') + '" data-shape="' + s + '">' + ic(s) + '</button>'; }).join('') + '</div>'; }
    h += '<div class="row">' + COLORS.map(function(c){ return '<button class="sw' + (S.color.toLowerCase() === c.toLowerCase() ? ' on' : '') + '" data-c="' + c + '" style="background:' + c + '" aria-label="' + c + '"></button>'; }).join('') + '<input type="color" id="cpick" value="' + (/^#[0-9a-f]{6}$/i.test(S.color) ? S.color : '#111111') + '" aria-label="Custom colour"></div>';
    h += '<div class="row"><span style="width:70px">Thickness</span><input type="range" id="pw" min="1" max="40" value="' + S.w + '"></div>';
    h += '<div class="row">' + [2, 4, 8, 14, 24].map(function(w){ return '<button class="chip' + (S.w === w ? ' on' : '') + '" data-w="' + w + '"><span style="display:block;width:' + Math.max(14, w * 1.6) + 'px;height:' + Math.max(3, w) + 'px;border-radius:99px;background:currentColor"></span></button>'; }).join('') + '</div>';
  } else if(kind === 'eraser'){
    h += '<h4>Eraser</h4><div class="row"><button class="chip' + (S.eraser === 'stroke' ? ' on' : '') + '" data-er="stroke">Whole stroke</button><button class="chip' + (S.eraser === 'area' ? ' on' : '') + '" data-er="area">Rub out</button></div>';
    h += '<div class="row"><span style="width:70px">Size</span><input type="range" id="es" min="12" max="140" value="' + S.esize + '"></div>';
    h += '<div class="row"><button class="chip warn" data-act="clear">' + ic('trash') + ' Clear this page</button></div>';
  } else if(kind === 'bg'){
    h += '<h4>Background</h4><div class="row">' + BGS.map(function(b){ return '<button class="chip' + (page().bg === b[0] ? ' on' : '') + '" data-bg="' + b[0] + '">' + b[1] + '</button>'; }).join('') + '</div>';
    h += '<div class="row"><button class="chip" data-act="allbg">Use on all pages</button></div>';
  } else if(kind === 'curtain'){
    h += '<h4>Curtain</h4><div class="row">' + [['bottom', 'From bottom'], ['top', 'From top'], ['left', 'From left'], ['right', 'From right']].map(function(s){ return '<button class="chip' + (CUR.side === s[0] ? ' on' : '') + '" data-cs="' + s[0] + '">' + s[1] + '</button>'; }).join('') + '</div>';
    h += '<div class="row">' + ['#2a3550', '#111111', '#FFFFFF', '#2F5D50', '#8B1E2D'].map(function(c){ return '<button class="sw' + (CUR.color === c ? ' on' : '') + '" data-cc="' + c + '" style="background:' + c + '"></button>'; }).join('') + '</div>';
    h += '<div class="row"><button class="chip on" data-act="curtain-on">Close curtain</button>' + (CUR.on ? '<button class="chip warn" data-act="curtain-off">Remove</button>' : '') + '</div>';
  } else if(kind === 'more'){
    h += '<h4>Background</h4><div class="row">' + BGS.map(function(b){ return '<button class="chip' + (page().bg === b[0] ? ' on' : '') + '" data-bg="' + b[0] + '">' + b[1] + '</button>'; }).join('') + '<button class="chip" data-act="allbg">Use on all pages</button></div>';
    h += '<h4>Save</h4><div class="row"><button class="chip" data-act="png">' + ic('save') + ' This page (PNG)</button><button class="chip" data-act="pdf">' + ic('save') + ' All pages (PDF)</button></div>';
    h += '<h4>Board</h4><div class="row"><button class="chip" data-act="boards">' + ic('boards') + ' My boards</button><button class="chip" data-act="full">' + ic('full') + ' Full screen</button></div>';
    h += '<h4>Pen</h4><div class="row"><button class="chip' + (S.ink ? ' on' : '') + '" data-act="ink">Fast ink trail' + (inkPresenter ? '' : ' (not available here)') + '</button><button class="chip' + (PERF ? ' on' : '') + '" data-act="perf">Speed numbers</button><button class="chip' + (S.sharp ? ' on' : '') + '" data-act="sharp">Max sharpness (slower)</button></div>';
    h += '<h4>Toolbar</h4><div class="row"><button class="chip' + (S.dock === 'l' ? ' on' : '') + '" data-dock="l">Left</button><button class="chip' + (S.dock === 'b' ? ' on' : '') + '" data-dock="b">Bottom</button><button class="chip' + (S.dock === 'r' ? ' on' : '') + '" data-dock="r">Right</button></div>';
  } else if(kind === 'export'){
    h += '<h4>Export</h4><div class="row"><button class="chip" data-act="png">This page (PNG)</button><button class="chip" data-act="pdf">All pages (PDF)</button></div>';
  }
  pop.innerHTML = h; pop.style.display = 'block';
  var r = anchor.getBoundingClientRect(), pw = pop.offsetWidth, ph = pop.offsetHeight, x, y;
  if(S.dock === 'b'){ x = r.left + r.width / 2 - pw / 2; y = r.top - ph - 12; } else if(S.dock === 'l'){ x = r.right + 12; y = r.top + r.height / 2 - ph / 2; } else { x = r.left - pw - 12; y = r.top + r.height / 2 - ph / 2; }
  x = Math.max(8, Math.min(W - pw - 8, x)); y = Math.max(8, Math.min(H - ph - 8, y)); pop.style.left = x + 'px'; pop.style.top = y + 'px';
}
pop.addEventListener('pointerdown', function(e){ e.stopPropagation(); });
pop.addEventListener('click', function(e){
  var b = e.target.closest('button'); if(!b) return;
  if(b.dataset.c){ S.color = b.dataset.c; if(S.tool === 'eraser' || S.tool === 'select' || S.tool === 'hand'){ S.tool = 'pen'; S.hlOn = false; } savePrefs(); var k = popFor, a = $(k === 'hl' ? 'bHl' : k === 'shape' ? 'bShape' : 'bPen') || $('bMore'); popFor = null; buildTb(); openPop(k, $(k === 'hl' ? 'bHl' : k === 'shape' ? 'bShape' : k === 'color' ? 'bMore' : 'bPen')); return; }
  if(b.dataset.w){ S.w = +b.dataset.w; savePrefs(); buildTb(); var k2 = popFor; popFor = null; openPop(k2, $(k2 === 'hl' ? 'bHl' : k2 === 'shape' ? 'bShape' : k2 === 'color' ? 'bMore' : 'bPen')); return; }
  if(b.dataset.shape){ S.shape = b.dataset.shape; S.tool = 'shape'; savePrefs(); closePop(); buildTb(); updateCursor(); return; }
  if(b.dataset.er){ S.eraser = b.dataset.er; savePrefs(); var k3 = popFor; popFor = null; openPop(k3, $('bEraser')); return; }
  if(b.dataset.dock){ S.dock = b.dataset.dock; savePrefs(); closePop(); buildTb(); return; }
  if(b.dataset.bg){ page().bg = b.dataset.bg; autoInk(); markDirty(); render(); closePop(); return; }
  if(b.dataset.cs){ CUR.side = b.dataset.cs; var k4 = popFor; popFor = null; openPop(k4, $('bCurtain')); if(CUR.on){ CUR.amt = 1; curRender(); } return; }
  if(b.dataset.cc){ CUR.color = b.dataset.cc; var k5 = popFor; popFor = null; openPop(k5, $('bCurtain')); if(CUR.on) curRender(); return; }
  var act = b.dataset.act;
  if(act === 'clear'){ var before = snapshot(); page().items = []; clearSel(); if(commitDiff(before)) toast('Page cleared. Undo brings it back.'); render(); closePop(); }
  else if(act === 'allbg'){ var bg = page().bg; S.board.pages.forEach(function(p){ p.bg = bg; }); markDirty(); closePop(); toast('Background applied to all pages'); }
  else if(act === 'curtain-on'){ CUR.on = true; CUR.amt = 1; closePop(); buildTb(); curRender(); }
  else if(act === 'curtain-off'){ CUR.on = false; closePop(); buildTb(); curRender(); }
  else if(act === 'ink'){ S.ink = !S.ink; savePrefs(); closePop(); toast('Fast ink trail ' + (S.ink ? 'on' : 'off')); }
  else if(act === 'sharp'){ S.sharp = !S.sharp; if(!S.sharp) S.dc = 1.5; savePrefs(); closePop(); resize(); toast(S.sharp ? 'Max sharpness' : 'Sharpness automatic'); }
  else if(act === 'perf'){ PERF = !PERF; hzStart(); try{ localStorage.setItem('boardPerf', PERF ? '1' : '0'); }catch(e){} if(!PERF && pfEl){ pfEl.remove(); pfEl = null; } closePop(); toast(PERF ? 'Speed numbers on: draw with the pen' : 'Speed numbers off'); }
  else if(act === 'boards'){ closePop(); openBoards(); }
  else if(act === 'full'){ closePop(); toggleFull(); }
  else if(act === 'png'){ closePop(); exportPng(); }
  else if(act === 'pdf'){ closePop(); exportPdf(); }
});
pop.addEventListener('input', function(e){
  if(e.target.id === 'pw'){ S.w = +e.target.value; savePrefs(); var s = $('wslider'); if(s) s.value = S.w; }
  else if(e.target.id === 'es'){ S.esize = +e.target.value; savePrefs(); }
  else if(e.target.id === 'cpick'){ S.color = e.target.value; savePrefs(); }
});
pop.addEventListener('change', function(e){ if(e.target.id === 'cpick'){ buildTb(); } });
function autoInk(){
  var dark = !!DARKBG[page().bg];
  if(dark && S.color.toLowerCase() === '#111111') S.color = '#FFFFFF'; else if(!dark && S.color.toLowerCase() === '#ffffff') S.color = '#111111';
  buildTb();
}

/* ---------- pages ---------- */
function addPage(){
  var cur = page(), np = newPage(cur.bg); S.board.pages.splice(S.board.cur + 1, 0, np); S.board.cur++; clearSel(); cancelCur(); markDirty(); render(); buildTb(); renderPagesBar(); toast('Page ' + (S.board.cur + 1) + ' of ' + S.board.pages.length);
}
function gotoPage(i){ if(i < 0 || i >= S.board.pages.length) return; S.board.cur = i; clearSel(); cancelCur(); markDirty(); render(); updateUndo(); renderPagesBar(); }
function togglePages(){ var el = $('pagesbar'); if(el.style.display === 'block'){ el.style.display = 'none'; return; } closePop(); $('boards').style.display = 'none'; el.style.display = 'block'; renderPagesBar(); }
function renderPagesBar(){
  var el = $('pagesbar'); if(el.style.display !== 'block') return;
  var h = '<div class="strip">', pgs = S.board.pages;
  pgs.forEach(function(p, i){ h += '<button class="th' + (i === S.board.cur ? ' on' : '') + '" data-i="' + i + '"><canvas width="300" height="192"></canvas><span>' + (i + 1) + '</span></button>'; });
  h += '</div><div class="acts"><button class="chip" data-a="add">' + ic('plus') + ' New</button><button class="chip" data-a="dup">' + ic('copy') + ' Duplicate</button><button class="chip" data-a="left">' + ic('left') + '</button><button class="chip" data-a="right">' + ic('right') + '</button><button class="chip warn" data-a="del">' + ic('trash') + ' Delete</button><button class="chip" data-a="close">Close</button></div>';
  el.innerHTML = h;
  el.querySelectorAll('.th canvas').forEach(function(c, i){
    var p = pgs[i], x = c.getContext('2d'), k = c.width / W, v = p.view;
    x.save(); x.scale(k, k); drawBg(x, p.bg, v, W, H); x.setTransform(k, 0, 0, k, 0, 0); paintPage(x, p, W, H, v, true); x.restore();
  });
  var on = el.querySelector('.th.on'); if(on) on.scrollIntoView({ inline:'center', block:'nearest' });
}
$('pagesbar').addEventListener('pointerdown', function(e){ e.stopPropagation(); });
$('pagesbar').addEventListener('click', function(e){
  var th = e.target.closest('.th'); if(th){ gotoPage(+th.dataset.i); return; }
  var b = e.target.closest('button'); if(!b) return; var a = b.dataset.a, pgs = S.board.pages, i = S.board.cur;
  if(a === 'add') addPage();
  else if(a === 'dup'){ var src = pgs[i], np = newPage(src.bg); np.items = src.items.map(function(it){ var c = cloneItem(it); c.id = uid(); return c; }); np.view = { x:src.view.x, y:src.view.y, s:src.view.s }; pgs.splice(i + 1, 0, np); S.board.cur = i + 1; markDirty(); render(); renderPagesBar(); updateUndo(); }
  else if(a === 'left' && i > 0){ var t = pgs[i]; pgs[i] = pgs[i - 1]; pgs[i - 1] = t; S.board.cur = i - 1; markDirty(); renderPagesBar(); }
  else if(a === 'right' && i < pgs.length - 1){ var t2 = pgs[i]; pgs[i] = pgs[i + 1]; pgs[i + 1] = t2; S.board.cur = i + 1; markDirty(); renderPagesBar(); }
  else if(a === 'del'){
    if(pgs.length === 1){ var before = snapshot(); page().items = []; commitDiff(before); render(); toast('Last page cleared. Undo brings it back.'); }
    else if(pgs[i].items.length === 0 || confirm('Delete page ' + (i + 1) + '?')){ pgs.splice(i, 1); S.board.cur = Math.min(i, pgs.length - 1); markDirty(); render(); updateUndo(); }
    renderPagesBar();
  } else if(a === 'close') $('pagesbar').style.display = 'none';
});

/* ---------- boards ---------- */
function openBoards(){
  closePop(); $('pagesbar').style.display = 'none'; var el = $('boards'); el.style.display = 'block'; flushSave();
  dbAll().then(function(list){
    list.sort(function(a, b){ return b.updated - a.updated; });
    var h = '<h3>Boards</h3><div style="display:flex;gap:8px;margin-bottom:12px"><button class="chip on" data-a="new">' + ic('plus') + ' New board</button><button class="chip" data-a="close">Close</button></div>';
    list.forEach(function(b){
      var cnt = b.pages.length + (b.pages.length === 1 ? ' page' : ' pages'), when = new Date(b.updated).toLocaleString('en-GB', { day:'numeric', month:'short', hour:'2-digit', minute:'2-digit' });
      h += '<div class="bi" data-id="' + b.id + '"><div class="nm">' + esc(b.name) + '<small>' + cnt + ' · ' + when + (b.id === S.board.id ? ' · open' : '') + '</small></div><button class="chip" data-a="open">Open</button><button class="chip" data-a="rename">Rename</button><button class="chip warn" data-a="del">' + ic('trash') + '</button></div>';
    });
    el.innerHTML = h;
  });
}
function esc(s){ return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
$('boards').addEventListener('pointerdown', function(e){ e.stopPropagation(); });
$('boards').addEventListener('click', function(e){
  var b = e.target.closest('button'); if(!b) return; var a = b.dataset.a, row = b.closest('.bi'), id = row && row.dataset.id;
  if(a === 'close'){ $('boards').style.display = 'none'; }
  else if(a === 'new'){ flushSave(); S.board = newBoard('Board ' + new Date().toLocaleDateString('en-GB', { day:'numeric', month:'short' })); markDirty(); flushSave(); afterBoardLoad(); $('boards').style.display = 'none'; }
  else if(a === 'open'){ flushSave(); dbGet(id).then(function(bd){ if(!bd) return; hydrate(bd); S.board = bd; afterBoardLoad(); $('boards').style.display = 'none'; }); }
  else if(a === 'rename'){ var nm = prompt('Board name', row.querySelector('.nm').firstChild.textContent); if(nm){ dbGet(id).then(function(bd){ if(!bd) return; bd.name = nm.slice(0, 60); if(S.board.id === id) S.board.name = bd.name; dbPut(bd).then(openBoards); }); } }
  else if(a === 'del'){ if(confirm('Delete this board for good?')){ dbDel(id).then(function(){ if(S.board.id === id){ S.board = newBoard('Board'); markDirty(); flushSave(); afterBoardLoad(); } openBoards(); }); } }
});
function hydrate(bd){ bd.pages.forEach(function(p){ p.undo = []; p.redo = []; if(!p.view) p.view = { x:0, y:0, s:1 }; }); }
function afterBoardLoad(){ clearSel(); cancelCur(); CUR.on = false; curRender(); updateUndo(); autoInkQuiet(); buildTb(); resize(); }
function autoInkQuiet(){ var dark = !!DARKBG[page().bg]; if(dark && S.color.toLowerCase() === '#111111') S.color = '#FFFFFF'; else if(!dark && S.color.toLowerCase() === '#ffffff') S.color = '#111111'; }

/* ---------- boot ---------- */
function boot(){
  openDb().then(function(){
    var last = null; try{ last = localStorage.getItem('boardLast'); }catch(e){}
    return last ? dbGet(last) : null;
  }).then(function(bd){
    if(bd && bd.pages && bd.pages.length){ hydrate(bd); S.board = bd; } else { S.board = newBoard('Board'); }
    var q = location.search.match(/[?&]new=1/); if(q){ S.board = newBoard('Board'); }
    resize(); buildTb(); autoInkQuiet(); buildTb(); updateUndo(); updateCursor();
    window.__board = { S:S, page:page, undo:undo, redo:redo, render:render, bbox:bbox, ser:ser };
  });
}
boot();
if('serviceWorker' in navigator){ /* the app's own sw.js already covers this origin */ }
})();
