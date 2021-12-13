# SWEA 1948 날짜 계산기
# 두 번째 날짜가 첫 번째 날짜의 며칠째인지?

def caculator(sm, sd, em, ed):
    result = 0
    if sm == em:
        return ed-sd + 1
    else:
        if sm in [1, 3, 5, 7, 8, 10, 12]:
            result = 31 - sd
        elif sm in [4, 6, 9, 11]:
            result = 30 - sd
        elif sm == 2:
            result = 28 - sd
        sm += 1

    while True:
        if sm == em:
            return result + ed + 1
        if sm < em:
            if sm in [1, 3, 5, 7, 8, 10, 12]: # 31일
                result += 31
            elif sm in [4, 6, 9, 11]: # 30일
                result += 30
            elif sm == 2:
                result += 28
            
            sm += 1


t = int(input())
for tc in range(1, t+1):
    sm, sd, em, ed = map(int, input().split())
    answer = caculator(sm, sd, em, ed)
    print(f'#{tc} {answer}')