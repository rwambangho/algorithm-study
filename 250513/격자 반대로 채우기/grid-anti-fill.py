n=int(input())
cnt=1
grid=[[0 for _ in range(n)]for _ in range(n)]
if n%2==0:
    for i in range(n-1,-1,-1):
        if i%2==1:
            for j in range(n-1,-1,-1):
                grid[j][i]=cnt
                cnt+=1
        else:
            for j in range(n):
                grid[j][i]=cnt
                cnt+=1
else:
    for i in range(n-1,-1,-1):
        if i%2==0:
            for j in range(n-1,-1,-1):
                grid[j][i]=cnt
                cnt+=1
        else:
            for j in range(n):
                grid[j][i]=cnt
                cnt+=1

for row in grid:
    for ele in row:
        print(ele,end=' ')
    print()

