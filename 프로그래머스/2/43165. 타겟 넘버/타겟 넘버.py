def solution(numbers, target):
    n = len(numbers)
    # 방법의 수를 세는 변수
    answer = 0
    
    # DFS 함수 정의: 현재 인덱스와 현재까지의 합계를 추적
    def dfs(index, current_sum):
        nonlocal answer # 외부의 answer 변수에 접근하기 위해 nonlocal 사용
        
        # 1. 종료 조건: 모든 숫자를 다 사용했을 때
        if index == n:
            # 2. 타겟 넘버와 일치하는지 확인
            if current_sum == target:
                answer += 1
            return
        
        # 3. 재귀 호출 (현재 숫자를 더하는 경우)
        # 다음 인덱스로 이동하며, 현재 숫자를 더한 새로운 합계를 전달
        dfs(index + 1, current_sum + numbers[index])
        
        # 4. 재귀 호출 (현재 숫자를 빼는 경우)
        # 다음 인덱스로 이동하며, 현재 숫자를 뺀 새로운 합계를 전달
        dfs(index + 1, current_sum - numbers[index])

    # DFS 시작 (0번 인덱스, 초기 합계 0)
    dfs(0, 0)
    
    return answer