n=[input() for _ in range(10)]
a=input()
cnt=0
for i in range(10):
    if n[i][-1] == a:
        print(n[i])
        cnt+=1
if cnt==0:
    print("None")
    
