# 프로그래머스 모의고사

def solution(answers):
    result = [0] * 3
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    idx = 0
    
    for i in answers:
        if i == p1[idx%5]:
            result[0] += 1
        if i == p2[idx%8]:
            result[1] += 1
        if i == p3[idx%10]:
            result[2] += 1
        idx += 1
        
    answer = []
    max_number = max(result)
    for i in range(len(result)):
        if max_number == result[i]:
            answer.append(i+1)
            
    return answer
        