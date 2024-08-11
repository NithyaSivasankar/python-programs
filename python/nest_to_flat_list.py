x=[1,2,[4,5],6]
list2=[]
def get_max(x):
    for i in x:
        if type(i)==list:
            get_max(i)
        else:
            list2.append(i)
    return max(list2)
print(get_max(x))
        