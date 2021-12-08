# SWEA 1986 지그재그 숫자

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    number = 1
    answer = 0
    while number < n+1:
        if number % 2:
            answer += number
        else:
            answer -= number
        
        number += 1

    print(f'#{tc} {answer}')