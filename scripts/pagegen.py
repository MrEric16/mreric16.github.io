#!/usr/bin/env python3
"""Generates standalone Lounge pages (themed, with lounge-core.js) from vocabulary.html's head.
Usage: python3 scripts/pagegen.py   (rebuilds every page listed in PAGES)
Each page = scripts/pages/<name>.js (the app code, wrapped in an IIFE with helpers) + optional <name>.css."""
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = {
  'connections.html': 'Connections',
  'spellingbee.html': 'Spelling Bee',
  'writing.html': 'IELTS Writing Checker',
  'listening.html': 'Listening Practice',
  'tashkent-route.html': 'Getting Around Tashkent',
  'tashkent-today.html': 'Tashkent Today',
  'speaking.html': 'Speaking Practice',
  'collocations.html': 'Collocations and Phrasal Verbs',
  'wordforms.html': 'Word Forms',
  'mocktimer.html': 'Exam Timer',
}
HELPERS = r"""
var app = document.getElementById('app');
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function shuffle(a){ a = a.slice(); for(var i=a.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function lsGet(k, d){ try{ var v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); }catch(e){ return d; } }
function lsSet(k, v){ try{ localStorage.setItem(k, JSON.stringify(v)); }catch(e){} }
function back(href, text){ return '<a class="back-link" href="' + href + '">← ' + text + '</a>'; }
function head(title, sub){ return '<div class="section-head" style="margin-top:8px;"><h2>' + title + '</h2></div>' + (sub ? '<div class="v-sub">' + sub + '</div>' : ''); }
function getJson(u){ return fetch(u, { cache: 'no-cache' }).then(function(r){ if(!r.ok) throw new Error('HTTP ' + r.status); return r.json(); }); }
function dayNumber(){ var d = new Date(); return Math.floor(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 86400000); }
function award(n, why){ if(window.LoungeXP) LoungeXP.award(n, why); }
"""
COMMON_CSS = """
.sp-card{border:1px solid var(--line);}
input::placeholder,textarea::placeholder{color:var(--ink-soft); opacity:.9;}
.tr-f input,.ls-in,.wf-in{border:2px solid var(--line);}
.gg-lvl,.gg-btn-main,.v-btn,.cl-tabs button.on,.cn-tile.sel,.mt-tabs button.on,.wr-sel button.on,.wf-base{color:var(--on-coral,#fff) !important;}
"""
ONCORAL = r"""
(function(){ try{
  var c = getComputedStyle(document.body).getPropertyValue('--coral').trim(), e = document.createElement('i'); e.style.color = c; document.body.appendChild(e);
  var m = getComputedStyle(e).color.match(/\d+(\.\d+)?/g); document.body.removeChild(e); if(!m) return;
  function L(v){ v = v / 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }
  var l = 0.2126 * L(+m[0]) + 0.7152 * L(+m[1]) + 0.0722 * L(+m[2]);
  document.body.style.setProperty('--on-coral', (1.05 / (l + 0.05)) >= ((l + 0.05) / 0.0556) ? '#fff' : '#111');
}catch(e){} })();
"""
def build():
    src = open(os.path.join(ROOT, 'vocabulary.html'), encoding='utf8').read()
    pre = src.split('<div class="wrap" id="app">')[0]
    for fn, title in PAGES.items():
        name = fn[:-5]
        jsf = os.path.join(ROOT, 'scripts', 'pages', name + '.js')
        if not os.path.exists(jsf): continue
        js = open(jsf, encoding='utf8').read()
        cssf = os.path.join(ROOT, 'scripts', 'pages', name + '.css')
        css = open(cssf, encoding='utf8').read() if os.path.exists(cssf) else ''
        head_ = re.sub(r'<title>.*?</title>', "<title>%s | Mr Eric's Lounge</title>" % title, pre)
        head_ = head_.replace('</head>', '<style>\n' + COMMON_CSS + css + '\n</style>\n</head>')
        html = head_ + '<div class="wrap" id="app"><div class="empty-card">Loading…</div></div>\n<script>\n(function(){\n' + ONCORAL + HELPERS + js + '\n})();\n</script>\n</body>\n</html>\n'
        open(os.path.join(ROOT, fn), 'w', encoding='utf8').write(html)
        print('built', fn, len(html) // 1024, 'KB')
if __name__ == '__main__':
    build()
