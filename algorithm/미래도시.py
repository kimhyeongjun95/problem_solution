# 1 ~ N 회사
# 특정 회사끼리 서로 도로를 통해 연결
# 방문 판매원 A: 1번 회사 위치
# X번 회사에 방문해 물건을 판매하고자 한다.

# 도로 연결: 1만큼의 시간으로 이동 가능

# A(1) => K => X
# 가능한 한 빠르게 이동하고자 한다.

# 회사 개수 N 경로의 개수 M

# M+1: 두 회사 번호 공백
# M+2: X, K 공백
# A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간
# else: -1
N, M = map(int, input().split())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

X, K = map(int, input().split())
answer = graph[1][K] + graph[X][K]

if answer >= float('inf'):
    print(-1)
else:
    print(answer)

