n=list(map(int,input().split()))
funder=list()
fup=list()
for elem in n:
    if elem < 500:
        funder.append(elem)
    elif elem > 500:
        fup.append(elem)
print(max(funder), min(fup))
