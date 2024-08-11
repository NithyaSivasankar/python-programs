def sel(s,n):
    t=""
    for i in s:
        if i==' ':
            if len(t)>=3:
                print(t)
            t=""
        else:
            t=t+i
    if t:
        if len(t)>=3:
                print(t)
s="Ramu is my friend"
n=int(input("enter1:"))
sel(s,n)