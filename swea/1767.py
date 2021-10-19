# SWEA 1767 프로세서 연결하기

#  N x N
# 전선은 직선으로만 설치가능, 교차 불가능
# 가장자리는 이미 연결된걸로 간주

# 0: 빈 셀, 1: Core
# 1. 최대한 많은 코어에 전원 연결
# 2. 최소 전선 길이의 합

# 경우의 수를 봐야하나?

def dfs

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    core = []

    for i in range(1, n-1):):
        for j in range(1, n-1):
            if arr[i][j] == 1:
                core.append((i, j))

