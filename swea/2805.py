import sys
sys.stdin = open('input.txt')

def harvester(farm):
    mid = n // 2
    left = 0
    right = mid + 1
    answer = 0
    flag = True
    count = 0 # while문 나가기 위한
    while count < n:
        for i in range(n):
            for j in range(mid-left, right):
                answer += farm[i][j]
                # print(answer, i, j)

            if left == mid:
                flag = False

            if flag:
                left += 1
                right += 1
                
            elif not flag:
                left -= 1
                right -= 1

        count += 1
    return answer

t = int(input())
for tc in range(1, t+1):
    # 농장의 크기는 홀수
    # 마름모 형태
    # 얻을 수 있는 수익은?
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    answer = harvester(farm)
    print('#{} {}'.format(tc, answer))