# 백준 2475 검증수

# 처음 5자리: 00000 ~ 99999중 수 하나
# 6번째 자리: 처음 5자리의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지

nums = list(map(int, input().split()))
answer = 0
for i in range(len(nums)):
    answer += nums[i] ** 2
answer %= 10
print(answer)