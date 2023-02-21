# 백준 1766 문제집

# N개의 문제
# 난이도 순서로 출제
# 1번: 가장 쉬운, N번: 가장 어려운

# 먼저 푸는 것이 좋은 문제가 있다.
# 1. N개의 문제를 모두 풀어야함.
# 2. 먼저 푸는 것이 좋은 문제는 반드시 먼저
# 3. 가능하면 쉬운 문제부터

# 위상 정렬

import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

result = []
heap = []

for i in range(1, N+1):
    if not indegree[i]:
        heapq.heappush(heap, i)

while heap:
    now = heapq.heappop(heap)
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if not indegree[i]:
            heapq.heappush(heap, i)
    
for i in result:
    print(i, end=' ')