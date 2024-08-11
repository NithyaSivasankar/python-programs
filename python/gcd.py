def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

x=int(input("enter the val1;"))
y=int(input("enter the val2:"))
print(gcd(x,y))
