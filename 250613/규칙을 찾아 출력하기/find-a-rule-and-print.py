n=int(input())
grid=[[" " for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            grid[i][j]='*'
        if i>=2:
            for k in range(1,i):
                grid[i][k]='*'
            

for row in grid:
    for elem in row:
        print(elem,end=' ')
    print()