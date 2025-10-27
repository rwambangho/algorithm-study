n = int(input())
def f(start):
    if start>n:
        return
    print(start,end=' ')
    f(start+1)

def f2(start):
    if start==0:
        return
    print(start,end=' ')
    f2(start-1)
f(1)
print()
f2(n)
# Please write your code here.