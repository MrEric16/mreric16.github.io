import sys,re
for i in sys.argv[1:]:
    p='src/%s.txt'%i; out=[]; inneg=False; removed=0
    for line in open(p,encoding='utf-8'):
        if line.startswith('## '): inneg = line[3:].strip().lower().startswith('negation')
        if inneg and line.startswith('ex:'): removed+=1; continue
        out.append(line)
    open(p,'w',encoding='utf-8').writelines(out); print(i,'removed',removed)
