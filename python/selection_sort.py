x=[3,5,2,1,7]
min_in=0
temp=0
for i in range(0,len(x)):
    min=x[i]
    min_in=i
    for j in range(i,len(x)):
        if(min>x[j]):
            min_in=j
            min=x[j]
    print(min)
    print(x[i])
    temp=x[i]
    x[i]=x[min_in]
    x[min_in]=temp
print(x)