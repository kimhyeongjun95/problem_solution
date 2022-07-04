# 백준 1085 직사각형에서 탈출
# 한수는 (x, y) 위치
# 각 변이 좌표축에 평행
# 직 사각형의 경계선까지 가는 거리의 최솟값 구하기

x, y, w, h = map(int, input().split())
answer = 0
result1 = abs(y-h)
result2 = abs(x-w)
answer = min(result1, result2, x, y)
print(answer)