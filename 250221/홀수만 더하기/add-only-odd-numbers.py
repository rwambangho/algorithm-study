n=int(input())
sum=0
for _ in range(n):
    a=int(input())
    if a%2!=0 and a%3==0:
        sum+=a

print(sum)
