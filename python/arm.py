import math
def arm(x):
    org=x
    count=0
    sum=0
    temp=x
   
    while(temp!=0):
        temp=temp//10
        #print('1')
        count+=1
    #print (count)
    while(x!=0):
        rem=x%10
        product=1
        for i in range(count):
            print(i)
            product*=rem
        print(product)
        sum+=product
        print("su ",sum)
        x=x//10
    print(int(sum))
    if(int(sum)==org):
        print("amstr")
    else:
        print("no")
x=int(input("enter value"))
arm(x)
