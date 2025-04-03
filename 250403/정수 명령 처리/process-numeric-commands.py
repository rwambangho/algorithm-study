N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    if line[0] == "pop":
        top= value.pop()
        print(top)
    if line[0] == "size":
        print(len(value))
        

    if line[0] == "empty":
        if not value:
            print(1)
        else:
            print(0)
    if line[0] == "top":
        print(value[-1])

        
