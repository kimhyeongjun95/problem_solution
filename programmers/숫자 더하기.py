# 프로그래머스 없는 숫자 더하기

from collections import defaultdict
def solution(numbers):
    check = defaultdict(int)
    for i in range(10):
        check[i] = 0

    for number in numbers:
        check[number] += 1
    
    answer = 0
    for key, value in check.items():
        if value == 0:
            answer += key
    return answer

print(solution([1,2,3,4,6,7,8,0])) # 14
print(solution([5,8,4,0,6,7,9])) # 6