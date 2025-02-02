import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

graph = {i: set() for i in range(1, n+1)}
visited = [False] * (n+1)

index = 2
for _ in range(m):
    u, v = int(data[index]), int(data[index+1])
    graph[u].add(v)
    graph[v].add(u)
    index += 2
    
count = 0

for node in range(1, n+1):
    if not visited[node]:
        count += 1
        queue = deque([node])
        visited[node] = True
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    
print(count)
