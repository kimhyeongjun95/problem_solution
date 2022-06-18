# 백준 17609 회문

# 유사회문: 한 문자를 삭제하여 회문으로 만들 수 있음
# 회문: 0
# 유사회문: 1
# else: 2

# 1. 회문인지 판단
# 2. 유사회문인지 판단
# 3. answer append

def palindrome(s, i, j):
    # 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

def check(s):
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            result1 = palindrome(s, i+1, j)
            result2 = palindrome(s, i, j-1)
            if result1 or result2:
                return 1
            else:
                return 2
    return 0

t = int(input())
arr = [list(input()) for _ in range(t)]
answer = []
for i in arr:
    answer.append(check(i))
for i in answer:
    print(i)