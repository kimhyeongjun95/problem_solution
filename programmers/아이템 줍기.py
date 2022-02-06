# 프로그래머스 아이템 줍기

# 다각형의 둘레를 따라서 이동
# 꼭지점이 겹치거나 변이 겹치는 경우 X

# 아이템을 줍기위해 가장 짧은 거리 return

def solution(rectangle, characterX, characterY, itemX, itemY):
    max_x, max_y = 0, 0
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)
    max_x += 1
    max_y += 1
    world = [[0] * max_x for _ in range(max_y)]
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        for i in range(x1, x2):
            for j in range(y1, y2):
                world[j][i] = 1

    for i in range(len(world)-1, -1, -1):
        print(world[i])

# 풀다 말음

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)) # 17
# print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)) # 11
