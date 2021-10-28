t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    nx = 0
    ny = 0
    cnt = 0

    for i in range(1, (n*n)+1):
        arr[nx][ny] = i
        nx += dx[cnt]
        ny += dy[cnt]

        if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] > 0:
            nx -= dx[cnt]
            ny -= dy[cnt]

            cnt = (cnt + 1) % 4

            nx += dx[cnt]
            ny += dy[cnt]

    print('#{0}'.format(tc))

    for x in arr:
        print(*x)
