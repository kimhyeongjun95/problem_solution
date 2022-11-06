# 백준 1504 특정한 최단 경로

# 방향성이 없는 그래프

# 주어진 두 정점 반드시 거치기

# 1번에서 N번에서 최단거리로 이동
# 없으면 -1 출력

import heapq
import sys
input = sys.stdin.readline

n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
def dijkstra(start):
    distance = [float('inf')] * (n+1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance

dist1 = dijkstra(1)
dist2 = dijkstra(v1)
dist3 = dijkstra(v2)
answer = min(dist1[v1] + dist2[v2] + dist3[n], dist1[v2]+dist3[v1]+dist2[n])
if answer < float('inf'):
    print(answer)
else:
    print(-1)
