h,w=map(int,input().split())
b=int((10000*w)/(h*h))
print(b)
if b >= 25:
    print("obesity")