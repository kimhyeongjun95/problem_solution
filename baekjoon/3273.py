# 백준 3273 두 수의 합

# n 개의 수열, 서로 다른 양의 정수
# 자연수 x
# a[i] + a[j] = x를 만족하는 쌍의 수 구하기
# two pointer

# 1. 정렬
# 2. == x라면 answer += 1, j -= 1
# 2-1. < x라면 i += 1
# 2-2. > x라면 j -= 1

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
answer = 0
i, j = 0, len(arr)-1
while i < j:
    if arr[i] + arr[j] == x:
        answer += 1

    if arr[i] + arr[j] < x:
        i += 1
        continue

    if arr[i] + arr[j] >= x:
        j -= 1

print(answer)