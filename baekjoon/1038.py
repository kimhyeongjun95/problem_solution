# 백준 1038 감소하는 수

# 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소 ?
# => 감소하는 수

# 321, 950 감소하는 수 O
# 322, 958 감소하는 수 X

# N번째 감소하는 수 출력
# 만약 N번째 감소하는 수가 없다면 -1

# 987654321 => 최대 감소하는 수 

from itertools import combinations

n = int(input())
answer = []

for i in range(1, 11):
    for combo in combinations(range(0, 10), i):
        combo = list(combo)
        combo.sort(reverse=True)
        answer.append(int(''.join(map(str, combo))))
answer.sort()

if len(answer) > n:
    print(answer[n])
else:
    print(-1)