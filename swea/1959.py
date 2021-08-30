import sys
sys.stdin = open('input.txt')

def caculator(short, long):
    if n > m:
        short, long = long, short

    result = []
    for i in range(len(long)-len(short)+1):
        temp = 0
        for j in range(len(short)):
            temp += short[j] * long[i+j]
        result.append(temp)

    return max(result)


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    short = list(map(int, input().split()))
    long = list(map(int, input().split()))

    answer = caculator(short, long)
    print('#{} {}'.format(tc, answer))