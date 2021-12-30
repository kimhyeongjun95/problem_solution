# 프로그래머스 2016년
# 1월 1일은 금요일
# a월 b일은 무슨 요일?
def solution(a, b):
    date = 0
    date += b
    month = 1
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    while True:
        if month == a:
            return days[date%7]
        # 31일
        if month in [1, 3, 5, 7, 8, 10, 12]:
            date += 31
        # 30일
        elif month in [4, 6, 9, 11]:
            date += 30
        # 29일(윤년)
        elif month == 2:
            date += 29
        
        month += 1

print(solution(5, 24)) # 'TUE'