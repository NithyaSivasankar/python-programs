s="python"
n=len(s)
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print("  ",end="")
    for j in range(i,-1,-1):
        print(s[j],end=" ")
    print()