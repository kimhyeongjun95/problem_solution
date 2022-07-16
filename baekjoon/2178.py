# 백준 2178 미로 탐색

# 1 이동 가능
# 0 이동 불가능
# 좌측상단에서 우측하단까지

# 최소의 칸 수 구하는 프로그램
# 시작위치, 도착위치 포함

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
queue = deque([(0, 0)])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if -1 < nx < N and -1 < ny < M and not visited[nx][ny] and arr[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

print(visited[-1][-1])