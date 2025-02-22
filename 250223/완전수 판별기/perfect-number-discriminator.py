n=int(input())
a=0
for i in range(1,n+1):
    if n%i==0 and n!=i:
        a+=i

if a==n:
    print('P')
else:
    print('N')