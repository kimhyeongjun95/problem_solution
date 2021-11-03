# 백준 1157 단어 공부

import sys
input = sys.stdin.readline
from collections import defaultdict

counter = defaultdict(int)
s = input().strip()
for i in s:
    temp = i.lower()
    counter[temp] += 1


max_value = 0
result = []
for key, value in counter.items():
    result.append(value)
    if value > max_value:
        max_value = value
        answer = key.upper()

if result.count(max_value) > 1:
    answer = '?'

print(answer)