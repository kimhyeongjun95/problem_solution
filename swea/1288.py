# SWEA 1288 새로운 불면증 치료법

# N의 배수를 센다. kN번 양
# n = 1295 | 1259
# 2n = 2590 | 01259
# ... 5n | 다 보게됨.

# 0부터 9까지의 모든 숫자를 보는 것은 최소 몇 번째 양?

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    number = n
    result = []
    answer = 0

    while len(result) < 10:
        for i in str(number):
            if i not in result:
                result.append(i)
        number += n
        answer += 1

    print(f'#{tc} {answer*n}')