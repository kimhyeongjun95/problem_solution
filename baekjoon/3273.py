# 백준 3273 두 수의 합

# n 개의 수열, 서로 다른 양의 정수
# 자연수 x
# a[i] + a[j] = x를 만족하는 쌍의 수 구하기
# two pointer

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

count = 0
for i in range(n):
    j = i + 1
    while j < n:
        if arr[i] + arr[j] == x:
            count += 1
        j += 1
print(count)
# ----- 다시 풀기 