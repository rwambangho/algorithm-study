cnt=0
while True:
    n=int(input())
    
    if n % 2 == 0:
        print(f"{n//2}")
        cnt+=1
    else:
        continue
    if cnt >=3:
        break