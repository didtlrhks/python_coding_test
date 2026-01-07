
import sys
from collections import deque

N = int(input())

graph = [list(input().strip()) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def BFS(x,y,graph,visit):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = True
    color = graph[x][y]
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0<= ny <N:
                if not visit[nx][ny] and graph[nx][ny] == color:
                    queue.append((nx,ny))
                    visit[nx][ny] = True
                
                
visit_normal = [[False] * N for _ in range(N)]
normal_count = 0

for i in range(N):
    for j in range(N):
        if not visit_normal[i][j]:
            BFS(i,j,graph,visit_normal)
            normal_count += 1
            
blind_graph = [[c for c in row] for row in graph]

for i in range(N):
    for j in range(N):
        if blind_graph[i][j] == 'R':
            blind_graph[i][j] = 'G'
            
visit_blind = [[False] * N for _ in range(N)]
blind_count = 0

for i in range(N):
    for j in range(N):
        if not visit_blind[i][j]:
            BFS(i, j, blind_graph, visit_blind)
            blind_count += 1
            
print(normal_count,blind_count)
        

        
        
        
        
            