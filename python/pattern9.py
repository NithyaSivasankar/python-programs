def pattern9(x):
    for i in range(1,x+1):
        for j in range(1,x+1):
            if j==i or j==x-i+1:
                print(i,end=" ")
            else:
                print(" ",end=" ")
        print()

x=5
pattern9(x)