n=int(input("enter the val:"))
def pattern(n):
    if n%400==0 or n%4==0 and n%100!=0:
        print("leap year")
    else:
        print("non leap year")
pattern(n)