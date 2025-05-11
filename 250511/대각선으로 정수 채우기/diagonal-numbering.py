n, m = map(int, input().split())
grid=[[0 for _ in range(m)] for _ in range(n)]
cnt=1

for j in range(m):
    for i in range(n):
        if j==0:
            break
        else:
            j-=1
        grid[i][j]=cnt
        cnt+=1
for row in grid:
    for elem in row:
        print(elem,end=' ')
    print()





        

# Please write your code here.
