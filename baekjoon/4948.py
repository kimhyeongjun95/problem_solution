# 백준 4948 베르트랑 공준

# 베르트랑 공준 : n보다 크고 2n 이하의 소수는
#                 적어도 하나는 존재한다.

# 10 < 공준 <= 20
# 11, 13, 17, 19 : 4개

# 개수 구하기
# 시간초과로 매번 계산하지말고
# 미리 계산한 numbers에서 구해보자.
import sys
input = sys.stdin.readline
import math

def prime_check(n):
    if n < 2 :
        return False
    elif n == 2:
        return True
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

numbers = []
for i in range(2, (123456 * 2)+1):
    if prime_check(i):
        numbers.append(i)

while True:
    result = []
    n = int(input())
    if n == 0:
        break
    double = 2 * n

    for i in numbers:
        if n < i <= double:
            result.append(i)
    print(len(result))
    