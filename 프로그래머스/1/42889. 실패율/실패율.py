def solution(N, stages): 
    # N은 총 스테이지 수
    # stages는 각 사용자의 현재 스테이지 위치
    ch=[0 for _ in range(N+3)] # 스테이지 별 도전자 수를 구함
    st=len(stages)
    for elem in stages: 
        ch[elem]+=1
    
    # 스테이지별 실패한 사용자 수 계산 
    # 스테이지별로 순회해서 스테이지랑 같은 수의 원소를 담으면 실패한 사용자 수임
    # 실패율을 구한다
    # 각 스테이지를 순회하며 실패율 계산=실패자/도전자
    failure={}
    for i in range(1,N+1):
        
        if ch[i]==0: # 도전한 사람이 없는 경우 실패율은 0
            failure[i]=0
        else:
            failure[i]=ch[i]/st
            st-=ch[i]
    # 다음 스테이지 실패율을 위해 현재 스테이지의 인원을 뺀다
    # 실패율이 높은 스테이지 부터 내림차순 정렬 
    answer=sorted(failure, key=lambda x: failure[x], reverse=True)
    
    return answer

