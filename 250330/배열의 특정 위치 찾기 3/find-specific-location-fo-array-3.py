arr=list(map(int,input().split()))
n=len(arr)
for i in range(n):
    if arr[i] == 0:
        print(sum(arr[i-3:i]))
        break

    

