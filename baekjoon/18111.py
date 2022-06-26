# 백준 18111 마인크래프트

# "땅 고르기"작업 : 땅의 높이를 모두 동일하게

# 세로 N 가로 M 크기의 집터, 맨 왼쪽 위의 좌표는 (0, 0)
# 1. (i, j)의 가장 위에 있는 블록 제거, 인벤토리에 넣기 : 2초
# 2. 인벤토리에서 블록을 꺼내 (i, j)의 가장 위에 놓기   : 1초

# 최소 시간, 땅의 높이 출력
# 답이 여러 개라면 그중에서 땅의 높이가 가장 높은것 출력 
# 인벤토리에 B개의 블록, 0 <= 높이 <= 256

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')
height = 0
for h in range(257):
    min_num = 0
    max_num = 0
    inven = 0
    time = 0
    for i in range(N):
        for j in range(M):
            # 블럭이 현재 높이보다 작으면
            if arr[i][j] < h:
                # 인벤토리에서 채워야함
                min_num += h - arr[i][j]
            else:
                # 인벤토리에 들어감
                max_num += arr[i][j] - h
    inven = max_num + B

    if inven >= min_num:
        time = (2 * max_num) + min_num
        if time <= answer:
            answer = time
            height = h

print(answer, height)