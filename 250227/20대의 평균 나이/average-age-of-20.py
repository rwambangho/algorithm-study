sum=0
cnt=0
result=0
while True:
    n=int(input())
    if n // 10 == 2:
        cnt+=1
        sum+=n
    if n // 10 != 2:
        result=sum/cnt
        print(f"{result:.2f}")
        break

    
