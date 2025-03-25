arr=list(map(int,input().split()))
cnt = 0
total=0

for elem in arr:
    if elem == 0:
        break
    cnt += 1

for i in range(cnt):
    total+=arr[i]
avg=total/cnt
print(f"{total} {avg:.1f}")

