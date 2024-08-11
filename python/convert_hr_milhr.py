s="12:56am"
crt=""
rem=0
t=0
t=[]
if s[-2:]=="pm":
    d=int(s[0:2])
    print(d)
    if d==12:
       crt=str(d)+s[2:5] 
       print(crt)
    elif d<12:
        #rem=d%12
        t=12+d
        print(t)
        crt=str(t)+s[2:5]
        print(crt)
else:
    if s[0:2]=="12":
        t="00"+s[2:5]
        print(t)
    else:
        print(s[0:5])