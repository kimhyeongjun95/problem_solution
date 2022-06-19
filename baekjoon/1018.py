# 백준 1018 체스판 다시 칠하기

# M x N 보드
# 검은색 or 흰색

# 보드를 체스판으로 만들려고 함
# 번갈아서 칠해져 있어야 한다.
# 체스판을 색칠하는 경우는 단 두가지
# 1. 맨 왼쪽 위 칸이 흰색인 경우
# 2. 검은색인 경우

# 보드가 체스판처럼 칠해져 있다는 보장 X
# 아무 곳에서나 8x8 크기의 체스판으로 잘라내고 칠해야하는 정사각형의 최소 개수

# 1. 모든 n-7 위치에서 탐색 시작
# 2. 좌측 상단이
# 2-1. 백인 경우 W
# 2-2. 흑인 경우 B
# 3. 탐색하며 answer 갱신

def search(x, y):
    global answer
    # 2-1 백인 경우
    count1 = counter(x, y, 'W', 'B')
    # 2-2 흑인 경우
    count2 = counter(x, y, 'B', 'W')

    answer = min(answer, count1, count2)

def counter(x, y, color, opposite):
    count = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            # 짝수의 row
            if i % 2 == 0:
                # 짝수의 col
                if j % 2 == 0:
                    if arr[i][j] != color:
                        count += 1
                # 홀수의 col
                else:
                    if arr[i][j] != opposite:
                        count += 1
            # 홀수의 row
            if i % 2 == 1:
                # 짝수의 col
                if j % 2 == 0:
                    if arr[i][j] != opposite:
                        count += 1
                else:
                    if arr[i][j] != color:
                        count += 1
    return count


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
answer = float('inf')

for i in range(n-7):
    for j in range(m-7):
        search(i, j)
print(answer)