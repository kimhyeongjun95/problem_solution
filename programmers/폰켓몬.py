# 프로그래머스 폰켓몬
# N/2마리 가져가기 (n은 언제나 짝수)
# 가질 수 있는 폰켓몬 종류 수의 최댓값은 2

from itertools import combinations
from collections import defaultdict
def solution(nums):
    # half = len(nums) // 2
    # answer = 0
    # for combo in combinations(nums, half):
    #     check = defaultdict(int)
    #     for i in combo:
    #         check[i] = 1
    #     answer = max(answer, sum(check.values()))
    # return answer

    check = defaultdict(int)
    n = len(nums) // 2
    for i in nums:
        if n == 0:
            break
        if check[i] >= 1:
            continue
        check[i] = 1
        n -= 1
    return sum(check.values())

print(solution([3,1,2,3])) # 2
print(solution([3,3,3,2,2,4])) # 3
print(solution([3,3,3,2,2,2])) # 2
