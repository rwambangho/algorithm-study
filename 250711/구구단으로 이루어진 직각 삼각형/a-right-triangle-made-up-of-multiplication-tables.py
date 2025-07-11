n=int(input())
t=n
for i in range(1,n+1):
    for j in range(1,t+1):
        if j!=t:
            print(f"{i} * {j} = {i*j}",end=' / ')
        else:
            print(f"{i} * {j} = {i*j}")
    t-=1
        

