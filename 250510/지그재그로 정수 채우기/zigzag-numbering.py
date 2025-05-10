n, m = map(int, input().split())
grid=[[0 for _ in range(m)] for _ in range(n)]
cnt=0
for i in range(m):
    
    for j in range(n):
        grid[j][i]=cnt
        cnt+=1
    
for row in grid:
    for ele in row:
        print(ele, end=' ')
    print()


        
        
# Please write your code here.
