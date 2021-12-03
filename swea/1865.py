# SWEA 1865 동철이의 일 분배

# N명의 직원
# 해야할 일 N개

# i번 직원이 j번 일을 하면 성공할 확률이 Pi,j

# 배분방법은 여러 가지
# '주어진 일이 모두 성공할 확률'의 최댓값 구하는 프로그램 작성

def finder(x):
    global answer, result

    if answer < result or result <= 0:
        return

    if x == n:
        if answer < result:
            answer = result
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            result *= possible[i][x]
            finder(x+1)
            result /= possible[i][x]
            visited[i] = 0   


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    possible = [list(map(int, input().split())) for _ in range(n)]

    answer = float('inf')
    result = 0
    visited = [0] * n
    finder(0)

    print(answer)