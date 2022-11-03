# 백준 11404 플로이드

# 모든 A, B에 대해서  A에서 B로 가는데 필요한 비용의 최솟값

n = int(input())
m = int(input())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()