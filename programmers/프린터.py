# 프로그래머스 프린터

# 중요도가 높은 문서를 먼저 인쇄하는 프린터
# 1. 대기목록 중 가장 앞에 있는 문서(J) 꺼냄
# 2. if 나머지 대기목록 중 중요도 > J: J를 마지막에 넣음
# 3. else: J 인쇄

# 요청한 문서가 몇번째로 인쇄되는지?

from collections import deque
def solution(priorities, location):
	priorities = deque(priorities)
	answer = 0
	idx = location
	while priorities:

		for priority in priorities:
			if priority > priorities[0]:
				temp = priorities.popleft()
				priorities.append(temp)
				idx = (idx - 1) % len(priorities)
				break
		else:
			answer += 1
			if idx == 0:
				return answer
			priorities.popleft()
			idx = (idx - 1) % len(priorities)
			
	return answer

print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5