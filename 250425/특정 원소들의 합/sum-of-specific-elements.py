total=0
for i in range(4):
    arr=list(map(int, input().split()))
    for j in range(i+1):
        total+=arr[j]
print(total)