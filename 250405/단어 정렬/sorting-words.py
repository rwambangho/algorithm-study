n=int(input())
s = [input().split() for _ in range(n)]
s_word=sorted(s)
for elem in s_word:
    print(*elem)
