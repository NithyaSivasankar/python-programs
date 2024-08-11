def palin(x):
    s=""
    n=len(x)
    for i in range(n-1,-1,-1):
        s+=x[i]
    print(s)
    if(s==org):
        print("palindrome")
    else:
        print("no")
x="madam"
org=x
palin(x)