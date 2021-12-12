# SWEA 1966 숫자를 정렬하자

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    numbers = ' '.join(map(str, numbers))
    print(f'#{tc} {numbers}')