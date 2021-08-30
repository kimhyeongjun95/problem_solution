import sys
sys.stdin = open('input.txt')

# 흰색(글씨가 들어갈자리)는 1 검은색은 0
def word_putter(arr):
    answer = 0 # 몇 개?

    for i in range(n): # 가로 확인
        count = 0
        for j in range(n):
            if arr[i][j] == 1:
                count += 1
            elif arr[i][j] == 0:
                if count == k: # count 갯수만큼 채우고 검은색 만났을때
                    answer += 1
                count = 0 # 무조건 count는 0으로 해줘야함 검은색 만나면
        if count == k: # 행이 끝났을때
            answer += 1

    for i in range(n): # 세로 확인
        count = 0
        for j in range(n):
            if arr[j][i] == 1:
                count += 1
            elif arr[j][i] == 0:
                if count == k:
                    answer += 1
                count = 0
        if count == k:
            answer += 1

    return answer

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = word_putter(arr)
    print('#{} {}'.format(tc, answer))