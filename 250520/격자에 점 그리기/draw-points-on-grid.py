n,m=map(int,input().split())
grid=[[0 for _ in range(n)]for _ in range(n)]
cnt=1
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    grid[r-1][c-1]=cnt
    cnt+=1

for row in grid:
    for ele in row:
        print(ele,end=' ')
    print()




