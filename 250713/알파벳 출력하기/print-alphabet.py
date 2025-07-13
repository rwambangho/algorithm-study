n=int(input())
cnt='A'
for i in range(1,n+1):
    for j in range(i):
        print(cnt,end='')
        if cnt!='Z':
            cnt=chr(ord(cnt)+1)
        else:
            cnt='A'
    print()