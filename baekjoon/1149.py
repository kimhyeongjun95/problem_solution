# 백준 1149 RGB거리

# 집이 N개
# 거리는 선분으로 나타낼 수 있고
# 1번 ~ N번 집
# RGB중 하나로 칠해야함

# 1번 != 2번 색
# N번 != N-1번 색
# i(2<=i<=n-1)번 집의 색은 i-1번, i+1번의 집의 색과 같지 않아야 함

# 모든 집을 칠하는 비용의 최솟값

n = int(input())
dp = [[0] * 3 for _ in range(n)]
r, g, b = map(int, input().split())
dp[0][0] = r
dp[0][1] = g
dp[0][2] = b
for i in range(n-1):
    r, g, b = map(int, input().split())
    dp[i+1][0] = min(dp[i][1:]) + r
    dp[i+1][1] = min(dp[i][0], dp[i][2]) + g
    dp[i+1][2] = min(dp[i][:2]) + b

print(min(dp[n-1]))