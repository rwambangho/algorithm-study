n = int(input())
def f(star,n):
    for _ in range(star):
        print('*',end='')
    print()
    if star < n:
        star+=1
        f(star,n)
    else:
        return

# Please write your code here.
f(1,n)