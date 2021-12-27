# 프로그래머스 시저 암호
def solution(s, n):
    rule = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in s:
        if i.isupper(): # 대문자
            answer += rule[(rule.find(i.lower()) + n) % 26].upper()
        elif i == ' ': # 스페이스
            answer += ' '
        else: # 소문자
            answer += rule[(rule.find(i) + n) % 26]
    
    return answer


print(solution('AB', 1)) # BC
print(solution('z', 1)) # a
print(solution('a B z', 4)) # eFd