a,b=map(int,input().split())
sum=0
if a > b:
    for i in range(a,b,-1):
        if i % 5 == 0:
            sum+=i
else:
    for i in range(a,b+1):
        if i % 5 == 0:
            sum+=i
print(sum)
