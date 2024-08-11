def vowcount(x):
    count=0
    for i in x:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
    print(count)
x="education"
vowcount(x)