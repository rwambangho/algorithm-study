n = int(input())
arr = list(map(int, input().split()))
for i in range(n-1):
    for j in range(i+1, n):
        if arr[j] < arr[i]:
          arr[i], arr[j] = arr[j], arr[i]
            
print(*arr)