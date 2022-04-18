# 프로그래머스 (2021 카카오 인턴십) 표 편집

# 선택, 삭제, 복구 프로그램 작성 과제

# "U X": 현재 선택된 행에서 X칸 위에 있는 행 선택
# "D X": 현재 선택된 행에서 X칸 아래에 있는 행 선택
# "C": 현재 선택된 행 삭제, 바로 아래 행 선택
#      if 삭제된 행이 가장 마지막 행: 바로 윗 행 선택
# "Z": 가장 최근에 삭제된 행 복구 / 선택된 행 변화 X

# n : 처음 표 행 개수
# k : 처음 선택된 행 위치
# cmd : 명령어

# 처음 표와 비교하여 OX 문자열 형태 return

# 1. UX와 DX는 순수 구현
# 2. C는 X위치를 pop하도록
# 2-1. if X == len(리스트) - 1: X -= 1
# 2-2. 삭제된 X deleted에 append하기
# 3. Z는 insert로 x 넣기

# 정확성 100 % 코드 효율성 X

from collections import defaultdict
def solution(n, k, cmd):
    arr = [1] * n
    length = n
    deleted = []
    S = k
    for c in cmd:
        flag = True    
        if c[0] == "U":
            X = int(c[2:])
            cnt = 1
            while X:
                if arr[S - cnt] == 1:
                    X -= 1
                    S -= cnt
                    cnt = 1
                    continue
                cnt += 1
        elif c[0] == "D":
            X = int(c[2:])
            cnt = 1
            while X:
                if arr[S + cnt] == 1:
                    X -= 1
                    S += cnt
                    cnt = 1
                    continue
                cnt += 1
        elif c == "C":

            for i in range(S+1, len(arr)):
                if arr[i] == 1:
                    flag = False
                    break

            # 2-1
            if flag:
                arr[S] = 0
                deleted.append(S)
                cnt = 1
                while True:
                    if arr[S - cnt] == 1:
                        S -= cnt
                        cnt = 1
                        break
                    cnt += 1
            # 2
            else:
                arr[S] = 0
                deleted.append(S)
                cnt = 1
                while True:
                    if arr[S + cnt] == 1:
                        S += cnt
                        cnt = 1
                        break
                    cnt += 1
            length -= 1
        # 3
        elif c == "Z":
            popped = deleted.pop()
            arr[popped] = 1
            length += 1

    answer = ''
    
    for i in arr:
        if i == 1:
            answer += "O"
        else:
            answer += "X"
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# "OOOOXOOO"
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
# "OOXOXOOO"
# "OOXOXOOO"
