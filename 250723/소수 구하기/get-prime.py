n=int(input())
for i in range(2,n+1):
    k=True
    for j in range(2,i):
        if i%j==0:
            k=False
            break
    if k==True:
        print(i,end=' ')


        

            
        
            
        
        
        


