# SWEA 5601 쥬스 나누기
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    if n > 1:
        answer = ('1/' + str(n) + ' ') * n
    else:
        answer = ('1/' + str(n)) * n
    print(f'#{tc} {answer}')