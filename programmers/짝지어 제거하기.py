# 프로그래머스 짝지어 제거하기

# 알파벳 2개 붙어있는 짝 찾기
# 제거 -> 문자열 이어 붙이기
# 반복 -> 모두 제거
# 가능 : 1 불가능 : 0 return

def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if stack:
        return 0
    return 1

print(solution("baabaa"))
# 1
print(solution("cdcd"))
# 0