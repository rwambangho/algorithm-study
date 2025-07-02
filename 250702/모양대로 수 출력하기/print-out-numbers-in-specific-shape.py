n=int(input())
cnt=n
tmp=n-cnt
for i in range(n):
    for j in range(cnt,0,-1):
        if cnt<n and j==cnt:
            for _ in range(tmp):
                print(' ',end=' ')    
        print(j,end=' ')
    cnt-=1
    print()
        