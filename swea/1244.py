# SWEA 1244 최대 상금
# 교환 후 가장 큰 금액 출력
def swapper(n, k):
    n = str(n)
    

t = int(input())
for tc in range(1, t+1):
    n, k = input().split()
    answer = swapper(n, k)
    print(f'#{tc} {answer}')