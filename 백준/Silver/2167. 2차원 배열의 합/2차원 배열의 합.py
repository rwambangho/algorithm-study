# i,j위치부터 x,y위치까지 저장되어 있는 수들의 합을 구하기

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
k=int(input())
ijxy=[list(map(int,input().split())) for _ in range(k)]
prefix_sum=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        prefix_sum[i][j]=prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]+arr[i-1][j-1]
        
for a in range(k):
    count=0
    i,j,x,y=ijxy[a][0], ijxy[a][1], ijxy[a][2], ijxy[a][3]
    
    count+=prefix_sum[x][y]-prefix_sum[i-1][y]-prefix_sum[x][j-1]+prefix_sum[i-1][j-1]
    
    print(count)
    


    
    
            
