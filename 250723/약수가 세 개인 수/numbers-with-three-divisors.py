start, end = map(int, input().split())
cnt=0
# Please write your code here.
for i in range(start,end):
    tmp=0
    for j in range(1,i+1):
        if i%j==0:
            tmp+=1
    if tmp==3:
        cnt+=1
print(cnt)