# 백준 11047 동전 0

# 동전 N 종류
# 합 K
# 동전 개수의 최소값

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
answer = 0
for i in range(n-1, -1, -1):
    if k >= arr[i]:
        count = k // arr[i]
        k -= count * arr[i]
        answer += count
    if k == 0:
        break
print(answer)