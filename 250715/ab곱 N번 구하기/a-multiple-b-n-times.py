
n=int(input())
for _ in range(n):
    sum_val=1
    arr=input().split()
    a,b=int(arr[0]),int(arr[1])

    for i in range(a,b+1):
        sum_val*=i
    print(sum_val)
