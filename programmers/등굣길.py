# 프로그래머스 등굣길

def solution(m, n, puddles):
	dp = [[1] * m for _ in range(n)]
	dp[0][0] = 1
	for pud in puddles:
		x, y = pud
		x -= 1
		y -= 1
		if x == 0:
			for i in range(y, n):
				dp[i][0] = 0
		if y == 0:
			for i in range(x, m):
				dp[0][i] = 0
		dp[y][x] = 0

	for i in range(1, n):
		for j in range(1, m):
			if dp[i][j] == 0:
				continue
			dp[i][j] = dp[i-1][j] + dp[i][j-1]

	return dp[n-1][m-1] % 1000000007

print(solution(4, 3, [[2, 2]]))