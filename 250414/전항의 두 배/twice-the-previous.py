n,m=map(int,input().split())
arr = [n, m]
cnt = 2

while cnt<10:
    arr.append(arr[cnt - 1] + (2*arr[cnt - 2]))
    cnt+=1
	

for elem in arr:
	print(elem, end=" ")
