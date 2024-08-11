s="he is my friend is my he"
val=0
set={}
t=""
for i in s:
    if i==' ':
        if t in set:
            set[t]+=1
            t=""
        else:
            set[t]=1
            t=""
            continue
    else:
        t=t+i
if t:
        if t in set:
            set[t]+=1
            t=""
        else:
            set[t]=1
            t=""
for i in set:
    if set[i]!=1:
        print(i)
print(set)