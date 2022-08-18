# 백준 10819 차이를 최대로

from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
answer = 0
for per in permutations(arr):
    result = 0
    for i in range(len(per)-1):
        temp = abs(per[i] - per[i+1])
        result += temp
    answer = max(answer, result)
print(answer)
        
