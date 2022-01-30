# 프로그래머스 [1차] 비밀지도
# n x n 지도
# 각 칸은 공백(" ") or 벽("#")

# 전체지도 = 두 장의 지도를 겹쳐서 얻음
# 하나라도 벽이면 전체지도에서도 벽
# 모두 공백인 부분은 전체지도에서도 공백

# 공백 0 벽 1
# 1. 각 지도를 10진수 -> 2진수로 바꾸기
# 2. zip으로 2진수 문자열 확인하면서 새로운 지도 만들기

def solution(n, arr1, arr2):
    map1 = []
    for i in arr1:
        temp = str(bin(i))[2:]
        if len(temp) < n:
            temp = ('0' * (n-len(temp))) + temp
        map1.append(temp)

    map2 = []
    for i in arr2:
        temp = str(bin(i))[2:]
        if len(temp) < n:
            temp = ('0' * (n-len(temp))) + temp
        map2.append(temp)
    
    answer = []
    for i, j in zip(map1, map2):
        temp = ''
        for k, l in zip(i, j):
            k, l = int(k), int(l)
            if k == 1 or l == 1: # 하나라도 벽이면
                temp += '#'
            
            elif k == 0 and l == 0: # 모두 공백이면
                temp += ' '
        answer.append(temp)
    return answer

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# ["#####","# # #", "### #", "# ##", "#####"]
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
# ["#####","# # #", "### #", "# ##", "#####"]