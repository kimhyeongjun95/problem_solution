# 프로그래머스 네트워크
def solution(n, computers):

    visited = [0] * n
    count = 0
    stack = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif computers[i][j] == 1 and not visited[j]:
                stack.append(j)
                count += 1
                break
        while stack:
            x = stack.pop()
            visited[x] = 1 
            for k in range(n):
                if not visited[k] and computers[x][k] == 1:
                    stack.append(k)

    for i in visited:
        if i == 0:
            count += 1
    return count

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	)) # 2
print(solution(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]]	)) # 2