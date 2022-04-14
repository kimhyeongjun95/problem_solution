# 백준 2206 벽 부수고 이동하기

# N x M 행렬
# 0 : 이동 O
# 1 : 벽
# (1, 1)에서 (N, M)까지 최단경로로 이동
# 벽을 한 개 까지 부수고 이동 가능

# 시작하는 칸, 끝나는 칸 포함해서 세기
# 최단거리 숫자 출력

# 1. 0,0에서 N, M까지 이동하면서 count += 1
# 2. 가면서 벽 만나면 wall = False
# 3. not wall 일때 벽 만나면 return

from collections import deque
dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def bfs():
	queue = deque([(0, 0, False, 1)])
	visited[0][0] = 1
	while queue:
		x, y, wall, count = queue.popleft()

		for dx, dy in dxy:
			nx = x + dx
			ny = y + dy
			if -1 < nx < n and -1 < ny < m:
				if not visited[nx][ny]:

					if not wall and arr[nx][ny] == 1:
						queue.append((nx, ny, True, count + 1))
						visited[nx][ny] = 1
						print((nx, ny, True, count + 1))

					if arr[nx][ny] == 0:
						if nx == n-1 and ny == m-1:
							return count + 1
						queue.append((nx, ny, wall, count + 1))
						print((nx, ny, wall, count + 1))

						visited[nx][ny] = 1
	return -1

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
answer = bfs()
print(arr)
for i in visited:
	print(i)
print(answer)