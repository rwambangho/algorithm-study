s=list(input())
for elem in s:
    if elem==s[0]:
        elem=s[1]
    elif elem==s[1]:
        elem=s[0]
    print(elem,end='')

