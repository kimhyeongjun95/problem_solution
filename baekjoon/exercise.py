# 백준 19236 청소년 상어

# 4 X 4
# 한 칸에는 물고기 한 마리 존재
# 각 물고기는 번호와 방향을 가짐

# 번호는 16이하
# 방향은 8가지 중 하나

# 0, 0 물고기 먹고 들어감 -> 상어의 방향은 물고기의 방향과 같음

# 물고기 이동 : 번호가 작은순부터
# 이동 O : 빈칸 or 다른 물고기 있는 칸
# 이동 X : 상어 o or 공간을 넘는 칸

# 이동할 수 있을때까지 반시계방향 45도 회전
# 이동 불가능 -> 이동 X
# 다른 물고기가 있는 칸? swap

# 물고기 이동이 끝나면 상어 이동
# 여러개 칸 이동 가능 -> 경우의 수가 생김

# 물고기 번호의 합의 최댓값 구하기

import copy

dxy = [
    (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)
]

answer = 0
arr = [[False] * 2 for _ in range(4) for _ in range(4)]

for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        arr[i][j][0] = temp[j*2]
        arr[i][j][1] = temp[j*2+1] - 1

def rotate(dir):
    return (dir + 1) % 8

def finder(arr, idx):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == idx:
                return (i, j)
    return False

def move_fish(arr, tx, ty):
    for i in range(1, 17):
        temp = finder(arr, i)
        if temp:
            x, y = temp[0], temp[1]
            dir = arr[x][y][1]

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if -1 < nx < 4 and -1 < ny < 4:
                    if nx != tx and ny != ty:
                        arr[x][y][1] = dir
                        arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                        break
                dir = rotate(dir)

def move_shark(arr, nx, ny):
    possible = []
    dir = arr[nx][ny][1]

    for i in range(4):
        nx += dxy[dir][0]
        ny += dxy[dir][1]
        if -1 < nx < 4 and -1 < ny < 4:
            if arr[nx][ny][0]

def dfs(arr, nx, ny, count):
    global answer

    arr = arr.copy()
    count += arr[nx][ny][0] # 물고기 먹기
    arr[nx][ny][0] = -1 

    move_fish(arr, nx, ny)
    possible = move_shark(arr, nx, ny)


dfs(arr, 0, 0, 0)