# SWEA 1946 간단한 압축 풀기
from collections import deque
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    result = deque([])
    for _ in range(n):
        s, num = input().split()
        for _ in range(int(num)):
            result.append(s)
    print(f'#{tc}')
    while True:
        printer = ''
        while result and len(printer) < 10:
            temp = result.popleft()
            printer += temp
        print(printer)
        if not result:
            break