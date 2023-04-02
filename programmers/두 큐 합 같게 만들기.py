# 프로그래머스 두 큐 합 같게 만들기

from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(q1)
    s2 = sum(q2)
    count = 0
    maxCount = len(queue1) * 3

    if s1 == s2:
        return 0

    while True:
        if s1 > s2:
            s1 -= q1[0]
            s2 += q1[0]
            q2.append(q1.popleft())
        elif s1 < s2:
            s1 += q2[0]
            s2 -= q2[0]
            q1.append(q2.popleft())
        else:
            return count
        count += 1
        if count == maxCount:
            return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
# 2