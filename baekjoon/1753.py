# 백준 1753 최단경로

# 다익스트라 알고리즘
# 방향 그래프가 주어짐
# 주어진 시작점에서 다른 모든 정점으로의 최단경로를 구하는 프로그램
#
# 모든 간선의 가중치 10 이하의 자연수

import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [float('inf') for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

heap = []
heapq.heappush(heap, (0, start))
distance[start] = 0
while heap:
    dist, node = heapq.heappop(heap)
    for i in graph[node]:
        cost = i[1] + dist
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(heap, (cost, i[0]))

for i in range(1, V+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])