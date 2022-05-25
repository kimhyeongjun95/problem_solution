# 백준 18428 감시 피하기

#  N x N 복도
# 선생님(T) or 학생(S) or 장애물(O)
# 선생님: 상하좌우 4가지 방향 감시 except 장애물

# 3개의 장애물 설치
# 모든 학생들이 감시 피할 수 있으면 YES
# else: NO

# 1. S로부터 각각 4방향으로 뻗어나가기
# 1-1. T를 만나는 방향이면 S -> T로 숫자 += 1 설치
# 2. 모든 숫자 Hash로 count
# 3. 높은 숫자부터...

# 완탐하면?
# 1. X의 모든 위치 구하기
# 2. combinations으로 각각 위치에 OBJ만들기
# 2-1. T로부터 4방향으로 뻗어나가기
# 2-2. S를 만난다면 break
# 3. 하나라도 된다면 YES
# 3-1. 모두 안된다면 NO

from itertools import combinations
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def watch(x, y, dir):
    # 왼
    if dir == 0:
        while y >= 0:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            y -= 1
    # 오
    if dir == 1:
        while y < n:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            y += 1
    # 위
    if dir == 2:
        while x >= 0:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            x -= 1
    # 아래
    if dir == 3:
        while x < n:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            x += 1
    return False
    
def find():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

n = int(input())
arr = [list(input().split()) for _ in range(n)]
locations = []
teachers = []
flag = False
# 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'X':
            locations.append((i, j))
        elif arr[i][j] == 'T':
            teachers.append((i, j))

for combo in combinations(locations, 3):
    # 2
    for com in combo:
        x = com[0]
        y = com[1]
        arr[x][y] = 'O'
    
    if not find():
        flag = True
        break

    for com in combo:
        x = com[0]
        y = com[1]
        arr[x][y] = 'X'

if flag:
    print("YES")
else:
    print("NO")