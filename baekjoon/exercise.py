# 백준 11726 2 x n 타일링

# 2xn 크기의 직사각형
# 1x2, 2x1로 채우는 방법의 수

# 2 x 1 : 1
# 2 x 2 : 2
# 2 x 3 : 3
# 2 x 4 : 5
# 피보나치

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n] % 10007)
