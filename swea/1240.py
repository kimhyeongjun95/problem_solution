# SWEA 1240 단순 2진 암호코드

# 8개의 숫자
# 앞 7자리 : 고유번호
# 뒤 1자리 : 검증 코드

# 검증코드 = sum(홀수) x 3 + sum(짝수) + 검증코드
# -> 10의 배수가 되어야 함. (올림)

# 8801234
# ((8+0+2+4) x 3) + (8+1+3) + 검증 코드
# 42 + 12 + 검증코드
# 54 + 검증코드가 10의 배수여야함.
# -> 검증코드 = 6
# 정상 암호코드: 88012346


t = int(input())

# 0이 앞에 와야하기에 문자열로 정리
dict = {
    '0001101':'0',
    '0011001':'1',
    '0010011':'2',
    '0111101':'3',
    '0100011':'4',
    '0110001':'5',
    '0101111':'6',
    '0111011':'7',
    '0110111':'8',
    '0001011':'9'
}

def idx_finder(arr):
    # 암호는 항상 1로 끝난다.
    # 그래서 1로 끝나는 것이 가장 처음 시작하는 위치 찾기.
    # 한 줄만 가져오면 됌.
    for i in range(n):
        for j in range(m-1, 0, -1):
            if arr[i][j]:
                return i, j

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
    row, column = idx_finder(arr)
    # 7 x 8 = 56
    password = arr[row][column-55:column+1]

    result = ''
    for i in range(0, len(password), 7):
        temp = password[i:i+7]

        strs = ''
        for j in range(len(temp)):
            strs += str(temp[j])

        result += dict[strs]

    result = str(result)
    odd = 0
    even = 0
    for j in range(len(result)): # idx는 0부터 시작
        if j % 2 == 1: # 짝수라면
            odd += int(result[j])
        elif j % 2 == 0: # 홀수라면
            even += int(result[j])

    answer = (even*3) + odd
    count = 0
    if answer % 10 == 0:
        for i in range(8):
            count += int(result[i])
    else:
        pass

    print('#{} {}'.format(tc, count))
