# 백준 1012 유기농 배추

# 배추흰지렁이 : 배추근처 서식, 해충을 먹음으로써 배추 보호
# 배추흰지렁이 간 이동 가능(상하좌우)

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def counter(x, y):
    stack = []
    stack.append((x, y))
    visited[x][y] = 1

    while stack:
        x, y = stack.pop()
        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if -1 < nx < n and -1 < ny < m and not visited[nx][ny] and arr[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = 1

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    visited = [[0] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                counter(i, j)
                count += 1
    print(count)
