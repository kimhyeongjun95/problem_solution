# 백준 1260 DFS와 BFS

from collections import deque

def dfs(arr, v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in arr[v]:
        if not visited[i]:
            dfs(arr, i, visited)

def bfs(arr, v, visited):
    visited = [0] * (n+1)
    queue = deque([v])
    visited[v] = 1
    while queue:
        popped = queue.popleft()
        print(popped, end=' ')
        for i in arr[popped]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)

n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    one, two = map(int, input().split())
    arr[one].append(two)
    arr[two].append(one)
    arr[one].sort()
    arr[two].sort()

visited = [0] * (n+1)
dfs(arr, v, visited)
print()
bfs(arr, v, visited)