R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

cnt=0


for i in range(1,R):
    for j in range(1,C):
        for k in range(i+1,R-1):
            for l in range(j+1,C-1):
                if grid[0][0]!=grid[i][j] and grid[i][j]!=grid[k][l] and grid[k][l]!=grid[R-1][C-1]:
                    cnt+=1
                    
        
   
    
    
                        
print(cnt)


        
# Please write your code here.