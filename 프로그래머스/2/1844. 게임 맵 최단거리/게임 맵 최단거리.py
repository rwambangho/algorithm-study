from collections import deque              
def solution(maps):
    answer = 0
    n=len(maps)
    m=len(maps[0])
    visited=[[-1] *m for _ in range(n)]
    move=[[0,1],[0,-1],[1,0],[-1,0]]
    
    def bfs(s):
        # 현재위치 푸시, 방문처리 
        count=1
        queue=deque([s])
        visited[s[0]][s[1]]=1
        

        while queue:
            node=queue.popleft()
            
            # 현재위치에서 어디어디 갈 수 있는지 보여주고 0이 아닌곳으로만 이동
            for adj in move:
                here_x=node[0]+adj[0]
                here_y=node[1]+adj[1]
                # 범위를 벗어나면 다음위치 탐색
                if here_x < 0 or here_x >= n or here_y < 0 or here_y >= m:
                    continue
                # maps에서 1이고 방문안했으면 푸시&방문처리
                if maps[here_x][here_y]==1 and visited[here_x][here_y]==-1:
                    queue.append([here_x,here_y])
                    visited[here_x][here_y]=visited[node[0]][node[1]]+1
                    
        if maps[n-1][m-1]==-1:
            return -1
        else:
            return visited[n-1][m-1]
                
    
    
        
    
    answer=bfs([0,0])
    return answer