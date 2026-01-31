def solution(n, computers):
    answer = 0
    visited=[False]*(n+1)
    c=len(computers)
    # 깊이우선탐색을 해서 더 이상 갈 곳이 없으면 answer+1
    def dfs(start_node):
        # 일단 시작노드 방문처리
        visited[start_node]=True
        for i in range(n):
            if computers[start_node][i]==1 and visited[i]==False:
                dfs(i)
        
        return 1
    
    answer+=dfs(0)
    for i in range(n):
        if not visited[i]:
            answer+=dfs(i)
    
          
    return answer