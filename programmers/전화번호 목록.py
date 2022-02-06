# 프로그래머스 전화번호 목록

# 전화번호 접두사

# 접두어인 경우 false
# 아닌 경우 true return
from collections import defaultdict
def solution(phone_book):
    
    check = defaultdict(int)
    for i in phone_book:
        for j in range(len(i)):
            check[i[:j]] = 1
    
    for i in phone_book:
        if check[i]:
            return False
    return True


print(solution(["119", "97674223", "1195524421"])) # false
print(solution(["123","456","789"])) # true
print(solution(["12","123","1235","567","88"])) # false
