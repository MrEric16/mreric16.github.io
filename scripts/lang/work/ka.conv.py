def conv(s):
    T = ["ts'", "ch'", "dz", "zh", "sh", "gh", "kh", "ch", "ts", "t'", "k'", "p'", "q'"]
    M = {"ts'":"წ","ch'":"ჭ","dz":"ძ","zh":"ჟ","sh":"შ","gh":"ღ","kh":"ხ","ch":"ჩ","ts":"ც","t'":"ტ","k'":"კ","p'":"პ","q'":"ყ",
         'a':'ა','b':'ბ','g':'გ','d':'დ','e':'ე','v':'ვ','z':'ზ','t':'თ','i':'ი','k':'ქ','l':'ლ','m':'მ','n':'ნ','o':'ო','p':'ფ','r':'რ','s':'ს','u':'უ','j':'ჯ','h':'ჰ'}
    out=[];i=0;s=s.lower()
    while i<len(s):
        for t in T:
            if s.startswith(t,i):
                out.append(M[t]);i+=len(t);break
        else:
            c=s[i];out.append(M.get(c,c));i+=1
    return ''.join(out)
