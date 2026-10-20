/* Mr Eric's Lounge shared core: XP + levels, cross-device sync (sync code), My Stats cards.
   Loaded by index.html, vocabulary.html and grammar.html. No dependencies.
   Sync talks to two Supabase RPCs (sync_get / sync_put); the table itself is not readable by the public. */
(function(){
  'use strict';
  if(window.LoungeCore) return;

  var SB_URL = 'https://uugjyucgeyopyvmhckdg.supabase.co';
  var SB_KEY = 'sb_publishable_F-idKUOOIWIpm7sMRtR-mA_m5Zir3Na';
  var ls = window.localStorage;
  var origSetItem = Storage.prototype.setItem;
  var rawSet = origSetItem.bind(ls);
  var rawGet = ls.getItem.bind(ls);
  var rawRemove = ls.removeItem.bind(ls);
  var applying = false; // true while sync merge writes, so the hook ignores them

  /* ---------- small helpers ---------- */
  function jget(k, d){ try{ var v = rawGet(k); return v === null ? d : JSON.parse(v); }catch(e){ return d; } }
  function jset(k, v){ try{ rawSet(k, JSON.stringify(v)); }catch(e){} }
  function today(){ var d = new Date(); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); }
  function esc(s){ return String(s).replace(/[&<>"']/g, function(c){ return ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[c]; }); }

  /* ---------- which keys sync ---------- */
  var SYNC_RE = /(Best|best|Streak|Wins|Played$|Moves)|^(vocabSaved|vocabBest_|bookmarks$|readArticles$|watchedVideos$|visitedFaculties$|unlockedBadges$|longestStreak$|totalActiveTimeMs$|siteOpenCount$|facultyVisitCount$|ggs_|xp\.)/;
  function isSynced(k){
    if(k === 'syncCode' || k === 'syncMeta' || k === 'xp.dev' || k === 'themeChoice' || k === 'darkMode') return false;
    if(/State_v1$/.test(k) || /LastPlayedDate$/.test(k)) return false;
    return SYNC_RE.test(k);
  }

  /* ---------- merge (never loses progress) ---------- */
  function mergeVal(a, b){
    if(a === undefined) return b;
    if(b === undefined) return a;
    if(typeof a === 'number' && typeof b === 'number') return Math.max(a, b);
    if(typeof a === 'boolean' && typeof b === 'boolean') return a || b;
    if(typeof a === 'string' && typeof b === 'string') return a >= b ? a : b; // ISO dates: later wins
    if(Array.isArray(a) && Array.isArray(b)){
      var seen = {}, out = [];
      a.concat(b).forEach(function(x){ var s = JSON.stringify(x); if(!seen[s]){ seen[s] = 1; out.push(x); } });
      return out;
    }
    if(a && b && typeof a === 'object' && typeof b === 'object' && !Array.isArray(a) && !Array.isArray(b)){
      var o = {};
      Object.keys(a).concat(Object.keys(b)).forEach(function(k){ if(!(k in o)) o[k] = mergeVal(a[k], b[k]); });
      return o;
    }
    return a;
  }
  function mergeKey(k, localRaw, remoteRaw){
    if(localRaw === null || localRaw === undefined) return remoteRaw;
    if(remoteRaw === null || remoteRaw === undefined) return localRaw;
    if(localRaw === remoteRaw) return localRaw;
    var a, b;
    try{ a = JSON.parse(localRaw); b = JSON.parse(remoteRaw); }catch(e){ return localRaw; }
    if(/^ggs_/.test(k)){ // grammar set state: whole-object, higher score wins, tie keeps local
      var sa = a && a.score != null ? a.score : -1, sb = b && b.score != null ? b.score : -1;
      return JSON.stringify(sb > sa ? b : a);
    }
    return JSON.stringify(mergeVal(a, b));
  }

  /* ---------- sync ---------- */
  function rpc(fn, body){
    return fetch(SB_URL + '/rest/v1/rpc/' + fn, {
      method: 'POST',
      headers: { 'apikey': SB_KEY, 'Authorization': 'Bearer ' + SB_KEY, 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      keepalive: JSON.stringify(body).length < 60000
    }).then(function(r){ if(!r.ok) throw new Error('HTTP ' + r.status); return r.json(); });
  }
  function snapshot(){
    var d = {};
    for(var i = 0; i < ls.length; i++){ var k = ls.key(i); if(isSynced(k)) d[k] = rawGet(k); }
    return d;
  }
  var syncing = false, dirtyTimer = null;
  var Sync = {
    code: function(){ return rawGet('syncCode') || ''; },
    status: function(){ return jget('syncMeta', {}); },
    _make: function(){
      var al = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789', out = '', arr = new Uint8Array(12);
      (window.crypto || window.msCrypto).getRandomValues(arr);
      for(var i = 0; i < 12; i++) out += al[arr[i] % al.length];
      return out;
    },
    run: function(){
      var code = Sync.code();
      if(!code || syncing || !navigator.onLine) return Promise.resolve(false);
      syncing = true;
      return rpc('sync_get', { p_code: code }).then(function(res){
        var remote = (res && res.data) || {};
        applying = true;
        try{
          Object.keys(remote).forEach(function(k){
            if(!isSynced(k)) return;
            var merged = mergeKey(k, rawGet(k), remote[k]);
            if(merged !== rawGet(k)) rawSet(k, merged);
          });
        } finally { applying = false; }
        return rpc('sync_put', { p_code: code, p_data: snapshot() });
      }).then(function(){
        jset('syncMeta', { last: Date.now() });
        syncing = false; LoungeUI.refresh(); XP.refresh();
        return true;
      }).catch(function(e){
        syncing = false; jset('syncMeta', { last: (Sync.status().last || 0), err: String(e && e.message || e) });
        return false;
      });
    },
    create: function(){
      var code = Sync._make();
      rawSet('syncCode', code);
      return Sync.run().then(function(ok){ if(!ok){ rawRemove('syncCode'); throw new Error('Could not reach the server.'); } return code; });
    },
    join: function(raw){
      var code = String(raw || '').toUpperCase().replace(/[^A-Z0-9]/g, '');
      if(code.length < 10) return Promise.reject(new Error('That code is too short.'));
      return rpc('sync_get', { p_code: code }).then(function(res){
        if(!res || !res.data) throw new Error('No profile found for that code.');
        rawSet('syncCode', code);
        return Sync.run().then(function(){ return code; });
      });
    },
    disconnect: function(){ rawRemove('syncCode'); rawRemove('syncMeta'); },
    markDirty: function(){
      if(!Sync.code()) return;
      clearTimeout(dirtyTimer);
      dirtyTimer = setTimeout(function(){ Sync.run(); }, 8000);
    }
  };

  /* ---------- XP ---------- */
  var LEVEL_NAMES = ['Newcomer','Learner','Reader','Thinker','Scholar','Analyst','Linguist','Strategist','Expert','Master','Professor','Sage','Legend'];
  function devId(){
    var d = rawGet('xp.dev');
    if(!d){ d = Math.random().toString(36).slice(2, 8); rawSet('xp.dev', d); }
    return d;
  }
  function totalXP(){
    var m = jget('xp.byDevice', {}), t = 0;
    Object.keys(m).forEach(function(k){ t += (+m[k] || 0); });
    return t;
  }
  // cumulative XP needed to reach level n+1 is 50*n*(n+1): 100, 300, 600, 1000 ...
  function levelOf(xp){
    var n = Math.floor((-1 + Math.sqrt(1 + xp / 12.5)) / 2);
    var cur = 50 * n * (n + 1), next = 50 * (n + 1) * (n + 2);
    return { level: n + 1, name: LEVEL_NAMES[Math.min(n, LEVEL_NAMES.length - 1)], into: xp - cur, span: next - cur, toNext: next - xp };
  }
  function streakDays(){ var s = jget('visitStreak', { count: 1 }); return Math.max(1, +s.count || 1); }
  function multiplier(){ return 1 + Math.min(streakDays(), 10) / 10; }
  var pending = 0, toastTimer = null;
  function toast(msg){
    var t = document.getElementById('xpToast');
    if(!t){
      t = document.createElement('div'); t.id = 'xpToast';
      t.style.cssText = 'position:fixed;left:50%;transform:translateX(-50%);bottom:calc(var(--tabbar-h,0px) + 78px);background:var(--ink,#222);color:var(--bg,#fff);padding:8px 16px;border-radius:999px;font:800 13px Nunito,system-ui,sans-serif;z-index:9999;opacity:0;transition:opacity .25s;pointer-events:none;';
      document.body.appendChild(t);
    }
    t.textContent = msg; t.style.opacity = '1';
    clearTimeout(toastTimer); toastTimer = setTimeout(function(){ t.style.opacity = '0'; }, 1600);
  }
  var XP = {
    total: totalXP,
    info: function(){ return levelOf(totalXP()); },
    multiplier: multiplier,
    award: function(n, why){
      n = Math.max(0, +n || 0); if(!n) return 0;
      var amt = Math.max(1, Math.round(n * multiplier()));
      var before = levelOf(totalXP()).level;
      var m = jget('xp.byDevice', {}); var id = devId();
      m[id] = (+m[id] || 0) + amt; jset('xp.byDevice', m);
      var after = levelOf(totalXP());
      pending += amt;
      clearTimeout(XP._t);
      XP._t = setTimeout(function(){
        toast('+' + pending + ' XP' + (after.level > before ? '  •  Level ' + after.level + ': ' + after.name : '')); pending = 0;
      }, 350);
      if(after.level > before) toast('Level ' + after.level + ': ' + after.name);
      XP.refresh(); Sync.markDirty();
      return amt;
    },
    daily: function(){
      var t = today();
      if(rawGet('xp.lastDaily') === t) return;
      rawSet('xp.lastDaily', t);
      XP.award(20, 'daily');
    },
    refresh: function(){
      var chip = document.getElementById('xpChip');
      if(chip){ var i = XP.info(); chip.querySelector('.xp-lv').textContent = 'Lv ' + i.level; }
    }
  };

  /* ---------- automatic awards from existing games ---------- */
  // Existing games already write these counters. A rise in a streak counter = a correct answer (+1);
  // a rise in a wins / games-played counter = a finished game (+10); a higher best score = +5.
  Storage.prototype.setItem = function(k, v){
    if(this !== ls) return origSetItem.call(this, k, v);
    var old = null;
    try{ old = rawGet(k); }catch(e){}
    origSetItem.call(this, k, v);
    if(applying) return;
    try{
      if(isSynced(k) && !/^xp\./.test(k)) Sync.markDirty();
      var nv = parseFloat(v), ov = parseFloat(old);
      if(!isFinite(nv) || String(nv) !== String(v).trim()) return;
      if(!isFinite(ov)) ov = 0;
      if(nv <= ov) return;
      if(/^(visitStreak|longestStreak|siteOpenCount|facultyVisitCount|totalActiveTimeMs)$/.test(k)) return;
      if(/Streak$/.test(k) && !/best/i.test(k)) XP.award(1, 'correct');
      else if(/(Wins|GamesPlayed|Played)$/.test(k)) XP.award(10, 'finish');
      else if(/Best(Score)?$/.test(k) && ov > 0) XP.award(5, 'best');
    }catch(e){}
  };

  /* ---------- header chip (main app only) ---------- */
  function mountChip(){
    var row = document.querySelector('.header-icon-row');
    if(!row || document.getElementById('xpChip')) return;
    var a = document.createElement('a');
    a.id = 'xpChip'; a.className = 'search-icon-btn'; a.href = 'index.html#my-stats'; a.title = 'Your level, XP and streak';
    a.style.cssText = 'width:auto;padding:0 10px;gap:4px;display:inline-flex;align-items:center;font:800 12px Nunito,system-ui,sans-serif;text-decoration:none;';
    a.innerHTML = '<span aria-hidden="true">⚡</span><span class="xp-lv">Lv 1</span>';
    row.insertBefore(a, row.firstChild);
    XP.refresh();
  }

  /* ---------- My Stats cards ---------- */
  var card = 'background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px;margin-bottom:14px;text-align:left;';
  var btn = 'display:inline-block;padding:9px 16px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--ink);font:800 13px Nunito,system-ui,sans-serif;cursor:pointer;margin:6px 8px 0 0;';
  var LoungeUI = {
    mountStats: function(){
      var host = document.getElementById('loungeCards');
      if(!host) return;
      host.innerHTML = '<div id="xpCard"></div><div id="syncCard"></div><div id="offlineCard"></div>';
      LoungeUI.refresh();
      if(window.LoungeOffline && LoungeOffline.mount) LoungeOffline.mount(document.getElementById('offlineCard'));
    },
    refresh: function(){
      var x = document.getElementById('xpCard'), s = document.getElementById('syncCard');
      if(x){
        var i = XP.info(), pct = Math.min(100, Math.round(i.into / i.span * 100));
        x.innerHTML = '<div style="' + card + '"><div style="display:flex;justify-content:space-between;align-items:baseline;gap:8px;"><b style="font-size:17px;">Level ' + i.level + ': ' + esc(i.name) + '</b><span style="opacity:.7;font-size:13px;">' + totalXP() + ' XP</span></div>' +
          '<div style="height:10px;border-radius:99px;background:var(--line);margin:10px 0 6px;overflow:hidden;"><div style="height:100%;width:' + pct + '%;background:var(--coral,#c0392b);"></div></div>' +
          '<div style="font-size:12.5px;opacity:.75;">' + i.toNext + ' XP to level ' + (i.level + 1) + '. Today\'s multiplier: x' + multiplier().toFixed(1) + ' (grows with your daily streak, up to x2).</div></div>';
      }
      if(s){
        var code = Sync.code(), st = Sync.status();
        if(code){
          var when = st.last ? new Date(st.last).toLocaleString() : 'not yet';
          s.innerHTML = '<div style="' + card + '"><b>Sync is on</b><div style="font-size:13px;opacity:.8;margin-top:6px;">Your sync code: <b style="letter-spacing:2px;font-size:16px;user-select:all;">' + esc(code.replace(/(.{4})/g, '$1 ').trim()) + '</b></div>' +
            '<div style="font-size:12.5px;opacity:.7;margin-top:4px;">Enter this code on your other device. Last synced: ' + esc(when) + (st.err ? '. Last attempt failed (' + esc(st.err) + ').' : '.') + '</div>' +
            '<button style="' + btn + '" id="syncNow">Sync now</button><button style="' + btn + '" id="syncOff">Turn off on this device</button>' +
            '<div style="font-size:12px;opacity:.65;margin-top:8px;">Syncs scores, streaks, XP, saved words and bookmarks. Anyone with the code can see them, so do not share it. Removing a saved word on one device does not remove it on another.</div></div>';
        } else {
          s.innerHTML = '<div style="' + card + '"><b>Sync across devices</b><div style="font-size:13px;opacity:.8;margin:6px 0;">Keep your scores, XP, streaks and saved words on your phone, laptop and tablet. No account or email needed.</div>' +
            '<button style="' + btn + '" id="syncNew">Create a sync code</button>' +
            '<div style="margin-top:8px;"><input id="syncIn" placeholder="Or enter a code" autocapitalize="characters" autocomplete="off" style="padding:9px 12px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--ink);font:700 14px Nunito,system-ui,sans-serif;width:170px;max-width:60%;"><button style="' + btn + 'margin-left:8px;" id="syncJoin">Connect</button></div>' +
            '<div id="syncMsg" style="font-size:12.5px;margin-top:6px;"></div></div>';
        }
        var msg = function(t){ var m = document.getElementById('syncMsg'); if(m) m.textContent = t; };
        var q = function(id, fn){ var e = document.getElementById(id); if(e) e.onclick = fn; };
        q('syncNew', function(){ msg('Creating...'); Sync.create().then(LoungeUI.refresh).catch(function(e){ msg(e.message); }); });
        q('syncJoin', function(){ msg('Connecting...'); Sync.join(document.getElementById('syncIn').value).then(LoungeUI.refresh).catch(function(e){ msg(e.message); }); });
        q('syncNow', function(){ this.textContent = 'Syncing...'; Sync.run().then(LoungeUI.refresh); });
        q('syncOff', function(){ if(confirm('Turn sync off on this device? Your data stays here and on the server.')){ Sync.disconnect(); LoungeUI.refresh(); } });
      }
    }
  };

  window.LoungeCore = { XP: XP, Sync: Sync, UI: LoungeUI };
  window.LoungeXP = XP; window.LoungeSync = Sync;

  function boot(){
    mountChip(); XP.daily(); XP.refresh();
    if(Sync.code()) Sync.run();
    document.addEventListener('visibilitychange', function(){ if(document.visibilityState === 'hidden' && Sync.code()) Sync.run(); else if(document.visibilityState === 'visible' && Sync.code()) Sync.run(); });
    window.addEventListener('online', function(){ if(Sync.code()) Sync.run(); });
  }
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
  window.LoungeUI = LoungeUI;
})();
