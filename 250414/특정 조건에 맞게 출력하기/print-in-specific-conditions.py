l=list(map(int,input().split()))
for elem in l:
    if elem == 0:
        break
    else:
        if elem % 2 == 0:
            print(elem//2,end=' ')
        else:
            print(elem+3,end=' ')
