n = int(input())

# Please write your code here.
def numrec(n):
    cnt=1
    for _ in range(n):
        for _ in range(n):
            if cnt != 10:
                print(f"{cnt}",end=' ')
                cnt+=1
                
            else:
                cnt=1
                print(f"{cnt}", end=' ')
                cnt+=1
        print()
                
    

numrec(n)

            