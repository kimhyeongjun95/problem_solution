# 백준 16926 배열 돌리기 1

# 배열 반 시계로 돌리기

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    # 4 4 2
    # 1 2 3 4
    # 5 6 7 8
    # 9 10 11 12
    # 13 14 15 16
    for i in range(min(n, m) // 2 ): # 0, 1
        x, y = i, i
        temp = arr[i][i]

        for j in range(i+1, n-i): # 좌
            # 0+1, 4-0
            # 1~3
            x = j
            value = arr[x][y] # 임시 저장
            arr[x][y] = temp # 밑으로 내려가고
            temp = value # 마지막 값 임시 저장

        for j in range(i+1, m-i): # 하
            y = j
            value = arr[x][y]
            arr[x][y] = temp
            temp = value

        for j in range(i+1, n-i): # 우
            x = n - j - 1
            value = arr[x][y]
            arr[x][y] = temp
            temp = value

        for j in range(i+1, m-i): # 상
            y = m-j-1
            value = arr[x][y]
            arr[x][y] = temp
            temp = value

print()
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()