def dupli(x):
    dup=0
    dup_ind=0
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if x[i]==x[j]:
                dup=x[i]
                dup_ind=j
                print(dup,"=",i,dup_ind)
                
                
    
x=[1,2,3,4,1,2,5]
dupli(x)