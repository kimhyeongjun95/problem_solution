# 백준 스도쿠 2580

# 최종 모습 출력

arr = [list(map(int, input().split())) for _ in range(9)]
tofill = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            tofill.append((i, j))


print(arr)