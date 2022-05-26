# 백준 1932 정수 삼각형

n = int(input())
arr = []
arr.append([int(input())])
for _ in range(n-1):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][0]
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

answer = max(arr[n-1])
print(answer)