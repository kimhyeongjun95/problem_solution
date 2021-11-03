# 백준 7568 덩치

# x kg , y cm -> (x, y)
# (x, y) (p, q)
# if x > p and y > q라면 A의 덩치가 B의 덩치보다 크다.

# 자신보다 더 큰 덩치의 사람이 k명이라면, 그 사람의 덩치등수는 k+1
# 각 사람의 덩치 등수를 계산하여 출력

import sys
input = sys.stdin.readline

n = int(input())
people = []
for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

answer = []
for i in range(len(people)):
    x = people[i][0] 
    y = people[i][1] 
    count = 0
    for j in range(len(people)):
        if i == j:
            continue

        if x < people[j][0] and y < people[j][1]:
            count += 1

    answer.append(count+1)
print(*answer)