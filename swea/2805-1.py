# SWEA 2805 농작물 수확하기

# 농장의 크기는 항상 홀수
# 농장은 정사각형 마름모 형태
# 농장 수확물 수익 구하기

def harvester(farm):

    # 1
    # 5
    # 14054
    # 44250
    # 02032
    # 51204
    # 52212
    answer = 0
    for i in range(n):
        middle = abs(i-n//2)
        answer += sum(farm[i][middle:n-middle])
    return answer

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    answer = harvester(farm)
    print('#{} {}'.format(tc, answer))