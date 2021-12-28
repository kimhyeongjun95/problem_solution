# 프로그래머스 이상한 문자 만들기
def solution(s):
    answer = []
    s = s.split(' ')
    for i in s:
        temp = ''
        for j in range(len(i)):
            if j % 2 == 0: # 짝수라면
                temp += i[j].upper()
            else: # 홀수라면
                temp += i[j].lower()
        answer.append(temp)
    answer = ' '.join(answer)
    return answer

print(solution("try hello world")) # "TrY HeLlO WoRlD"
