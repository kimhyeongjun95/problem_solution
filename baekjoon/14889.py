# 백준 14889 스타트와 링크

# 짝수의 N명
# N/2명으로 이루어진 스타트 팀, 링크 팀

# 1 ~ N번
# S[i][j] i번 사람과 j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치
# 팀의 능력치: 팀에 속한 모든 쌍의 능력치의 합
# Sij와 Sji는 다를 수 있다.
# i번 사람과 j번 사람이 같은팀 -> 팀에 더해지는 능력치는 Sij와 Sji

# 팀 간의 능력치 차이 최소화
# 능력치 차이 최솟값 출력

# 1. 모든 팀 경우의 수 구하기
# 2. 각 팀 간의 점수 구하기
# 3. 차이 최소값 갱신

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
answer = float('inf')

def dfs(count, idx):
    global answer
    if count == N // 2:
        result1 = 0
        result2 = 0
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    result1 += arr[i][j] + arr[j][i]
                elif not visited[i] and not visited[j]:
                    result2 += arr[i][j] + arr[j][i]
        answer = min(answer, abs(result1 - result2))
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(count + 1, i + 1)
            visited[i] = 0

dfs(0, 0)
print(answer)
