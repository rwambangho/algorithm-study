n=int(input())

minus=-1
cnt=1
m=n*cnt
for i in range(n):
    for j in range(m,0,minus):
        print(j,end=' ')
    print()
    minus-=1
    cnt+=1
    m=n*cnt