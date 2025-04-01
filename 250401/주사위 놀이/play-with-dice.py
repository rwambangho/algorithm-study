arr=list(map(int,input().split()))
cnt_arr=[0 for _ in range(10)]
for elem in arr:
    cnt_arr[elem]+=1
for i in range(1,7):
    cnt=cnt_arr[i]
    print(f"{i} - {cnt}")
