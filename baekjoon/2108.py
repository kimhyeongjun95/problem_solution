# 백준 2108 통계학

# n개의 수
# 산술평균
# 중앙값
# 최빈값
# 범위 출력

from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
answer = [0] * 4
answer[0] = round(sum(arr) / n)
arr2 = sorted(arr)
answer[1] = arr2[n//2]
count = [0]
temp = Counter(arr2)

flag = 0
result = []
if len(temp) > 1:
    for key, val in temp.items():
        result.append((key, val))
    result.sort(key = lambda x: -x[1])
    if result[0][1] == result[1][1]:
        answer[2] = result[1][0]
    else:
        answer[2] = result[0][0]
else:
    answer[2] = arr[0]
answer[3] = abs(arr2[0] - arr2[-1])

for i in answer:
    print(i)
