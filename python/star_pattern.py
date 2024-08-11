def pattern15(n,col):
    mid=col//2
    for i in range(n):
        for j in range(col):
            if i==2 or i==n-3 or i+j==mid or i+j==col+1 or j-i==mid or i-j==2:
                print("*",end="")
            else:
                print(" ",end="")
        print()
n=int(input("enetr the val:"))
col=n+n-5
pattern15(n,col)