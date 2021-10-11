# 백준 17471 게리맨더링

# N개의 구역
# 각 구역은 두 선거구 중 하나에 포함
# 한 선거구에 포함된 구역 -> 모두 연결

# 두 선거구 인구의 차이 최소화 -> 최솟값 구하기
# 나눌 수 없으면 -1

# 1. 선거구를 2개로 나눈다.
# 1-1. 모든 경우의 수 만들기


import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

n = int(input())
# 인구 구역
populations = list(map(int, input().split()))

# 인접한 구역의 정보
connect = [0]
arr = [list(map(int, input().split())) for _ in range(n)]
for i in arr:
    connect.append(i[1:]-1)

for i in range(1, n//2+1):
    combo = list(combinations(range(n), i))

print(connect)