n=int(input())
nn=n*2+1
grid=[[" " for _ in range(nn)]for _ in range(nn)]
for i in range(nn):
    for j in range(nn):
        if i==0 or i==nn-1 or j==0 or j==nn-1:
            grid[i][j]="*"
        elif i%2==0 or j%2==0:
            grid[i][j]="*"

        
for row in grid:
    for ele in row:
        print(ele,end=' ')
    print()