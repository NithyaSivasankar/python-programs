n=int(input("enter the val:"))
def pattern(n):
    for row in range(n):
        val=row+1
        dec=n-1
        for col in range(row+1):
            print(format(val,"<4"),end="")
            val=val+dec
            dec=dec-1
        print()
pattern(n)