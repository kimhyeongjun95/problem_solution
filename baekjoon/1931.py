# 백준 1931 회의실 배정

# N개의 회의
# 회의실 사용표

# 각 회의에 대해 시작 시간 / 끝나는 시간
# 겹치지 않게 회의실 사용 최대 개수

# 한 회의가 끝나면서 다음 회의 시작 가능
# 시작 시간과 끝나는 시간이 같을수도 있음

N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append((s, e))
arr.sort(key = lambda x: (x[1], x[0]))

count = 0
point = 0
for s, e in arr:
    if point <= s:
        count += 1
        point = e
print(count)