n=int(input())
num=list(map(int,input().split()))
result=101
for i in range(n-1,-1,-1):
    for j in range(i):
        if num[i]-num[j] < result:
            result=num[i]-num[j]
print(result)
