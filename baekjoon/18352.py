# 백준 18352 특정 거리의 도시 찾기

from collections import deque

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

queue = deque([x])
while queue:
    now = queue.popleft()
    for next in arr[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

flag = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)
