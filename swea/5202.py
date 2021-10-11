import sys
sys.stdin = open('input.txt')

t = int(input())

# 24시간 동안 A도크의 사용 신청 확인
# 최대한 많은 화물차가 화물을 싣고 내림
# 최대 몇대의 화물차 이용?

# 앞 작업의 종료 동시에 다음 작업 시작 가능

# 끝나는 시간끼리 계산하면...

for tc in range(1, t+1):
    temp = []
    n = int(input())
    for _ in range(n):
        s, e = map(int, input().split())
        temp.append((s, e))

    # 끝나는 시간 순으로 오름차순 정렬
    temp.sort(key = lambda x : x[1])
    print(temp)

    work_end = 0
    result = 0

    for start, end in temp:
        if start >= work_end:
            result += 1
            work_end = end

    print('#{} {}'.format(tc, result))
