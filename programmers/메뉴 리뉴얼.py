# 프로그래머스 (2021 카카오) 메뉴 리뉴얼

# 단품메뉴 -> 코스요리
# 코스요리 : 1. 최소 2가지 이상의 단품메뉴 구성
#            2. 2명 이상의 손님으로부터 주문된 단품메뉴 조합

# 오름차순으로 정렬 return

from collections import defaultdict
from itertools import combinations
def solution(orders, course):

    check = defaultdict(int)
    for cor in course:
        for order in orders:
            for combo in combinations(order, cor): 
                combo = ''.join(sorted(combo))
                check[combo] += 1
    check = sorted(check.items(), key = lambda x: x[1], reverse=True)
    result = []
    for cor in course:
        temp = []
        for key, val in check:
            if cor == len(key) and val >= 2:
                temp.append((key, val))
        result.append(temp)
    answer = []
    for i in result:
        if not i:
            continue
        temp = []
        base = i[0][1]
        for j in range(len(i)):
            if base != i[j][1]:
                break
            temp.append(i[j][0])
        answer.extend(temp)
    answer.sort()
    return answer

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# ["AC", "ACDE", "BCFG", "CDE"]
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
# ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
# ["WX", "XY"]

