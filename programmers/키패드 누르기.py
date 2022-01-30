# 프로그래머스 키패드 누르기

# 왼손 * 오른손 #
# 왼손 : 147
# 오른손 : 369
# 가운데 : 2580 -> 더 가까운 엄지손가락
# if 거리가 같으면 무슨 손잡이인지에 따라..

dist = {
    1:{2:1, 5:2, 8:3, 0:4},
    4:{2:2, 5:1, 8:2, 0:3},
    7:{2:3, 5:2, 8:1, 0:2},
    3:{2:1, 5:2, 8:3, 0:4},
    6:{2:2, 5:1, 8:2, 0:3},
    9:{2:3, 5:2, 8:1, 0:2},
    '*':{2:4, 5:3, 8:2, 0:1},
    '#':{2:4, 5:3, 8:2, 0:1},

    2:{2:0, 5:1, 8:2, 0:3},
    5:{2:1, 5:0, 8:1, 0:2},
    8:{2:2, 5:1, 8:0, 0:1},
    0:{2:3, 5:2, 8:1, 0:0},
}


def solution(numbers, hand):
    answer = ''
    be_l = '*'
    be_r = '#'

    for number in numbers:
        if number in [1, 4, 7]:
            be_l = number
            answer += 'L'
        elif number in [3, 6, 9]:
            be_r = number
            answer += 'R'
        elif number in [2, 5, 8, 0]:
            if dist[be_l][number] < dist[be_r][number]: # 왼손이 가까우면
                be_l = number
                answer += 'L'
            elif dist[be_l][number] > dist[be_r][number]: # 오른손이 가까우면
                be_r = number
                answer += 'R'
            elif dist[be_l][number] == dist[be_r][number]: # 거리가 같으면
                if hand == 'left':
                    be_l = number
                    answer += 'L'
                elif hand == 'right':
                    be_r = number
                    answer += 'R'
    
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# "LRLLLRLLRRL"