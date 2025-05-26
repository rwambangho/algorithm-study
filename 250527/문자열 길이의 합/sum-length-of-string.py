n=int(input())
grid=[input() for _ in range(n)]
lencnt,cnt=0,0
for i in range(n):
    lencnt+=len(grid[i])
    if grid[i][0]=='a':
        cnt+=1

print(lencnt,cnt)
    
    
