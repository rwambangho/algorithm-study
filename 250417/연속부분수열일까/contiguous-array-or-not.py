n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
cnt=0

ans=False
if b[0] in a:
    start=a.index(b[0])
    for j in range(start,n-m+1):
        for i in range(m):
            if a[j]==b[i]:
                cnt+=1
            j+=1
        if cnt==m:
            ans=True
        else:
            cnt=0
        
            
if ans:
    print("Yes")
else:
    print("No")



     
    
    
        