arr=list(map(int,input().split()))
total=0
total1=0
cnt=0
for i in range(1,10,2):
    total+=arr[i]
for i in range(2,10,3):
    total1+=arr[i]
    cnt+=1

    

print(f"{total} {total1/cnt}")

    