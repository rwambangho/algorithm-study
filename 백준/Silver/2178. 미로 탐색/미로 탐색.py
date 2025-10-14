from collections import deque
n,m=map(int,input().split()) # 행, 열
maps=[input() for _ in range(n)]
visited=[[-1] *m for _ in range(n)]
move=[[0,1],[0,-1],[-1,0],[1,0]]

def bfs(s):
    queue=deque([s])
    visited[s[0]][s[1]]=1
    
    while queue:
        node=queue.popleft()
        for adj in move:
            row=node[0]+adj[0]
            col=node[1]+adj[1]
            if row < 0 or row >= n or col < 0 or col >= m:
                continue
            if maps[row][col]=='0':
                continue
            if maps[row][col]=='1' and visited[row][col]==-1:
                queue.append([row,col])
                visited[row][col]=visited[node[0]][node[1]]+1
    
    return visited[n-1][m-1]

print(bfs([0,0]))