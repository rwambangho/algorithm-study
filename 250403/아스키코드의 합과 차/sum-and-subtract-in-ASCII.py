s,k=input().split()
if ord(s)>ord(k):
    t=ord(s)-ord(k)
else:
    t=ord(k)-ord(s)
print(f"{ord(s)+ord(k)} {t}")
