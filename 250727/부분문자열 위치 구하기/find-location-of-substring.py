input_str = input()
target_str = input()


if target_str not in input_str:
    print(-1)
else:
    for i in range(len(input_str)):
        if input_str[i]==target_str[0]:
            print(i)
            break


    
# Please write your code here.
