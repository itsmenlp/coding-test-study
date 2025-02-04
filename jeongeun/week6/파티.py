import heapq
import sys

def dijkstra(start, n, graph):
    INF = float('inf')
    distance = [INF] * (n+1)
    distance[start] = 0
    pq = [(0, start)]
    
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
            
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
                
    return distance

data = sys.stdin.read().splitlines()
n, m, x = map(int, data[0].split())

graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

for i in range(1, m+1):
    start, end, time = map(int, data[i].split())
    graph[start].append((end, time))
    reverse_graph[end].append((start, time))
    
to_x = dijkstra(x, n, reverse_graph)
from_x = dijkstra(x, n, graph)

max_time = 0
for i in range(1, n+1):
    if i != x:
        max_time = max(max_time, to_x[i] + from_x[i])

print(max_time)
