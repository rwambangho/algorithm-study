sat=True
for _ in range(5):
    a=int(input())
    if a % 3 != 0:
        sat=False
        break
    else:
        continue
if sat==True:
    print(1)
else:
    print(0)