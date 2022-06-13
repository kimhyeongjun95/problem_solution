# 백준 2667 단지번호붙이기

# 정사각형 모양의 지도
# 0: 집 X
# 1: 집 O

# 1. 순회하며 방문처리 및 answer.append(count +=)
# 2. 출력

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(i, j):
    
    visited[i][j] = 1
    stack = [(i, j)]
    count = 1
    while stack:
        x, y = stack.pop()
        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if -1 < nx < n and -1 < ny < n and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = 1
                count += 1
                stack.append((nx, ny))
    return count


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
num = 0
answer = []
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            count = dfs(i, j)
            answer.append(count)
            num += 1

print(num)
answer.sort()
for i in answer:
    print(i)