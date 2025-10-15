def solution(n, computers):
    answer = 0
    c=len(computers)
    visited=[False] *c
    stack=[]
    def dfs(start_node):
        count=0
        # 현재노드 방문처리
        visited[start_node]=True
        stack.append(start_node)
        # 인접노드 순회해서 방문안한노드 방문하기
        for i in range(c):
            if computers[start_node][i]==1 and visited[i]==False:
                dfs(i)
        
        count+=1
        return count
    
    answer+=dfs(0)
    for i in range(c):
        if not visited[i]:
            answer+=dfs(i)
            
    return answer       
    