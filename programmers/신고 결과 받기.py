# 프로그래머스 신고 결과 받기

# 각 유저는 한 번에 한명의 유저 신고
# - 횟수 제한 x
# - 한 유저 - 동일한 유저 - 1회 처리
# k번 이상 -> 정지
# 신고한 모든 유저에게 정지사실 메일로 발송

# 각 유저별로 처리결과 메일 횟수 배열 return
from collections import defaultdict
def solution(id_list, report, k_num):
    answer = [0] * len(id_list)
    suspended = defaultdict(set)
    result = defaultdict(int)
    banned = set()
    answer_num = defaultdict(int)
    for act in report:
        reporter, ted = act.split(' ')
        suspended[reporter].add(ted)
    for i, j in suspended.items():
        for k in j:
            result[k] += 1

    for key, val in result.items():
        if val >= k_num:
            banned.add(key)

    for i, j in suspended.items():
        for k in j:
            if k in banned:
                answer_num[i] += 1
    
    for i in range(len(answer)):
        answer[i] = answer_num[id_list[i]]
    return answer

    

            



print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
# [2, 1, 1, 0]