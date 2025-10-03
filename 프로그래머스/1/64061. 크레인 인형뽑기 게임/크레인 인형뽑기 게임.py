def solution(board, moves):
    answer=0
    b=len(board)
    lanes=[[] for _ in range(b)]
    stack=[]
    
    for i in range(b-1,-1,-1): #board의 열
        for j in range(b): #board의 행
            # board를 담을 스택을 만든다
            if board[i][j]:
                lanes[j].append(board[i][j])
            
    
    #인형뽑기 시작
    for elem in moves:
        if lanes[elem-1]:
            doll=lanes[elem-1].pop()

            if stack and stack[-1]==doll: # 뽑기통에 인형이 있고 스택의 인형과 같다면
                stack.pop() # 같다면 stack을 pop함
                answer+=2


            else:
                stack.append(doll)
            
        
            
                          
            
    return answer