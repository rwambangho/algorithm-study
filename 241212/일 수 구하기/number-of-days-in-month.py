n=int(input())
if n % 2 == 0 and n != 2 and n != 8:
    print('30')
elif n % 2 == 1 or n == 8:
    print('31')
else:
    print('28')