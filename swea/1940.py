# SWEA 1940 가랏! RC카!
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    speed = 0
    result = 0
    for _ in range(n):
        temp = list(input().split())
        if len(temp) == 2:
            if int(temp[0]) == 1:
                speed += int(temp[1])
            elif int(temp[0]) == 2:
                speed -= int(temp[1])
        if speed < 0:
            speed = 0
        result += speed

    print(f'#{tc} {result}')