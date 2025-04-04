from collections import deque
N = int(input())
command = []
A = deque()

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    if line[0] == "pop":
        num=A.popleft()
        print(num)
    if line[0] == "size":
        print(len(A))
    if line[0] == "empty":
        print(1 if len(A) == 0 else 0)
    if line[0] == "front":
        print(A[0])

# Please write your code here.