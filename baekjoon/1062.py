# 백준 1038 감소하는 수

# K개의 글자를 가르칠 시간
# 학생들은 K개의 글자로만 이루어진 단어만 read O
# 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어가 최대가 되는지?

# 모든 단어는 
# starts with "anta"
# ends with "tica"
# 남극 언어는 N개만 존재

# antatica로 5개를 가져감.
# K가 5개 미만이라면 0 return

# from collections import defaultdict
# from itertools import combinations
# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# words = []
# for _ in range(n):
#     words.append(input().strip())
# print(words)
# def find():
#     if k < 5:
#         return 0
#     if k >= 26:
#         return n
    
#     result = 0
#     check = defaultdict(int)
#     for word in words:
#         for i in range(4, len(word)-4):
#             check[word[i]] = 1
#     checked_set = []
#     for word in words:
#         val = set("antatica")
#         for i in word:
#             val.add(i)
#         checked_set.append(val)
#     for combo in combinations(check, k-5):
#         isin = set('antatica')
#         temp = ''.join(combo)
#         for i in temp:
#             isin.add(i)
#         count = 0
#         for check_set in checked_set:
#             if check_set.issubset(isin):
#                 count += 1
#         result = max(result, count)
#     return result
    
# answer = find()
# print(answer)

import sys

n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26

for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

def dfs(idx, cnt):
    global answer
    if cnt == k - 5:
        see = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                see += 1
        answer = max(answer, see)
        return
    
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt+1)
            learn[i] = False

dfs(0, 0)
print(answer)