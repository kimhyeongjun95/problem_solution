import sys
sys.stdin = open('input.txt')

t = int(input())

dxy = [(1, 0), (0, 1)]

def bfs(x, y):

    global path, count

    if count > path:
        return

    if x == n-1 and y == n-1:
        if path > count:
            path = count

    for dx, dy in dxy:
        nx = dx + x
        ny = dy + y
        if -1 < nx < n and -1 < ny < n and not visited[nx][ny]:
            visited[nx][ny] = 1
            count += arr[nx][ny]
            bfs(nx, ny)
            visited[nx][ny] = 0
            count -= arr[nx][ny]

for tc in range(1, t+1):
    n = int(input())

    # 0,0에서 [n-1][n-1]까지 이동했을때 최소 합
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]
    path = 99999
    count = arr[0][0]
    bfs(0, 0)
    print('#{} {}'.format(tc, path))