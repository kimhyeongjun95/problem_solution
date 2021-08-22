import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    array = []

    for _ in range(n):
        array.append(list(map(int, input().split())))

    result = []

    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            for k in range(m):
                for l in range(m):
                    total += array[i+k][j+l]

            result.append(total)

    max_number = result[0]

    for i in result:
        if max_number < i:
            max_number = i

    print('#{} {}'.format(tc, max_number))