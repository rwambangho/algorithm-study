n=int(input())

sum=1
for i in range(1,1024): #x가 올라가는 수

    sum*=2


    if n==sum:
        print(i)
        break


