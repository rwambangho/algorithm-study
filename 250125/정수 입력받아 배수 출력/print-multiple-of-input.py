n=int(input().split())
for n in numbers:
    for i in range(n, n * 6, n):
        print(i, end=' ')
    print()