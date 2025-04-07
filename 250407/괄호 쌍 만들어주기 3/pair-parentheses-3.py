A = input()
n=len(A)
total=0
for i in range(n):
    for j in range(i+1,n):
        if A[i]=='(' and A[j]==')':
            total+=1
print(total)
        
# Please write your code here.