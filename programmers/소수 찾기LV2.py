# 프로그래머스 LV2 소수 찾기

# 흩여진 종이 조각을 붙여 소수 몇개를 만들 수 있을지?
# [1, 7] => [7, 17, 71]
# [0, 1, 1] => [11, 101]

# 1. 경우의 수 permutations로 만들기
# 2. 소수인지 판별
# 3. 소수라면 answer += 1

from itertools import combinations, permutations
def solution(numbers):

    answer = 0
    result = []
    for i in range(1, len(numbers)+1):
        for combo in list(permutations(numbers, i)):
            result.append(int(''.join(combo)))

    answer = 0
    # print(list(set(result)))
    for i in list(set(result)):
        if i < 2:
            continue
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            answer += 1

    return answer

print(solution("17"))
# 3
print(solution("011"))
# 2