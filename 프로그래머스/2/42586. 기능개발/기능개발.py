import math
def solution(progresses, speeds):
    answer = [] # 배포하는 기능의 수
    n=len(progresses)
    days_left=[math.ceil((100-progresses[i])/speeds[i]) for i in range(n)]
    
    count=0
    md=days_left[0]
    
    for i in range(n):
        if days_left[i] <= md:
            count+=1
        else:
            answer.append(count)
            count=1
            md=days_left[i]
    
    answer.append(count)
        
            
    
    
            
            
            
            
        
    return answer