# 프로그래머스 로또의 최고 순위와 최저 순위

# 알아볼 수 없는 번호 : 0
# 최고 : 0은 맞출수 있는 걸로 판단
# 최저 : 0은 무조건 틀리는 걸로 판단
from collections import defaultdict
def solution(lottos, win_nums):
    check = defaultdict(int)
    for nums in win_nums:
        check[nums] += 1
    
    extra = 0
    count = 0
    for lotto in lottos:
        if lotto == 0:
            extra += 1
        elif check[lotto]:
            count += 1

    winner = {
        6:1,
        5:2,
        4:3,
        3:4,
        2:5,
        1:6,
        0:6
    }
    answer = []
    answer.append(winner[count+extra])
    answer.append(winner[count])

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # 	[3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])) # 	[1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])) # 	[1, 1]
