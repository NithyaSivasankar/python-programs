def pattern5(x):
    for i in range(1,x+1):
        for j in range(i,x+1):
            print(" ",end="")
        for j in range(i,0,-1):
            print(j,end="")
        for j in range(1,i):
            
            print(j+1,end="")
            
        print()

x=int(input("enter the val1;"))
pattern5(x)