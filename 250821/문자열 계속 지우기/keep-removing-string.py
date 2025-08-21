A = input().strip()
B = input().strip()
m = len(B)

stack = []
for ch in A:
    stack.append(ch)
    # 스택 끝부분이 B와 같으면 삭제
    if len(stack) >= m and ''.join(stack[-m:]) == B:
        for _ in range(m):
            stack.pop()

print(''.join(stack))
