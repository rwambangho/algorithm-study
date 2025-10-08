def solution(s):
    answer = True
    stack=[]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    for elem in s:
        if elem=='(':
            stack.append(elem)
        else:
            if not stack:
                answer=False
            else:
                stack.pop()
    if stack:
        answer=False

    return answer