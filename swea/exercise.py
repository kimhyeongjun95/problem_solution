# SWEA 6485 삼성시의 버스 노선

def diagonalPass(row, col):
    for i in range(row):
        # 행과 열의 차이가 같다면 동일 대각선에 있음
        if row - i == abs(col-arr[i]):
            return False
    return True

def check(idx):
    global answer
    
    if idx == n:
        answer += 1
        return

    for i in range(n):
        # row / diagonal 체크
        if not visited[i] and diagonalPass(idx, i):
            visited[i] = 1
            arr[idx] = i
            check(idx+1)
            visited[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    answer = 0
    arr = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]

    check(0)

    print(f'#{tc} {answer}')
