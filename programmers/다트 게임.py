# 프로그래머스 다트 게임

# SDT 제곱(1, 2, 3)
# # 스타상 : 2배
# * 아차상 : 마이너스
# 스타상과 아차상 둘 중 하나만 존재 가능

def solution(dartResult):
    temp = ''
    result = []
    for i in dartResult:
        if i == 'S':
            result.append(int(temp) ** 1)
            temp = ''
        elif i == 'D':
            result.append(int(temp) ** 2)
            temp = ''
        elif i == 'T':
            result.append(int(temp) ** 3)
            temp = ''
        
        elif i == '*':
            length = len(result) - 2
            if len(result) == 1:
                length = 0
            for i in range(length, len(result)):
                result[i] = result[i] * 2
        elif i == '#':
            result[-1] = result[-1] * -1
        else:
            temp += i
    return sum(result)

print(solution('1S2D*3T')) # 37
print(solution('1D2S#10S')) # 9
print(solution('1D2S0T')) # 3
print(solution('1S*2T*3S')) # 23
print(solution('1D2S3T*')) # 59