inp = input()
arr = inp.split()
c = (arr[0])
n = int(arr[1])

if c == 'A':
    for i in range(1, n+1):
        print(i,end=' ')
        i+=1
elif c == 'D':
    for _ in range(1,n+1):
        print(n,end=' ')
        n-=1
else:
    print("fuck")