m=int(input())
for _ in range(m):
    cnt=0
    n=int(input())

    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
        cnt+=1
    print(cnt)



