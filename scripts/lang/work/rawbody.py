import sys
L=sys.argv[1]
sk=[l.rstrip('\n') for l in open('skeleton.txt') if l.strip()]
raw=[l.rstrip('\n') for l in open(L+'.raw.txt') if l.strip()]
# split into groups
def groups(lines,note_ok):
    out=[];cur=None
    for l in lines:
        if l.startswith('[') or l.startswith('##'):
            cur=[l,[]];out.append(cur)
        else: cur[1].append(l)
    return out
gs=groups(sk,0);gr=groups(raw,1)
if [g[0] for g in gs]!=[g[0] for g in gr]: 
    a=[g[0] for g in gs];b=[g[0] for g in gr]
    for i,(x,y) in enumerate(zip(a,b)):
        if x!=y: print('HEADER MISMATCH',i,x,'|',y);break
    else: print('header count',len(a),len(b))
    sys.exit(1)
bad=0;res=[]
for (h,items),(h2,r) in zip(gs,gr):
    n=[x for x in r if not x.startswith('>')]
    if len(n)!=len(items):
        print('COUNT',h,len(items),len(n));bad=1
        for i in range(max(len(items),len(n))):
            print(' ',items[i] if i<len(items) else '-','=>',n[i] if i<len(n) else '-')
        continue
    res.append(h)
    k=0
    for x in r:
        res.append(x)
open(L+'.body.txt','w').write('\n'.join(res)+'\n')
sys.exit(bad)
