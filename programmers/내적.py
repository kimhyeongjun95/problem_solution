# 프로그래머스 LEVEL 1: 월간코드 챌린지 시즌 1 > 내적

def solution(a, b):
    # a와 b의 길이는 동일하다.
    answer = 0
    for i in range(len(a)):
        answer += (a[i]*b[i])
        
    return answer