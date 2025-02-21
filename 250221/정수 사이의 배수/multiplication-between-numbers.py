a,b=map(int,input().split())
sum=0
avg=0
cnt=0
for i in range(a,b+1):
    if i%5==0 or i%7==0:
        sum+=i
        cnt+=1

avg=sum/cnt
a=round(avg,1)
print(sum,a)