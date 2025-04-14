n=int(input())
l=map(int,input().split())
r=[]
for elem in l:
    if elem % 2 == 0:
        r.append(elem)
print(*r)
