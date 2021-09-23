# 백준 12904 A와 B

# A와 B로만 이루어진 영어단어

# S와 T
# 두 가지 연산만 가능.
# 1. 문자열 뒤에 A 추가
# 2. 뒤집고 뒤에 B 추가

# 가능하다면 1 아니라면 0
import sys
input = sys.stdin.readline

s = list(str(input().strip()))
t = list(str(input().strip()))

# s를 t로 변환하는 과정은 너무 경우의 수가 많음.
# t를 s로 변환해보자.
# print(s, t)
while len(s) < len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()

if s == t:
    print(1)
else:
    print(0)

    