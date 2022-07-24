# 백준 1697 숨바꼭질

# 수빈 N 동생 K
# 수빈 : 걷기 or 순간이동
#        걷기 : 위치 X일때 걸으면, 1초 후 X-1 or X+1
#        순간이동 : 1초 후 2*X 

# 수빈이가 동생을 찾는 가장 빠른 시간 출력

from collections import deque

def find():
    queue = deque([(N)])
    visited = [0] * 100001
    while queue:
        x = queue.popleft()
        if x == K:
            return visited[x]
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 100000 and not visited[i]:
                queue.append((i))
                visited[i] = visited[x] + 1

N, K = map(int, input().split())
answer = find()
print(answer)