# 백준 1987 알파벳

# 세로 r 가로 c
# 1, 1에는 말이 있고 각각 알파벳이 있음.
# 각각 다른 알파벳을 지나가야함
# 최대 몇칸 갈 수 있는지?

from collections import defaultdict

dxy = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def dfs():

    visited = [[0] * c for _ in range(r)]
    visited[0][0] = 1
    check = defaultdict(int)
    check[arr[0][0]] += 1
    stack = [(0, 0)]
    max_count = 0
    while stack:
        x, y = stack.pop()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if -1 < nx < r and -1 < ny < c:
                if not visited[nx][ny] and not check[arr[nx][ny]]:
                    visited[nx][ny] = 1
                    check[arr[nx][ny]] += 1
                    stack.append((nx, ny))
                    print(x, y)
                    print(nx, ny, check)
    return max_count


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
answer = dfs()
print(answer)