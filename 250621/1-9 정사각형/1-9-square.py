n=int(input())
cnt=1
for i in range(n):
    for j in range(n):
        print(cnt,end='')
        cnt+=1
        if cnt==10:
            cnt=1
    print()
        
        
