n=int(input())
count_arr=[0 for _ in range(100)]
arr=list(map(int,input().split()))
for elem in arr:
    count_arr[elem]+=1
for i in range(1,10):
    cnt=count_arr[i]
    print(cnt)
