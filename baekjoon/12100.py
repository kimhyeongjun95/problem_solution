# 백준 12100 2048(Easy)

# N x N 보드
# 0은 빈칸 원소는 모두 2의 제곱꼴
# 최대 5번 중 최대값은?

# 미완성 코드

from copy import deepcopy

def rotate(n, arr):
    temp = deepcopy(arr)
    for i in range(n):
        for j in range(n):
            temp[j][n-i-1] = arr[i][j]
    return temp

def caculate(n, arr):
    temp = [i for i in arr if i != 0]
    for i in range(1, len(temp)):
        if temp[i-1] == temp[i]:
            temp[i-1] *= 2
            temp[i] = 0
    temp = [i for i in temp if i != 0]
    return temp


def dfs(n, arr, count):
    result = max([max(i) for i in arr])
    if count == 5:
        return result

    for _ in range(4):
        Narr = [caculate(n, i) for i in arr]
        result = max(result, dfs(n, Narr, count + 1))
        arr = rotate(n, arr)
    return result

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dfs(n, arr, 0)