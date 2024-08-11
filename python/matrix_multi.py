p=int(input("enter the row:"))
n=int(input("enter the col:"))
matrix1=[[int(input()) for i in range(n)]for j in range(p)]
print(matrix1)
for i in range(p):
    for j in range(n):
        print(format(matrix1[i][j],"<3"),end="")
    print()
n=int(input("enter the row:"))
q=int(input("enter the col:"))
matrix2=[[int(input()) for i in range(q)]for j in range(n)]
print(matrix2)
for i in range(n):
    for j in range(q):
        print(format(matrix2[i][j],"<3"),end="")
    print()
res=[[0 for i in range(q)]for j in range(p)]
print(res)
for i in range(p):
    for j in range(q):
        for k in range(n):
            res[i][j]=res[i][j]+matrix1[i][k]*matrix2[k][j]
for i in range(p):
    for j in range(q):
        print(format(res[i][j],"<3"),end="")
    print()
