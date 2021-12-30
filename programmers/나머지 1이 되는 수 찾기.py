# 프로그래머스 나머지 1이 되는 수 찾기

def solution(n):
    answer = 1
    while True:
        if n % answer == 1:
            return answer
        answer += 1

print(solution(10)) # 3
print(solution(12)) # 11