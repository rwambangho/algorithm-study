def solution(n, lost, reserve):
    answer = 0
    # 여벌 있는 사람 중 자기 자신이 도난당한 경우 제거
    reserve = set(reserve)
    lost = set(lost)
    
    # 여벌도 있고 도난도 당한 사람은 제외
    intersect = reserve & lost
    reserve -= intersect
    lost -= intersect
    
    for elem in sorted(reserve):
        if elem-1 in lost:
            lost.remove(elem-1)
        elif elem+1 in lost:
            lost.remove(elem+1)
    answer=n-len(lost)
    return answer