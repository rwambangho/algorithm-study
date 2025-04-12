s=list(map(int,input().split()))
for i in range(len(s)):
    if s[i] % 3 == 0:
        print(s[i-1])
        break
