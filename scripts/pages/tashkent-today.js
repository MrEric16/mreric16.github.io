var BACK = back('index.html#events-hub', 'Back to Tashkent');
var D = null;
function tk(){
  try{
    var f = new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Tashkent', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false }).formatToParts(new Date()), o = {};
    f.forEach(function(p){ o[p.type] = p.value; }); o.hour = String(+o.hour % 24).padStart(2, '0');
    return { iso: o.year + '-' + o.month + '-' + o.day, min: (+o.hour) * 60 + (+o.minute), sec: (+o.hour) * 3600 + (+o.minute) * 60 + (+o.second) };
  }catch(e){ var d = new Date(); return { iso: d.toISOString().slice(0, 10), min: d.getHours() * 60 + d.getMinutes(), sec: d.getHours() * 3600 + d.getMinutes() * 60 + d.getSeconds() }; }
}
function toMin(t){ var p = t.split(':'); return (+p[0]) * 60 + (+p[1]); }
function ageH(k){ var s = D.stamps && D.stamps[k]; return s ? (Date.now() - Date.parse(s)) / 3600000 : 9999; }
function ago(iso){ var m = Math.max(0, Math.round((Date.now() - Date.parse(iso)) / 60000)); if(m < 60) return m + ' min ago'; if(m < 2880) return Math.round(m / 60) + ' h ago'; return Math.round(m / 1440) + ' days ago'; }
function airTag(){ var s = D.stamps && D.stamps.air; if(!s) return ''; var h = ageH('air'); return '<span class="td-up' + (h > 4 ? ' old' : '') + '">Updated ' + ago(s) + (h > 4 ? '. This may be out of date.' : '') + '</span>'; }
function sec(title, tag, body){ return '<section class="td-sec"><div class="td-h"><b>' + title + '</b>' + (tag || '') + '</div>' + body + '</section>'; }

