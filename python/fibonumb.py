 def perfectsqr(n):
    total=0
    i=1
    if n<0:
        return False
    while total<n:
        total+=i
        #print("tot",total)
        i+=2
    #print("tot",total)
    return total==n    
n=int(input("enetr the val1:"))
res1=5*n*n+4
res2=5*n*n-4
print("res",res1,res2)
if perfectsqr(res1) or perfectsqr(res2):
    print("fibonumb")
else:
    print("non fibo")






