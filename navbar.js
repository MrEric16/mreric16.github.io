/* Shared bottom bar + fast return to the main page for the separate pages.
   - Bar: Home / Brain Train / (this page's own section).
   - Any link to index.html jumps BACK in history to the main page entry when one exists
     (the main page is restored instead of being downloaded and rebuilt), then lands on the
     wanted route. Falls back to a normal link when it cannot. */
(function(){
  var file = (location.pathname.split('/').pop() || '').toLowerCase();
  var SECTION = {
    'reading.html':['Study','index.html#geography-hub/study'],
    'listening.html':['Study','index.html#geography-hub/study'],
    'speaking.html':['Study','index.html#geography-hub/study'],
    'amendments.html':['Study','index.html#geography-hub/study'],
    'writing-hub.html':['Study','index.html#geography-hub/study'],
    'languages.html':['Study','index.html#geography-hub/study'],
    'grammar.html':['Study','index.html#geography-hub/study'],
    'vocabulary.html':['Vocabulary','index.html#vocab-hub'],
    'collocations.html':['Vocabulary','index.html#vocab-hub'],
    'wordforms.html':['Vocabulary','index.html#vocab-hub'],
    'tashkent-today.html':['Tashkent','index.html#events-hub'],
    'writing.html':['Writing','writing-hub.html'],
    'writing-models.html':['Writing','writing-hub.html'],
    'writing-band9.html':['Writing','writing-hub.html']
  };
  var NOBAR = {'globe.html':1,'book.html':1,'board.html':1};

  function isIndexUrl(u){
    try{
      var x = new URL(u, location.href);
      if (x.origin !== location.origin) return false;
      var f = x.pathname.split('/').pop().toLowerCase();
      return f === '' || f === 'index.html';
    }catch(e){ return false; }
  }

  function goIndex(href){
    var target = new URL(href, location.href);
    var hash = target.hash || '#';
    try{
      var nav = window.navigation;
      if (nav && nav.entries && nav.traverseTo){
        var es = nav.entries(), cur = nav.currentEntry ? nav.currentEntry.index : -1;
        for (var i = cur - 1; i >= 0; i--){
          if (isIndexUrl(es[i].url)){
            try{ sessionStorage.setItem('__goto', JSON.stringify({h:hash, t:Date.now()})); }catch(e){}
            nav.traverseTo(es[i].key);
            return true;
          }
        }
      }
    }catch(e){}
    return false;
  }

  document.addEventListener('click', function(e){
    if (e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || a.target === '_blank') return;
    var h = a.getAttribute('href');
    if (!h || h.charAt(0) === '#' || !isIndexUrl(h)) return;
    if (goIndex(h)) e.preventDefault();
  }, true);

  if (NOBAR[file]) return;
  var sec = SECTION[file];

  var css = document.createElement('style');
  css.textContent =
    '#nbar{position:fixed;left:0;right:0;bottom:0;z-index:50;display:flex;justify-content:center;gap:0;' +
    'background:var(--card,#fff);border-top:1px solid var(--line,rgba(0,0,0,.12));' +
    'padding:0 6px calc(env(safe-area-inset-bottom,0px));box-shadow:0 -2px 10px rgba(0,0,0,.06);}' +
    '#nbar a{flex:1 1 0;max-width:200px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;' +
    'height:46px;text-decoration:none;color:var(--ink-soft,#666);font:700 11px/1.1 Nunito,-apple-system,Segoe UI,Roboto,sans-serif;}' +
    '#nbar a:active{background:rgba(127,127,127,.15);}' +
    '#nbar svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}' +
    'body{padding-bottom:calc(52px + env(safe-area-inset-bottom,0px)) !important;}' +
    '@media print{#nbar{display:none}body{padding-bottom:0 !important}}';
  document.head.appendChild(css);

  var ICON = {
    home:'<svg viewBox="0 0 24 24"><path d="M3 11l9-8 9 8"/><path d="M5 10v10h5v-6h4v6h5V10"/></svg>',
    brain:'<svg viewBox="0 0 24 24"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/></svg>',
    sec:'<svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h10"/></svg>'
  };
  function build(){
    if (document.getElementById('nbar')) return;
    var n = document.createElement('nav'); n.id = 'nbar'; n.setAttribute('aria-label','Quick navigation');
    var h = '<a href="index.html">' + ICON.home + 'Home</a>' +
            '<a href="index.html#geography-hub">' + ICON.brain + 'Brain Train</a>';
    if (sec) h += '<a href="' + sec[1] + '">' + ICON.sec + sec[0] + '</a>';
    n.innerHTML = h;
    document.body.appendChild(n);
  }
  if (document.body) build(); else document.addEventListener('DOMContentLoaded', build);
})();
