x=[2,20,8,9,1,6]

for i in range(0,len(x)):
    for j in range(1,len(x)-i):
        if(x[j-1]>x[j]):
            temp=x[j-1]
            x[j-1]=x[j]
            x[j]=temp
print(x)