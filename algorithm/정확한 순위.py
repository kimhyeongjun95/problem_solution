# 정확한 순위

# 선생님은 N명의 성적 분실
# 성적을 비교한 결과의 일부만 가지고 있음.
# 학생 N명의 성적은 모두 다름

# 성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은
# 모두 몇 명인가?

n, m = map(int, input().split())
graph = [[float('inf') * (n+1) for _ in range(n+1)]]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + [i][b])

answer = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != float('inf') or graph[j][i] != float('inf'):
            count += 1
    if count == n:
        answer += 1
print(answer)