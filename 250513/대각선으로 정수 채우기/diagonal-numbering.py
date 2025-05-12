n, m = map(int, input().split())
grid=[[0 for _ in range(m)] for _ in range(n)]
cnt=1
sum=0
while(sum<=n*m):
    for i in range(n):
        for j in range(m):
            if i+j==sum:
                grid[i][j]=cnt
                cnt+=1
            else:
                continue
    sum+=1       
         
for row in grid:
    for elem in row:
        print(elem,end=' ')
    print()





        

# Please write your code here.
