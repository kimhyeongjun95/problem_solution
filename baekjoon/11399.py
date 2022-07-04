# 백준 11399 ATM

# ATM 1대
# N명의 사람들
# i번 사람이 돈 인출 시간 Pi분

# 줄을 서는 순서에 따라 돈을 인출하는데 필요한 시간의 합이 달라진다.

# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값 출력

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
count = 0
for i in arr:
    count += i
    answer += count
print(answer)