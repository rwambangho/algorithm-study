n=int(input())
cnt=1
for i in range(n,0,-1):
    for j in range(i):
        if j==0:
            for k in range(n-i):
                print(" ",end=' ')
        print(cnt,end=' ')
        if cnt != 9:
            cnt+=1
        else:
            cnt=1
    print()