a=2000
b=3200
list=[]
for i in range(2000,3200+1):
    if i%7==0 and i%5!=0:
        list.append(i)
    else:
        continue
print(list)