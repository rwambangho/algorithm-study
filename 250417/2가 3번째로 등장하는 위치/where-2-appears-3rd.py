n=int(input())
n_arr=list(map(int,input().split()))
cnt=0
for i in range(n):
    if n_arr[i] == 2: #2등장
        cnt+=1
    if cnt == 3: #2가 3번 등장
        print(i+1)
        break
    
