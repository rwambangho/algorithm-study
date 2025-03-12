n, m = map(int, input().split())

# Please write your code here.
def num(n,m):
    for i in range(n-1, 1 ,-1):
            if n % i == 0 and m % i == 0:
                print(i)
                break
            else:
                continue
num(n,m)
            

