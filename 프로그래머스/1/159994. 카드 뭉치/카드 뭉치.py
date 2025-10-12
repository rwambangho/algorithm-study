from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'
    goal=deque(goal)
    cards1=deque(cards1)
    cards2=deque(cards2)
    
    
    # goal을 탐색 
    # cards1과 cards2의 popleft에 goal의 첫번째 단어가 있는지 확인
    # 
    # 둘 다 없다면 answer에 No를 반환
    while goal:
        
        if cards1[0]==goal[0]:
            goal.popleft()
            c1=cards1.popleft()
            cards1.append(c1)
        elif cards2[0]==goal[0]:
            goal.popleft()
            c2=cards2.popleft()
            cards2.append(c2)
        else:
            answer='No'
            break
            
        
        
        
    
        
        
    
        
    return answer