# SWEA 1234 비밀번호
def check(s):
    s = list(str(s))
    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return stack


for tc in range(1, 11):
    t, s = input().split()
    answer = check(s)
    answer = ''.join(answer)
    print(f'#{tc} {answer}')