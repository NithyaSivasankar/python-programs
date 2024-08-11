def num(n):
    if n==1:
        return 1
    else:
        return n+num(n-1)
n=int(input("enter the val:"))
k=num(n)
def pattern(n,k):
    for row in range(n):
        val=k-row
        dec=n-1
        for col in range(row+1):
            print(format(val,"<4"),end="")
            val=val-dec
            dec=dec-1
        print()
pattern(n,k)