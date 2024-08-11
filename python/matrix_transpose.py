p=int(input("enter the row:"))
n=int(input("enter the col:"))
matrix1=[[int(input()) for i in range(n)]for j in range(p)]
print(matrix1)
for i in range(p):
    for j in range(n):
        print(format(matrix1[i][j],"<3"),end="")
    print()
res=[[0 for i in range(p)]for j in range(n)]
print(res)
for i in range(n):
    for j in range(p):
        #for k in range(n):
        res[i][j]=matrix1[j][i]
for i in range(n):
    for j in range(p):
        print(format(res[i][j],"<3"),end="")
    print()
