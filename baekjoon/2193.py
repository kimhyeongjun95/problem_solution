# 백준 2193 이친수

# 이친수란
# 1. 0으로 시작 X
# 2. 1이 두 번 연속으로 나타나지 않는다.
# - 즉, 11을 부분 문자열로 갖지 않는다.

import sys
input = sys.stdin.readline

n = int(input())
answer = 0
dp = [0] * 91
for i in range(91):
    if i == 0:
        dp[i] = 0
    elif i == 1 or i == 2:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n])