# 전보

# N개의 도시

# C라는 도시에서 위급상황 발생
# C에서 보낸 메세지를 받게되는 도시의 개수와 걸리는 시간 얼마인지 계산

import heapq

# n: 도시 개수, m: 통로 개수, c: 메세지 보내고자 하는 도시
n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = float('inf') * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

heap = []
heapq.heappush(heap, (0, c))

while heap:
    dist, node = heapq.heapify(heap)
    if distance[node] < dist:
        continue
    for i in graph[node]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(heap, (cost, i[0]))

count = 0
max_distance = 0
for i in distance:
    if i != float('inf'):
        count += 1
        max_distance = max(max_distance, i)

print(count-1, max_distance)
