arr=list(map(int,input().split()))
cnt=0
cnt1=0
total=0
for elem in arr:
    if elem==0:
        break
    cnt+=1

for i in range(cnt):
    if arr[i] % 2 == 0:
        total+=arr[i]
        cnt1+=1
print(cnt1, total)