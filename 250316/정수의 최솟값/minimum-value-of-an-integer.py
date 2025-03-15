a, b, c = map(int, input().split())

# Please write your code here.
def add(a,b,c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    elif c <= a and c <= b:
        return c

print(add(a,b,c))
        