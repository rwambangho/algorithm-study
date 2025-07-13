n=int(input())
cnt='A'
for i in range(n,0,-1):
    for j in range(i):
        if j==0:
            for k in range(n-i):
                print(" ",end=' ')
        print(cnt,end=' ')
        if cnt!='Z':
            cnt=chr(ord(cnt)+1)
        else:
            cnt='A'
    print()