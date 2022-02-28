# 백준 13460 구슬 탈출 2

# 빨간 구슬을 구멍을 통해서 빼내기 / 파란 구슬 실패 / 동시에 빠져도 실패
# 왼쪽 / 오른쪽 / 위쪽 / 아래쪽 기울이기 가능

# '.' : 빈 칸
# '#' : 장애물 또는 벽
# 'O' : 구멍 위치
# 'R' : 빨간 구슬의 위치
# 'B' : 파란 구슬의 위치

# 최소 몇 번 만에 구멍을 통해 빼낼 수 있는가? / 10번 초과 -> -1

# 1. DFS로 R을 O까지 이동
# 2. R의 움직임에 따라 B를 움직이도록하고
# 3. B가 O에 도착하는지 안하는지 보기

from collections import deque

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

def toNext(rx, ry, bx, by, k):
    nrx, nry, nbx, nby = rx, ry, bx, by

    while True:
        nrx = nrx + dxy[k][0]
        nry = nry + dxy[k][1]
        
        # 구멍
        if board[nrx][nry] == 'O':
            nrx, nry = -1, -1
            break

        # 장애물, 벽
        elif board[nrx][nry] == '#':
            nrx = nrx - dxy[k][0]
            nry = nry - dxy[k][1]
            break

    while True:
        nbx = nbx + dxy[k][0]
        nby = nby + dxy[k][1]

        # 구멍
        if board[nbx][nby] == 'O':
            nbx, nby = -1, -1
            break

        # 장애물, 벽
        elif board[nbx][nby] == '#':
            nbx = nbx - dxy[k][0]
            nby = nby - dxy[k][1]
            break
    
    # 구슬들이 구멍에 들어가지 않고 않고 충돌했을 경우
    if nrx != -1 and nry == nby and nrx == nbx:
        if k == 0:
            
        elif k == 1:

        elif k == 2:

        elif k == 3:


while True:
    rx, ry, bx, by, dist = deque.popleft()
    # 파란 구슬이 빠진다면
    if bx == -1 and by == -1:
        continue

    if rx == -1 and rx == -1:
        return dist

    if dist < 10:
        ndist = dist + 1
        for k in range(4):
            nrx, nry, nbx, nby = toNext(rx, ry, bx, by, k)