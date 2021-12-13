# SWEA 1859 백만 장자 프로젝트

def calculator(price):
    high_number = 0
    result = 0
    stack = []

    high_number = max(price)
    while True:
        popped = price.popleft()
        if popped == high_number:
            for i in stack:
                result += (high_number - i)
            stack = []
            if not price:
                return result
            high_number = max(price)
            continue

        stack.append(popped)

        if not price:
            return result


from collections import deque
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    price = deque(list(map(int, input().split())))

    answer = calculator(price)

    print(f'#{tc} {answer}')

# 10
# 629 3497 7202 7775 4325 3982 4784 8417 2156 1932
# #3 20065 
# 26725가 나와야됌