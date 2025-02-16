b=0
c=0
for _ in range(10):
    a=int(input())
    if a % 3 == 0:
        b+=1
    else:
        c+=1

print(b,end=' ')
print(c)