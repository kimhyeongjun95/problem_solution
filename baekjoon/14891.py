# 백준 14891 톱니바퀴

# 8개의 톱니, 톱니바퀴 4개
# N극 또는 S극을 나타내는 톱니, 각자 번호를 가짐
# K번 회전, 한 칸을 기준 (시계방향 or 반시계방향)

# 같은 극 : 회전 X
# 다른 극 : 회전 O (영향 받는 톱니바퀴는 반대방향으로 회전)

# N극 : 0, S극 : 1

# 출력
# 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
# 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
# 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
# 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점

# 점수 총합 출력

#---------------------------------------------------------------

import sys
input = sys.stdin.readline
from collections import deque
# C:/Python39/python.exe c:/Users/김형준/Desktop/problem_solution/baekjoon/exercise.py

def rotater(number, direction):
    # 주체자를 제외한 나머지를 반대방향으로 계속 돌려준다.
    # count : 동시에 회전시켜야함

    temp_direction = -direction
    # 왼쪽
    count = 0
    for i in range(number, 0, -1):
        #  같은 극
        if gears[i][6] == gears[i-1][2]:
            # 그 이후로도 영향을 주지 않기에
            break
        count += 1

    for i in range(number, number-count, -1):
        rotate(gears[i-1], temp_direction)
        temp_direction = -temp_direction # 회전이 바뀜

    temp_direction2 = -direction
    # 오른쪽
    count = 0
    for i in range(number, 3):
        if gears[i][2] == gears[i+1][6]:
            # 그 이후로도 영향을 주지 않기에
            break
        count += 1
    
    for i in range(number, number+count):
        rotate(gears[i+1], temp_direction2)
        temp_direction2 = -temp_direction2 # 회전이 바뀜

def rotate(arr, direction):
    # 시계 방향
    if direction == 1:
        popped = arr.pop()
        arr.appendleft(popped)
    else:
        popped = arr.popleft()
        arr.append(popped)

# 12시 방향부터 시계방향 순서대로 주어짐.
# 즉, idx[2] = 오른쪽 
#     idx[6] = 왼쪽
gears = [deque(list(map(int, input().strip()))) for _ in range(4)]
# 회전 횟수 
k = int(input())

for _ in range(k):
    # 번호, 방향(1: 시계, -1: 반시계)
    number, direction = map(int, input().split())
    number = number-1 # 인덱스
    rotater(number, direction)
    # 마지막 자기자신 돌리기
    rotate(gears[number], direction)

answer = 0
for i in range(4):
    answer += (2**i) * gears[i][0]
print(answer)