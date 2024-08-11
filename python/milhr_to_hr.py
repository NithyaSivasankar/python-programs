s="11:50"
crt=""
d=0
rem=0
d=int(s[0:2])
if d>12:
    if d<24:
        rem=d%12
        crt=str(rem)+s[2:5]+"pm"
    elif d==24:
        crt="12"+s[2:5]+"am"
    else:
        print("invalid")
elif d==0:
    crt="00"+s[2:5]+"am"
elif d==12:
    crt="12"+s[2:5]+"pm"
else:
    crt=s[0:]+"am"
print(crt)
    