/* ---------- Exchange rates ---------- */
var CUR = ['USD', 'EUR', 'GBP', 'RUB', 'AED', 'KZT', 'CNY', 'KGS'];
var NAMES = { UZS: 'Uzbekistan', USD: 'US dollar', EUR: 'Euro', GBP: 'Pound sterling', RUB: 'Russian rouble', AED: 'UAE dirham', KZT: 'Kazakhstani tenge', CNY: 'Chinese yuan', KGS: 'Kyrgyz som' };
var conv = lsGet('tashkentConv2', { from: 'USD', to: 'UZS', amt: '100' });
if(['UZS'].concat(CUR).indexOf(conv.from) < 0) conv.from = 'USD';
if(['UZS'].concat(CUR).indexOf(conv.to) < 0) conv.to = 'UZS';
function unit(c){ if(c === 'UZS') return 1; var x = D.rates.items[c]; return x.rate / x.nominal; }
function fmtN(n){ return n >= 100 ? Math.round(n).toLocaleString('en-GB') : n.toFixed(2); }
function fmtAmt(n, c){
  if(!isFinite(n)) return '';
  if(c === 'UZS') return Math.round(n).toLocaleString('en-GB');
  var a = Math.abs(n);
  if(a !== 0 && a < 0.01) return n.toLocaleString('en-GB', { maximumSignificantDigits: 3 });
  return n.toLocaleString('en-GB', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}
function fmtRate(n){
  if(n >= 1000) return Math.round(n).toLocaleString('en-GB');
  if(n >= 1) return n.toLocaleString('en-GB', { minimumFractionDigits: 2, maximumFractionDigits: 4 });
  return n.toLocaleString('en-GB', { maximumSignificantDigits: 4 });
}
function ratesStale(){
  var R = D.rates; if(!R || ageH('rates') > 30) return true;
  var p = R.date.split('.'), d = Date.UTC(+p[2], +p[1] - 1, +p[0]), t = tk().iso.split('-'), today = Date.UTC(+t[0], +t[1] - 1, +t[2]);
  return (today - d) / 86400000 > 3;
}
function opts(sel){ return ['UZS'].concat(CUR).map(function(c){ return '<option' + (c === sel ? ' selected' : '') + '>' + c + '</option>'; }).join(''); }
function rates(){
  var R = D.rates; if(!R) return sec('Exchange rates', '', '<div class="v-hint">Not available yet.</div>');
  var warn = ratesStale() ? '<div class="td-warn">These rates could not be refreshed recently and may be out of date. Check cbu.uz before you exchange money.</div>' : '';
  var h = warn + '<table class="td-tb">' + CUR.map(function(c){
    var x = R.items[c]; if(!x) return '';
    var d = x.diff / x.nominal;
    return '<tr><td><b>' + c + '</b><span>' + NAMES[c] + '</span></td><td>' + fmtN(unit(c)) + ' UZS</td><td>' + (d ? '<i class="td-ch ' + (d > 0 ? 'up' : 'dn') + '">' + (d > 0 ? '▲ ' : '▼ ') + fmtN(Math.abs(d)) + '</i>' : '') + '</td></tr>';
  }).join('') + '</table>';
  h += '<div class="td-cvh">Converter</div><input id="tdAmt" class="td-in" type="number" inputmode="decimal" value="' + esc(conv.amt) + '" aria-label="Amount">' +
    '<div class="td-cv"><select id="tdFrom" class="td-in" aria-label="From">' + opts(conv.from) + '</select><button class="td-btn" id="tdSwap" aria-label="Swap currencies">⇄</button><select id="tdTo" class="td-in" aria-label="To">' + opts(conv.to) + '</select></div>' +
    '<div id="tdRes" class="td-res"></div><div id="tdUnit" class="td-unit"></div>';
  return sec('Exchange rates', '', h);
}
function convPaint(){
  var el = document.getElementById('tdRes'), u = document.getElementById('tdUnit'); if(!el || !D.rates) return;
  var a = parseFloat(conv.amt);
  if(!isFinite(a)){ el.textContent = ''; u.textContent = ''; return; }
  var r = unit(conv.from) / unit(conv.to);
  el.textContent = a.toLocaleString('en-GB', { maximumFractionDigits: 6 }) + ' ' + conv.from + ' = ' + fmtAmt(a * r, conv.to) + ' ' + conv.to;
  u.textContent = '1 ' + conv.from + ' = ' + fmtRate(r) + ' ' + conv.to;
}

/* ---------- Prayer times ---------- */
function prayer(){
  var P = D.prayer; if(!P) return sec('Prayer times', '', '<div class="v-hint">Not available yet.</div>');
  var t = tk(), day = P.days[t.iso];
  if(!day) return sec('Prayer times', '', '<div class="td-warn">Today\'s prayer times are missing from the data. Check the Muslim Board of Uzbekistan for today\'s times.</div>');
  var keys = ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha'], nxt = null, cd = '';
  keys.forEach(function(k){ if(!nxt && toMin(day[k]) * 60 > t.sec) nxt = k; });
  if(nxt){ var d = toMin(day[nxt]) * 60 - t.sec; cd = nxt + ' in ' + Math.floor(d / 3600) + ' h ' + Math.floor((d % 3600) / 60) + ' min'; }
  else { var dt = new Date(Date.parse(t.iso + 'T00:00:00Z') + 86400000).toISOString().slice(0, 10), td = P.days[dt]; if(td){ var d2 = 86400 - t.sec + toMin(td.Fajr) * 60; cd = 'Fajr in ' + Math.floor(d2 / 3600) + ' h ' + Math.floor((d2 % 3600) / 60) + ' min'; } }
  return sec('Prayer times', '', '<div class="td-cd">' + esc(cd) + '</div><div class="td-pr">' + keys.map(function(k){ return '<div class="' + (k === nxt ? 'on' : '') + '"><span>' + k + '</span><b>' + day[k] + '</b></div>'; }).join('') + '</div>');
}

/* ---------- Air quality ---------- */
function aqiInfo(v){
  if(v <= 50) return ['Good', '#2E7D32', 'Air quality is fine for everyone.', '#fff'];
  if(v <= 100) return ['Moderate', '#E0B400', 'Fine for most people. Very sensitive people may want to cut back on long hard exercise outdoors.', '#111'];
  if(v <= 150) return ['Unhealthy for sensitive groups', '#E07B00', 'Children, older people and anyone with asthma or heart or lung problems should limit time outdoors. A mask helps on the road.', '#111'];
  if(v <= 200) return ['Unhealthy', '#C62828', 'Everyone should reduce hard outdoor exercise. Keep windows shut on busy roads.', '#fff'];
  if(v <= 300) return ['Very unhealthy', '#8F3F97', 'Avoid outdoor exercise. Stay inside with windows closed if you can.', '#fff'];
  return ['Hazardous', '#7E0023', 'Stay indoors.', '#fff'];
}
function air(){
  var A = D.air; if(!A) return sec('Air quality', '', '<div class="v-hint">Not available yet.</div>');
  var c = A.current, v = Math.round(c.us_aqi), i = aqiInfo(v), t = tk();
  var hours = A.hours.filter(function(x){ return x[0].slice(0, 10) > t.iso || (x[0].slice(0, 10) === t.iso && toMin(x[0].slice(11, 16)) >= Math.floor(t.min / 60) * 60); }).slice(0, 24);
  var bars = hours.map(function(x){ var inf = aqiInfo(x[1] == null ? 0 : x[1]); return '<i title="' + x[0].slice(11, 16) + ': ' + Math.round(x[1] || 0) + '" style="height:' + Math.max(6, Math.min(60, (x[1] || 0) / 3)) + 'px;background:' + inf[1] + '"></i>'; }).join('');
  return sec('Air quality', airTag(),
    '<div class="td-aq"><div class="td-aqn" style="background:' + i[1] + ';color:' + i[3] + ';">' + v + '</div><div><b>' + i[0] + '</b><div class="v-hint" style="margin:2px 0 0;">US AQI. PM2.5 ' + Math.round(c.pm2_5) + ' µg/m³, PM10 ' + Math.round(c.pm10) + ' µg/m³.</div></div></div>' +
    '<div class="v-hint" style="margin-top:8px;">' + esc(i[2]) + '</div>' +
    '<div class="v-hint" style="margin:10px 0 4px;font-weight:800;">Next 24 hours (model forecast)</div><div class="td-bars">' + bars + '</div>');
}

function view(){
  app.innerHTML = BACK + head('Tashkent Today', 'Exchange rates, prayer times and air quality.') + rates() + prayer() + air();
  var amt = document.getElementById('tdAmt'), f = document.getElementById('tdFrom'), t = document.getElementById('tdTo'), sw = document.getElementById('tdSwap');
  if(amt){
    function save(){ lsSet('tashkentConv2', conv); convPaint(); }
    amt.oninput = function(){ conv.amt = amt.value; save(); };
    f.onchange = function(){ conv.from = f.value; save(); };
    t.onchange = function(){ conv.to = t.value; save(); };
    sw.onclick = function(){ var x = conv.from; conv.from = conv.to; conv.to = x; f.value = conv.from; t.value = conv.to; save(); };
    convPaint();
  }
}
getJson('data/tashkent-today.json').then(function(d){ D = d; view(); setInterval(function(){ var f = document.activeElement; if(f && (f.tagName === 'INPUT' || f.tagName === 'SELECT')) return; view(); }, 60000); }).catch(function(){ app.innerHTML = BACK + '<div class="v-hint">Could not load. Check your connection.</div>'; });
