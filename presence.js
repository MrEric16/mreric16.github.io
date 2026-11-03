/* Counts students on the separate pages (Globe, Languages, Grammar, books...) in the "N users on the site right now"
   footer on the main page. Joins the same Realtime presence channel as index.html and just tracks itself.
   busy:true keeps these pages out of game-challenge invites, which only the main page can answer. */
(function(){
  'use strict';
  if(window.__loungePresence) return; window.__loungePresence = true;
  var URL_ = 'https://uugjyucgeyopyvmhckdg.supabase.co', KEY = 'sb_publishable_F-idKUOOIWIpm7sMRtR-mA_m5Zir3Na';
  function start(){
    try{
      if(!window.supabase || !window.supabase.createClient) return;
      var client = window.supabase.createClient(URL_, KEY);
      var key = Math.random().toString(36).slice(2) + '-' + Date.now();
      var ch = client.channel('site-presence', { config: { presence: { key: key } } });
      ch.subscribe(function(status){
        if(status === 'SUBSCRIBED'){ try{ ch.track({ online_at: new Date().toISOString(), busy: true, page: (location.pathname.split('/').pop() || '').replace(/\.html$/, '') }); }catch(e){} }
      });
    }catch(e){}
  }
  function load(){
    if(window.supabase && window.supabase.createClient) return start();
    var s = document.createElement('script');
    s.src = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2'; s.async = true; s.onload = start;
    document.head.appendChild(s);
  }
  if(document.readyState === 'complete') load(); else window.addEventListener('load', load);
})();
