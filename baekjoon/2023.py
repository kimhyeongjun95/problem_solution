# 백준 2023 신기한 소수

# 7331: 733, 73, 7도 소수
# 이러한 숫자를 신기한 소수라고 한다.

# N이 주어졌을때 N자리 신기한 소수 모두 찾아서
# 오름차순 출력

# 1. 첫째 자리가 소수인지 판단
# 1-1. 소수가 되는 길이 + 1 재귀
# 2. 길이가 n이 될떄까지 반복
# 2-1. 길이가 n이면 신기한 소수인지 판단

def judge(num):
    if num == 2 or num == 3:
        return True
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def find(n, count, num):
    global answer
    if count == n:
        if judge(num):
            answer.append(num)
        return
    
    if judge(num):
        for i in range(1, 10):
            temp = str(num)
            temp += str(i)
            if judge(int(temp)):
                find(n, count + 1, int(temp))

n = int(input())
answer = []
for i in range(2, 10):
    find(n, 1, i)
for i in answer:
    print(i)