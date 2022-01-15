# 프로그래머스 체육복
def solution(n, lost, reserve):
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)
    print(_reserve, _lost)
    
    for i in _reserve:
        if i+1 in _lost:
            _lost.remove(i+1)        
        elif i-1 in _lost:
            _lost.remove(i-1)

    return n - len(_lost)

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3])) # 4
print(solution(3, [3], [1])) # 2
print(solution(9, [2, 3, 4, 5, 8], [1, 4, 5, 6, 9])) # 8
