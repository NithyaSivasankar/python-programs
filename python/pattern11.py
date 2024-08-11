n=int(input("enter the val:"))
for i in range(n):
    k=111
    for j in range(n-i-1):
        print(format(" ","<5"),end="")
    for j in range(i+1):
        print(format(k,"<5"),end="")
        k=k+111
    print()