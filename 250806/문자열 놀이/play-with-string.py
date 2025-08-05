arv=input().split()
s,q=arv[0],int(arv[1])

for _ in range(q):
    num,a,b=input().split()
    s=list(s)
    
    if num=='1':
        a,b=int(a)-1,int(b)-1
        s[a],s[b]=s[b],s[a]
        
       

    elif num=='2':
        if a in s:
            for i in range(len(s)):
                if s[i]==a:
                    s[i]=b
            
    s=''.join(s)
    print(s)
            

