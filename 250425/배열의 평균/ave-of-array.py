width_avg=0
height_avg=0
whole_avg=0
s=[list(map(int,input().split()))for _ in range(2)]
for i in range(2):
    for j in range(4):
        width_avg+=s[i][j]
    print(f"{(width_avg/4):.1f}",end=' ')
    width_avg=0
print()
for j in range(4):
    for i in range(2):
        height_avg+=s[i][j]
    print(f"{(height_avg/2):.1f}",end=' ')
    height_avg=0
print()
for i in range(2):
    for j in range(4):
        whole_avg+=s[i][j]
print(f"{(whole_avg/8):.1f}",end=' ')
        