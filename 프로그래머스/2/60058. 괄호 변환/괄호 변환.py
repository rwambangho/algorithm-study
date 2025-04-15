def cor(a):
    left_stack=[]
    right_stack=[]
    
    for elem in a:
        if elem == '(':
            left_stack.append(elem)
        else:
            if len(left_stack) == 0:
                right_stack.append(elem)
            else:
                left_stack.pop()
    
    if len(left_stack) != 0 and len(right_stack) != 0:
        return False
    else:
        return True

        
            
def solution(p):
    answer = ''
    temp=''
    u,v= [],[]
    if p=='': #빈 문자열이면 빈 문자열 반환
        return p
    
    if cor(p): #올바른 괄호 문자열이면 그대로 반환
        return p
    else: #아니라면 u,v로 분리
        for i in range(len(p)): #p를 하나씩 꺼내면서 u가 균형잡힌 문자열이 될때까지 담음
            u.append(p[i])
            if u.count('(') == u.count(')'): #u가 균형잡힌 문자열이면 나머지를 v에 담음
                v.append(p[i+1:])
                break
            
                
        if cor(u): #u가 올바른 문자열이면 u를 저장해두고 v를 재귀적으로 실행
            answer=''.join(u) + solution(''.join(v))
            
        else: 
            #u가 올바른 문자열이 아니라면   
            #빈 문자열에 첫번째 문자로 '('를 붙인다
            #v를 재귀적으로 수행한 결과를 이어 붙인다
            #')'를 붙인다
            #u의 첫번째, 마지막 문자 제거후 나머지 문자열의 방향을 뒤집어서 뒤에 붙인다
            answer = ''.join('(')
            answer += solution(''.join(v)) 
            answer += ''.join(')')
            u=u[1:-1]
            for i in range(len(u)):
                if u[i] == '(':
                    u[i]=')'
                else:
                    u[i]='('
            answer += ''.join(u)
            
        
    return answer