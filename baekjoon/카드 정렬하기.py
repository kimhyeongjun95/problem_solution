# 백준 1715 카드 정렬하기

# 정렬된 두 묶음의 숫자 카드
# 각 묶음의 카드의 수 A, B
# 하나로 합치려면 A+B번의 비교
# ex) 20, 30 => 50번 비교

import heapq
n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

answer = 0
while len(heap) > 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    value = one + two
    answer += value
    heapq.heappush(heap, value)
print(answer)