# SWEA 1217 거듭제곱
for _ in range(1, 11):
    tc = int(input())
    n, squared = map(int, input().split())
    answer = n ** squared
    print(f'#{tc} {answer}')