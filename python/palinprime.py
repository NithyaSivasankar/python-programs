def paliprime(x):
    rem=0
    sumi=0
    org=x
    while(x!=0):
        rem=x%10
        sumi=sumi*10+rem
        x=x//10
    print(sumi)
    if sumi==org:
        #print("true")
        isbool=True
        for i in range(2,int(org*0.5)+1):
            if(org%i==0):
                isbool=False
                print(i)
                return isbool
        return isbool
x=int(input("enter val:"))
print(paliprime(x))