/* Back navigation shared by every page of the app.
   A "Back" link goes to the page the user actually came from, one step at a time, using the
   browser's own history. Each history entry is stamped with a position (history.state.ni) so we
   know whether there is a previous page of ours to return to. With no previous page (opened
   from a bookmark or a shared link) the link falls back to its own href. */
(function(){
  'use strict';
  if(window.BackNav) return;
  var KEY = 'navCur';
  var cur = 0, delta = 0;

  function stored(){ try{ var v = sessionStorage.getItem(KEY); var n = v === null ? NaN : parseInt(v, 10); return isNaN(n) ? null : n; }catch(e){ return null; } }
  function save(n){ try{ sessionStorage.setItem(KEY, String(n)); }catch(e){} }

  function note(){
    var s = history.state, ni = (s && typeof s === 'object' && typeof s.ni === 'number') ? s.ni : null;
    if(ni === null){
      var last = stored();
      ni = last === null ? 0 : last + 1;
      try{ history.replaceState(Object.assign({}, (s && typeof s === 'object') ? s : {}, { ni: ni }), ''); }catch(e){}
    }
    if(ni !== cur) delta = ni - cur;   /* popstate and hashchange both report one move: keep its direction */
    cur = ni; save(ni);
  }
  note();
  window.addEventListener('popstate', note);
  window.addEventListener('hashchange', note);
  window.addEventListener('pageshow', note);

  function norm(u){ return u.replace(/#$/, ''); }

  document.addEventListener('click', function(e){
    if(e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey) return;
    var a = e.target.closest && e.target.closest('a.back-link, a[data-back]');
    if(!a || a.hasAttribute('data-mt-exit') || a.getAttribute('data-nav-bypass')) return;
    var href = a.getAttribute('href'); if(!href) return;
    var target; try{ target = new URL(href, location.href); }catch(x){ return; }
    if(target.origin !== location.origin) return;
    if(norm(target.href) === norm(location.href)) return;   /* a link to the current page is a reset, not a back */
    if(cur <= 0) return;                                    /* nothing behind us: follow the link */
    e.preventDefault(); e.stopImmediatePropagation();
    var moved = false, mark = function(){ moved = true; };
    window.addEventListener('popstate', mark, { once: true });
    window.addEventListener('pagehide', mark, { once: true });
    history.back();
    setTimeout(function(){
      window.removeEventListener('popstate', mark); window.removeEventListener('pagehide', mark);
      if(moved || document.hidden) return;
      a.setAttribute('data-nav-bypass', '1'); a.click();
    }, 2500);
  }, true);

  window.BackNav = { depth: function(){ return cur; }, lastDelta: function(){ return delta; } };
})();
