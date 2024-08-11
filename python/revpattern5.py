def pattern5(x):
    for i in range(1,x+1):
        for j in range(i,x+1):
            print(" ",end="")
        for j in range(1,i+1):
            print(j,end="")
        for j in range(1,i):
            n=i
            print(n,end="")
            
        print()

x=int(input("enter the val1;"))
pattern5(x)