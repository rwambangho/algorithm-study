n,m=map(int,input().split())
grid=[[0 for _ in range(n)]for _ in range(n)]
cnt=1
for _ in range(m):
    i,j=tuple(map(int,input().split()))
    grid[i-1][j-1]=i*j

for row in grid:
    for ele in row:
        print(ele,end=' ')
    print()
    



