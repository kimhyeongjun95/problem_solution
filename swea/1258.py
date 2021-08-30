def finder(x, y):

    nx = 0
    while x + nx < h and arr[x+nx][y] != 0:
        nx += 1

    ny = 0
    while y + ny < w and arr[x][y+ny] != 0:
        ny += 1

    for i in range(x, x+nx):
        for j in range(y, y+ny):
            arr[i][j] = 0

    return nx, ny, nx*ny

t = int(input())
for tc in range(1, 11):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    # 사각형들은 각각 차원이 다름.
    # 0 은 빈 용기
    # 출력은 갯수, 크기가 작은 순
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                x, y, score= finder(i, j)
                result.append((x, y, score))

    result = sorted(result, key = lambda x: (x[2], x[0])) # 크기가 작은순 / 크기가 같다면 행이 작은 순
    answer = [] # 문자열로 입력받자니 마지막 공백처리가 힘듬
    count = 0
    for i in result:
        answer.append(i[0])
        answer.append(i[1])
        count += 1

    print('#{} {}'.format(tc, count), end=' ')
    print(*answer)