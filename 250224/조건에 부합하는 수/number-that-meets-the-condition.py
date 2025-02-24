a=int(input())
r=0
k=0
for i in range(1,a+1):
    r = i // 8
    k = i % 7
    if i % 2 == 0 and i % 4 != 0:
        continue
        
    if r % 2 == 0:
        continue

    if k < 4:
        continue
    
    print(i, end=' ')