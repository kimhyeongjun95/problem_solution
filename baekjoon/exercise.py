# 백준 2193 이친수

# 이친수란
# 1. 0으로 시작 X
# 2. 1이 두 번 연속으로 나타나지 않는다.
# - 즉, 11을 부분 문자열로 갖지 않는다.

import sys
input = sys.stdin.readline

n = int(input())
answer = 0

def find(num, count):
    global answer
    if count == n:
        answer += 1
        return

    find(num+'0', count+1)
    if num[-1] == '0':
        find(num+'1', count+1)

find('1', 1)

print(answer)