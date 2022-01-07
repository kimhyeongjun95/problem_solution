# 프로그래머스 완주하지 못한 선수

from collections import defaultdict
def solution(participant, completion):
    result = defaultdict(int)
    for i in participant:
        result[i] += 1
    
    for i in completion:
        result[i] -= 1
    
    answer = []
    for key, val in result.items():
        if val > 0:
            answer.append(key)
    return ''.join(answer)