s=[list(input().split())for _ in range(5)]
for i in range(5):
    for j in range(3):
        k=s[i][j]
        print(k.upper(),end=' ')
    print()

