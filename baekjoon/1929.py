import sys
import math
m, n = map(int, sys.stdin.readline().split())

arr = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1
    
for i in range(m, n+1):
    if i in [0, 1]:
        continue
    elif arr[i]:
        print(i)