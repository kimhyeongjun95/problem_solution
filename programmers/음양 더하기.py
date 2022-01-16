# 프로그래머스 음양 더하기

def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign == True:
            answer += absolute
        elif sign == False:
            answer -= absolute
    return answer

print(solution([4,7,12], [true,false,true])) # 9
print(solution([4,7,12], [true,false,true])) # 0