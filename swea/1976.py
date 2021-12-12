# SWEA 1976 시각 덧셈

t = int(input())
for tc in range(1, t+1):
    sh, sm, eh, em = map(int, input().split())
    
    ah = sh + eh
    am = sm + em
    if ah > 12:
        ah -= 12
    if am > 59:
        ah += 1
        am -= 60

    print(f'#{tc} {ah} {am}')