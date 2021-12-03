# SWEA 2056 연월일 달력

def check(check_month, check_day):
    check_month =  int(''.join(check_month))
    check_day = int(''.join(check_day))
    if 1 > check_month or check_month > 12:
        return False

    # 31일
    if check_month in [1, 3, 5, 7, 8, 10, 12]: 
        if 1 > check_day or check_day > 31:
            return False
    # 30일
    elif check_month in [4, 6, 9, 11]:
        if 1 > check_day or check_day > 30:
            return False
    
    # 28일
    elif check_month == 2:
        if 1 > check_day or check_day > 28:
            return False

    return True

t = int(input())
for tc in range(1, t+1):
    date = list(str(input()))
    year = date[:4]
    month = date[4:6]
    day = date[6:]

    if check(month, day):
        year = ''.join(year)
        month = ''.join(month)
        day = ''.join(day)
        answer = year + '/' + month + '/' + day
    else:
        answer = -1
    
    print(f'#{tc} {answer}')