# 프로그래머스 LV1 소수 찾기

import math
def solution(n):
    answer = 0
    numbers = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1):
        j = 2
        while j * i <= n:
            numbers[j*i] = False
            j += 1
    answer = 0
    for i in range(2, len(numbers)):
        if numbers[i]:
            answer += 1
    return answer