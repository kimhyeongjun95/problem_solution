# 프로그래머스 신규 아이디 추천

# 규칙에 맞지 않는 아이디 -> 규칙에 맞는 아이디 추천

# (1). 3자 이상 15자 이하
# (2). 소문자, 숫자, 빼기, 밑줄, 마침표 only
# (3). 마침표 처음과 끝에 X -> 연속 사용 x

# 1. 대문자 -> 소문자
# 2. (2) 제외 제거
# 3. 마침표 연속 -> 하나로 치환
# 4. 마침표 처음이나 끝에 위치 -> 제거
# 5. 빈 문자열이면 a 대입
# 6. if len >= 16:
        # 첫 15문자 제외 제거
        # .가 마지막에 있다면 . 제거
# 7. if len <= 2:
        # 3이 될때까지 마지막 문자 반복해서 붙임

def solution(new_id):
    
    temp = ''

    # 1
    for i in new_id:
        if i.isupper():
            temp += i.lower()
        else:
            temp += i
    
    # 2
    temp2 = ''
    for i in temp:
        if i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.':
            temp2 += i
    # 3
    stack = []
    for i in temp2:
        if stack and stack[-1] == '.' and i == '.':
            continue
        stack.append(i)
    # 4
    if stack and stack[0] == '.':
        stack.pop(0)
    if stack and stack[-1] == '.':
        stack.pop()
    
    # 5
    if not stack:
        stack = ['a']
    
    # 6
    if len(stack) >= 16:
        stack = stack[:15]
    if stack[-1] == '.':
        stack.pop()
    
    # 7
    if len(stack) <= 2:
        temp = stack[-1]
        while len(stack) < 3:
            stack.append(temp)
    
    answer = ''.join(stack)
    return answer


    




print(solution("...!@BaT#*..y.abcdefghijklm"))
# "bat.y.abcdefghi"
print(solution("z-+.^."	))
# "z--"
print(solution("=.="	))
# "aaa"
print(solution("123_.def"))
# "123_.def"
print(solution("abcdefghijklmn.p"	))
# "abcdefghijklmn"
