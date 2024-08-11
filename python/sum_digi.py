def sum_digi(x):
    rem=0
    sumi=0
    while(x!=0):
        rem=x%10
        sumi+=rem
        x=x//10
    print(sumi)
x=int(input("enter val:"))
sum_digi(x)