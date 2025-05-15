n=int(input())
grid=[[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    grid[i][0]=1
    for j in range(1,n):
        if grid[i-1][j-1] in grid and grid[i-1][j] in grid: 
            grid[i][j]=grid[i-1][j-1]+grid[i-1][j]
        else:
            grid[i][j]=1

for row in grid:
    for elem in row:
        print(elem,end=' ')
    print()