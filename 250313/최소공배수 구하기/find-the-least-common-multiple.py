n, m = map(int, input().split())

# Please write your code here.
def f(n,m):

    for i in range(1,101):
        if i % n ==0 and i % m == 0:
            print(i)
            break
        else:
            continue

f(n,m)

