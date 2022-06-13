# 백준 2493 탑

# 왼쪽으로 레이저 발사

# 각각의 탑에서 발사한 레이저 신호
# 어느 탑에서 수신하는지 idx return

n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = []

for i in range(len(arr)):
    while stack and stack[-1][1] < arr[i]:
        stack.pop()
    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1][0] + 1)
    stack.append((i, arr[i]))

print(*answer)