a=input()
if len(a)%2==0:
    for i in range(len(a)-1,-1,-2):
        print(a[i],end='')
else:
    for i in range(len(a)-2,-1,-2):
        print(a[i],end='')
