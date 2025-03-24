n=int(input())
arr= list(map(float,input().split()))

sum=0
cnt=0
for i in range(n):
    sum+=arr[i]
    cnt+=1
val=sum/cnt
if val > 0:
    print(f"{val:.1f}")
    if val >= 4.0:
        print("Perfect")
    elif val >= 3.0:
        print("Good")
    else:
        print("Poor")


