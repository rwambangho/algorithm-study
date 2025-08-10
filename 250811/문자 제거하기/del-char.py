s=input()
while(len(s)>1):
    k=int(input())
    s=list(s)
    if k > len(s):
        del s[-1]
    else:
        del s[k]
    s=''.join(s)
    print(s)

