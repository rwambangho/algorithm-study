n=int(input())
p, pp = 1, n
print(p, pp, end=' ')
while True:
    p+=pp
    pp+=p
    if p>=100:
        print(p)
        break
    elif pp>=100:
        print(pp)
        break
    else:
        print(p, pp,end=' ')
    
    
    