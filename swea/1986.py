# SWEA 1986 초심자의 회문 검사

t = int(input())
for tc in range(1, t+1):
    s = input()

    mid = len(s) // 2

    left = []
    for i in range(mid):
        left.append(s[i])

    right = []
    if len(s) % 2 == 0:
        for i in range(len(s)-1, mid-1, -1):
            right.append(s[i])
    else:
        for i in range(len(s)-1, mid, -1):
            right.append(s[i])
    
    if left == right:
        answer = 1
    else:
        answer = 0
    
    print(f'#{tc} {answer}')