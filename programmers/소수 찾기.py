# 프로그래머스 소수 찾기
# 소수의 개수를 반환하는 함수
import math
def solution(n):
    answer = 0
    for i in range(2, n+1):
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer

print(solution(10)) # 4
print(solution(5)) # 3