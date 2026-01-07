import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

# 0: 빈 공간, 1: 직사각형 or 방문
board = [[0] * N for _ in range(M)]

# 직사각형 칠하기 (좌표 변환 주의!)
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[M - y - 1][x] = 1  # y 좌표 뒤집기

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sy, sx):
    queue = deque()
    queue.append((sy, sx))
    board[sy][sx] = 1
    area = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < M and 0 <= nx < N:
                if board[ny][nx] == 0:
                    board[ny][nx] = 1
                    queue.append((ny, nx))
                    area += 1
    return area

areas = []

for y in range(M):
    for x in range(N):
        if board[y][x] == 0:
            areas.append(bfs(y, x))

areas.sort()
print(len(areas))
print(*areas)
