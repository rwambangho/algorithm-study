N = int(input())
def f(n):
    def c(n):
        if n>N:
            return
        print(n,end=' ')
        c(n+1)
    if n==0:
        c(1)
        return
    print(n,end=' ')
    f(n-1)
 
f(N)


# Please write your code here.