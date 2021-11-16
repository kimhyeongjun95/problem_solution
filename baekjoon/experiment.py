# 프로그래머스 위클리 챌린지 9주차 : 전력망을 둘로 나누기

# 2개로 분할해서
# 송전탑 개수의 차이 최소값

from collections import defaultdict
def solution(n, wires):
    
    result = []
    tree = defaultdict(list)
    for one, two in wires:
        tree[one].append(two)
        tree[two].append(one)

    for one, two in wires:
        tree[one].remove(two)
        tree[two].remove(one)

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))