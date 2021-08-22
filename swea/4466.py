t = int(input())

for i in range(1, t+1):
    n, k = map(int ,input().split())
    scores = list(map(int, input().split()))
    max_sum = 0

    for j in range(k):
        max_sum += max(scores)
        scores.remove(max(scores))

    print(f'#{i} {max_sum}')