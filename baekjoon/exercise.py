# 백준 20057 마법사 상어와 토네이도

# A[r][c] : 모래의 양
# 가운데 칸부터 토네이도의 이동 시작

# 토네이도의 양은 1,1까지 이동한 뒤 소멸
# 소멸 뒤, 격자의 밖으로 나간 모래의 양은?

import sys
input = sys.stdin.readline

    #좌, 하, 우, 상 -> 좌회전
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def shark_tornado():
    direction = 0
    nx = n//2
    ny = n//2

    for _ in range(n**2):
        temp = arr[nx][ny]
        
        nx += dx[direction]
        ny += dy[direction]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            nx -= dx[direction]
            ny -= dy[direction]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

shark_tornado()