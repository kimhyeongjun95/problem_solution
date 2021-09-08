# 9012 괄호

# PS : 두 개의 괄호 기호인 '('와 ')'만으로 구성된 문자열
# VPS : 괄호의 모양이 바르게 구성된 문자열
# 한 쌍의 기호로 된 '()' 문자열은 기본 VPS

# VPS면 YES 아니면 None

# 길이 2 <= s <= 50

def finder(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return 'NO'

    if stack:
        return 'NO'
    else:
        return 'YES'

t = int(input())

for _ in range(t):
    s = input()
    answer = finder(s)
    print(answer)