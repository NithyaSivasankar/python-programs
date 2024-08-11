def rev(s):
    j=len(s)-1
    t=""
    while(j>=0):
       t+=s[j]
       j=j-1
    print(t)       
s=input("enter teh val1;")
rev(s)