n=int(input())
cnt=11
grid=[[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(n):
        grid[i][j]=cnt
        cnt+=2
    cnt=grid[i][1]


for row in grid:
    for elem in row:
        print(elem,end=' ')
    print()

