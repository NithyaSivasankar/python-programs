l=[12,3,54,6,7]
n=len(l)
print(n)
max=l[0]
prev=0
for i in range(n):
    if(l[i]>max):
        prev=max
        max=l[i]
    else:
        continue
print(prev)