# SWEA 1984 중간 평균값 구하기

t = int(input())
for tc in range(1, t+1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    
    print(f'#{tc} {round(sum(numbers[1:9])/8)}')