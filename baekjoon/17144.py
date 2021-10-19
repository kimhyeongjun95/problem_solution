# 백준 17144 미세먼지 안녕!

# 공기청정기 항상 1열(i), 크기는 두 행(2i)
# 설치되지 않은 칸은 미세먼지

# 1. 미세먼지 확산, : 미세먼지 // 5
# 남은 양 : 원래 양 - 원래 양 // 5 x 방향의 수
# 1-1. 인접한 방향에 공기청정기 o or 칸 x 확산 x
# 2. 공기청정기 작동: (위)반시계 (아래)시계 -> 테두리만 움직이게 함.
# 2-1. 미세먼지 -> 바람의 방향대로 한 칸씩 이동

import sys
input = sys.stdin.readline

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def cleaner(x, y, direction, temp):
    for i in range(4):
        while True:
            nx = x + dxy[direction[i]][0]
            ny = y + dxy[direction[i]][1]
            if -1 < nx < n and -1 < ny < m and room[nx][ny] == -1:
                return
            if -1 < nx < n and -1 < ny < m:
                room[nx][ny] = temp[x][y]
            else:
                break
            x, y = nx, ny

def everything():
    # 0: 공간, -1: 공기청정기, 숫자: 미세먼지
    filter = []
    for _ in range(t):
        temp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if room[i][j] == -1:
                    temp[i][j] = -1
                    filter.append((i, j))
                    continue
                if room[i][j] > 0:
                    count = 0
                    for dx, dy in dxy:
                        nx = dx + i
                        ny = dy + j
                        # 확산할 수 있고 보는 곳이 공기청정기가 아니라면
                        if -1 < nx < n and -1 < ny < m and room[nx][ny] != -1:
                            temp[nx][ny] += room[i][j] // 5
                            count += 1
                    temp[i][j] += room[i][j] - room[i][j] // (5*count)
        
        for i in range(n):
            for j in range(m):
                room[i][j] = temp[i][j]

        x, y = filter.pop()
        cleaner(x+1, y, [0, 2, 1, 3], temp)
        room[i][j+1] = 0 # 공기청정기 옆칸은 0
        x, y = filter.pop()
        cleaner(x+1, y, [0, 3, 1, 2], temp)
        room[i][j+1] = 0
    
    answer = 0
    for i in range(n):
        answer += sum(room[i])

    return answer + 2 # 공기청정기의 합이 -2

# x, y, 시간
n, m, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
everything()
print(everything)