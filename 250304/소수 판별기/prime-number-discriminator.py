n=int(input())
sat=True
for i in range(2,n):
    if n % i == 0:
        sat=False
        break
    else:
        continue
        
if sat==True:
    print("P")
else:
    print("C")