# 프로그래머스 (2018 카카오 3차) 압축

# LZW 압축

# 1. 알파벳 base 사전 만들기
# 2. 현재 입력(w)이 in check 중 가장 긴 문자열 찾기:
# 2-1. answer에 check (w)val push
# 2-2. check에 w + c : val

from collections import defaultdict
def solution(msg):

    alpha = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    check = defaultdict(int)
    for i in range(1, len(alpha)):
        check[alpha[i].upper()] = i
    idx = 0
    idx_r = 0
    result = []
    count = 27
    while idx < len(msg):
        # 2
        while check[msg[idx:idx_r]]:
            idx_r += 1
        # 2-1
        print(check[msg[idx:idx_r+1]])
        result.append(check[msg[idx:idx_r+1]])
        check[msg[idx:idx_r+2]] = count
        print(result)
        print(check)
        idx = idx_r + 1
        idx_r = idx
        count += 1
        

print(solution("KAKAO"))
# [11, 1, 27, 15]
# print(solution("TOBEORNOTTOBEORTOBEORNOT"))
# [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# print(solution("ABABABABABABABAB"))
# [1, 2, 27, 29, 28, 31, 30]
