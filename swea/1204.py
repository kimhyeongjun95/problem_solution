# SWEA 1204 최빈수 구하기
# 최빈수가 여러개면 가장 큰 점수 출력

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    scores = list(map(int, input().split()))
    scores.sort()

    sub = []
    result = {}
    temp = set(scores)
    for i in temp:
        result[i] = scores.count(i)
    
    count = max(result.values())
    for key, value in result.items():
        if value == count:
            sub.append(key)
    
    answer = max(sub)
    print(f'#{tc} {answer}')