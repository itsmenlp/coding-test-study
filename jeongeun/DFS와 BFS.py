from collections import deque

n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# DFS
visited = {i: False for i in range(1, n+1)}
stack = [v]
dfs_result = []

while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        dfs_result.append(node)
        stack.extend(sorted(graph[node], reverse=True))

print(" ".join(map(str, dfs_result)))

# BFS
visited = {i: False for i in range(1, n+1)}
queue = deque([v])
bfs_result = []

while queue:
    node = queue.popleft()
    if not visited[node]:
        visited[node] = True
        bfs_result.append(node)
        queue.extend(sorted(graph[node]))

print(" ".join(map(str, bfs_result)))
