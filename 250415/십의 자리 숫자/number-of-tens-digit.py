n=list(map(int,input().split()))
cnt_arr=[0 for _ in range(10)]
for elem in n:
    if elem == 0:
        break
    i=elem//10
    cnt_arr[i] += 1

for i,elem in enumerate(cnt_arr):
    if i>0:
        print(f"{i} - {elem}")
        

