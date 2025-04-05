n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph=[[0 for _ in range(n+1)] for _ in range(n+1)]
for a,b in edges:
    graph[a][b]=1
    graph[b][a]=1


visited=[False]*(n+1)

# def dfs(node):
#     visited[node]=True
#     for neighbor in graph[node]:
#         if not visited[neighbor]:
#             dfs(neighbor)

# dfs(1)
# print(visited.count(True)-1)

def dfs(node):
    visited[node]=True
    for i in range(1,n+1):
        if graph[node][i]==1 and visited[i]==False:
            visited[i]=True
            dfs(i)
dfs(1)
print(visited.count(True)-1)
# Please write your code here.
