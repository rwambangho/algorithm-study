n=int(input())
arr= list(map(float,input().split()))

total=sum(arr)


val=total/n
if val > 0:
    print(f"{val:.1f}")
    if val >= 4.0:
        print("Perfect")
    elif val >= 3.0:
        print("Good")
    else:
        print("Poor")


