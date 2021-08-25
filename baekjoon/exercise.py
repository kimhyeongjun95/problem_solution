import sys
sys.setrecursionlimit(100000)

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def find_area(x, y, height):
    # for i in range(4):
    #     visited[x][y] = 1
    #     nx = x + dx[i]
    #     ny = y + dy[i]

    #     if -1 < nx < n and -1 < ny < n and area[nx][ny] > height and visited[nx][ny] == 0:
    #         find_area(nx, ny, height)

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and area[nx][ny] > height and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append((nx, ny))

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

temp = []
for i in area:
    temp.append(max(i))
max_height = max(temp)

answer = []
for height in range(max_height+1):
    count = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] > height and visited[i][j] == 0:
                visited[i][j] = 1
                find_area(i, j, height)
                count += 1
    # print(visited)
    answer.append(count)

print(max(answer))