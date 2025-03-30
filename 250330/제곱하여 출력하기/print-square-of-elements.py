n=int(input())
arr=list(map(int,input().split()))
list1=[i**2 for i in arr]
for elem in list1:
    print(elem, end=' ')

