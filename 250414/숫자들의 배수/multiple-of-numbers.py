n=int(input())
cnt=0
s=1
while cnt!=2:
    elem=n*s
    s+=1
    if elem % 5 == 0:
        cnt+=1
    print(elem,end=' ')
