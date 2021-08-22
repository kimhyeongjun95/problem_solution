import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    bong = list(input().split())

    n = len(bong)
    i = 0
    cnt = 0
    stick = 0

    while i < n:
        if bong[i] == '(' and bong[i+1] == ')':
           cnt += stick
           i += 2

        elif bong[i] == '(':
            stick == 1
            i += 1
        else:
            cnt += 1
            stick -= 1
            i += 1

    print('#{} {}'.format(tc, cnt))