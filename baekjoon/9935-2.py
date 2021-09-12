# if 폭발 문자열 in 문자열:
#     모든 폭발 문자열 -> 폭발
#     남은 문자열 새로 이어붙임.
#     새로 생긴 문자열이 폭발 문자열일수도

# 남아 있는 문자가 없으면 'FRULA'

# 방법 
# 1: 리스트로 remove
# 2. 문자열 슬라이싱
# 3. 2중 반복문?

import sys

S = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

# while bomb in S:
#     stack = []
#     j = 0

#     for i in S:
#         stack.append(i)

#         if j > 0 and i != bomb[j]:
#             j = 0

#         if i == bomb[j]:

#             j += 1
        
#         if j == len(bomb):
#             for _ in range(j):
#                 stack.pop()
#             j = 0

#         # print(i, j, stack)

#     S = ''.join(stack)

# if S:
#     print(S)
# else:
#     print('FRULA')

