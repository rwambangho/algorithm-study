def solution(n, k, cmd):
    answer = ''
    deleted=[]
    up=[i-1 for i in range(n+2)]    
    down=[i+1 for i in range(n+1)]
    k+=1
    for elem in cmd:   
        # 삭제
        if elem.startswith('C'):
            deleted.append(k)
            up[down[k]]=up[k]
            down[up[k]]=down[k]
            k=up[k] if n<down[k] else down[k]
            
        # 복구
        elif elem.startswith('Z'):
            r=deleted.pop()
            down[up[r]]=r
            up[down[r]]=r
        
        # 업 or 다운
        else: 
            action,num=elem.split()
            if action=='U':
                for _ in range(int(num)):
                    k=up[k]
            else:
                for _ in range(int(num)):
                    k=down[k]
        
    answer=["O"]*n
    for i in deleted:
        answer[i-1]="X"
            
            
    return "".join(answer)