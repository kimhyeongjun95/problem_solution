# 백준 11048 이동하기

# 1,1 에서 n,m으로
# 우, 하, 대각선 우하
# 우, 하로만 이동했을때 이전 값 갱신하면 될듯하다.

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = arr[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n][m])