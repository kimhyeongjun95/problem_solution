# SWEA 1215 회문1
# 회문의 총 개수 구하기

for tc in range(1, 11):
    n = int(input())
    # 8x8 행렬
    arr = [list(input()) for _ in range(8)]
    count = 0

    # 가로
    for i in range(8):
        for j in range(8-n+1): # 0 1 2 3 4
            if arr[i][j:j+n] == arr[i][j:j+n][::-1]:
                count += 1

    # 세로
    for i in range(8):
        for j in range(8-n+1):
            temp = ''
            for k in range(j, j+n):
                temp += arr[k][i]
            if temp == temp[::-1]:
                count += 1

    print(f'#{tc} {count}')
