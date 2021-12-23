# SWEA 2817 부분 수열의 합
from itertools import combinations
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    count = 0
    for i in range(len(numbers)):
        for combo in combinations(numbers, i):
            if sum(combo) == k:
                count += 1

    print(f'#{tc} {count}')