from collections import deque

def dfs():
    visited = [[0] for _ in range(n)]
    

n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    one, two = map(int, input().split())
    arr[one].append(two)
    arr[two].append(one)