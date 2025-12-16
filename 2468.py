import sys
from collections import deque



N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
count = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]






def BFS(x,y,h,graph,visit):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = True
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < N and 0 <= ny < N:
                if not visit[nx][ny] and graph[nx][ny] > h :
                    visit[nx][ny] = True
                    queue.append((nx,ny))
                    count += 1
                    

                    
            
        
        
        
        
        
        
        