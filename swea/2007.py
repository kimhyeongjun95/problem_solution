# SWEA 2007 패턴 마디의 길이

def check(s):
    answer = 1
    while True:
        if s[:answer] == s[answer:answer*2]:
            return answer
        
        answer += 1

t = int(input())
for tc in range(1, t+1):
    s = input()
    answer = check(s)
    print(f'#{tc} {answer}')
    