l=input()
o=''
o=l
print(l)
state=True
while state==True:
    l=l[-1]+l[:-1]
    
    if l==o:
        state = False
        
    print(l)


