n,m = tuple(map(int,input().split()))
arr=list()
arr.append(n)
arr.append(m)
for i in range(2, 10):
    arr.append((arr[i-2]+arr[i-1])%10)
print(*arr)
