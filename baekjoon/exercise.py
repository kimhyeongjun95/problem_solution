# 백준 2096

# 밑으로 내려가기
# 최대점수와 최소 점수 출력하기
# DP문제

import sys
input = sys.stdin.readline()
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):