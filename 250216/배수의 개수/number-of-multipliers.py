b=0
c=0
for _ in range(10):
    a=int(input())
    if a % 3 == 0 and a % 5 != 0:
        b+=1
    elif a % 5 == 0 and a % 3 != 0:
        c+=1
    elif a % 3 == 0 and a % 5 == 0:
        b+=1
        c+=1

    

print(b,end=' ')
print(c)