n=int(input())
cnt=0
while True:
    if n == 1:
        print(0)
        break
    if n % 2 == 0:
        n=n//2
    else:
        n=n*3+1
    cnt+=1
    if n != 1:
        continue
    else:
        print(cnt)
        break