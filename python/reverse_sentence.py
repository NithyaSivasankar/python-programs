def rev(s):
    t=" "
    st=""
    stack=[]
    for i in s:
        if i==" ":
            stack.append(t)
            t=""
            print(stack)
        else:
            t+=i
    if i:
        stack.append(t)
        print(t)
    while stack:
        st+=stack.pop()
        print(st)
        st+=" "
    #print(s)
s="nithya is a good girl"
rev(s)