n=int(input())
grid=[[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    grid[i][0]=1
    for j in range(i):
        grid[i][j+1]=grid[i-1][j]+grid[i-1][j+1]

for row in grid:
    for elem in row:
        if elem != 0:
            print(elem,end=' ')
    print()