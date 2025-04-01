n,m = map(int,input().split())
arr=list()
arr.append(n)
arr.append(m)
for _ in range(4):
    n, m= n+m, n+m+m
    arr.append(n%10)
    arr.append(m%10)
print(*arr)
