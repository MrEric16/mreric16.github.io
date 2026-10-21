var BACK = back('index.html#geography-hub/study', 'Back to Train Your Brain');
function list(){ return window.LoungeAmend ? LoungeAmend.get() : []; }
function draw(){
  var a = list();
  app.innerHTML = BACK + head('Amendments', a.length + (a.length === 1 ? ' word' : ' words') + ' to review') +
    (a.length ? '<div class="v-row"><button class="v-btn alt" id="amBlur">Blur all again</button><button class="v-btn alt" id="amMix">Shuffle</button></div>' : '<div class="empty-card">Nothing to amend. Words you get wrong in the games will appear here.</div>') +
    '<div id="amList">' + a.map(function(x){
      return '<div class="v-card random-tile" data-k="' + esc(x.k) + '"><div class="v-word" style="font-size:26px;"><span class="blur">' + esc(x.w) + '</span></div>' +
        '<div class="v-def"><span class="blur">' + esc(x.d) + '</span></div>' +
        '<div style="margin-top:8px;display:flex;justify-content:space-between;align-items:center;"><span class="v-pos">' + esc(x.s) + '</span><button class="v-save" data-rm="' + esc(x.k) + '">Got it</button></div></div>';
    }).join('') + '</div>' + (a.length > 5 ? '<button class="v-save" id="amClear" style="margin-top:6px;">Clear all</button>' : '');
  app.querySelectorAll('.blur').forEach(function(b){ b.onclick = function(){ b.classList.toggle('show'); }; });
  app.querySelectorAll('[data-rm]').forEach(function(b){ b.onclick = function(){ var y = window.scrollY; LoungeAmend.remove(b.getAttribute('data-rm')); draw(); window.scrollTo(0, y); }; });
  var bl = document.getElementById('amBlur'); if(bl) bl.onclick = function(){ app.querySelectorAll('.blur.show').forEach(function(x){ x.classList.remove('show'); }); };
  var mx = document.getElementById('amMix'); if(mx) mx.onclick = function(){ var box = document.getElementById('amList'), kids = shuffle([].slice.call(box.children)); kids.forEach(function(k){ box.appendChild(k); }); };
  var cl = document.getElementById('amClear'); if(cl) cl.onclick = function(){ if(confirm('Remove all ' + list().length + ' words from Amendments?')){ LoungeAmend.clear(); draw(); } };
}
draw();
window.addEventListener('pageshow', draw);
