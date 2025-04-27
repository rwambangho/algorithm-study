s=[list(map(int,input().split())) for _ in range(7)]
k=[[0 for _ in range(3)]for _ in range(3)]
for i in range(3):
    for j in range(3):
        k[i][j]=s[i][j]*s[i+4][j]
for row in k:
    for elem in row:
        print(elem, end=' ')
    print()

