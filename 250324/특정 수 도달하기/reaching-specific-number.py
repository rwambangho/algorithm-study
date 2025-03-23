n = list(map(int, input().split())) 

total=0
cnt=0
for i in range(10):
    if n[i] < 250 :
        total+=n[i]
        cnt+=1
    else:
        break

eval = total/cnt
if cnt > 0:
    print(f"{total} {eval:.1f}")
else:
    print(0)





