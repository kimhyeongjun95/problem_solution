# 프로그래머스 (2022 카카오) 양궁대회

# 전 우승자인 라이언에게 불리하게
# # 어피치 n발 -> 라이언 n발
# k점, 어피치 : a발, 라이언: b발
# 더 많은 화살을 k점에 맞힌 선수가 k점을 가져감

# if a = b: 어피치가 k점을 가져감
# if a == b == 0: 어느 누구도 k점 X

# # 최종 점수 계산
# 어피치가 화살을 다 쏜 상태
# 라이언이 가장 큰 점수 차이로 우승하기 위해 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지?

# 10점부터 0점까지 순서대로 배열 return
#  지거나 비기는 경우 return [-1]
# if 가장 큰 점수 차이로 우승할 수 있는 방법 > 1:
# return 가장 낮은 점수를 더 많이 맞힌 경우

# 점수가 낮은 것부터 비교해야 된다.
# 해당 점수를 얻을 것이라면 한발을 더 맞추거나
# else: 아예 쏘지 않거나

import copy
def solution(n, info):
	global max_score, answer
	answer = [0] * 11
	max_score = 0
	def find(apeach, lion, idx, arrow, arr):
		global max_score, answer
		if n < arrow:
			return

		if idx > 10:
			score = lion - apeach
			if score > max_score:
				max_score = score
				arr[10] = n - arrow
				answer = arr
			return 
		
		# 라이언이 이긴 경우
		if arrow < n:
			next = copy.deepcopy(arr)
			next[10-idx] = info[10-idx] + 1
			find(apeach, lion + idx, idx + 1, arrow + info[10-idx]+1, next)

		# 어피치가 이긴 경우
		# print(info, idx)
		if info[10-idx] > 0:
			find(apeach + idx, lion, idx+1, arrow, arr)
		else:
			# 비긴 경우
			find(apeach, lion, idx+1, arrow, arr)
	
	find(0, 0, 0, 0, answer)
	if max_score > 0:
		return answer
	return [-1]


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# [0,2,2,0,1,0,0,0,0,0,0]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# [-1]
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# [1,1,2,0,1,2,2,0,0,0,0]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# 