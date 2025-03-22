n=int(input())
cnt1=1
cnt2=n
for i in range(n*2):
    if i%2==0:
        for _ in range(cnt1):
            print("*",end=' ')
            
        cnt1+=1
    else:
        for _ in range(cnt2):
            print("*",end=' ')
            
        cnt2-=1

    print()






