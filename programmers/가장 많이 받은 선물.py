# 다음 달에 누가 선물을 많이 받을 것인가?

# 선물 지수 = 이번달 까지 자신이 친구들에게 준 선물의 수 - 받은 선물의 수

# 선물을 더 준 사람이 다음 달에 선물 하나 받음
# 기록 X or 같으면 "선물 지수"가 더 큰 사람이 받음
# 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 X

# 선물을 가장 많이 받을 친구가 받을 선물의 수

# friends: 친구들의 이름
# gifts: 이번 달까지 주고받은 선물 기록을 담은 1차원 문자열

from collections import defaultdict
def solution(friends, gifts):
    answer = 0
    보낸기록 = defaultdict(lambda: defaultdict(int))
    받은기록 = defaultdict(lambda: defaultdict(int))
    for gift in gifts:
        보내는사람, 받는사람 = gift.split(' ')
        보낸기록[보내는사람][받는사람] += 1
        받은기록[받는사람][보내는사람] += 1
    
    print(보낸기록)
    선물지수 = defaultdict(int)
    for friend in friends:
        보낸기록Count = sum(보낸기록[friend].values())
        받은기록Count = sum(받은기록[friend].values())
        선물지수[friend] = 보낸기록Count - 받은기록Count
    
    length = len(friends)
    answer = 0
    for i in friends:
        count = 0
        for j in friends:
            if i == j:
                continue
            if 보낸기록[i][j] > 받은기록[i][j]:
                count += 1
                continue
            elif 보낸기록[i][j] == 받은기록[i][j]:
                if 선물지수[i] > 선물지수[j]:
                    count += 1
                    continue
        answer = max(count, answer)
    return answer
            
                
            
            
            
            
        
        