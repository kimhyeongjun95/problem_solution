import sys
sys.stdin = open('input.txt')

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def find_start(maze):
    start = []
    end = []
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start.append((i, j))
    return start

def dfs(start):
    stack = []
    stack.append(start.pop())
    visited = [[0] * 16 for _ in range(16)]
    while stack:
        x, y = stack.pop()


        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if maze[nx][ny] == 3:
                return 1
            if -1 < nx < 16 and -1 < ny < 16 and not visited[nx][ny] and maze[nx][ny] == 0:
                visited[nx][ny] = 1
                maze[nx][ny] = 10
                stack.append((nx, ny))
    return 0

for tc in range(1, 11):
    # 0 길 1 벽 2 출발점 3 도착점
    t = int(input())
    # 16 x 16
    maze = [list(map(int, input())) for _ in range(16)]
    start = find_start(maze)
    answer = dfs(start)
    # for i in maze:
    #     print(i)
    print('#{} {}'.format(tc, answer))
