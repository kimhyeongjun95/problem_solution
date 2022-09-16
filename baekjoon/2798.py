# 백준 2798 블랙잭

# 카드의 합이 21을 넘지 않게
# 카드의 합을 최대한 크게 만드는 게임

# N장의 카드 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합 출력

from itertools import combinations

n, m = map(int, input().split())
numbers = map(int, input().split())
answer = 0

for combo in combinations(numbers, 3):
    if sum(combo) <= m:
        answer = max(answer, sum(combo))
print(answer)
