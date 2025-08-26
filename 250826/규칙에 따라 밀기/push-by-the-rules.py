a=input()
c=input()
len_c=len(c)
for i in range(len_c):
    if c[i]=='L':
        a=a[1:]+a[0]
    elif c[i]=='R':
        a=a[-1]+a[:-1]
print(a)