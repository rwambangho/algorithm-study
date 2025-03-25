arr=list(map(int,input().split()))
cnt=0
total=0
for elem in arr:
    if elem==0:
        break
    if elem%2==0:
        total+=elem
        cnt+=1
print(cnt,total)