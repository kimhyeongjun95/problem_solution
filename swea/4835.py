t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 가장 큰 구간합과 가장 작은 구간합의 차이를 구한다.

    result = []

    for i in range(len(numbers)-m+1):
        idx = 0
        total = 0
        for j in range(m):
            total += numbers[i+idx]
            idx += 1
        result.append(total)

    max_result = result[0]
    min_result = result[0]

    for i in result:
        if max_result < i:
            max_result = i
        
        if min_result > i:
            min_result = i

    answer = max_result - min_result
    
    print('#{} {}'.format(tc, answer))