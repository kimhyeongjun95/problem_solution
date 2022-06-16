# 백준 20291 파일 정리

# 1. 확장자 별로 정리해서 몇 개씩 있는지
# 2. 사전순 정렬

from collections import defaultdict
n = int(input())
arr = [list(input()) for _ in range(n)]
check = defaultdict(int)

for i in range(n):
    for j in range(len(arr[i])):
        if arr[i][j] == '.':
            temp = ''.join(arr[i][j+1:])
            check[temp] += 1
            break

answer = sorted(check.items())
for i in answer:
    print(*i)