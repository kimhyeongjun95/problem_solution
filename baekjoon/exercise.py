# 백준 13460 구슬 탈출 2

# 빨간 구슬을 구멍을 통해서 빼내기 / 파란 구슬 실패 / 동시에 빠져도 실패
# 왼쪽 / 오른쪽 / 위쪽 / 아래쪽 기울이기 가능

# '.' : 빈 칸
# '#' : 장애물 또는 벽
# 'O' : 구멍 위치
# 'R' : 빨간 구슬의 위치
# 'B' : 파란 구슬의 위치

# 최소 몇 번 만에 구멍을 통해 빼낼 수 있는가? / 10번 초과 -> -1

from collections import deque

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            srx, sry = i, j
        elif board[i][j] == 'B':
            sbx, sby = i, j

def move(x, y, dx, dy):
    count = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    check = set()
    queue = deque()
    check.add((srx, sry, sbx, sby))
    queue.append((srx, sry, sbx, sby, 1))

    while queue:
        rx, ry, bx, by, dist = queue.popleft()

        if dist > 10:
            break

        for dx, dy in dxy:
            nrx, nry, r_count = move(rx, ry, dx, dy)
            nbx, nby, b_count = move(bx, by, dx, dy)
    

            if board[nbx][nby] == 'O': # 파란구슬이 구멍에 들어가면
                continue
            if board[nrx][nry] == 'O':
                return dist

            if nrx == nbx and nrx == nby: # 충돌
                if r_count > b_count:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if (nrx, nry, nbx, nby) not in check:
                check.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, dist+1))
        
    return -1

print(bfs())