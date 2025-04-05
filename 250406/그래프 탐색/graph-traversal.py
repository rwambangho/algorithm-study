n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph=[[] for _ in range(n+1)]
for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)


visited=[False]*(n+1)
def dfs(node):
    visited[node]=True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(1)
print(visited.count(True)-1)


# Please write your code here.
