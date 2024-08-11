s="ramu is boy"
x="rani is girl"
t=""
dict={}
for i in s:
    if i==" ":
        dict[t]=1
        print(dict)
        t=""
    else:
      t+=i 
if t:
    if t in dict:
        dict[t]+=1
    else:
        dict[t]=1
print(dict)
t=""
for j in x:

    if j==" ":
        if t in dict:
            dict[t]+=1
            t=""
        else:
            dict[t]=1
            t=""
    else:
        t+=j
if t:
    if t in dict:
        dict[t]+=1
    else:
        dict[t]=1
print(dict)
for k in dict:
    if dict[k]>1:
        #print(k,dict[k])
        continue
    else:
        print(k,dict[k])