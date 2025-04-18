n = int(input())
nums = list(map(int, input().split()))
cnt_arr=[0 for _ in range(1001)]
stack=[]
for elem in nums:
    cnt_arr[elem]+=1
for i in range(1001):
    if cnt_arr[i] == 1:
        stack.append(i)
if len(stack) != 0:
    print(max(stack))
else:
    print(-1)






    


    



    




    
# Please write your code here.
