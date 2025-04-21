import sys
n = int(input())
a = list(map(int, input().split()))


while n>0:
    s=max(a)
    for i in range(n):
        if a[i]==s: 
            print(i+1,end=' ')#최댓값 인덱스 출력
            break
    n=i
    a=a[:i]
            
            
        

        
        

       
            
        

    

        
