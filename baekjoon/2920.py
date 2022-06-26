# 백준 2920 음계

# 다장조: cdefgabC 총 8개 음
# 8개 음 => c:1, d:2 ...
# 1~8 ascending 8~1 descending else: mixed

nums = list(map(int, input().split()))
answer = ''
if nums[0] == 1:
    for i in range(1, len(nums)):
        if nums[i] != i + 1:
            answer = 'mixed'
            break
    else:
        answer = 'ascending'
elif nums[0] == 8:
    for i, j in zip(range(len(nums)-1, -1, -1), range(1, len(nums))):
        if nums[j] != i:
            answer = 'mixed'
            break
    else:
        answer = 'descending'
else:
    answer = 'mixed'

print(answer)