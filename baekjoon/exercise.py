# 2960 에라토스테네스의 체

# 7 3
# 2 3 4 5 6 7
# 2, 4, 6 -> 3번째
# -> 6

# 15 12
# 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 3 5 7 9 11 13 15 -> 7개 나감
# 5 7 11 13 -> 7+4 = 11개 나감
# 

import sys
import math
n, k = int(sys.stdin.readline().split())

number = [i for i in range(2, n+1)]
arr = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if arr[i]: # True라면(소수라면)