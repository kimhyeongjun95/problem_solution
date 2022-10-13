# 백준 11660 구간 합 구하기 5

# N x N
# (x1, y1)부터 (x2, y2)까지 합을 구하기

import sys
inpur = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sumArr = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        sumArr[i][j] = arr[i-1][j-1] + sumArr[i-1][j] + sumArr[i][j-1] - sumArr[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = sumArr[x2][y2] - sumArr[x2][y1-1] - sumArr[x1-1][y2] + sumArr[x1-1][y1-1]
    print(result)

