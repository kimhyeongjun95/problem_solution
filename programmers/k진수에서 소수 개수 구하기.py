# 프로그래머스 (2022 카카오) k진수에서 소수 개수 구하기

# 정수 n -> k 진수로 변환
# 조건에 맞는 소수(prime number)는 몇개인지?

# 1. 0P0 : 소수 양쪽에 0
# 2. P0 : 왼쪽 X 오른쪽 0
# 3. 0P : 왼쪽 0 오른쪽 X
# 4. P : 소수 양쪽에 아무 것도 X
	# P는 자릿수에 0을 포함 X

# k : 3 ~ 10진수

def zero_check(stack):
	if '0' in stack:
		return False
	return True

def prime(x):
	if x < 2:
		return False
	for i in range (2, int(x**0.5) + 1):
		if x % i == 0:		
			return False
	return True	

def transfer(n, q):
	temp = ''
	while n > 0:
		n, mod = divmod(n, q)
		temp += str(mod)
	return temp[::-1] 

def solution(n, k):
	changed = transfer(n, k)
	answer = 0
	stack = []
	idx = []
	zero = False
	four = False
	for i in range(len(changed)):
		idx.append(i)
		if int(changed[i]) == 0:
			four = True
			# 2
			if not zero and stack and zero_check(stack) and prime(int(''.join(stack))):
				answer += 1
			# 1
			elif zero and idx[0] > 0 and int(changed[idx[0]-1]) == 0 and stack and zero_check(stack) and prime(int(''.join(stack))):
				answer += 1
			zero = True
			stack = []
			idx = []
		# 0이 아닌 경우
		else:
			stack.append(changed[i])
	# 3
	if zero and stack and zero_check(stack) and prime(int(''.join(stack))):
		four = True
		answer += 1
	# 4
	if stack and not four and prime(int(''.join(stack))):
		answer += 1
	return answer


print(solution(437674, 3))
# 3
print(solution(110011, 10))
# # 2