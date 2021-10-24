# SWEA 4881 배열 최소 합

def finder(x):
    global result, answer

    if answer < result:
        return

    if x == n:
        if answer > result:
            answer = result
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            result += arr[i][x]
            finder(x+1)
            result -= arr[i][x]
            visited[i] = 0
    

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    answer = float('inf')
    result = 0
    finder(0)

    print('#{} {}'.format(tc, answer))