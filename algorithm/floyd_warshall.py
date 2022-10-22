n = int(input())
m = int(input())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[a][b] == float('inf'):
            print('INF')
        else:
            print(graph[a][b])
        