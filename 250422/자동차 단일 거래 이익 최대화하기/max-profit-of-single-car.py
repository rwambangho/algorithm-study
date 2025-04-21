n = int(input())
price = list(map(int, input().split()))
result=-1
for i in range(n-1,-1,-1):
    for j in range(i):
        if price[i]-price[j] >= 0 and price[i]-price[j]>result:
            result=price[i]-price[j]
if result < 0:
    print(0)
else:
    print(result)       




    
    
# Please write your code here.
