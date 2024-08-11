def spiral(x,rowup,rowlow,colup,collow):
    res=[]
    while(rowup<rowlow and colup<collow):
        for i in range(colup,collow):
            res.append(x[rowup][i])
            #print(res)
        rowup=rowup+1
        for i in range(rowup,rowlow):
            res.append(x[i][collow-1])
            #print(res)
        collow=collow-1
        for i in range(collow-1,colup-1,-1):
            res.append(x[rowlow-1][i])
            #print(res)
        rowlow=rowlow-1
        for i in range(rowlow-1,rowup-1,-1):
            res.append(x[i][colup])
            #print(res)
        colup=colup+1
    print(res)

x=[[1,2,3],[4,5,6],[7,8,9]]
rowup=0
rowlow=len(x)
colup=0
collow=len(x[0])
spiral(x,rowup,rowlow,colup,collow)