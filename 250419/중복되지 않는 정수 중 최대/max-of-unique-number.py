n = int(input())
nums = list(map(int, input().split()))
cnt_arr=[0 for _ in range(1001)]
stack=[]
for elem in nums:
    cnt_arr[elem]+=1
for elem in cnt_arr:
    if elem == 1:
        stack.append(cnt_arr.index(elem))
if len(stack) != 0:
    print(max(stack))
else:
    print(-1)






    


    



    




    
# Please write your code here.
