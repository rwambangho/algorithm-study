n=int(input())
p, pp = 1, n
print(p, pp, end=' ')
while True:
    p+=pp
    pp+=p
    if p>=100:
        print(p)
        break
    elif p<100 and pp>=100:
        print(p, pp)
        break
    print(p, pp,end=' ')
    
    
    