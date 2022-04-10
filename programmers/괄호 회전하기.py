# 프로그래머스 괄호 회전하기

# always (), [], {} 올바른 괄호 문자열
# if A == "올바른 괄호 문자열"
# then : (A), [A], {A} 올바른 괄호 문자열
# if [] == 올과문, ([]) 올과문

# if A, B 올과문
# then : AB 올과문

# if {}, ([])
# then : {}([])

# s를 왼쪽만큼 x(s의 길이)칸 만큼 회전
# return s 올과문 x의 개수

from collections import deque
def check(s):
    stack = []
    for i in s:
        if stack:
            if stack[-1] == '[' and i == ']':
                stack.pop()
                continue
            elif stack[-1] == '{' and i == '}':
                stack.pop()
                continue
            elif stack[-1] == '(' and i == ')':
                stack.pop()
                continue
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack:
        return False
    return True

def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        if check(s):
            answer += 1
        s.append(s.popleft())
    return answer

print(solution("[](){}"))
# 3
# print(solution("}]()[{"))
# # 2
# print(solution("[)(]"))
# # 0
