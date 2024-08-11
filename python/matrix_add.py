row=int(input("enter the row:"))
col=int(input("enter the col:"))
matrix1=[[int(input()) for i in range(col)]for j in range(row)]
print(matrix1)
for i in range(row):
    for j in range(col):
        print(format(matrix1[i][j],"<3"),end="")
    print()
matrix2=[[int(input()) for i in range(col)]for j in range(row)]
print(matrix2)
for i in range(row):
    for j in range(col):
        print(format(matrix2[i][j],"<3"),end="")
    print()
res=[[0 for i in range(col)]for j in range(row)]
print(res)
for i in range(row):
    for j in range(col):
        res[i][j]=matrix1[i][j]+matrix2[i][j]
for i in range(row):
    for j in range(col):
        print(res[i][j])