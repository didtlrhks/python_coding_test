import sys
from collections import deque


N = int(input())
graph = [list(input().strip()) for _ in range(N)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]



def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = True
    color = graph[x][y]
    

    
    while queue:
        x,y = queue.popleft()      
        
        for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        
        if 0 <= nx < N and 0 <= ny < N:
            if not visit[nx][ny] and graph[nx][ny] == color:
                visit[nx][ny] == True
                queue.appned((nx,ny))
                
                
visit

        
        
            