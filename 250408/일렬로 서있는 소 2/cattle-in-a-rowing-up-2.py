n = int(input())
A = list(map(int, input().split()))
total=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if A[i] <= A[j] <= A[k]:
                total+=1

            



print(total)
            
            
                
# Please write your code here.