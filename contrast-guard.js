/* Contrast guard: keeps every piece of text readable in every theme, on every page, in every state.
   For each text element it works out the real background behind it (stacked backgrounds, translucent
   tints, gradients) and, if the contrast ratio is below WCAG AA (4.5:1, or 3:1 for large text), nudges
   the text colour towards black or white just enough to pass. Runs before paint (MutationObserver
   microtasks), re-runs when a theme changes or when content changes. Turn off for testing with
   localStorage.contrastGuard = 'off'. */
(function(){
  'use strict';
  if(window.__contrastGuard) return;
  try{ if(localStorage.getItem('contrastGuard') === 'off') return; }catch(e){}
  var TARGET = 4.6, TARGET_LARGE = 3.1, MARK = 'data-cg';
  var cache = null;

  function parse(c){
    var m = c && c.match(/rgba?\(([^)]+)\)/);
    if(!m) return null;
    var p = m[1].split(/[,\s\/]+/).filter(Boolean).map(parseFloat);
    return [p[0], p[1], p[2], p.length > 3 && !isNaN(p[3]) ? p[3] : 1];
  }
  function over(top, bot){
    var a = top[3] + bot[3] * (1 - top[3]);
    if(a <= 0) return [0, 0, 0, 0];
    return [0, 1, 2].map(function(i){ return (top[i] * top[3] + bot[i] * bot[3] * (1 - top[3])) / a; }).concat([a]);
  }
  function lum(c){
    var f = [c[0], c[1], c[2]].map(function(v){ v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
    return 0.2126 * f[0] + 0.7152 * f[1] + 0.0722 * f[2];
  }
  function ratio(a, b){ var x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }
  function gradColors(img){
    var out = [], re = /rgba?\([^)]*\)/g, m;
    while((m = re.exec(img))) out.push(parse(m[0]));
    return out.filter(Boolean);
  }
  var rootBg = [255, 255, 255, 1];
  function refreshRoot(){
    rootBg = [255, 255, 255, 1];
    var hb = parse(getComputedStyle(document.documentElement).backgroundColor);
    if(hb && hb[3] > 0) rootBg = over(hb, rootBg);
    var bb = document.body && parse(getComputedStyle(document.body).backgroundColor);
    // body paints over html; handled by the ancestor walk
  }
  // Background variants, cumulative opacity and computed style for an element, cached per pass.
  function bgOf(el){
    var hit = cache.get(el);
    if(hit) return hit;
    var parent = el.parentElement;
    var base = parent ? bgOf(parent) : { v: [rootBg.slice()], img: false, op: 1 };
    var v = base.v, img = base.img;
    var cs = getComputedStyle(el);
    var bc = parse(cs.backgroundColor);
    if(bc && bc[3] > 0) v = v.map(function(b){ return over(bc, b); });
    var bi = cs.backgroundImage;
    if(bi && bi !== 'none'){
      if(/gradient/.test(bi) && !/url\(/.test(bi)){
        var g = gradColors(bi);
        if(g.length){
          var nv = [];
          g.forEach(function(gc){ v.forEach(function(b){ nv.push(over(gc, b)); }); });
          v = nv.length > 12 ? nv.filter(function(_, i){ return i % Math.ceil(nv.length / 12) === 0; }) : nv;
        }
      } else if(/url\(/.test(bi)) img = true;
    }
    var own = parseFloat(cs.opacity); if(isNaN(own)) own = 1;
    var o = { v: v, img: img, op: base.op * own, own: own, cs: cs };
    cache.set(el, o);
    return o;
  }
  function worstRatio(fg, variants){
    var worst = 99;
    for(var i = 0; i < variants.length; i++){
      var b = variants[i];
      if(b[3] < 1) b = over(b, [255, 255, 255, 1]);
      var r = ratio(over(fg, b), b);
      if(r < worst) worst = r;
    }
    return worst;
  }
  function mix(a, b, t, alpha){ return [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t, alpha]; }
  // Find the colour closest to fg (same hue, pushed to black or white) that passes on every background variant.
  // alpha is the effective opacity the colour will be shown at (ancestor opacity).
  var fixMemo = {};
  function fixColour(fg, variants, need, alpha){
    var mk = fg.slice(0, 3).map(Math.round).join(',') + '|' + need + '|' + alpha.toFixed(2) + '|' + variants.map(function(b){ return b.map(Math.round).join(','); }).join(';');
    if(fixMemo[mk]) return fixMemo[mk];
    var res = fixColourRaw(fg, variants, need, alpha);
    if(Object.keys(fixMemo).length > 4000) fixMemo = {};
    return (fixMemo[mk] = res);
  }
  function fixColourRaw(fg, variants, need, alpha){
    var black = [0, 0, 0, alpha], white = [255, 255, 255, alpha], base = [fg[0], fg[1], fg[2], alpha];
    var rb = worstRatio(black, variants), rw = worstRatio(white, variants);
    var dir = rb >= rw ? black : white, best = Math.max(rb, rw);
    if(best < need) return [dir[0], dir[1], dir[2], 1];
    var lo = 0, hi = 1;
    for(var i = 0; i < 14; i++){
      var mid = (lo + hi) / 2;
      if(worstRatio(mix(base, dir, mid, alpha), variants) >= need) hi = mid; else lo = mid;
    }
    var m = mix(base, dir, hi, 1);
    return m;
  }
  function rgb(c){ return 'rgb(' + Math.round(c[0]) + ',' + Math.round(c[1]) + ',' + Math.round(c[2]) + ')'; }

  function restore(el){
    var o = el.getAttribute(MARK);
    if(o === null) return;
    var parts = o.split('|');
    if(parts[0]) el.style.setProperty('color', parts[0], parts[1] || ''); else el.style.removeProperty('color');
    if(parts[2] !== undefined && parts[2] !== 'x'){ if(parts[2]) el.style.setProperty('opacity', parts[2], parts[3] || ''); else el.style.removeProperty('opacity'); }
    el.removeAttribute(MARK);
    var f = el.getAttribute('data-cg-f');
    if(f !== null){ var fp = f.split('|'); el.style.setProperty('-webkit-text-fill-color', fp[0], fp[1] || ''); el.removeAttribute('data-cg-f'); }
  }
  var TEXT_RE = /[A-Za-z0-9À-￿]/;
  function processText(el){
    if(el.hasAttribute(MARK)){
      var c0 = getComputedStyle(el), f0 = parse(c0.color);
      if(f0 && el.getClientRects().length){
        var b0 = bgOf(el), sz = parseFloat(c0.fontSize), wt = parseInt(c0.fontWeight, 10) || 400;
        var nd = (sz >= 24 || (sz >= 18.66 && wt >= 700)) ? TARGET_LARGE : TARGET;
        if(!b0.img && worstRatio([f0[0], f0[1], f0[2], f0[3] * b0.own], b0.v) >= nd - 0.05) return;  // our fix still holds: leave it (no flicker)
      }
      restore(el);
    }
    var tag = el.tagName;
    if(/^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE|OPTION|OPTGROUP|HEAD|META|LINK|SVG|CANVAS|AUDIO|VIDEO|IFRAME)$/i.test(tag)) return;
    if(el.closest('svg')) return;
    if(!el.getClientRects().length) return;
    var bg = bgOf(el), cs = bg.cs;
    if(cs.visibility === 'hidden') return;
    var fg = parse(cs.color);
    var tf = parse(cs.webkitTextFillColor);
    if(tf && tf[3] === 0) return;                  // gradient/clip text or deliberately blanked
    if(!fg || fg[3] === 0) return;
    if(cs.backgroundClip === 'text' || cs.webkitBackgroundClip === 'text') return;
    var op = bg.own;                               // ancestor fades (carousel cross-fades etc.) are transient: judge at full opacity
    if(op < 0.3) return;                           // decorative / faded out on purpose
    if(bg.img) return;                              // photo or pattern behind: cannot know the colour
    var size = parseFloat(cs.fontSize), weight = parseInt(cs.fontWeight, 10) || 400;
    var need = (size >= 24 || (size >= 18.66 && weight >= 700)) ? TARGET_LARGE : TARGET;
    var eff = [fg[0], fg[1], fg[2], fg[3] * op];
    if(worstRatio(eff, bg.v) >= need) return;
    // Apply: if the element itself is what faded the text, restore full opacity; then fix the colour.
    var ownOp = bg.own, changedOpacity = false;
    var inlineColor = el.style.getPropertyValue('color'), inlineColorPri = el.style.getPropertyPriority('color');
    var inlineOp = el.style.getPropertyValue('opacity'), inlineOpPri = el.style.getPropertyPriority('opacity');
    var opRest = op;
    // A dimmed label that fails is restored to full strength. Anything that transitions or animates its opacity
    // (toasts, fades) is never touched: forcing it would leave it stuck on screen.
    var opTrans = /(^|,\s*)(opacity|all)(\s*,|$)/.test(cs.transitionProperty) && !/^(0s)(,\s*0s)*$/.test(cs.transitionDuration);
    if(ownOp < 1 && ownOp >= 0.5 && !opTrans && !(el.getAnimations && el.getAnimations().some(function(a){ return (a.playState === 'running' || a.playState === 'pending') && (a.transitionProperty ? a.transitionProperty === 'opacity' : true); }))){
      opRest = op / ownOp; el.style.setProperty('opacity', '1', 'important'); changedOpacity = true;
    }
    if(worstRatio([fg[0], fg[1], fg[2], fg[3] * opRest], bg.v) < need){
      var fixed = fixColour(fg, bg.v, need, fg[3] * opRest);
      el.style.setProperty('color', rgb(fixed), 'important');
      var f0 = el.style.getPropertyValue('-webkit-text-fill-color');
      if(f0){ el.setAttribute('data-cg-f', f0 + '|' + el.style.getPropertyPriority('-webkit-text-fill-color')); el.style.setProperty('-webkit-text-fill-color', rgb(fixed), 'important'); }
    }
    el.setAttribute(MARK, (inlineColor || '') + '|' + (inlineColorPri || '') + '|' + (changedOpacity ? inlineOp : 'x') + '|' + (inlineOpPri || ''));
  }
  function processInput(el){
    // placeholder colour (cannot be set inline, so use a custom property + attribute rule)
    if(el.hasAttribute('data-cg-ph')){ el.removeAttribute('data-cg-ph'); el.style.removeProperty('--cg-ph'); }
    if(!el.placeholder || el.value) return;
    var pcs = getComputedStyle(el, '::placeholder'), pc = parse(pcs.color);
    if(!pc) return;
    var bg = bgOf(el);
    if(bg.img) return;
    var a = [pc[0], pc[1], pc[2], pc[3] * (parseFloat(pcs.opacity) || 1)];
    if(worstRatio(a, bg.v) >= TARGET) { el.removeAttribute('data-cg-ph'); return; }
    el.style.setProperty('--cg-ph', rgb(fixColour(pc, bg.v, TARGET, 1)));
    el.setAttribute('data-cg-ph', '1');
  }
  var st = document.createElement('style');
  st.textContent = '[data-cg-ph]::placeholder{color:var(--cg-ph) !important; opacity:1 !important;}';
  (document.head || document.documentElement).appendChild(st);

  function scan(root){
    cache = new Map();
    try{
      var els = [];
      if(root.nodeType === 1) els.push(root);
      var all = (root.nodeType === 1 || root.nodeType === 9 || root.nodeType === 11) ? root.querySelectorAll('*') : [];
      for(var i = 0; i < all.length; i++) els.push(all[i]);
      for(var k = 0; k < els.length; k++){
        var el = els[k];
        try{
        var hasText = false;
        for(var c = el.firstChild; c; c = c.nextSibling){ if(c.nodeType === 3 && TEXT_RE.test(c.nodeValue)){ hasText = true; break; } }
        var tn = el.tagName;
        if(tn === 'INPUT' || tn === 'TEXTAREA'){ if(!/^(checkbox|radio|hidden|range|color|file)$/.test(el.type)){ processInput(el); if(el.value) processText(el); } continue; }
        if(tn === 'SELECT'){ processText(el); continue; }
        if(el.hasAttribute(MARK) && !hasText) restore(el);
        if(hasText) processText(el);
        }catch(err){ if(!window.__cgErr){ window.__cgErr = err; } }
      }
    }catch(e){}
    cache = null;
  }
  function resetAll(){
    document.querySelectorAll('[' + MARK + ']').forEach(restore);
    document.querySelectorAll('[data-cg-ph]').forEach(function(e){ e.removeAttribute('data-cg-ph'); });
  }

  function themeSig(){
    var b = document.body ? Array.prototype.filter.call(document.body.classList, function(c){ return /^(usertheme-|theme-)/.test(c) || c === 'dark-mode'; }).sort().join(' ') : '';
    return b + '|' + (document.documentElement.getAttribute('data-theme') || '');
  }
  var lastSig = '';
  var obs, pending = [], pendingAttr = [], full = false, doReset = false, scheduled = false, attrTimer = 0, themeTimer = 0;
  function runScan(list){
    var seen = new Set();
    list.forEach(function(n){
      if(!n.isConnected) return;
      if(n.nodeType === 3) n = n.parentElement;
      if(!n || seen.has(n)) return;
      seen.add(n); scan(n);
    });
  }
  function flush(){
    scheduled = false;
    if(!document.body) return;
    obs.disconnect();
    refreshRoot();
    if(full){ if(doReset){ resetAll(); doReset = false; } scan(document.body); }
    else runScan(pending.concat(pendingAttr));
    pending = []; pendingAttr = []; full = false;
    observe();
  }
  function schedule(){
    if(scheduled) return; scheduled = true;
    Promise.resolve().then(flush);
  }
  function observe(){
    obs.observe(document.documentElement, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ['class', 'style', 'hidden', 'disabled', 'aria-selected', 'data-theme'] });
  }
  obs = new MutationObserver(function(recs){
    var content = false, attr = false;
    for(var i = 0; i < recs.length; i++){
      var r = recs[i];
      if(r.type === 'attributes'){
        if(r.target === document.body || r.target === document.documentElement){
          full = true; content = true;
          var sig = themeSig();
          if(sig !== lastSig){ lastSig = sig; doReset = true; clearTimeout(themeTimer); themeTimer = setTimeout(function(){ full = true; doReset = true; schedule(); }, 900); } // after the theme cross-fade settles
        } else { pendingAttr.push(r.target); attr = true; }
      } else if(r.type === 'characterData'){ pending.push(r.target); content = true; }
      else { r.addedNodes.forEach(function(n){ if(n.nodeType === 1 || n.nodeType === 3) pending.push(n); }); if(r.target.nodeType === 1) pending.push(r.target); content = true; }
    }
    if(content) schedule();
    else if(attr && !attrTimer){ attrTimer = setTimeout(function(){ attrTimer = 0; schedule(); }, 120); }
  });
  observe();
  function start(){ full = true; schedule(); }
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
  window.addEventListener('load', function(){ setTimeout(start, 200); });
  // Pages fade/slide content in (CSS animations end at their real opacity); look again once they settle.
  function later(){ [700, 1600].forEach(function(ms){ setTimeout(start, ms); }); }
  window.addEventListener('hashchange', later);
  // Hover / focus / pressed styles change colours without any DOM mutation: re-judge the touched control.
  var HOVER_SEL = 'a,button,summary,label,[role=button],[role=tab],[tabindex],li,tr,[class*=tile],[class*=card],[class*=row],[class*=item]';
  function interact(e){
    var t = e.target; if(!t || t.nodeType !== 1) return;
    var c = t.closest(HOVER_SEL) || t;
    [30, 120, 400].forEach(function(ms){ setTimeout(function(){ if(c.isConnected){ pendingAttr.push(c); schedule(); } }, ms); });
  }
  ['pointerover', 'pointerout', 'pointerdown', 'pointerup', 'focusin', 'focusout'].forEach(function(n){ document.addEventListener(n, interact, true); });
  document.addEventListener('animationend', function(e){ if(e.target && e.target.nodeType === 1){ pendingAttr.push(e.target); if(!attrTimer) attrTimer = setTimeout(function(){ attrTimer = 0; schedule(); }, 200); } }, true);
  window.__contrastGuard = { run: start, version: 1 };
})();
