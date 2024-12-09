age,sex=input().split()
age=int(age)
age2,sex2=input().split()
age2=int(age2)
if (age >= 19 and sex == 'M') or (age2 >= 19 and sex2 == 'M'):
    print('1')
else:
    print('0')
