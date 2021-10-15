# 백준 2875 대회 or 인턴

# N명의 여학생 M명의 남학생
# 학생들 중 K명은 반드시 인턴쉽 프로그램 참여
# 인턴쉽 참여 -> 대회 참여 X
# 최대한 많은 팀 만들기

# 2명의 여학생 1명의 남학생
# 여, 남, 인턴쉽 인원
# 즉, k <= m+n
n, m, k = map(int, input().split()) # 6 3 2 -> 2
count = 0
while True:
    if n < 2 or m < 1 or (n+m)-k < 3:
        break
    n -= 2
    m -= 1
    count += 1
print(count)