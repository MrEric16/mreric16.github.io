# Extracts every theme rule (body.usertheme-*, body.theme-*, body.dark-mode ...) from the main app's
# stylesheet into theme-pages.css, so standalone pages (vocabulary.html) match the active theme.
import re,sys,os
root=os.path.join(os.path.dirname(__file__),'..','..')
s=open(os.path.join(root,'index.html'),encoding='utf8').read()
css=re.search(r'<style[^>]*>(.*?)</style>',s,re.S).group(1)
css=re.sub(r'/\*.*?\*/','',css,flags=re.S)
def blocks(t):
    i=0;n=len(t);out=[]
    while i<n:
        j=i
        while j<n and t[j] not in '{;':j+=1
        if j>=n:break
        if t[j]==';':out.append((t[i:j].strip(),None));i=j+1;continue
        d=1;k=j+1
        while k<n and d:
            if t[k]=='{':d+=1
            elif t[k]=='}':d-=1
            k+=1
        out.append((t[i:j].strip(),t[j+1:k-1]));i=k
    return out
THEME=re.compile(r'(usertheme-|\.theme-|body\.dark-mode|nebula|aurora|hacker|synthwave)')
kept=[];kf={}
def walk(bl,ind=''):
    res=[]
    for sel,body in bl:
        if body is None:continue
        if sel.startswith('@keyframes') or sel.startswith('@-webkit-keyframes'):
            kf[sel.split()[1]]=f'{sel}{{{body}}}';continue
        if sel.startswith('@media') or sel.startswith('@supports'):
            inner=walk(blocks(body))
            if inner:res.append(f'{sel}{{{"".join(inner)}}}')
            continue
        if sel.startswith('@'):continue
        if THEME.search(sel) and sel.lstrip().startswith(('body','html','#nebula','.nebula','#hacker')) or re.match(r'\s*(#|\.)(nebula|hacker|synth|rain|aurora)',sel):
            res.append(f'{sel}{{{body}}}')
    return res
rules=walk(blocks(css))
txt=''.join(rules)
used=[k for k in kf if re.search(r'\b'+re.escape(k)+r'\b',txt)]
txt=''.join(kf[k] for k in used)+txt
open(os.path.join(root,'theme-pages.css'),'w',encoding='utf8').write(txt)
print(len(rules),len(used),len(txt))
