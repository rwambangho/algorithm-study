n=int(input())
total=0

cnt=0
for _ in range(n):
    arr=list(map(int,input().split()))
    for elem in arr:
        total+=elem
    if total/len(arr) >= 60:
        print("pass")
        cnt+=1
           
    else:
        print("fail")
        
    total=0
    arr=[]
print(cnt)

