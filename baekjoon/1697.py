# 백준 1697 숨바꼭질

# 수빈 N 동생 K
# 수빈 : 걷기 or 순간이동
#        걷기 : 위치 X일때 걸으면, 1초 후 X-1 or X+1
#        순간이동 : 1초 후 2*X 

# 수빈이가 동생을 찾는 가장 빠른 시간 출력

# 1. K가 N보다 큰지 작은지 확인
# 2. 완전탐색

def find(count, now):
    global answer

    if now == K:
        answer = min(answer, count)
        return
    if count > 100000 or now < 0 or now > 100000:
        return
    
    if ((now - 1) * 2) - K < ((now * 2) - 1) - K:
        find(count + 1, now - 1)
    else:
        find(count + 1, now * 2)
    

N, K = map(int, input().split())
answer = float('inf')
find(0, N)
print(answer)