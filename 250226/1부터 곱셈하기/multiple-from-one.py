n=int(input())
sum=1
for i in range(1,11,+1):
    sum*=i
    if sum >= n:
        print(i)
        break