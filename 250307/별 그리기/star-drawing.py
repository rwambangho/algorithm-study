n = int(input())

# Please write your code here.
for i in range(n):
    for j in range(n-1-i):
        print(" ",end='')
    
    for j in range(i*2+1):
        print("*",end='')
    
    print()

for i in range(n-1):
    for j in range(n+i-2):
        print(" ",end='')
    
    for j in range(n-i*2):
        print("*",end='')
    print()