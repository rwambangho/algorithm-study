n,m=tuple(map(int,input().split()))
s=[input().split() for _ in range(n)]
k=[input().split() for _ in range(n)]
y=[[0 for _ in range(m)]for _ in range(n)]
for i in range(n):
    for j in range(m):
        if s[i][j]!=k[i][j]:
            y[i][j]=1
for row in y:
    for elem in row:
        print(elem, end=' ')
    print()        

