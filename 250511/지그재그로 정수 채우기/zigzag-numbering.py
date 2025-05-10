n, m = map(int, input().split())
grid=[[0 for _ in range(m)] for _ in range(n)]
cnt=0
for i in range(m):
    if i%2==0:
        for j in range(n):
            grid[j][i]=cnt
            cnt+=1
    else:
        for j in range(n-1,-1,-1):
            grid[j][i]=cnt
            cnt+=1
    
    
        
    
for row in grid:
    for ele in row:
        print(ele, end=' ')
    print()


        
        
# Please write your code here.
