import sys
from collections import deque

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, graph, visit, N, M):
    queue = deque()
    queue.append((x, y))
    visit[y][x] = True
    
    while queue:
        x, y = queue.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            # 범위 체크
            if 0 <= nx < M and 0 <= ny < N:
                # 배추가 있고 방문 안 했으면
                if not visit[ny][nx] and graph[ny][nx] == 1:
                    visit[ny][nx] = True
                    queue.append((nx, ny))
    
    return 1   # BFS 1번 실행 = 지렁이 1마리 필요

for _ in range(T):
    M, N, K = map(int, input().split())
    
    graph = [[0] * M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
        
    worm_count = 0
    
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visit[y][x]:
                BFS(x, y, graph, visit, N, M)
                worm_count += 1
    
    print(worm_count)
