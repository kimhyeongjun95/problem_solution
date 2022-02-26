# 백준 21608 상어 초등학교

# 교실 N x N
# 학생 수 N^2

# 학생의 자리를 정하려고 한다

# 1. 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸
# 2. 1 만족 다수 -> 인접한 칸 중 비어있는 칸이 가장 많은 칸
# 3. 2 만족 여러 개 -> 3-1. 행의 번호가 가장 작은 칸, 3-2. 여러 개 -> 열의 번호가 가장 작은 칸

# 학생의 만족도 총합 출력

# 3
# 4 2 5 1 7 // 2
# 3 1 9 4 5 // 3
# 9 8 1 2 3
# 8 1 9 3 4
# 7 2 3 4 8
# 1 9 2 5 7
# 6 5 2 3 4
# 5 1 9 2 8
# 2 9 3 1 4

from collections import defaultdict

def req1(val, room):
    result = defaultdict(list)

    for i in range(n):
        for j in range(n):
            # 비어있으면서
            if room[i][j] == 0:
                count = 0

                for dx, dy in dxy:
                    nx = dx + i
                    ny = dy + j

                    if -1 < nx < n and -1 < ny < n:
                        # 좋아하는 친구가 얼마나 많은지
                        if room[nx][ny] in val:
                            count += 1
                result[count] += (i, j)
    return result

def req2(room):
    result = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if room[i][j] == 0:
                count = 0

                for dx, dy in dxy:
                    nx = dx + i
                    ny = dy + j

                    if -1 < nx < n and -1 < ny < n and room[nx][ny] == 0:
                        count += 1
            result[count] += ((i, j))
    return result


dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n = int(input())

room = [[0] * n for _ in range(n)]
students = defaultdict(int)
for i in range(n**2):
    arr = list(map(int, input().split()))
    students[arr[0]] = arr[1:]

for key, val in students.items():
    result = req1(val, room)
    result = req2(room)

    # if len(result[max(result)]) > 2:
    print(result[max(result)])  