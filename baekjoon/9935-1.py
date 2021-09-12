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

print(S, bomb)

while bomb in S:
    i = 0
    j = 0
    s = S

    temp = []
    while i <= len(s): # s의 길이만큼만
        if j > 0 and s[i] != bomb[j]: # 처음 글자만 같을수도 있으니 다시 초기화
            j = 0
            temp = []
        if s[i] == bomb[j]: # C4 : i는 6과 7에 여기서 활성화..
            j += 1
            temp.append(i)

        i += 1

        # print(s, i, j, temp)
        if j == len(bomb): # 만약 bomb이 s에 들어가 있다면..
            break

    S = s[:temp[0]] + s[temp[-1]+1:]
    # print(S, '결과물')

if S:
    print(S)
else:
    print('FRULA')