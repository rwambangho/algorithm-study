def validation(s):
    stack=[]
    for elem in s:
        if elem=='(' or elem=='[' or elem=='{':
            stack.append(elem)
        else:
            if stack:
                if elem ==')' and stack[-1]=='(':
                    stack.pop()

                elif elem ==']' and stack[-1]=='[':
                    stack.pop()

                elif elem =='}' and stack[-1]=='{':
                    stack.pop()

            else:
                return False
                    
    if not stack:
        return True
    else:
        return False
    
        
                
            
            
    
def solution(s):
    answer = 0
    
    n=len(s)
    # n번만큼 문자열을 왼쪽으로 밀어준다
    for _ in range(n):
        s=s[1::]+s[0]
        if validation(s):
            answer+=1
        
        
            
    return answer