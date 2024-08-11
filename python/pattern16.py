def pattern15(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print("  ",end="")
        for j in range(i):
            print("* ",end="")
        for j in range(1,i+1):
            print(" ",end="")
            print(j,end="")
        print()
    des=0
    for i in range(1,n+1):
        for j in range(1,i):
            print(" ",end=" ")
        k=4
        for j in range(n-i+1) :
            print(k,end=" ")
            k=k-1
        
        
    
        for j in range(1,n-i+2):
            
            k=des+(2*j-1)
            print(" ",end="")
            print(k,end="")
        des+=2   
        print()
        
        

n=int(input("enter the val1:"))
pattern15(n)