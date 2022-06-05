# 백준 14500 테트로미노

# 폴리오미노 : 1x1 정사각형을 여러 개 이어서 붙인 도형
# 조건
#   1. 정사각형은 서로 겹치기 X 
#   2. 도형은 모두 연결 
#   3. 정사각형의 변끼리 연결. 즉, 꼭짓점과 꼭짓점만 맛닿아 있으면 X

# 테트로미노 : 정사각형 4개를 이어 붙인 폴리오미노
# 5가지 방법의 테트로미노

# N x M
# 테트로미노 하나, 테트로미노 칸에 쓰여 있는 수들의 최대 합 

# DFS 완전탐색
# 1. 모든 위치에서 dfs
# 2. count 4 까지 재귀
# 2-1. 방문처리
# 3. count == 4: 갱신
# 4. 십자형(1개 뺀) 만들어야함
# 4-1. 모든 위치에서 십자로 value 계산
# 4-2. edge가 3개인 경우
# 4.3. edge가 4개인 경우 계산

import sys
input = sys.stdin.readline

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def dfs(x, y, count, value):
    global answer
    if count == 3:
        answer = max(answer, value)
        return

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if -1 < nx < n and -1 < ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            value += arr[nx][ny]
            dfs(nx, ny, count + 1, value)
            value -= arr[nx][ny]
            visited[nx][ny] = 0
    
def cross(x, y, value):
    global answer
    edges = 0

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if -1 < nx < n and -1 < ny < m:
            edges += 1
            value += arr[nx][ny]
    
    if edges == 3:
        answer = max(answer, value)
        return
    
    if edges == 4:
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            value -= arr[nx][ny]
            answer = max(answer, value)
            value += arr[nx][ny]

visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = 0

for i in range(n):
    for j in range(m):
        cross(i, j, arr[i][j])

print(answer)