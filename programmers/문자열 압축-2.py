# 프로그래머스 (2020 카카오) 문자열 압축
# 재풀이

def solution(s):
    answer = len(s)

    for i in range(1, (len(s) // 2) + 1):
        temp = ''
        prev = s[:i]
        count = 1
        for j in range(i, len(s), i):
            if prev == s[j:j+i]:
                count += 1
            else:
                if count >= 2:
                    temp += str(count) + prev
                    count = 1
                else:
                    temp += prev

                prev = s[j:j+i]

        if count >= 2:
            temp += str(count) + prev
        else:
            temp += prev

        answer = min(answer, len(temp))

    return answer


print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))