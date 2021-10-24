# SWEA 1961 숫자 배열 회전

def turning(matrix):
    answer = []
    for i in range(n):
        temp = []
        for j in range(n-1, -1, -1):
            temp.append(matrix[j][i])
        answer.append(temp)
    return answer

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # 세번 출력 해야하는데
    # 90도 / 180도 / 270도
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    arr_90 = turning(arr)
    arr_180 = turning(arr_90)
    arr_270 = turning(arr_180)

    print('#{}'.format(tc))
    for i, j, k in zip(arr_90, arr_180, arr_270):
        print(*i, sep='', end=' ')
        print(*j, sep='', end=' ')
        print(*k, sep='', end=' ')
        print()