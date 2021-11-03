# 백준 1764 듣보잡

import sys
input = sys.stdin.readline

# 듣도 못한 사람 N 보도 못한 사람 M
# 듣보잡의 수와 명단 사전순으로 출력

n, m = map(int, input().split())
deut = []
for _ in range(n):
    deut.append(input().strip())
bo = []
for _ in range(m):
    bo.append(input().strip())

result = list((set(deut) & set(bo)))

result.sort()

print(len(result))
for i in result:
    print(i)