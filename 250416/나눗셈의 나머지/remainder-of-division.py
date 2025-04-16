n,m=map(int,input().split())
cnt_arr=[0 for _ in range(10)]
while n>1:
    cnt_arr[n%m]+=1
    n=n//m

total=0
for elem in cnt_arr:
    total+=elem**2
print(total)





