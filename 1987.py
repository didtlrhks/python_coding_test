import sys
from collections import deque


R,C = map(int,input().split())
visit = [[False]*R for _ in range(C)]
graph = [list(input().strip()) for _ in range(C)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y,v,g):
    queue = deque()
    queue.append((x,y))
   # visit[x][y] = True
    
        while queue:
            x,y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < R and 0 <= ny < C:
                    if not visit[nx][ny] and graph[nx][ny] == graph[nx][ny] - 1:
                        visit[nx][ny] = True
                        queue.appned((nx,ny))
                        
                        
                        
              
