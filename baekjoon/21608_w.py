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
                result[count].append((i, j))
    return result

def req2(result1, room):
    result = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if room[i][j] == 0:
                count = 0

                for dx, dy in dxy:
                    nx = dx + i
                    ny = dy + j

                    if -1 < nx < n and -1 < ny < n and room[nx][ny] == 0 and (i, j) in result1[max(result1)]:
                        count += 1
                result[count].append((i, j))
    return result

def contentCheck(key, val, room):
    for i in range(n):
        for j in range(n):
            if room[i][j] == key:
                count = 0

                for dx, dy in dxy:
                    nx = dx + i
                    ny = dy + j

                    if -1 < nx < n and -1 < ny < n:
                        if room[nx][ny] in val:
                            count += 1
    return count

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n = int(input())

room = [[0] * n for _ in range(n)]
students = defaultdict(int)
for i in range(n**2):
    arr = list(map(int, input().split()))
    students[arr[0]] = arr[1:]

for key, val in students.items():
    result1 = req1(val, room) # 1
    if len(result1[max(result1)]) > 1:
        result2 = req2(result1, room)
        if len(result2[max(result2)]) > 1: # 3
            result3 = sorted(result2[max(result2)], key=lambda x : (x[0], x[1]))
            i, j = result3[0]
        else: # 2
            i, j = result2[max(result2)][0]

    else:
        i, j = result1[max(result1)][0]

    room[i][j] = key
print(room)

answer = 0
for key, val in students.items():
    count = contentCheck(key, val, room)
    if count == 1:
        answer += 1
    elif count == 2:
        answer += 10
    elif count == 3:
        answer += 100
    elif count == 4:
        answer += 1000

print(answer)

