n = int(input())

def star(byeol):
    if byeol==0:
        return
    for _ in range(byeol):
        print('*',end=' ')
    print()
    star(byeol-1)
    for _ in range(byeol):
        print('*',end=' ')
    print()
    

star(n)
# Please write your code here.