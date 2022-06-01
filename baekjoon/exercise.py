# 백준 2504 괄호의 값

# 올바른 괄호란
# 1. () and []
# 2. X가 올바른 괄호열 => (X) [X] 올바른 괄호열
# 3. X and Y 모두 올바른 괄호열 => XY 올바른 괄호열

# 괄호값
# () 2
# [] 3
# (X) => 2 x 값(X)
# [X] => 3 x 값(X)
# XY => 값(XY) = 값(X) + 값(Y)

# 괄호값 return
# 올바르지 못한 괄호열 => 0 return

# 1. stack에 ) or ]이면 [-1]이 ( or [
# 1-1. (나 [면 들어와도 된다.
# 2. (( [[ 겹치면 mul에 append
# 2-1. mul[-1]과 i가 매치한다면 pop의 type에 따라 *=
# 2-2. val에 더하기 

def caculate():
    stack = []
    answer = 0
    count = 1
    for i in range(len(s)):
        if s[i] == '(':
            count *= 2
            stack.append(s[i])
        if s[i] == '[':
            count *= 3
            stack.append(s[i])
        if s[i] == ')':
            if not stack or stack[-1] == '[':
                return 0
            if s[i-1] == '(':
                answer += count
                stack.pop()
                count //= 2
        if s[i] == ']':
            if not stack or stack[-1] == '(':
                return 0
            if s[i-1] == '[':
                answer += count
                stack.pop()
                count //= 3
        print(stack)
        print(answer, count, s[i])
        print(i, len(s))
    return answer

s = input()
answer = caculate()
print(answer)