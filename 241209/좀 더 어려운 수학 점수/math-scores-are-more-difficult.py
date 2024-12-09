a,b=map(int,input().split()) 
c,d=map(int,input().split())
if (a > c and b == d) or (a > c and b <= d) or (a > c and b >= d):
    print("A")
elif (a < c and b == d) or (a < c and b <= d) or (a < c and b >= d):
    print("B")
elif (a == c and b > d):
    print("A")
elif (a == c and b < d):
    print("B")
else:
    print("fuck")