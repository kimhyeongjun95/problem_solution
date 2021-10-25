# 백준 16926 배열 돌리기 1

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m)//2):
        x = i
        y = i
        temp = arr[x][y]

        # 왼쪽
        for j in range(i+1, n-i):
            x = j
            value = arr[x][y]
            arr[x][y] = temp
            temp = value
        
        # 아래
        for j in range(i+1, m-i):
            y = j
            value = arr[x][y]
            arr[x][y] = temp
            temp = value

        # 오른쪽
        for j in range(i+1, n-i):
            x = n - 1 - j
            value = arr[x][y]
            arr[x][y] = temp
            temp = value

        # 위쪽
        for j in range(i+1, m-i):
            y = m - 1 - j
            value = arr[x][y]
            arr[x][y] = temp
            temp = value
    
for i in arr:
    print(*i)