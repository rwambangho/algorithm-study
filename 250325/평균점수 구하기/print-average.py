arr=list(map(float,input().split()))
total=0
avg=0
for i in range(8):
    total+=arr[i]
avg=total/8
print(f"{avg:.1f}")
