t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        result = 0

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color


                if arr[i][j] == 3:
                    result += 1

    print('#{} {}'.format(tc, result))
    