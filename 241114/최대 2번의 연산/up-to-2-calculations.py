a = int(input())

if a % 2 == 0:
    c=a/2

if c % 2 != 0:
    c+=1
    c/=2

print(int(c))