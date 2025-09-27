def solution(s):
    answer = -1
    
    stack=[]
    for elem in s:
        if len(stack)!=0:
            if stack[-1]==elem:
                stack.pop()
            else:
                stack.append(elem)
        else:
            stack.append(elem)
            
    if len(stack)==0:
        answer=1
    else:
        answer=0
        
        
        
        
            

    

    return answer