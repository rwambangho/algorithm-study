n=map(int,input().split())
cnt_arr=[0 for _ in range(11)]

for elem in n:
    
    if elem == 0:
        break
    else:
        i = elem // 10 
    cnt_arr[i]+=1

for i in range(len(cnt_arr)-1,0,-1):
    print(f"{i*10} - {cnt_arr[i]}")
    
