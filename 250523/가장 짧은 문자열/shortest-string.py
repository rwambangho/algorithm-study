grid=[0 for _ in range(3)]
for i in range(3):
    n=input()
    grid[i]=len(n)

print(max(grid)-min(grid))