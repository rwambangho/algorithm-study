a = int(input()) # 남자는 0, 여자는 1
b= int(input()) # 나이

if a==0:
    if b >= 19:
        print('MAN')
    else:
        print('BOY')
else:
    if b >= 19:
        print('WOMAN')
    else:
        print('GIRL')