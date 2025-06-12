n=int(input())
grid=[[" " for _ in range(n)]for _ in range(n)]
for i in range(1):
    for j in range(n):
        grid[i][j]='*'
        if j%2!=0:
            for k in range(j+1):
                grid[k][j]='*'

for row in grid:
    for elem in row:
        print(elem,end=' ')
    print()

        
