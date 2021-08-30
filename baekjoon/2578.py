from collections import deque

def check(arr, popped):
    bingo = 0
    # 가로 탐색
    for i in range(5):
        nj = 0
        for j in range(5):
            if arr[i][0] == 0:
                while nj + j < 5 and arr[i][nj] == 0:
                    nj += 1
                if j + nj  == 5:
                    bingo += 1

    # 세로 탐색
    for i in range(5):
        ni = 0
        for j in range(5):
            if arr[0][i] == 0:
                while ni + i <  5 and arr[i+ni][j] == 0:
                    ni += 1
                if i + ni == 5:
                    bingo += 1
    
    # 오른쪽 대각선 탐색
    count = 0
    for i in range(5):
        for j in range(i, i+1):
            count += arr[i][j]
    if count == 0:
        bingo += 1

    # 왼쪽 대각선 탐색
    count = 0
    for i in range(5):
        for j in range(4, -1, -1):
            count += arr[i][j]
    if count == 0:
        bingo += 1

    if bingo >= 3:
        print(popped, '1')
        return popped

arr = [list(map(int, input().split())) for _ in range(5)]

bingo = [deque(map(int, input().split())) for _ in range(5)]
answer = []
for bing in bingo:
    for _ in range(5):
        popped = bing.popleft()

        for i in range(5):
            for j in range(5):
                if arr[i][j] == popped:
                    arr[i][j] = 0
                    answer.append(check(arr, popped))

        if answer:
            print(answer[0])
