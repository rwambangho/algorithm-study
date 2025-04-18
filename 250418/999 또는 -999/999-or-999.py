import sys
n=map(int,input().split())
max_val=-sys.maxsize
min_val=sys.maxsize
for elem in n:
    if elem != 999 and elem != -999:
        if elem > max_val:
            max_val=elem
        if elem < min_val:
            min_val=elem
print(max_val, min_val)
        
