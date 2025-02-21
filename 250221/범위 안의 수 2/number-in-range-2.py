sum=0
avg=0
cnt=0
for _ in range(10):
    a=int(input())
    if a>=0 and a<=200:
        sum+=a
        cnt+=1

avg=sum/cnt
print(f"{sum} {avg:.1f}")