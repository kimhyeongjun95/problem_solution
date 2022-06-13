# 백준 3085 사탕 게임

#  N x N 크기에 사탕을 채워 놓는다.
# 사탕의 색이 다른 인접한 두 칸을 고름.
# 사탕을 서로 교환
# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 or 열)을 고르고
# 그 사탕을 모두 먹는다.

# 빨: C, 파: P, 초: Z, 노: Y

# 먹을 수 있는 사탕의 최대 개수 return

# 1. N-1길이 만큼 행과 열 각각 탐색
# 2. 다음 원소와 색이 다르면 swap
# 2-1. 모든 행과 모든 열 가장 긴 문자열 구하기
# 2-2. 되돌리기

n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 0

def find():
    global answer

    for i in range(n):
        count = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                count += 1
            else:
                count = 1
            answer = max(answer, count)
        answer = max(answer, count)
    answer = max(answer, count)

    for i in range(n):
        count = 1
        for j in range(n-1):
            if arr[j][i] == arr[j+1][i]:
                count += 1
            else:
                count = 1
            answer = max(answer, count)
        answer = max(answer, count)
    answer = max(answer, count)

for i in range(n):
    for j in range(n-1):
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            find()
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

for i in range(n-1):
    for j in range(n):
        if arr[i][j] != arr[i+1][j]:
            arr[i+1][j], arr[i][j] = arr[i][j], arr[i+1][j]
            find()
            arr[i+1][j], arr[i][j] = arr[i][j], arr[i+1][j]

print(answer)