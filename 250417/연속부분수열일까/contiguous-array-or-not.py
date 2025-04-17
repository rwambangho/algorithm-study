n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if b[0] in a:
    start=a.index(b[0])
    for i in range(len(b)):
        if i==len(b)-1 and a[start] == b[i]:
            print("Yes")
            break
        
        if a[start] != b[i]:
            print("No")
            break
        else:
            start+=1
else:
    print("No")       
    
    
        