import sys
sys.stdin = open('input.txt')

# n개의 식재료
# n/2개씩 나누어 두개의 요리 (n은 짝수)
# A음식과 B음식의 맛의 차이가 최소가 되도록 재료 배분

# 시너지 정보 -> 두 음식 간의 맛의 차이 최소화
# 차이 : abs(a-b)
from itertools import combinations

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    synergy = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    for combo1 in combinations(range(n), n//2):
        combo2 = [i for i in range(n) if i not in combo1]
        for i in range(n//2-1):
            for j in range(i+1, n//2):
                result1 = synergy[combo1[i]][combo1[j]] + synergy[combo1[i]][combo1[j]]
                result2 = synergy[combo2[i]][combo2[j]] + synergy[combo2[i]][combo2[j]]

    # 차이
    result = abs(result1 - result2)
    answer = min(answer, result)
    print('#{} {}'.format(tc, answer))
