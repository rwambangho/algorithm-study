cnt,total=0,0
n=int(input())
grid=[input() for _ in range(n)]
a=input()

for i in range(n):
    if grid[i][0] == a:
        cnt+=1
        total+=len(grid[i])
avg=total/cnt
    
print(f"{cnt} {avg:.2f}")
