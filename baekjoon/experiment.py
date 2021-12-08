dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def start(n, m, mountain):
    for i in range(n):
        for j in range(m):
            if mountain[i][j] == 2:
                return i, j

def climb(visited):

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if -1 < nx < m and -1 < ny < n:
                if not visited[nx][ny] and not count:


    

t = int(input())
for tc in range(1, t+1):
    m, n, l = map(int, input().split())
    count = l
    mountain = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    result = 0
    answer = 0
    x, y = start()
    queue = deque([(x, y)])
    visited[x][y] = 1
    climb()