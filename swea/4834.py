import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cards = list(map(int, input()))
    cards_num = {}
    for i in cards:
        if i in cards_num:
            cards_num[i] += 1
        else:
            cards_num[i] = 1

    temp = 0
    answer = 0
    for idx, val in cards_num.items():
        if temp < val:
            temp = val
            answer = idx

        if temp == val:
            if answer < idx:
                answer = idx

    print('#{} {} {}'.format(tc, answer, temp))