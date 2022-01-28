# 프로그래머스 게임 맵 최단거리

from collections import deque
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    start = (0, 0)
    queue = deque([start])
    visited = [[1] * m for _ in range(n)]
    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            print(nx, ny)
            if nx == n-1 and ny == m-1:
                return visited[x][y] + 1
            
            if -1 < nx < n and -1 < ny < n and visited[nx][ny] == 1 and maps[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return -1
        

print(solution(
[[1,0,1,1,1],
 [1,0,1,0,1],
 [1,0,1,1,1],
 [1,1,1,0,1],
 [0,0,0,0,1]])) # 11
