// Injected into a page. Returns an array of contrast problems for every visible piece of text.
(function(opts){
  opts = opts || {};
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
    var f = c.slice(0, 3).map(function(v){ v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
    return 0.2126 * f[0] + 0.7152 * f[1] + 0.0722 * f[2];
  }
  function ratio(a, b){ var x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }
  function gradColors(img){
    var out = [], re = /rgba?\([^)]*\)/g, m;
    while((m = re.exec(img))) out.push(parse(m[0]));
    return out.filter(Boolean);
  }
  var rootBg = [255, 255, 255, 1];
  var htmlBg = parse(getComputedStyle(document.documentElement).backgroundColor);
  if(htmlBg && htmlBg[3] > 0) rootBg = over(htmlBg, rootBg);
  // Build the list of background candidates for an element: [{c:[r,g,b,a]}|{grad:[colors]}|{img:true}] from root to element
  function layers(el){
    var chain = [], n = el;
    while(n && n.nodeType === 1){ chain.unshift(n); n = n.parentElement; }
    var res = [];
    chain.forEach(function(e){
      var cs = getComputedStyle(e);
      var bc = parse(cs.backgroundColor);
      if(bc && bc[3] > 0) res.push({ c: bc });
      var bi = cs.backgroundImage;
      if(bi && bi !== 'none'){
        if(/gradient/.test(bi)){ var g = gradColors(bi); if(g.length) res.push({ grad: g }); }
        if(/url\(/.test(bi)) res.push({ img: true });
      }
    });
    return res;
  }
  function opacityOf(el){
    var o = 1, n = el;
    while(n && n.nodeType === 1){ o *= parseFloat(getComputedStyle(n).opacity); n = n.parentElement; }
    return o;
  }
  function bgVariants(el){
    var ls = layers(el), variants = [rootBg.slice()], img = false;
    ls.forEach(function(l){
      if(l.c){ variants = variants.map(function(v){ return over(l.c, v); }); }
      else if(l.grad){
        var nv = [];
        l.grad.forEach(function(gc){ variants.forEach(function(v){ nv.push(over(gc, v)); }); });
        variants = nv.length > 24 ? nv.filter(function(_, i){ return i % Math.ceil(nv.length / 24) === 0; }) : nv;
      } else if(l.img) img = true;
    });
    return { v: variants, img: img };
  }
  function visible(el, r){
    if(r.width < 1 || r.height < 1) return false;
    var cs = getComputedStyle(el);
    if(cs.visibility === 'hidden' || cs.display === 'none') return false;
    if(opacityOf(el) < 0.05) return false;
    if(r.bottom < 0 || r.right < 0 || r.left > innerWidth + 5) return false;
    // clipped away by an overflow-hidden ancestor
    var n = el.parentElement;
    while(n && n !== document.body){
      var s = getComputedStyle(n);
      if(s.display === 'none' || s.visibility === 'hidden') return false;
      if(/(hidden|clip)/.test(s.overflow + s.overflowX + s.overflowY)){
        var pr = n.getBoundingClientRect();
        if(pr.width < 1 || pr.height < 1) return false;
        if(r.right < pr.left || r.left > pr.right || r.bottom < pr.top || r.top > pr.bottom) return false;
      }
      n = n.parentElement;
    }
    return true;
  }
  function sel(el){
    var p = [], n = el, i = 0;
    while(n && n.nodeType === 1 && i < 4){
      var s = n.tagName.toLowerCase();
      if(n.id) s += '#' + n.id; else if(n.className && typeof n.className === 'string') s += '.' + n.className.trim().split(/\s+/).slice(0, 2).join('.');
      p.unshift(s); n = n.parentElement; i++;
    }
    return p.join(' > ');
  }
  var out = [], seen = {};
  function check(el, text, fg, size, weight, kind){
    var r = el.getBoundingClientRect();
    if(!visible(el, r)) return;
    var o = parseFloat(getComputedStyle(el).opacity); if(isNaN(o)) o = 1; // ancestor fades are transient; judge at full opacity
    var bv = bgVariants(el);
    var worst = 99, wfg = null, wbg = null;
    bv.v.forEach(function(b){
      var bb = b[3] < 1 ? over(b, [255, 255, 255, 1]) : b;
      var f = [fg[0], fg[1], fg[2], fg[3] * o];
      var comp = over(f, bb);
      var rt = ratio(comp, bb);
      if(rt < worst){ worst = rt; wfg = comp; wbg = bb; }
    });
    var large = size >= 24 || (size >= 18.66 && weight >= 700);
    var need = large ? 3 : 4.5;
    if(worst < need){
      var key = sel(el) + '|' + text.slice(0, 30) + '|' + worst.toFixed(1);
      if(seen[key]) return; seen[key] = 1;
      out.push({ sel: sel(el), text: text.replace(/\s+/g, ' ').trim().slice(0, 48), ratio: +worst.toFixed(2), need: need, fg: wfg.slice(0, 3).map(Math.round).join(','), bg: wbg.slice(0, 3).map(Math.round).join(','), img: bv.img, kind: kind, size: size, x: Math.round(r.left), y: Math.round(r.top + scrollY) });
    }
  }
  var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null);
  var node;
  while((node = walker.nextNode())){
    var t = node.nodeValue;
    if(!t || !/[A-Za-z0-9\u00C0-\uFFFF]/.test(t.replace(/[\u2190-\u2BFF\uD800-\uDFFF\u3000-\u303F\uFE00-\uFE0F]/g,''))) continue;
    var el = node.parentElement; if(!el) continue;
    var tag = el.tagName;
    if(/^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE|OPTION)$/.test(tag)) continue;
    if(el.closest('svg')) continue;
    var cs = getComputedStyle(el);
    var fg = parse(cs.webkitTextFillColor && cs.webkitTextFillColor.indexOf('rgb') === 0 ? cs.webkitTextFillColor : cs.color);
    if(!fg || fg[3] === 0) continue;
    var disabled = el.closest('[disabled],[aria-disabled="true"]');
    check(el, t, fg, parseFloat(cs.fontSize), parseInt(cs.fontWeight, 10) || 400, disabled ? 'disabled' : 'text');
  }
  // form controls: typed value and placeholder
  document.querySelectorAll('input,textarea,select').forEach(function(el){
    var cs = getComputedStyle(el);
    if(/^(checkbox|radio|hidden|range|color|file|submit|button)$/.test(el.type)) return;
    var fg = parse(cs.color);
    var txt = el.tagName === 'SELECT' ? (el.options[el.selectedIndex] ? el.options[el.selectedIndex].text : '') : el.value;
    if(txt) check(el, txt, fg, parseFloat(cs.fontSize), parseInt(cs.fontWeight, 10) || 400, 'input');
    if(el.placeholder && !el.value){
      var pc = parse(getComputedStyle(el, '::placeholder').color);
      if(pc) check(el, el.placeholder, pc, parseFloat(cs.fontSize), 400, 'placeholder');
    }
  });
  // SVG text
  document.querySelectorAll('svg text').forEach(function(el){
    var cs = getComputedStyle(el), f = parse(cs.fill);
    var hal = cs.stroke && cs.stroke !== 'none' && parseFloat(cs.strokeWidth) >= 2 && cs.paintOrder.indexOf('stroke') === 0;
    if(!hal && f && f[3] > 0 && /[A-Za-z0-9]/.test(el.textContent)) check(el, el.textContent, f, parseFloat(cs.fontSize) || 12, parseInt(cs.fontWeight, 10) || 400, 'svg');
  });
  return out;
})
