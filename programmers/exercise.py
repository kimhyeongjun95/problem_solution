# 프로그래머스 다단계 칫솔 판매
# 10% 가 추천인에게 넘어감.
# 원 단위에서 절사, 10%가 1원 미만인 경우 모든 이익은 자신이 가짐

# enroll 순서대로 이익금 리스트 return
# enroll[i] -> referral[i] 추천인 (하 -> 상)
# 추천인 x -> '-'
# 칫솔 1개 100원
import math
def solution(enroll, referral, seller, amount):
    profit = [0] * len(enroll)

    for i in range(len(seller)):
        idx = enroll.index(seller[i])
        money = amount[i] * 100
        while True:
            if (money*0.1) >= 1:
                profit[idx] += math.ceil(money * 0.9)
                parent_idx = referral[idx]
                if parent_idx == '-':
                    break
                parent_idx = enroll.index(referral[idx])
                if math.ceil(money*0.1) > 1:
                    money = math.ceil(money*0.1)
                idx = parent_idx

            else:
                profit[idx] += money
                break
    
    return profit

print(solution(
["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], # enroll
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], # referral
["young", "john", "tod", "emily", "mary"], # seller
[12, 4, 2, 5, 10])) # amount
# [360, 958, 108, 0, 450, 18, 180, 1080]