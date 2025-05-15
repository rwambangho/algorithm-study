n=int(input())
grid=[[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    grid[0][i]=1
    grid[i][0]=1

for i in range(1,n):
    for j in range(1,n):
        grid[i][j]=grid[i][j-1]+grid[i-1][j-1]+grid[i-1][j]

for row in grid:
    for elem in row:
        print(elem,end=' ')
    print()