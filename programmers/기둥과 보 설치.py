# 프로그래머스 기둥과 보 설치

# 기둥 : 바닥 위 or 보의 한쪽 끝 위 or 다른 기둥 위
# 보 : 한쪽 끝 기둥 위 or 양쪽 끝 다른 보 동시 연결

# build_frame : [x, y, a, b]
# x, y : 설치 or 삭제할 교차점 좌표 [가로, 세로]
# a : 0 기둥 1 보
# b : 0 삭제 1 설치
# 구조물 : 교차점 좌표 오른쪽, 기둥 : 위쪽

# return [x, y, a]
# x, y 기둥
# a : 0 기둥 1 보
# x, y 오름차순 정렬, 기둥이 보 보다 앞에

# 1. 나눠주면서 명령 수행
# 2. 설치 : 기둥과 보가 조건 O
# 3. 삭제 : 기둥과 보가 조건 X

# 정답률 1.9%..

# 해당 구조물이 설치 가능한 구조물인지?
def possible(answer):
    for x, y, thing in answer:
        if thing == 0: # 기둥
            # 바닥 위 or 보의 한쪽 끝 위 or 다른 기둥 위
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        if thing == 1: # 보
            # 한쪽 끝 기둥 위 or 양쪽 끝 다른 보 동시 연결
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y-1, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, thing, order = frame
        if order == 0: # 삭제
            answer.remove([x, y, thing]) # 일단 삭제
            if not possible(answer): # 가능한 구조물인지?
                answer.append([x, y, thing]) # 가능한 구조물이 아니라면 다시 설치
        elif order == 1: # 설치
            answer.append([x, y, thing]) # 일단 설치
            if not possible(answer): # 가능할 구조물인지?
                answer.remove([x, y, thing]) # 가능한 구조물이 아니라면 삭제
    return sorted(answer)
                

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

# [
# [1,0,0]
# [1,1,1]
# [2,1,0]
# [2,2,1]
# [3,2,1]
# [4,2,1]
# [5,0,0]
# [5,1,0]
# ]

