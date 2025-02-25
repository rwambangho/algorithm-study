n=int(input())


for i in range(1,n+1):
    n/=i
    if n <= 1:
        i-=1
        break
    
print(i)        
   
