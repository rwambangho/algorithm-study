from collections import deque
def solution(n):
    answer = 1
    queue=deque([0,1])
    for _ in range(n-1):
        answer+=queue.popleft()
        queue.append(answer)
    answer%=1234567
    return answer