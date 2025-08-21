s=input()
s=list(s)
k=len(s)
for i in range(k):
    if s[i]=='e':
        s.pop(i)
        break
s=''.join(s)
print(s)