s=input()
s=list(s)
f=s[1]
for i in range(len(s)):
    if s[i]==f:
        s[i]=s[0]

s=''.join(s)
print(s)