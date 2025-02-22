n=int(input())
a=0
sum=0
avg=0
for i in range(n):
    a=int(input())
    sum+=a

avg=sum/n
print(f"{sum} {avg:.1f}")