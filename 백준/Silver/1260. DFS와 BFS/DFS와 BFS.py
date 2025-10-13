from collections import defaultdict, deque
# 전역변수 생성
N,M,V=map(int,input().split())
graph=defaultdict(list)
visited=[False] *(N+1)

# 그래프 생성. 양방향처리 
for _ in range(1,M+1):
    n,adj=map(int,input().split())
    graph[n].append(adj)
    graph[adj].append(n)

# 숫자가 낮은거부터 방문
for i in range(1,M+1):
    graph[i].sort()

def dfs(start_node):
    # 시작노드 방문처리
    visited[start_node]=True
    print(start_node,end=' ')
    # 인접노드 순회, 미방문 노드로 재귀호출
    for neighbor in graph[start_node]:
        if not visited[neighbor]:
            dfs(neighbor)

def bfs(start_node):
    visited=[False] *(N+1)
    # 방문처리하고 큐에 푸시
    visited[start_node]=True
    queue=deque([start_node])
    print()
    print(start_node,end=' ')
    # 최근노드를 팝하고 인접노드 순회해서 미방문노드 푸시,방문처리
    while queue:
        node=queue.popleft()
        for adj_node in graph[node]:
            if not visited[adj_node]:
                queue.append(adj_node)
                visited[adj_node]=True
                print(adj_node,end=' ')
    
dfs(V)
bfs(V)