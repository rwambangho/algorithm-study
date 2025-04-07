n = int(input())
A = list(map(int, input().split()))
total=[0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        total[i]+=A[j]*abs(j-i)

total=set(total)

    
print(min(total))
# Please write your code here.