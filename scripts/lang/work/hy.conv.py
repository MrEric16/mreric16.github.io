import re
def conv(s):
    T = ["ts'", "ch'", "t'", "p'", "k'", "dzh", "dz", "zh", "kh", "gh", "sh", "rr", "ts", "ch"]
    M = {"ts'":"ց","ch'":"չ","t'":"թ","p'":"փ","k'":"ք","dzh":"դժ","dz":"ձ","zh":"ժ","kh":"խ","gh":"ղ","sh":"շ","rr":"ռ","ts":"ծ","ch":"ճ",
         'a':'ա','b':'բ','g':'գ','d':'դ','e':'ե','ê':'է','ə':'ը','z':'զ','i':'ի','l':'լ','k':'կ','h':'հ','m':'մ','y':'յ','n':'ն','o':'ո','ô':'օ',
         'p':'պ','j':'ջ','s':'ս','v':'վ','t':'տ','r':'ր','u':'ու','f':'ֆ'}
    s=s.lower().replace('ev','\x01')
    out=[];i=0
    while i<len(s):
        for t in T:
            if s.startswith(t,i):
                out.append(M[t]);i+=len(t);break
        else:
            c=s[i];out.append('և' if c=='\x01' else M.get(c,c));i+=1
    return ''.join(out)
