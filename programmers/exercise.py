# 프로그래머스 신규 아이디 추천

def solution(new_id):
    answer = ''
    return answer

def solution(time, plans):
    # 매번 금요일에 출근하여 월요일에 돌아오도록 여행 일정

    # 남은 휴가 : time
    # 여행 일정 : plans
    # 남은 휴가시간내에 갈수 있는 마지막 여행지가 어딘지?

    # plans : 여행지, 출발시간, 도착시간
    # 출발시간 금요일 기준, 도착시간 월요일 기준  
    # 홍콩은 휴가사용 x
    # 엘에이는 휴가 사용 o

    result = ''
    for plan in plans:
        destination, depart, arrive = plan
        how_long = 0

        # 출발시간 때 휴가가 얼마나 필요한가
        if len(depart) == 4:
            day_or_night = depart[2:]
            depart_time = int(depart[:2])
        elif len(depart) == 3:
            day_or_night = depart[1:]
            depart_time = int(depart[:1])
        
        if day_or_night == 'AM': # 오전에 출발하면
            how_long = (12-depart_time) + 6

        if day_or_night == 'PM': # 오후에 출발하면
            if depart_time < 6: # 휴가가 필요할 때
                how_long = (6 - depart_time)
                # 오후 6시이후로는 휴가필요 X

        # 도착날
        if depart == '12AM': # 밤 12시에 출발하면 무조건 18시간 필요
            how_long = 18
        if depart == '12PM':
            how_long = 6
        
        if len(arrive) == 4:
            day_or_night = arrive[2:]
            arrive_time = int(arrive[:2])
        elif len(arrive) == 3:
            day_or_night = arrive[1:]
            arrive_time = int(arrive[:1])
        
        # 도착날 오전엔 휴가필요 x
        if day_or_night == 'PM':
            if arrive_time > 1:
                how_long += arrive_time - 1 # 출발할때 휴가 사용 + 도착날 휴가 사용

        # print(time)
        # print(how_long)
        if time >= how_long:
            result = destination
            time = time - how_long
    
    return result

print(solution("...!@BaT#*..y.abcdefghijklm"))
# "bat.y.abcdefghi"
print(solution("z-+.^."	))
# "z--"
