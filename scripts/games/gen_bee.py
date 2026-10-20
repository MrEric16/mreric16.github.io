#!/usr/bin/env python3
"""Builds data/games/bee.json (Spelling Bee puzzles).
Inputs (not committed): /tmp/words_alpha.txt (dwyl/english-words), /usr/share/hunspell/en_US.dic (proper-noun filter), wordfreq.
Answer words = in words_alpha AND common enough (wordfreq zipf >= 2.9) AND accepted lowercase by the en_US hunspell dictionary (drops proper nouns) AND not US-only spelling AND not on the blocklist.
Puzzles avoid the letter S (no plural explosion). Each puzzle stores its full accepted-word list, so the page needs no dictionary."""
import json, random, re, itertools, collections
from wordfreq import zipf_frequency
from spylls.hunspell import Dictionary
HS=Dictionary.from_files('/usr/share/hunspell/en_US')
random.seed(20261020)
words=set(w.strip().lower() for w in open('/tmp/words_alpha.txt') if w.strip())
dic=open('/usr/share/hunspell/en_US.dic',encoding='latin-1').read().split('\n')[1:]
lower_ok=set(); cap=set()
for l in dic:
    w=l.split('/')[0].strip()
    if not w: continue
    (lower_ok if w[0].islower() else cap).add(w.lower())
proper=cap-lower_ok
US_ONLY=set("""color colors colored favor favors favored favorite favorites honor honors honored labor labors neighbor neighbors humor flavor flavors harbor harbors center centers theater theaters fiber defense offense behavior behaviors endeavor rumor vapor vigor valor armor candor clamor glamor parlor savior splendor tumor odor ardor rigor saber somber skeptic skeptical catalog dialog analog pajamas gray mold plow tire aluminum jewelry mustache sulfur cozy donut draft maneuver specter liter meter kilometer licence""".split())
# 'licence','meter' etc: keep GB-valid ones out of the US list
US_ONLY-= {'licence','meter','kilometer','gray','draft','mold','tire'}
BLOCK=set("""fuck fucks fucked fucker shit shits shitty cunt cunts bitch bitches bastard bastards whore whores slut sluts dick dicks cock cocks piss pissed nigger nigga fag fags faggot retard retards rape raped rapes rapist anal anus penis vagina tits twat wank wanker porn porno nazi nazis anna cain biggie femme antarctic gigi kike spic chink coon coons homo homos dyke dykes tranny pussy pussies cum jizz boob boobs butt butts arse arses damn damned hell""".split())
def good(w):
    return (4<=len(w)<=12 and w.isalpha() and w in words and w not in US_ONLY and w not in BLOCK
            and zipf_frequency(w,'en')>=2.9 and HS.lookup(w))
cands=[w for w in words if 4<=len(w)<=12 and w.isalpha() and 's' not in w]
valid=[w for w in cands if good(w)]
print('valid no-s words',len(valid))
byset=collections.defaultdict(list)
for w in valid:
    byset[frozenset(w)].append(w)
pang_sets=[s for s,ws in byset.items() if len(s)==7 and any(zipf_frequency(w,'en')>=3.4 for w in ws)]
print('pangram sets',len(pang_sets))
out=[]
allvalid=valid
for s in pang_sets:
    letters=''.join(sorted(s))
    inside=[w for w in allvalid if set(w)<=s]
    pangs=[w for w in inside if set(w)==s]
    for c in letters:
        ans=[w for w in inside if c in w]
        if 16<=len(ans)<=50 and any(c in p for p in pangs):
            score=sum(1 if len(w)==4 else len(w) for w in ans)+7*len(pangs)
            out.append({'l':letters,'c':c,'w':sorted(ans),'p':sorted(pangs),'n':len(ans),'s':score})
print('candidate puzzles',len(out))
random.shuffle(out)
# one puzzle per letter set
seen=set(); final=[]
for p in sorted(out,key=lambda x:(-1 if 25<=x['n']<=40 else 0, random.random())):
    if p['l'] in seen: continue
    seen.add(p['l']); final.append(p)
    if len(final)>=220: break
random.shuffle(final)
json.dump(final,open('data/games/bee.json','w'),separators=(',',':'))
import os;print(len(final),'puzzles',os.path.getsize('data/games/bee.json')//1024,'KB')
for p in final[:6]: print(p['l'],p['c'],p['n'],p['p'],p['w'][:12])
