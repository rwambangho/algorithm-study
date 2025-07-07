n=int(input())
cnt=n
for i in range(1,n+1):
    for j in range(i):
        
        print(cnt,end=' ')
        
        if j==i-1:
            cnt-=i
        else:
            cnt+=1
    print()
        
            

    

