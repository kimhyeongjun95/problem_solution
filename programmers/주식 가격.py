# 프로그래머스 주식 가격

# 가격이 떨어지지 않은 기간은 몇초인지 list return

from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        count = 0
        popped = prices.popleft()
        for price in prices:
            count += 1
            if popped > price:
                break

        answer.append(count)
    return answer

print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]