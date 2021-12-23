# 3431 준환이의 운동관리
# L분 이상 U분 이하 해야 몸 유지
# X분만큼 운동했음

# 시간을 넘었는지? 아니면 몇분 더 운동을 해야 제한을 맞추는지 출력

t = int(input())
for tc in range(1, t+1):
    l, u, x = map(int, input().split())
    # 초과 : -1
    # 적절하면 0
    # 운동이 필요하다면 몇분 해야하는지
    answer = 0
    if x < l:
        answer = l - x
    elif l <= x <= u:
        answer = 0
    elif x > l:
        answer = -1
    
    print(f'#{tc} {answer}')