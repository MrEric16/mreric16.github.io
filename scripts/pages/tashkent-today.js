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
function ago(iso){ if(!iso) return 'unknown'; var m = Math.max(0, Math.round((Date.now() - Date.parse(iso)) / 60000)); if(m < 60) return m + ' min ago'; if(m < 2880) return Math.round(m / 60) + ' h ago'; return Math.round(m / 1440) + ' days ago'; }
function staleTag(k, limitH){ var s = D.stamps && D.stamps[k]; if(!s) return ''; var h = (Date.now() - Date.parse(s)) / 3600000; return '<span class="td-up' + (h > limitH ? ' old' : '') + '">Updated ' + ago(s) + (h > limitH ? '. This may be out of date.' : '') + '</span>'; }
var NAMES = { fajr: 'Fajr', sunrise: 'Sunrise', dhuhr: 'Dhuhr', asr: 'Asr', maghrib: 'Maghrib', isha: 'Isha' };
function prayer(){
  var P = D.prayer; if(!P) return '<div class="sp-card"><b>Prayer times</b><div class="v-hint">Not available yet.</div></div>';
  var t = tk(), day = P.days[t.iso];
  if(!day) return '<div class="sp-card"><b>Prayer times</b><div class="v-hint">Today\'s times are not in the data yet. Check back after the next update.</div></div>';
  var keys = ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha'], nxt = null;
  keys.forEach(function(k){ if(!nxt && toMin(day[k]) * 60 > t.sec) nxt = k; });
  var tom = null, cd = '';
  if(nxt){ var d = toMin(day[nxt]) * 60 - t.sec; cd = nxt + ' in ' + Math.floor(d / 3600) + ' h ' + Math.floor((d % 3600) / 60) + ' min'; }
  else { var dt = new Date(Date.parse(t.iso + 'T00:00:00Z') + 86400000).toISOString().slice(0, 10), td = P.days[dt]; if(td){ var d2 = 86400 - t.sec + toMin(td.Fajr) * 60; cd = 'Fajr in ' + Math.floor(d2 / 3600) + ' h ' + Math.floor((d2 % 3600) / 60) + ' min'; } }
  return '<div class="sp-card"><div style="display:flex;justify-content:space-between;align-items:baseline;"><b style="font-size:18px;">Prayer times</b>' + staleTag('prayer', 24 * 20) + '</div>' +
    '<div class="v-hint" style="margin:2px 0 8px;font-weight:800;">' + esc(cd) + '</div>' +
    '<div class="td-pr">' + keys.map(function(k){ return '<div class="' + (k === nxt ? 'on' : '') + '"><span>' + k + '</span><b>' + day[k] + '</b></div>'; }).join('') + '</div>' +
    '<div class="v-hint" style="margin-top:8px;">Calculated for Tashkent: ' + esc(P.method) + '. The Muslim Board of Uzbekistan timetable can differ by a few minutes, so check it for exact times.</div></div>';
}
var PREF = ['USD', 'EUR', 'RUB', 'GBP', 'KZT', 'TRY', 'CNY', 'AED', 'KRW', 'JPY', 'CHF', 'KGS'];
var conv = lsGet('tashkentConv', { cur: 'USD', amt: '100', dir: 'to' });
function unit(c){ var x = D.rates.items[c]; return x.rate / x.nominal; }
function fmtN(n){ return n >= 100 ? Math.round(n).toLocaleString('en-GB') : n.toFixed(2); }
function rates(){
  var R = D.rates; if(!R) return '<div class="sp-card"><b>Exchange rates</b><div class="v-hint">Not available yet.</div></div>';
  var cur = PREF.filter(function(c){ return R.items[c]; });
  var h = '<div class="sp-card"><div style="display:flex;justify-content:space-between;align-items:baseline;"><b style="font-size:18px;">Exchange rates (UZS)</b>' + staleTag('rates', 36) + '</div><div class="v-hint" style="margin:2px 0 8px;">Official Central Bank rate for ' + esc(R.date) + '. Banks and exchange offices buy and sell at different prices.</div>';
  h += '<table class="td-tb">' + cur.map(function(c){ var x = R.items[c], d = x.diff / x.nominal; return '<tr><td><b>' + c + '</b></td><td>' + fmtN(unit(c)) + '</td><td class="' + (d > 0 ? 'up' : d < 0 ? 'dn' : '') + '">' + (d > 0 ? '▲ ' : d < 0 ? '▼ ' : '') + (d ? fmtN(Math.abs(d)) : '') + '</td></tr>'; }).join('') + '</table>';
  h += '<div class="td-cv"><input id="tdAmt" type="number" inputmode="decimal" value="' + esc(conv.amt) + '"><select id="tdCur">' + cur.map(function(c){ return '<option' + (c === conv.cur ? ' selected' : '') + '>' + c + '</option>'; }).join('') + '</select><button class="tr-loc" id="tdDir">' + (conv.dir === 'to' ? 'to UZS' : 'from UZS') + '</button></div><div id="tdRes" class="td-res"></div></div>';
  return h;
}
function convPaint(){
  var a = parseFloat(conv.amt), el = document.getElementById('tdRes'); if(!el || !D.rates || !D.rates.items[conv.cur]) return;
  if(!isFinite(a)){ el.textContent = ''; return; }
  var u = unit(conv.cur); el.textContent = conv.dir === 'to' ? a.toLocaleString('en-GB') + ' ' + conv.cur + ' = ' + Math.round(a * u).toLocaleString('en-GB') + ' soum' : a.toLocaleString('en-GB') + ' soum = ' + (a / u).toLocaleString('en-GB', { maximumFractionDigits: 2 }) + ' ' + conv.cur;
}
function aqiInfo(v){
  if(v <= 50) return ['Good', '#3E9B4F', 'Air quality is fine for everyone.'];
  if(v <= 100) return ['Moderate', '#C9A400', 'Fine for most people. Very sensitive people may want to cut back on long hard exercise outdoors.'];
  if(v <= 150) return ['Unhealthy for sensitive groups', '#E07B00', 'Children, older people and anyone with asthma or heart or lung problems should limit time outdoors. A mask helps on the road.'];
  if(v <= 200) return ['Unhealthy', '#D8352A', 'Everyone should reduce hard outdoor exercise. Keep windows shut on busy roads.'];
  if(v <= 300) return ['Very unhealthy', '#8F3F97', 'Avoid outdoor exercise. Stay inside with windows closed if you can.'];
  return ['Hazardous', '#7E0023', 'Stay indoors.'];
}
function air(){
  var A = D.air; if(!A) return '<div class="sp-card"><b>Air quality</b><div class="v-hint">Not available yet.</div></div>';
  var c = A.current, v = Math.round(c.us_aqi), i = aqiInfo(v), t = tk();
  var hours = A.hours.filter(function(x){ return x[0].slice(0, 10) > t.iso || (x[0].slice(0, 10) === t.iso && toMin(x[0].slice(11, 16)) >= Math.floor(t.min / 60) * 60); }).slice(0, 24);
  var bars = hours.map(function(x){ var inf = aqiInfo(x[1] == null ? 0 : x[1]); return '<i title="' + x[0].slice(11, 16) + ': ' + Math.round(x[1] || 0) + '" style="height:' + Math.max(6, Math.min(60, (x[1] || 0) / 3)) + 'px;background:' + inf[1] + '"></i>'; }).join('');
  return '<div class="sp-card"><div style="display:flex;justify-content:space-between;align-items:baseline;"><b style="font-size:18px;">Air quality</b>' + staleTag('air', 4) + '</div>' +
    '<div class="td-aq"><div class="td-aqn" style="background:' + i[1] + ';">' + v + '</div><div><b>' + i[0] + '</b><div class="v-hint" style="margin:2px 0 0;">US AQI. PM2.5 ' + Math.round(c.pm2_5) + ' µg/m³, PM10 ' + Math.round(c.pm10) + ' µg/m³.</div></div></div>' +
    '<div class="v-hint" style="margin-top:8px;">' + esc(i[2]) + '</div>' +
    '<div class="v-hint" style="margin:10px 0 4px;font-weight:800;">Next 24 hours (model forecast)</div><div class="td-bars">' + bars + '</div>' +
    '<div class="v-hint" style="margin-top:6px;">Modelled for the city as a whole by Open-Meteo, not measured at your street. Real readings near busy roads and in winter can be worse.</div></div>';
}
function view(){
  app.innerHTML = BACK + head('Tashkent Today', 'Prayer times, official exchange rates and air quality.') + prayer() + rates() + air();
  var amt = document.getElementById('tdAmt'), cur = document.getElementById('tdCur'), dir = document.getElementById('tdDir');
  if(amt){
    amt.oninput = function(){ conv.amt = amt.value; lsSet('tashkentConv', conv); convPaint(); };
    cur.onchange = function(){ conv.cur = cur.value; lsSet('tashkentConv', conv); convPaint(); };
    dir.onclick = function(){ conv.dir = conv.dir === 'to' ? 'from' : 'to'; dir.textContent = conv.dir === 'to' ? 'to UZS' : 'from UZS'; lsSet('tashkentConv', conv); convPaint(); };
    convPaint();
  }
}
getJson('data/tashkent-today.json').then(function(d){ D = d; view(); setInterval(function(){ var f = document.activeElement; if(f && f.tagName === 'INPUT') return; view(); }, 60000); }).catch(function(){ app.innerHTML = BACK + '<div class="v-hint">Could not load. Check your connection.</div>'; });
