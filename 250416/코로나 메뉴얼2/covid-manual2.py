cnt_arr=[0 for _ in range(4)]
for _ in range(3):
    s=input().split()
    if s[0] =='Y' and int(s[1])>=37:
        cnt_arr[0]+=1
    elif s[0] == 'N' and int(s[1])>=37:
        cnt_arr[1]+=1
    elif s[0] == 'Y' and int(s[1])<37:
        cnt_arr[2]+=1
    elif s[0] == 'N' and int(s[1])<37:
        cnt_arr[3]+=1
    

for elem in cnt_arr:
    print(elem, end=' ')
if cnt_arr[0]>=2:
    print('E')
    

    