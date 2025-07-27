a=input()
b=input()
cnt=0
for i in range(len(a)):
    if b[0]==a[i] and b[1]==a[i+1]:
        cnt+=1
print(cnt)